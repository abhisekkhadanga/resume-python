import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')

print("Retrieving", url)
data = urllib.request.urlopen(url, context=ctx).read().decode()
print(f'Retrieved {len(data)} characters')
tree = ET.fromstring(data)

lst = tree.findall('.//comment')
print('Count:', len(lst))

nums = [int(item.find('count').text) for item in lst]
print('Sum:', sum(nums))