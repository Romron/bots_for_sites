import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
import sys

# подключаю свои модули:
sys.path.append(os.path.join( os.path.dirname( __file__ ), '../../../moduls' ))
import functions_BfS 
import ParsProxy.pars_proxy as ParsProxy
import ParsProxy.run_ThroughProxy as r_ThP





proxyList_file = 'proxylist 13-03-2021 18.27.46 .json'
URL = 'http://prostofilm.ml/' 

path_proxyList_dir = os.path.join( os.path.dirname( __file__ ), 'proxy_lists')
# ParsProxy.get_ProxyList(path_proxyList_dir)

path_proxyList_file = path_proxyList_dir + '/' + proxyList_file

with open(path_proxyList_file) as file_handle:	# получаю прокси из файла в список
	proxyList = json.load(file_handle)

# print("proxyList = ", proxyList)

r_ThP.run_ThroughProxy(proxyList,functions_BfS.bot_PF_1,URL,flag_check_Captcha=True)




