import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
import sys
import platform

# подключаю свои модули:
sys.path.append(os.path.join( os.path.dirname( __file__ ), '../../../moduls' ))
import functions_BfS 
import ParsProxy.pars_proxy as ParsProxy
import ParsProxy.run_ThroughProxy as run_Proxy



print(sys.maxsize)
print(2**31)

if sys.maxsize < 2**31 :
	is_bits_sistem = '32 bits'
else:
	is_bits_sistem = '64 bits'

print("is_bits_sistem: ", is_bits_sistem)




# 'E:\\Python project\\bots_for_sites\\moduls\\ParsProxy'] 