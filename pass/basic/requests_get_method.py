import requests


#  requests.get(url)  -- response object
response = requests.get('https://www.google.com')


#  Content
#  response.content
print(response.content)

#  Status codes
"""
1xx     Informational
2xx     Success
3xx     Redirection
4xx     Client Error
5xx     Server Error
"""
print(response.status_code)


#  Headers returned

#  response.headers
# print(response.headers)
for key, value in response.headers.items():
    print(key, '    ', value)

