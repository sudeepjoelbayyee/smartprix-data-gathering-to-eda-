from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))

driver.get('https://www.smartprix.com/mobiles')
time.sleep(1)

driver.find_element(By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(1)

old_height = driver.execute_script('return document.body.scrollHeight')
while True:
    try:
        driver.find_element(By.XPATH,value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    except:
        break

    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    print(old_height)
    print(new_height)
    if new_height == old_height:
        break
    old_height = new_height

html = driver.page_source
with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)