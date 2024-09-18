
import sys # python lookup all the paths in sys to import the module

sys.path.append('/user/walelign/desktop') # this is to include the path which is outside the python path

import importModule as im # we can also import the function only from the module
from importModule import * # import all modules from the module

import random,math,string,datetime,calendar,time,datetime,os
print(sys.path) # displays the current working directory for python

print(math.pi)

today = datetime.datetime.today()
print(today)


print(random.choice)

print(calendar.isleap(2017))

print(os.getcwd()) # displays the current working directory

print(os.__file__) # displays the current working directory 