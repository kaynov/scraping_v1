from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time
import databases
from sqlalchemy import create_engine
from typing import List
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, ForeignKey, create_engine, \
    func, select, Date, desc, literal_column, insert
from datetime import datetime
from models import metadata, comps
import psycopg2


engine = create_engine('postgresql://postgres:s1t@localhost/test_1')
conn = engine.connect()
ins = insert(comps)


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r"C:\pythonProjects\chrmdrv\chromedriver.exe")

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

data = {}
# counts = 0


for page in range(1, 20):
        url = f"https://www.holodilnik.ru/digital_tech/notebook/sankt-peterburg/?page={page}"
        driver.get(url)
        time.sleep(1)

        blocks = driver.find_elements(By.CLASS_NAME, "product-specification")

        for block in blocks:
                item_name = block.find_element(By.CLASS_NAME, "product-name").find_element(By.TAG_NAME, "a").find_element(By.TAG_NAME, "span").text
                link = block.find_element(By.CLASS_NAME, "product-name").find_element(By.TAG_NAME, "a").get_attribute("href")
                price = block.find_element(By.CLASS_NAME, "item-order").find_element(By.CLASS_NAME, "price").text.replace(' ', '').replace('₽', '')
                if '\n' in price:
                        price = price.split('\n')[1]
                data[item_name] = {'item_name': item_name,
                        'items_link': link,
                        'price': price
                }


for link in data:
        driver.get(data[link]['items_link'])
        time.sleep(1)

        cpu = driver.find_element(By.CSS_SELECTOR,
                                  '#opisAndTTH > div.det-content-block > div.det-content-inner > div > div:nth-child(7) > div.params-list__item-value > span').text
        try:
                ram = float(driver.find_element(By.CSS_SELECTOR,
                                      '#opisAndTTH > div.det-content-block > div.det-content-inner > div > div:nth-child(12) > div.params-list__item-value > span').text)
        except:
                print(data[link]['items_link'])
                print(data[link]['price'])
                print(ram)
                ram = 8

        rate = 0
        try:
                if cpu[0:3] == 'Int':
                        rate = (150 + ram * 200 + (float(data[link]['price']) * -0.005))
                elif cpu[0:3] == 'AMD':
                        rate = (100 + ram * 200 + (float(data[link]['price']) * -0.005))
                else:
                        rate = (50 + ram * 200 + (float(data[link]['price']) * -0.005))
        except:
                continue

#         print(data[link]['item_name'])
#         print(float(data[link]['price']))
#         print(data[link]['items_link'])
# #        print(rate)
#         counts += 1
#         print(counts)
#         print()
        r = conn.execute(ins,
                         items_name=data[link]['item_name'],
                         price=float(data[link]['price']),
                         items_link=data[link]['items_link'],
                         rate=rate
                         )




