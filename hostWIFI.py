#!/usr/bin/env python

from __future__ import print_function
import os
import sys
print(sys.version)

try:
    input = raw_input
except NameError:
    pass
print(sys.version)

def startprevious():
    for i in range(0, 20):
            print('===', end='')
    print('\nPress 0 to return to the main menu.')
    ifStartp = input('Press any key to start a previous hosting... ')
    if ifStartp == '0':
        return menu()
    else:
        return os.system('netsh wlan start hostednetwork')

def assignment():
    for i in range(0, 20):
            print('===', end='')
    ssid = input('\nSSID = ')
    print('SSID has been set to ' + ssid)
    key = input('KEY = ')
    print('Key has been set to ' + key)
    command = 'netsh wlan set hostednetwork mode= allow ssid= ' + ssid + ' key = ' + key
    print(command)
    os.system(command)

def start():
    for i in range(0, 20):
            print('===', end='')
    print('\nPress 0 to return to the main menu.')
    ifStart = input('Press any number to start new hosting... ')
    if ifStart == '0':
        return menu()
    else:
        return os.system('netsh wlan start hostednetwork')

def setup():
    for i in range(0, 20):
            print('===', end='')
    print('\nONE LAST STEP! Congratulations! Your hosted network has been successfully set up, now please follow the '
          '\ninstructions below before you can finally share it:'
          '\n1. A Network Connection window will automatically pop up, right click on the Ethernet icon and choose '
          '\nproperties'
          '\n2. On the share tab, click and check the first box and choose Local Connection 4'
          '\n3. Your hosted WIFI is ready to go. Make sure the host is connected to the internet! ')
    print('Press 0 to return to the main menu.')
    ifSetup = input('Press any other key to start hosting... ')
    if ifSetup == '0':
        return menu()
    else:
        os.system('ncpa.cpl')

def shutdown():
    for i in range(0, 20):
        print('===', end='')
    print('\n')
    os.system('netsh wlan stop hostednetwork')
    return menu()

def show():
    for i in range(0, 20):
            print('===', end='')
    os.system('netsh wlan show hostednetwork')
    return menu()

def menu():
    ask = True
    while ask is True:
        for i in range(0, 20):
            print('===', end='')
        print('\nWelcome to hostWIFI! How can I help you? \n1. Start a previous hosted network \n2. Start a new hosted '
              'network \n3. Stop a hosted network \n4. Show status \nPress 0 to return to the main menu. Press 5 to '
              'exit')
        menuNub = input('Please enter 1 , or 2, or 3, or 4, or 5: ')
        if menuNub == '1':
            startprevious()
        if menuNub == '2':
            assignment()
            start()
            setup()
        if menuNub == '3':
            shutdown()
        if menuNub == '4':
            show()
        if menuNub == '5':
            print('Thanks for using hostWIFI! See ya!')
            for i in range(0, 20):
                print('===', end='')
            ask = False
    return

if __name__ == '__main__':
    menu()

