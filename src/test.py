from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.common.alert import Alert
import time

base_url = "https://www.pooq.co.kr/player/vod.html?programid=CR02_DN0000000121"
driverPath = "./chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("referer=https://www.pooq.co.kr/")
chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36")
driver = webdriver.Chrome(driverPath, chrome_options=chrome_options)

try:
	driver.get(base_url)
except Exception:
	alert = driver.switch_to_alert()
	alert.accept()

base_url = "https://www.pooq.co.kr/player/vod.html?programid=S01_V0000010171"
#driverPath = "./chromedriver"
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("referer=https://www.pooq.co.kr/")
#chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36")
#driver = webdriver.Chrome(driverPath, chrome_options=chrome_options)
try:
	driver.get(base_url)
except Exception:
	alert = driver.switch_to_alert()
	alert.accept()

base_url = "https://www.pooq.co.kr/player/vod.html?programid=S01_V0000353336"
#driverPath = "./chromedriver"
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("referer=https://www.pooq.co.kr/")
#chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36")
#driver = webdriver.Chrome(driverPath, chrome_options=chrome_options)
try:
	driver.get(base_url)
except Exception:
	alert = driver.switch_to_alert()
	alert.accept()
	

time.sleep(5)