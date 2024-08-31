from requests_html import HTMLSession
import pandas as pd
import time
import sys 
import random
from tqdm import tqdm

try:
    f = open("config.txt", encoding='utf-8' )
    url=f.readline().split('URL :')[1].strip()
    try:
        url=url.split('?page=')
        pageInit=int(url[1])
        url=url[0]
    except:
        pageInit=1
        url=url[0]
    print(url)
    maxvr=int(f.readline().split('LAST_PAGE_NUMBER (It can be left at 0 to get to the last possible page) :')[1].strip())
    times=float(f.readline().split('TIME(s) :')[1].strip())
    f.close()
except:
    print('\n'*5,'Make sure that the .confg.txt file is written correctly')
    time.sleep(8)
    sys.exit()

colum = {'Phone':[],'Titel':[],'City':[],'Page':[]}

url="https://carsoug.com/?page=1"

url=url.split('?page=')
urlNopage=url[0]
try:
    pageInit=int(url[1])
except:
    pageInit=1

session = HTMLSession()

while True:
    r = session.get(urlNopage+'?page='+str(pageInit))
    author = r.html.find('.infinite-scroll',first=True).find('.car_aa')
    if len(author)==0:
        break
    if maxvr!=0 and pageInit==maxvr+1:
        break
    #print(len(author))
    for ads in author:
        
        try:
            colum['Phone'].append(ads.xpath('//div/div/div[2]/div[4]/div[2]/button/@data-content')[0].strip())
        except:
            colum['Phone'].append(None)
                 
        try:
            colum['Titel'].append(ads.find('.navy-blue',first=True).text)
        except:
            colum['Titel'].append(None)
            
        try:
            colum['City'].append(ads.find('.blue-text',first=True).text)
        except:
            colum['City'].append(None)
            
        try:
            colum['Page'].append(pageInit)
        except:
            colum['Page'].append(None)
        
    print("Page Nomber :",pageInit)
    pageInit+=1
    time.sleep(times)


data=pd.DataFrame(colum)
data.to_excel(str(random.randint(0,99999))+'.xlsx',sheet_name='sheet1',index=False) 