from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.common.alert import Alert
import selenium
import pandas as pd
import csv
import time
import random

def searchVideoLength(webdriver, search_url, base_url, content_title):
	time.sleep(random.randint(3, 6))
	try:
		webdriver.get(search_url)
		content_length_info = webdriver.find_element_by_class_name('txt-type01').text
		content_length = int(content_length_info.split()[2][:-1])*60
	except Exception:
		webdriver.switch_to_alert().accept();
		
		"""webdriver.get(base_url)
		button_list = webdriver.find_elements_by_tag_name('button')
		ActionChains(webdriver).move_to_element(button_list[0]).click(button_list[0]).perform()

		input_content_title = webdriver.find_element_by_id('search-ip')
		input_content_title.send_keys(content_title)
		input_content_title.send_keys(Keys.ENTER)
	
		best_search_result = webdriver.find_element_by_xpath("//span/strong/span")
		ActionChains(webdriver).move_to_element(best_search_result).click(best_search_result).perform()
		content_length_info = webdriver.find_element_by_class_name('txt-type01').text
		content_length = int(content_length_info.split()[2][:-1])*60"""
		return -1

	return content_length

def main():
	base_url = "https://www.pooq.co.kr/player/vod.html?programid="
	driverPath = "./chromedriver"
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("referer=https://www.pooq.co.kr/")
	chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36")
	driver = webdriver.Chrome(driverPath, chrome_options=chrome_options)

	content_info = csv.reader(open('../content_info_file.csv', 'r', encoding = 'utf-8'))
	count = 0

	f = open('content_info_with_length.csv', 'w', encoding='utf-8', newline='')
	wr = csv.writer(f)

	for content in content_info:
		url = base_url+content[1]
		content_title = content[2]

		content_length = searchVideoLength(driver, url, base_url, content_title)
		content.append(content_length)

		wr.writerow(content)

	f.close()
	
if __name__ == '__main__':
	main()