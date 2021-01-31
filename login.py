#this is the login py for th ebasic billing script

#import moduals on  these lines
import os
import time
import PySimpleGUI as sg

#these lines are the credentials, they are pre made to make this this scripts easy to use

UN = ('MDH')
PW = ('12345')

#making the GUI for the log in

layout = [sg.Text('Please enter your user name'), sg.Input()],
     [sg.Text('please enter your password'), sg.Input()]
     [sg.Button('quit')]]

window = sg.Window('Billing Login', layout)


