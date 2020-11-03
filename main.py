from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup

page_num = 1

headers = "Page,Product,Link \n"
f = open("Nicerebate.csv", "w", encoding="utf-8")
f.write(headers)

while True:
    my_url = f"https://www.nicerebate.com/home/product?c_id=&search_text=&order_by=&per_page={page_num}"
    req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    containers = page_soup.findAll("div", {"class": "item-box"})
    for container in containers:
        title = container.findAll("div", {"class": "item-title"})
        before_product = title[0].text
        before_link = title[0].a["href"]
        link = f"https://www.nicerebate.com{before_link}"
        second_product = before_product.replace("\n","")
        product = second_product.replace("  ","")

        f.write(str(page_num) + "," + product.replace(",", "|") + "," + link + "\n")
        print(f"{page_num},{product},{link},")
    page_num += 1
