import requests
from fake_useragent import UserAgent

#  Use UserAgent to change headers and fool site that a browser is accessing, not a crawler.
ua = UserAgent()
header = {'user-agent': ua.chrome}

page = requests.get('https://www.google.com', headers=header)
print(page.content)

#  Put timeout parameter so code could continue if server doesn't respond.
page = requests.get('https://www.google.com', timeout=3)
