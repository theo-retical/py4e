import ssl
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# variables
total_counter = 0

# loop to read the xml file
while True:
    # get address and break if empty
    address = input('Enter location: ')
    if len(address) < 1:
        break
    # read xml data from inputted address
    data = urllib.request.urlopen(address, context=ctx).read()

    # parse the xml to be usable
    tree = ET.fromstring(data.decode())
    # search for all instances of count
    counts = tree.findall('.//count')
    # read through counts and extract the number
    for count in counts:
        # only check if not none, remove any whitespaces
        if count.text is not None and count.text.strip():
            # convert count value to int and add to total counter
            total_counter = total_counter + int(count.text)
    print(total_counter)
