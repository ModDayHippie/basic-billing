#this scripts preps an rpi for use of this program

#import moduals

import os
import time
#&import PyCrypt
#&pycrypt is not part of base and cannot be imported untill after it is installed via pip
import base64

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

#these lines install and tell user what is being installed

print('--------------------------------------------------------------------------------')
print('Installing System Updates')
print('--------------------------------------------------------------------------------')
time.sleep(3)
os.system('sudo apt-get update')
os.system('sudo apt-get install')
print('--------------------------------------------------------------------------------')
print('**System Updates Installed')
print('--------------------------------------------------------------------------------')
time.sleep(3)
print('Installing pip3')
print('--------------------------------------------------------------------------------')
time.sleep(3)
os.system('sudo apt install python-pip')
print('--------------------------------------------------------------------------------')
print('***pip3 has been installed**')
print('--------------------------------------------------------------------------------')
time.sleep(3)
print('Installing PySimpleGUI')
print('-------------------------------------------------------------------------------')
time.sleep(3)
#&os.system('sudo pip install cryptography')
os.system('sudo pip install PySimpleGUI')
print('-------------------------------------------------------------------------------')
print('**PySimple Has Been Installed**')
time.sleep(3)
print('All Moduals Have Been Installed')

#these commads ask if the user wants to run right after installing 

RUN = input('Do you want to run the billing login.py?(y/n):')

if RUN == 'y':
   os.system('sudo python3 login.py')
if RUN == 'n':
   input(exit())

#these are encrypthion scripts
#from Crypto.cipher import AES

#def encryption(privateInfo):
#   BLOCK_SIZE = 16
#   PADDING ='{'
#   pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
#   EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
#   secret = os.urandom(BLOCK_SIZE)
#   print 'encriptioon key:', secret
#   cipher = AES.new(secret)
#   encoded = EndcodeAES(cipher, pricateInfo)
   
