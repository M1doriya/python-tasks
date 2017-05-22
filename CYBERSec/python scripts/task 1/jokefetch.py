import requests
import json
from bs4 import BeautifulSoup
from random import randint
import time
page_num = randint(1, 11)
jokes={}
url=("http://123hindijokes.com/very-funny-jokes/"+str(page_num))
r = requests.get(url)
data=BeautifulSoup(r.content,"lxml")
joke=data.find_all("ul",{"class":"statusList"})
for i in joke:
    joke1 =i.find_all('li')
    for joke2 in joke1:
        joke3=joke2.get_text()
        jokes[1]=joke3
with open("hindijoke.json",'w') as joke3:
    
    json.dump(jokes,joke3,ensure_ascii=False,indent=8)
    time.sleep(15)
    
