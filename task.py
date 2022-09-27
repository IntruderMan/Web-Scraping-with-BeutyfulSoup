from email.quoprimime import header_check
import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.flipkart.com/search?q=iphone%2011%20%2064%20gb&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

page = requests.get(url)
# print(page)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('div',class_="col col-7-12")
# print(lists)

# title = soup.title 
# print(type(title.string))

container = soup.find(id='container')

with open('task.csv','w', encoding='utf8',newline='') as f:
    thewriter = writer(f)
    header = ['title','price','user_rating','specifications']
    thewriter.writerow(header)
    for item in container:   #strings
        title = item.find('div',class_="_4rR01T").text
        price = item.find('div',class_="_30jeq3 _1_WHN1").text
        user_rating = item.find('span',class_="_2_R_DZ").text
        specifications = item.find('div',class_="fMghEO").text
        info = [title,price,user_rating,specifications]
        thewriter.writerow(info)

