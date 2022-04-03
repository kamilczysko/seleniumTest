from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

s=Service(ChromeDriverManager().install())

options = Options()
options.add_argument("--headless")  # comment it to run with normal way
driver = webdriver.Chrome(service=s, options=options)

driver.get('http://books.toscrape.com/')

# find some elements
elements = driver.find_elements_by_xpath('//div[@class="side_categories"]//ul//ul//a')

# display elements
for item in elements:
    print('category:', item.text)

driver.close()
