from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")  # comment it to run with normal way

#driver = webdriver.Chrome(chrome_options=options)  # DeprecationWarning: chrome_options
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('http://books.toscrape.com/')

# find some elements
elements = driver.find_elements_by_xpath('//div[@class="side_categories"]//ul//ul//a')

# display elements
for item in elements:
    print('category:', item.text)

driver.close()
