import requests

response = requests.get("http://192.168.56.1:5000/teste")
print(response.text)