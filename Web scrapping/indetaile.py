import requests
from bs4 import BeautifulSoup

r= requests.get('https://www.aacomputercollege.com/category/courses/')
r=r.content
soup= BeautifulSoup(r ,"html.parser")
content=soup.find_all('div',{'class':'post-excerpt'})
for i in content:
    print(i.text.strip('\n'))