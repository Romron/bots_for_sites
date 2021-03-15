import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
import sys

# подключаю свои модули:
sys.path.append(os.path.join( os.path.dirname( __file__ ), '../../../moduls' ))
import functions_BfS 
import bot_PF_1
import ParsProxy.pars_proxy as ParsProxy
import ParsProxy.run_ThroughProxy as r_ThP


def main():

	'''
		Проверить наличие лог файла

		Получить установленное количество запусков на текущие сутки 
			неудачных запусков
			удачных запусков
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

	amounth_start_of_bot = 3
	count_start_of_bot = 0
	count_proxyIP = 0
		
	proxyList_file = 'proxylist 15-03-2021 13.39.59 .json'
	URL = 'http://prostofilm.ml/' 

	path_proxyList_dir = os.path.join( os.path.dirname( __file__ ), 'proxy_lists')
	# ParsProxy.get_ProxyList(path_proxyList_dir)

	path_proxyList_file = path_proxyList_dir + '/' + proxyList_file

	with open(path_proxyList_file) as file_handle:	# получаю прокси из файла в список
		proxyList = json.load(file_handle)

	# print("proxyList = ", proxyList)

	r_ThP.run_ThroughProxy(proxyList,bot_PF_1.Actions,URL,flag_check_Captcha=True,flag_headless=True)






if __name__ == '__main__':
	main()