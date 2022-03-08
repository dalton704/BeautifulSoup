
from bs4 import BeautifulSoup
import requests


page = 1
book_title = []
# while loop to cycle through the pages
while page != 51:
    url = f'http://books.toscrape.com/catalogue/page-{page}.html'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    books = soup.find_all('article', class_='product_pod')
    # A for loop to find titles of all books on all pages
    for book in books:    
        for link in book.find_all('a'):
            if 'title' in link.attrs:
                Title = link.attrs['title']
                Price = book.find('p', class_ = 'price_color').text.replace('Â', '')
                Stars = book.find('p')
                Rating = str(Stars)[22: -137] + ' Star(s)'

                print(f'''
                     Book Title: {Title}
                     Book Price: {Price}
                     Book Rating: {Rating}
                        ''')
    page = page + 1
