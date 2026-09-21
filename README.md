# scraping_v1
To run the project, you need to install the required libraries from the requirements file and the Chrome WebDriver.

Internet access :)

And some faith that the anti-bot protection on the websites has not changed :) It worked for me for four days in a row.

Two websites are scraped: www.holodilnik.ru and www.svyaznoy.ru. More than 1,000 product items can be collected. The data is stored in PostgreSQL.

The rating is calculated as follows.

For processors, there are three categories:

if Intel: 150

if AMD: 100

anything else: 50

svg

RAM has a weight of 200 per 1 GB.

Price has a weight of -0.005.

Top 5 laptops )))

The marketing team still needs to work on the evaluation criteria )))

https://www.holodilnik.ru/digital_tech/notebook/hp/45m81es/sankt-peterburg/
https://www.holodilnik.ru/digital_tech/notebook/redmi/xma2007_aj/sankt-peterburg/
https://www.holodilnik.ru/digital_tech/notebook/apple/macbook_air_13_late_2020_mgn73ru_a_space_gray/sankt-peterburg/
https://www.holodilnik.ru/digital_tech/notebook/hiper/workbook_q15uhr_kc29a2b4/sankt-peterburg/
https://www.holodilnik.ru/digital_tech/notebook/asus/90nb0ty3_m002y0/sankt-peterburg/

