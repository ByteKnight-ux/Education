import requests

reponse = requests.get('https://www.codewithharry.com')
# print(reponse.text)
with open('index.html', 'w') as f:
    f.write(reponse.text)