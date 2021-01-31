#this scripts preps an rpi for use of this program

#import moduals

import os
import time
import PyCrypt
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

os.system('sudo apt-get pip3')
os.system('sudo pip install cryptography')
os.system('sudo pip install PySimpleGUI')


#these are encrypthion scripts
from Crypto.cipher import AES

def encryption(privateInfo):
#   BLOCK_SIZE = 16
#   PADDING ='{'
#   pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
#   EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
#   secret = os.urandom(BLOCK_SIZE)
#   print 'encriptioon key:', secret
#   cipher = AES.new(secret)
#   encoded = EndcodeAES(cipher, pricateInfo)
   
