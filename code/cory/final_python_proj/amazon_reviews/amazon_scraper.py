from bs4 import BeautifulSoup # Parses the text
import csv
import requests

# Book counter
book_counter = 0

# Trying to fix Amazon filter issue (works)
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

# Url to scrape from, use page # to loop from pages.
page_url = "https://www.amazon.com/s/ref=sr_pg_2?rh=n%3A283155%2Cn%3A%211000%2Cn%3A25%2Cn%3A16272&page=1&sort=review-rank&ie=UTF8&qid=1541699809&lo=stripbooks"

# Opening connection, grabbing the page
amazon_link = requests.get(page_url, headers=headers)

# HTML parsing
page_soup = BeautifulSoup(amazon_link.content,"html5lib")

# Create file to write data to
filename = "scrape_data.csv"
amazon_writer = csv.writer(open(filename, 'w', newline=''))
amazon_writer.writerow(['Purchase Link', 'Title', 'Author', 'Publish Date', 'Cost', 'Book Types', 'Rating', 'Review Number', 'Synopsis'])

# header = 'Purchase Link, Title, Author, Publish Date, Cost, Book Types, Rating, Review Number, Synopsis\n'

# with open(filename, 'w') as f:
#     f.write(header)
# f.close()

# Main containers to scrape data from
containers = []
for num in range(60):
    container = page_soup.findAll("li",{"id": f"result_{num}"})
    containers.append(container)

#Main Loop < -------------------------------------------------------
# for i in range(37, 38):
for i in range(len(containers)):
    # Need to use [0][0] to point at the string inside the list, not the list itsself
    container = containers[i][0]

    # Purchase Link
    purchase_url = container.find("div",{"class": "a-row a-spacing-none"}).div.                                                         a["href"].strip()
    
    # print(purchase_url)

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
    
    # print(title)

    # Author(Couldn't figure out how to add second title, Audio Book kept returning)
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

        # print(author)                                              

    if author_pass:
        for i in range(len(author_list)):
            author += author_list[i].a.text + ', '

        author = author.strip().strip(',')
        # print(author)

    # Publish Date
    date = container.find('span',{'class':"a-size-small a-color-secondary"})                                                                  .text.strip()
    
    # print(date)

    # Cost
    cost = container.find("span",{"class":"a-size-base a-color-base s-price"})                                                                 .text.strip()
    
    # print(cost)

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
    
    # print(book_type)

    # Rating
    rating = container.find('i', {'class':'a-icon a-icon-star a-star-5'})                                                                   .text.strip()
    
    # print(rating)

    # Review Number(reverse of Book Types)
    rating_list = container.findAll('a',                                                               {'class':'a-size-small a-link-normal a-text-normal'})

    review = rating_list[-1].text.strip()
    
    # print(review)

    # Synopsis
    try:
        synopsis = book_container.find('div').p.text
    except AttributeError as AttributeError:
        synopsis = book_soup.find('div',{'id':'bookDescription_feature_div'}).noscript.text.strip()
    
    # # Function to help check grammar.
    def punct_checker(sentance):

        sentance = list(sentance)
        end_punctuation = ['.', '!', '?', ',']
        
        for i in range(len(sentance)):
            for punct in end_punctuation:
                if not sentance[-1]:
                    if sentance[i] == punct:
                        if sentance[i + 1] == ' ':
                            pass
                        else:
                            sentance.insert((i+1), ' ')
            
        # Might replace ',' with + for easier csv

        # for i in range(len(sentance)):
        #     if sentance[i] == ',':
        #         sentance[i].replace(',', '+')

        sentance = ''.join(sentance).strip()
        # sentance = '"' + sentance + '"'
        return sentance
    
    def unicode_remover(sentance):

        sentance = list(sentance)
        return ''.join([i if ord(i) < 128 else '' for i in sentance])

    synopsis = unicode_remover(synopsis)
    synopsis = punct_checker(synopsis)
    # print(synopsis)

    # Writes to file
    amazon_writer.writerow([purchase_url, title, author, date, cost, book_type, rating, review, synopsis])
    
    # synopsis = 'test'

    # with open(filename, 'w') as f:
    #     f.write(purchase_url + ',' + title + ',' + author + ',' + date + ',' + cost + ',' + book_type + ',' + rating + ',' + review + ',' + synopsis + '\n')
    # f.close()    


    '''
    Having issues with a·byss[əˈbis] characters, need to figure out how to accept or replace them.
    '''
    

    book_counter += 1
    print(f'Book number {book_counter} complete.')
   


