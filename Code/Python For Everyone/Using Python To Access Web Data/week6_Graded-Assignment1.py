import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')

print("Retrieving", url)
data = urllib.request.urlopen(url, context=ctx).read().decode()
print(f'Retrieved {len(data)} characters')

info = json.loads(data)

counts = [int(comment['count']) for comment in info['comments']]
print('Count:', len(counts))
print('Sum:', sum(counts))