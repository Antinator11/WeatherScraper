import requests, sqlite3
from bs4 import BeautifulSoup

url = 'http://www.bom.gov.au/places/qld/brisbane/forecast/detailed/'

Page = requests.get(url)
Soup = BeautifulSoup(Page.text, 'html.parser')
outputlist = []

# find title based on tag
today = Soup.find('h2', class_="pointer").text
outputlist.append(today)

# find price based on tag
price = Soup.find('span', class_ ="sale-price").text
outputlist.append(price)

# find date published based on tag
date = Soup.find('span', itemprop ="datePublished").text
outputlist.append(date)

# find image address based on tag
img = Soup.find('img', itemprop="image")['src']
outputlist.append(img)

# find rating based on tag
rating = Soup.find('span', itemprop="ratingValue").text.strip()
outputlist.append(rating)

# ------------------------Book SCaper Stuff. WIll fix later ----------- #
# def addbook(bookdata):
    # connect = sqlite3.connect('bookscrape.db')
    # c = connect.cursor()
    # sqlcommand = "INSERT INTO books (title, price, datePub, imageLink, rating) VALUES (?,?,?,?,?)"
    # c.execute(sqlcommand, bookdata)

    # connect.commit()
    # connect.close()


print(today)
print(price)
print(date)
print(img)
print(rating)

# outputtuple = tuple(outputlist)
# addbook(outputtuple)