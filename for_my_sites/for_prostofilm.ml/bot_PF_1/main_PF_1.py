import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
import sys

# подключаю свои модули:
sys.path.append(os.path.join( os.path.dirname( __file__ ), '../../../moduls' ))
import functions_BfS 
import ParsProxy.pars_proxy as ParsProxy



def main():

	'''
		Получить установленное количество запусков на текущие сутки 
		Проверить количество выполненных запусков за текущие сутки
		если запуски ещё нужны
			Проверить наличие актуального proxyList_file
			если нет 
				Запустить ParsProxy.get_ProxyList()
			если запуск ParsProxy.get_ProxyList() был успешен
				Запустить  bot_PF_1() через proxy (ParsProxy.run_ThroughProxy(bot_PF_1,proxyList))
			если запуск bot_PF_1() через proxy был успешен
				Увеличить счётчик успешных запусков на 1
				собрать статистику
				сохранить статистику
				если нужно 
					Запустить  bot_PF_1() через proxy (ParsProxy.run_ThroughProxy(bot_PF_1,proxyList))

	'''

	
	proxyList_file = 'proxylist 03-03-2021 16.12.57 .json'		# актуальный прокси лист
	URL = 'http://prostofilm.ml/'
	
	amounth_start_of_bot = 3
	count_start_of_bot = 0
	count_proxyIP = 0


	# URL = 'http://prostofilm.ml/films/1034049/'	# for tests
	# URL = 'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'		# страница тестирования невидимости автоматического управления браузером

	path_proxyList_dir = os.path.join( os.path.dirname( __file__ ), '../../../../ParsProxy/Proxylist/' + proxyList_file )
	with open(path_proxyList_dir) as file_handle:	# получаю прокси из файла в список
		list_Proxy = json.load(file_handle)


	

	while (amounth_start_of_bot > count_start_of_bot):
		


		run_ThroughProxy(function,proxylist)






if __name__ == '__main__':
	main()