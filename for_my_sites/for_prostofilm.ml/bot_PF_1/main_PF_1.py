import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import bot_PF_1 
# from bot_PF_1 import main_bot_PF_1



def main():
	
	URL = 'http://prostofilm.ml/'

	# URL = 'http://prostofilm.ml/films/1034049/'	# for tests
	# URL = 'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'		# страница тестирования невидимости автоматического управления браузером

	pathDriver = os.path.dirname(os.path.abspath(__file__)) + "\\geckodriver.exe"
	options = Options()
	options.set_preference("dom.webdriver.enabled", False)
	browser = webdriver.Firefox(executable_path=pathDriver,options=options)


	bot_PF_1.main_bot_PF_1(URL,browser)



















if __name__ == '__main__':
	main()