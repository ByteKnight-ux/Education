import requests

# print(requests.get('http://httpbin.org/get', params={'key':'value'}).json()['origin'])

payload = {'key':'value'}
response = requests.post('http://httpbin.org/post', data=payload)
print(response.text)