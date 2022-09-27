from pydoc import pager
from typing import Container
from xml.dom.minidom import Element
import requests
from bs4 import BeautifulSoup
url = "https://www.flipkart.com/search?q=iphone%2011%20%2064%20gb&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent,'html.parser')

# print(soup.prettify)

#tag
#navigablestring
#beautifulsoup
#comment
'''
markup = "<p><!--this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))
exit()
'''
# get the title of html page

title = soup.title 

# print(type(soup))
# print(type(title))
# print(type(title.string))

paras = soup.find_all('p')
# print(paras)

anchors = soup.find_all('a')

# print(anchors)


# print(soup.find('p')['class'])

# find all the Element with class lead

# print(soup.find_all('p',class_="lead"))

# get  the text from the soup 
# print(soup.find('p').get_text())
# print(soup.get_text())

anchors = soup.find_all('a')
all_links = set()

for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://www.flipkart.com/search?q=iphone%2011%20%2064%20gb&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off" +link.get('href')
        all_links.add(link)
        # print(linkText) 

container = soup.find(id='container')
# print(container.children)  # contents 
# .contents - A tag's children are available as a list (not fast)
# .children - A tag's children are available as a generator (fast)
# for elem in container.contents:
    # print(elem)

# for item in container.stripped_strings:   #strings
    # print(item)

# print(container.parent)
# print(container.parents)

# for item in container.parents:
#     print(item.name)

# print(container.next_sibling.next_sibling)
# print(container.previous_sibling.previous_sibling)

elem = soup.select('.modal-footer')  # (.loginModal,#loginModal) --
print(elem)
