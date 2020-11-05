import requests, sqlite3
from bs4 import BeautifulSoup

url = 'http://www.bom.gov.au/places/qld/brisbane/forecast/detailed/'

Page = requests.get(url)
Soup = BeautifulSoup(Page.text, 'html.parser')
outputlist = []


# find location based on title
Location = Soup.find('title').text
outputlist.append(Location)

# find Rain Chance based on title
RainChance = Soup.findAll('td')
outputlist.append(Location)


# find Today based on class
today = Soup.find('h2', class_="pointer").text
outputlist.append(today)

# find table based on summary
TempTable = Soup.find('table', summary ="3 Hourly Temperatures Forecast for Thursday").text.strip("")
outputlist.append(TempTable)

# find date published based on tag
# date = Soup.find('span', itemprop ="datePublished").text
# outputlist.append(date)

# find image address based on tag
# img = Soup.find('img', itemprop="image")['src']
# outputlist.append(img)

# find rating based on tag
# rating = Soup.find('span', itemprop="ratingValue").text.strip()
# outputlist.append(rating)

# ------------------------Book SCaper Stuff. WIll fix later ----------- #
# def addbook(bookdata):
    # connect = sqlite3.connect('bookscrape.db')
    # c = connect.cursor()
    # sqlcommand = "INSERT INTO books (title, price, datePub, imageLink, rating) VALUES (?,?,?,?,?)"
    # c.execute(sqlcommand, bookdata)

    # connect.commit()
    # connect.close()


print(Location)
print(today)
# print(TempTable)
# print(date)
# print(img)
# print(rating)

# outputtuple = tuple(outputlist)
# addbook(outputtuple)

# ------------- THIS SHIT DOESN'T WORK ---------------- #