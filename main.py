import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.amazon.co.uk'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14.5; rv:115.0) Gecko/20100101 Firefox/115.0'
}




top_products = []
top_products_url = []
top_products_rating = []
top_products_price = []

for page in range(1, 3):
    r = requests.get(f"https://www.amazon.co.uk/Best-Sellers-Beauty/zgbs/beauty/ref=zg_bs_pg_{page}_beauty?_encoding=UTF8&pg={page}")
    soup = BeautifulSoup(r.content, 'lxml')

    productlist = soup.find_all('div', class_="_cDEzb_p13n-sc-css-line-clamp-3_g3dy1")
    for product in productlist:
        top_products.append(str(product.text))
#print(len(top_products))

    product_url_list = soup.find_all('a', class= "a-link-normal")

    for url in product_url_list:
        top_products_url.append(baseurl + str(url['href']))
        #print(top_products_url)

print(len(top_products_url))