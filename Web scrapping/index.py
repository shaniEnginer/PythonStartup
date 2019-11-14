import requests
from bs4 import BeautifulSoup
courses=[]
test={}
for i in range(2,5):
    print(i)
    if  i <=2 :
        r= requests.get('https://www.aacomputercollege.com/category/courses/')
    else:
        print(i)
        r=requests.get(f'https://www.aacomputercollege.com/category/courses/page/{i}/')


    r=r.content
    soup= BeautifulSoup(r,"html.parser")
    for heading in soup.find_all('h2'):
        for content in soup.find_all('div',{'class':'post-excerpt'}):

            test[heading.text.strip('\n')]=content.text

        # courses.append(i.text.strip('\n'/))
        # print(i.text)


# print(courses)
print(test)