from urllib.request import urlopen as url_request # Grabs the page
from bs4 import BeautifulSoup as soup # Parses the text


# Create file to write data to
filename = "products.csv"
f = open(filename, 'w')
header = "brand, product_name, shipping\n"
f.write(header)

for num in range(1, 21):
    my_url = f"https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=graphics%20card&bop=And&Page={num}&PageSize=36&order=BESTMATCH"

    # Opening connection, grabbing the page
    user_client = url_request(my_url)
    page_html = user_client.read()
    user_client.close()

    # Html parsing
    page_soup = soup(page_html, "html.parser")

    # HTML from website is <div = class="item-container  ">. Below the findAll function looks for 'div', and inside that div we make a dictionary with the 'class' attribute and the 'item-container' value
    containers = page_soup.findAll("div",{"class": "item-container"})

    # Removes 'You May Also Be Interested:' items in page.
    for i in range(4):
        containers.pop(0)

    # Shows which page were on while downloading
    print(num)

    # Parsing each container, finding elements we need (36 containers(graphics cards)). Adding counter to see which product errors out.
    container_counter = 0
    for container in containers:
        container_counter += 1
        print(container_counter)
        # Grabs brand of item
        try:
            brand = container.find('div', {'class': 'item-branding'}).a.img["title"]
        
        except AttributeError as aer:
            print("brand > AttributeError: 'NoneType' object has no attribute 'img'")
            title_container = container.findAll('a', {'class':'item-title'})   
            product_name = title_container[0].text.strip().split()
            brand = [product_name[num] for num in range(3)]
            brand = ' '.join(brand)
        
        except TypeError as ter:
            print("brand > TypeError: 'NoneType' object is not subscriptable")
            product_name = title_container[0].text.strip().split()
            brand = [product_name[num] for num in range(3)]
            brand = ' '.join(brand)

        # Grabs full title of item
        try:
            title_container = container.findAll('a', {'class':'item-title'})   
            product_name = title_container[0].text.strip()
        except AttributeError as aer:
            print("product_name > AttributeError: 'NoneType' object has no attribute 'img'")
            product_name = 'product_name not available for this item'
        

        # Grabs shipping cost of item
        try:
            shipping_container = container.findAll('li', 
                                                {'class': 'price-ship'})
            shipping_cost = shipping_container[0].text.strip()
        except AttributeError as aer:
            print("shipping_cost > AttributeError: 'NoneType' object has no attribute 'img'")
            shipping_cost = 'shipping_cost not available for this item'

        # Writes results to csv file
        f.write(brand + "," + product_name.replace(",", "|") + "," + shipping_cost + "\n")



f.close()


