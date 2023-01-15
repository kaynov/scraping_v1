from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time

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


for page in range(2):
        url = f"https://www.holodilnik.ru/digital_tech/notebook/sankt-peterburg/?page={page}"
        driver.get(url)
        time.sleep(3)

        blocks = driver.find_elements(By.CLASS_NAME, "product-specification")

        for block in blocks:
                item_name = block.find_element(By.CLASS_NAME, "product-name").find_element(By.TAG_NAME, "a").find_element(By.TAG_NAME, "span").text
                print(item_name)
                links = block.find_element(By.CLASS_NAME, "product-name").find_element(By.TAG_NAME, "a").get_attribute("href")
                print(links)
                price = block.find_element(By.CLASS_NAME, "item-order").find_element(By.CLASS_NAME, "price").text.replace(' ', '').replace('₽', '')
                print(price)


        # block_orders = driver.find_elements(By.CLASS_NAME, "item-order").find_element(By.CLASS_NAME, "price")
        # print(block_orders)

                # for block_order in block_orders:
                #         price = block_order.find_element(By.TAG_NAME, "a").get_attribute("href")

        # for post in posts:
        #         title = post.find_element(By.CLASS_NAME, )

# url = "https://www.holodilnik.ru/"
# driver.get(url)
# time.sleep(5)
# driver.quit()