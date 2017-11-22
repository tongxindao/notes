import requests

r = requests.get("https://www.shiyanlou.com")
print("Status code: {0}".format(r.status_code))
print("header: {0}".format(r.headers["content-type"]))
print("text: {0}".format(r.text))

s = requests.get("https://api.github.com")
print("github api json data: {0}".format(s.json()))
