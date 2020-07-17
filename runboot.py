import requests
from bs4 import  BeautifulSoup as bs
url = "https://www.runoob.com/python/python-100-examples.html"
headersr= {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
response = requests.get(url,headersr).text

example_htnl = bs(response,"lxml")
find = example_htnl.find(id="content").find_all_next("a")
##print(response)
print(find) # a标签
print(len(list(find)))
"""
F12--network--python-100-examples--
request-header:
  cookies
  user-agent:
  Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
"""