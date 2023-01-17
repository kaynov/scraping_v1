from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time
import undetected_chromedriver
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

driver = undetected_chromedriver.Chrome()

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
#
# # options.add_argument("--headless")
#
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# driver = webdriver.Chrome(options=options, executable_path=r"C:\pythonProjects\chrmdrv\chromedriver.exe")
#
# stealth(driver,
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )

data = {}
# counts = 0

count = 0
for page in range(2, 5):
        url = f"https://www.svyaznoy.ru/catalog/notebook/1738/page-{page}"
        driver.get(url)
        time.sleep(3)

        blocks = driver.find_elements(By.CLASS_NAME, "b-product-block__info")

        for block in blocks:
                item_name = block.find_element(By.CLASS_NAME, "b-product-block__name").text
                link = block.find_element(By.TAG_NAME, "a").get_attribute("href")
                print(link)
                count += 1
                print(count)
                data[item_name] = {'item_name': item_name,
                        'items_link': link,
                }


for link in data:
        driver.get(data[link]['items_link'])
        time.sleep(3)
        print(data[link]['items_link'])
        print(data[link]['item_name'])
        try:
                price = driver.find_element(By.CLASS_NAME, "b-offer-box__price-container").find_element(By.TAG_NAME,
                                                                                                        "span").text.replace(
                        ' ', '')
                if type(price) != int:
                        price = driver.find_element(By.CLASS_NAME, "b-offer-box__price-container").find_element(
                                By.CLASS_NAME,
                                "b-offer-box__price").text.replace(
                                ' ', '').replace('руб.', '')
                print(price)
        except:
                print('price error here>' + str(data[link]['items_link']))
                continue
        try:
                cpus = driver.find_element(By.CLASS_NAME, "b-product-view-box__tech-chars-table").find_elements(
                        By.TAG_NAME, "td")
                cpu = cpus[5].text
                ram = cpus[11].text
                if str(ram)[0] == '4':
                        ram = 4
                elif str(ram)[0] == '8':
                        ram = 8
                else:
                        ram = int(str(ram)[0:2])
                print(cpu)
                print(ram)
        except:
                print('cpu/ram error here>' + str(data[link]['items_link']))
                continue
        try:
                if cpu[0:3] == 'Int':
                        rate = (150 + ram * 200 + int(price) * -0.005)
                elif cpu[0:3] == 'AMD':
                        rate = (100 + ram * 200 + int(price) * -0.005)
                else:
                        rate = (50 + ram * 200 + int(price) * -0.005)
                print(rate)
        except:
                continue
        print()
        r = conn.execute(ins,
                         items_name=data[link]['item_name'],
                         price=price,
                         items_link=data[link]['items_link'],
                         rate=rate
                         )