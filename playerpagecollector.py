from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException


class PlayerPageCollector:

	PLAYER_IDS = {"VLADIMIRGUERREROJR":665489, "FORRESTWHITLEY":666215}
	base_url = 'http://www.milb.com/player/index.jsp'
	chromedriver_path = 'util/chromedriver'

	def add_player_id(self, lastname, firstname, id):
		player_name_key = self.get_player_name_key(lastname, firstname)
		self.PLAYER_IDS[player_name_key] = id

	def get_player_name_key(self, lastname, firstname):
		player_name_key = (firstname.upper() + lastname.upper()).replace(' ','')
		return player_name_key

	def get_player_page_url_by_name(self, lastname, firstname):
		player_name_key = self.get_player_name_key(lastname, firstname)
		return self.base_url + '?player_id=' + str(self.PLAYER_IDS[player_name_key])

	def get_player_page_url_by_id(self, player_id):
		return self.base_url + '?player_id=' + str(player_id)

	def setupBrowser(self):
		option = webdriver.ChromeOptions()
		option.add_argument(" - incognito")

		browser = webdriver.Chrome(executable_path=self.chromedriver_path, chrome_options=option)
		return browser

	def get_player_page(self, url) :
		browser = self.setupBrowser()
		browser.get(url)

		# Wait 5 seconds for page to load
		timeout = 5
		try:
			WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='stats_table']")))
		except TimeoutException:
			print("Timed out waiting for page to load")
			browser.quit()
		return browser

	def get_stats_table_data(self, url):
		browser = self.get_player_page(url)
		stats_table = browser.find_elements_by_xpath("//table[@class='stats_table']")
		return stats_table[0].text.splitlines()

	def get_latest_game_data(self, url):
		stats_arr = self.get_stats_table_data(url)
		headers = stats_arr[0].split(' ')
		data = stats_arr[-2].split(' ')
		latest_game_data = {}
		for i in list(range(len(data) - 1)):
			latest_game_data[headers[i]] = data[i]
		return latest_game_data	
