from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import random
import sys

try:
    f = open("URL-Search.txt", encoding='utf-8' )
    url=f.read().strip()
    f.close()
except:
    print('\n'*5,'Make sure that the "URL-Search.txt" file is written correctly')
    time.sleep(8)
    sys.exit()

list1 = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

driver.implicitly_wait(7)  
                                      
try:
    driver.find_element(by=By.XPATH,value="//*[@id='__next']/div[2]/div[2]/div/div[2]/div[5]/div/div/button").click()
except:
    driver.find_element(by=By.XPATH,value="//*[@id='__next']/div[2]/div[2]/div/div[2]/div[4]/div/button").click()

time.sleep(3)

def scroll():
    driver.execute_script("window.scrollTo(0, parseInt(document.body.scrollHeight)-parseInt(626));")
    time.sleep(1)
    
numkent=1
numerror=0 #30
nubold=0
while True:
    try:
        a = driver.find_element(by=By.XPATH,value=f"//*[@id='postsList']/div[{numkent}]/div[1]/div[1]/a").get_attribute("href")
        tim = driver.find_element(by=By.XPATH,value=f"//*[@id='postsList']/div[{numkent}]/div[1]/div[2]/div[2]/span").text
        f = open("LenksHaraj.txt", "a")
        f.write(f'{a}<|>')
        print(numkent,tim,a)
        f.close()
        
        numkent+=1
    except:
        if nubold!=numkent:
            nubold=numkent
            try:
                scroll()
            except:
                numerror+=1              
        else:
            numkent+=1    
    if numerror==30:
        break