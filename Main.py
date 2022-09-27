import requests
from bs4 import BeautifulSoup
from csv import writer
import pandas as pd

# Url of website
url = "https://www.flipkart.com/search?q=apple&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

page = requests.get(url)
# print(page)

# create lists for inserting data
List = []
Name = []
Price = []
Usrt = []
Spcfn = []

soup = BeautifulSoup(page.content, 'html.parser')

# lists = soup.find_all('div',class_="col col-7-12")        #List for all data
# for i in lists:
#     try:
#         List.append(i.text)                   
#     except:
#         List.append(None)

name = soup.find_all('div',class_ = '_4rR01T')            #Name of the Title
for i in name :
    try:
        Name.append(i.text)
    except:
        Name.append(None)

price = soup.find_all('div',class_ = '_1_WHN1')           #Price of the Mobile
for i in price:
    try:
        Price.append(i.text)
    except:
        Price.append(None)

user_rating = soup.find_all('div',class_='_3LWZlK')       #User rating of post 
for i in user_rating:
    if user_rating != float:
        Usrt.append(i.text)
    else:
        continue

specification = soup.find_all('ul',class_='_1xgFaf')      #specification of product
for i in specification:
    try:
        Spcfn.append(i.text)
    except:
        Spcfn.append(None)


print(len(name))
print(len(price))
print(len(user_rating))
print(len(specification))

Name = pd.Series(Name)   
Price = pd.Series(Price)   
Usrt = pd.Series(Usrt)  
Spcfn = pd.Series(Spcfn)

# Convert into Data Frame 
df=pd.DataFrame({'name':Name,'price':Price,'user_rating':Usrt,'specification':Spcfn})
df.head(10)

#Create CSV file 
df.to_csv('tas1.csv', encoding = 'utf-8-sig') 
