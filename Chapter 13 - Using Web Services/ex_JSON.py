# import libs
import json
import ssl
import urllib.error
import urllib.parse
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# variable
total_counter = 0

#address = 'http://py4e-data.dr-chuck.net/comments_42.json'

address = input('Enter location: ')
data = urllib.request.urlopen(address, context=ctx).read()

info = json.loads(data)

for item in info['comments']:
  total_counter += int(item['count'])
print(total_counter)
