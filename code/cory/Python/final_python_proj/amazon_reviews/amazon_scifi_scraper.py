from bs4 import BeautifulSoup # Parses the text
import csv
import requests
import datetime

# Using + to replace commas for csv splitting
def remove_comma(string):

    new_string = ''
    for char in string:
        if char == ',':
            new_string += '+'
        else:
            new_string += char

    return (new_string)

# Function to help check grammar.
def punct_checker(sentance):

    sentance = list(sentance)
    end_punctuation = ['.', '!', '?', ',']

    for punct in end_punctuation:
        for i in range(len(sentance) - 1, -1, -1):
            if i != len(sentance) - 1:
                if sentance[i] == punct:    
                    if sentance[i + 1] == ' ':
                        pass
                    else:
                        sentance.insert((i+1), ' ')

    sentance = ''.join(sentance).strip()
    return sentance

# Function to remove unicode
def unicode_remover(sentance):

        sentance = list(sentance)
        return ''.join([i if ord(i) < 128 else '' for i in sentance])

# Book counter
book_counter = 0

# Url to scrape from, use page # to loop from pages.
page_url = "https://www.amazon.com/s/ref=sr_pg_2?rh=n%3A283155%2Cn%3A%211000%2Cn%3A25%2Cn%3A16272&page=1&sort=review-rank&ie=UTF8&qid=1541699809&lo=stripbooks"

# Trying to fix Amazon filter issue (works)
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

# Opening connection, grabbing the page
amazon_link = requests.get(page_url, headers=headers)

# HTML parsing
page_soup = BeautifulSoup(amazon_link.content,"html5lib")

# Used to create unique filename
now = datetime.datetime.now().strftime("%b-%d-%Y_%H-%M-%S")

# Create file to write data to
filename = f"scrape_scifi_data_{now}.csv"
amazon_writer = csv.writer(open(filename, 'w', newline=''))
amazon_writer.writerow(['Purchase Link', 'Title', 'Author', 'Publish Date', 'Cost', 'Book Types', 'Rating', 'Review Number', 'Synopsis'])

# Main containers to scrape data from
containers = []
for num in range(60):
    container = page_soup.findAll("li",{"id": f"result_{num}"})
    containers.append(container)

#Main Loop < -------------------------------------------------------
for i in range(len(containers)):

    # Need to use [0][0] to point at the string inside the list, not the list itsself
    container = containers[i][0]

    # Purchase Link
    purchase_url = container.find("div",{"class": "a-row a-spacing-none"}).div.                                                         a["href"].strip()
    
    # Used to scrape info for individual book < ------------------------------------
    book_link = requests.get(purchase_url, headers=headers)
    book_soup = BeautifulSoup(book_link.content,"html5lib")
    book_container = book_soup.find('div',{'class':'a-fixed-left-grid'})
    # Used to scrape info for individual book < ------------------------------------

    # Title
    try:
        title = container.find('h2',{"data-max-rows": "0"}).text.strip()
    except AttributeError as AttributeError:
        title = container.find('div', {'class': 'a-row a-spacing-mini sx-line-clamp-4'}).a['title']

    title = remove_comma(title)
    
    # Author
    author = ''
    author_pass = True
    author_list = book_container.findAll('span',{'class':'author notFaded'})

    try:
        author_list[0]
    except IndexError:
        author_pass = False
        author_container = book_soup.find('span',{'class':'author notFaded'})       
        author = author_container.find('span',{'class':'a-size-medium'}).text.                                                          strip().split()
        author = ' '.join(author).strip()

    if author_pass:
        for i in range(len(author_list)):
            author += author_list[i].a.text + ', '

        author = author.strip().strip(',')

    author = remove_comma(author)

    # Publish Date
    date = container.find('span',{'class':"a-size-small a-color-secondary"})                                                                  .text.strip()
    
    date = remove_comma(date)

    # Cost
    cost = container.find("span",{"class":"a-size-base a-color-base s-price"})                                                                 .text.strip()

    cost = remove_comma(cost)
    
    # Book Types (Audiobook, Paperback, Hardcover, Kindle)
    # Needs type permission to remove review count
    type_permission = ["Hardcover", "Kindle Edition", "Paperback",                                       "Audible Audiobook", '…More']

    # Notice findAll for this call
    book_type_list = container.findAll('a',                                                                         {'class':'a-size-small a-link-normal a-text-normal'})

    book_type = ''
    for i in range(len(book_type_list)):
        if book_type_list[i].text in type_permission:
            book_type += book_type_list[i].text + ', '

    book_type = book_type.strip().strip(',')
    
    book_type = remove_comma(book_type)

    # Rating
    rating = container.find('i', {'class':'a-icon a-icon-star a-star-5'})                                                                   .text.strip()

    rating = remove_comma(rating)
    
    # Review Number(reverse of Book Types)
    rating_list = container.findAll('a',                                                               {'class':'a-size-small a-link-normal a-text-normal'})

    review = rating_list[-1].text.strip()
    
    review = remove_comma(review)

    # Synopsis
    try:
        synopsis = book_container.find('div').p.text
    except AttributeError as AttributeError:
        synopsis = book_soup.find('div',{'id':'bookDescription_feature_div'}).noscript.text.strip()
    
    synopsis = punct_checker(synopsis)    
    synopsis = unicode_remover(synopsis)
    synopsis = remove_comma(synopsis)

    amazon_writer.writerow([purchase_url, title, author, date, cost, book_type, rating, review, synopsis])

    book_counter += 1
    percent_var = ((book_counter / 60) * 100)
    print(f'Book number {book_counter} complete... %{round(percent_var, 2)} complete.')