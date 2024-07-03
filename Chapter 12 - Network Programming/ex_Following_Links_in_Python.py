import ssl
from urllib.request import urlopen

from bs4 import BeautifulSoup

# list for numbers ??
content_list = list()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # pull the contents of the tag and append to the list
    content_list.append(int(tag.contents[0]))

    # total the values
    total = sum(content_list)

# print the total
print(total)
