#this scripts preps an rpi for use of this program

#import moduals

import os
import time


#Info about moduals about to be installed

print('---------------------------------------------------------------------------------')
print('Modual Installer For Basic-Billing.py By:MDH')
print('---------------------------------------------------------------------------------')
time.sleep(3)
print('This program will instal all the needed modual for python to run correctly')
print('this program is under a free to use licence')
print('---------------------------------------------------------------------------------')
time.sleep(3)
print('Moduals to be installed are:')
time.sleep(3)
print('rasbian system updates')
print('Python3')
print('pip3')
print('PySimpleGUI')
print('--------------------------------------------------------------------------------')
time.sleep(5)

#EULA AREA

EULA = input('do you agree to theses changes to your computer (y/n):')

if EULA == 'n':
   print('exiting program')
   input(exit())


