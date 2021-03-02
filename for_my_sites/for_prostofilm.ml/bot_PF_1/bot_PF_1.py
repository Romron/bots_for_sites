from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import os
import time
import random

def main_bot_PF_1(URL,browser):

	try:
		browser.get(URL)
		browser.implicitly_wait(10)
		
	except Exception as e:
		raise
	else:

		list = browser.find_elements_by_tag_name('a')	# поличить список всех ссылок на главной странице сайта
		
		count_try_clicks_links = 0
		while True:
			try:
				time.sleep(random.uniform(1,30))		# случайное число с плавающей точкой
				random.choice(list).click()	# выбор случайной ссылки из списка и переход по ней
				break
			except Exception as e:
				# raise e
				count_try_clicks_links += 1
				print(count_try_clicks_links, '. попытка кликнуть случайную ссылку' )

		# !!!	
			# сделать скрол страницы 
			# так что бы выбранный элемент стал видимым
		# !!!


		# Собрать все ссілки на страницы фильмов
		list_elements = browser.find_elements_by_xpath('//html/body/div[1]/div/div/div/article/div/div/div/a/h2')
		time.sleep(random.uniform(1,30))		# случайное число с плавающей точкой

		count_try_clicks_films = 0
		while True:
			try:
				element_Wait = WebDriverWait(browser, 30).until(
					EC.element_to_be_clickable((By.XPATH, '//html/body/div[1]/div/div/div/article/div/div/div/a/h2'))
				)
				time.sleep(random.uniform(1,30))		# случайное число с плавающей точкой
				random.choice(list_elements).click()	# выбор случайной ссылки из списка и переход по ней на страницу фильма
				break
			except Exception as e:
				# raise e
				count_try_clicks_films += 1
				print(count_try_clicks_links, '. попытка кликнуть случайный фильм' )

		# запускаю плеер
		time.sleep(random.uniform(1,30))		# случайное число с плавающей точкой

		try:
			element = browser.find_element_by_xpath('//*[@id="yohoho"]')
			element.click()
			time_look_filme = random.uniform(60,2400)
			print('Установленное время просмотра фильма: ', round(time_look_filme/60), ' минут')
			time.sleep(time_look_filme)		# случайное число с плавающей точкой
		except Exception as e:
			print(e) 
			print('Ошибка запуска плеера')


	finally:
		pass
		browser.close()
		browser.quit()