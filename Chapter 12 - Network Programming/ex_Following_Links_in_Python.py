import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_list = list()

# first link
url = input("Enter URL: ")

#parameters
repeat = int(input("Enter count: "))
position = int(input("Enter position: "))

for i in range(repeat):
    # get the html from the link provided
    html = urllib.request.urlopen(url, context=ctx).read()
    # use beautiful soup to parse the html
    soup = BeautifulSoup(html, 'html.parser')
    # retrieve all of the anchor tags
    tags = soup('a')
    counter = 0
    
    # loop through the tags
    for tag in tags:
        counter = counter +1
        if counter > position:
            break
        # set url to latest page overwriting Fikret
        content = tag.contents[0]
        url = tag.get('href', None)
        
# print the last name in the list
print(content)  

        
