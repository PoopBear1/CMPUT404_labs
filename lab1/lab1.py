import requests

# print(requests.__version__)
var = requests.get("http://www.google.com")
r = requests.get("https://raw.githubusercontent.com/PoopBear1/CMPUT404-Labs/master/lab1.py")
print(var.content)
print(r.content)