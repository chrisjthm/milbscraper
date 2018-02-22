from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_argument(" - incognito")

browser = webdriver.Chrome(executable_path='/Users/chrismonsen/dev/milbscraper/util/chromedriver', chrome_options=option)
url = 'http://www.milb.com/player/index.jsp?player_id=665489'

browser.get(url)

# Wait 5 seconds for page to load
timeout = 5
try:
	WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='stats_table']")))
except TimeoutException:
	print("Timed out waiting for page to load")
	browser.quit()

stats_table_arr = browser.find_elements_by_xpath("//table[@class='stats_table']")
stats_table = [x.text for x in stats_table_arr]
print stats_table
