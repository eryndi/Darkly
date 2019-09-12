#!/sgoinfre/goinfre/Perso/dwald/anaconda3/bin/python

import requests
url = "http://10.11.200.225/?page=member&id=1%3D1&Submit=Submit#"
data = requests.get(url)
print("hello")
print(data)
