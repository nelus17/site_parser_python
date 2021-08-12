import requests
from bs4 import BeautifulSoup as BS

r = requests.get("your_link")
html = BS(r.content, 'html.parser')

for el in html.select("your html_tag_classes"):
    title = el.select('your_element_classes')
    print(title[0].text)

# parse products_name or other info that you need.
