# Its a good idea to create a html file of a single div item you are trying to parse. It will make it easier to hone in on the variables you need.

# Try >>>
'''
# Opening connection, grabbing the page
    user_client = uReq(my_url)
    page_html = user_client.read()
    user_client.close()

    # Html parsing
    page_soup = soup(page_html, "html.parser")

    # HTML from website is <div = class="item-container  ">. Below the findAll function looks for 'div', and inside that div we make a dictionary with the 'class' attribute and the 'item-container' value
    containers = page_soup.findAll("div",{"class": "item-container"})
'''

# Then set something like container = containers[0]. Print container and create a new html file in vscode after running it through js beautifier online.



# Container finds (div with class: item-branding), finds the first 'a', finds 'img' in the first 'a', finds 'img' in 'a', and then finds 'title'.
'''
container.find('div', {'class': 'item-branding'}).a.img["title"]
'''



# You can skip a child key if you were to do:
'''
container.find('div', {'class': 'item-branding'})
'''



# Cycle through indexes, use in powershell to see which index you need
'''
for i in range(len(container.find('div', {'class': 'item-branding'}))):
    print('\n')
    container.find('div', {'class': 'item-branding'}).contents[i]
'''


# How to find text in a singled out group of code, notice that it returns a list with a single index
'''
>>> title_container = container.findAll('a', {'class':'item-title'})

>>>[<a class="item-title" href="https://www.newegg.com/Product/Product.aspx?Item=N82E16814487290&amp;Description=graphics%20card&amp;cm_re=graphics_card-_-14-487-290-_-Product" title="View Details"><i class="icon-premier icon-premier-xsm"></i>EVGA GeForce GTX 1050 Ti GAMING, 04G-P4-6251-KR, 4GB GDDR5, DX12 OSD Support (PXOC)</a>]<<<
'''

# We want the product name, which is 'EVGA GeForce GTX 1050 Ti GAMING, 04G-P4-6251-KR, 4GB GDDR5, DX12 OSD Support (PXOC)'
# which is the 'text' in index[0] in title_container

'''
>>> title_container[0].text
'EVGA GeForce GTX 1050 Ti GAMING, 04G-P4-6251-KR, 4GB GDDR5, DX12 OSD Support (PXOC)'
'''