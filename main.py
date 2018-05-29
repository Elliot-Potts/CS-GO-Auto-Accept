"""
Counter Strike: Global Offensive Auto Acceptor
    A program which automatically accepts competitive matches for you

Written by Elliot Potts
    https://github.com/Elliot-Potts
"""

import time
import pyautogui
import keyboard
import configparser
import urllib.request
import os

ASCII_ART = """
   ___ ___  ___  ___      _       _         _                  _           
  / __/ __|/ __|/ _ \    /_\ _  _| |_ ___  /_\  __ __ ___ _ __| |_ ___ _ _ 
 | (__\__ \ (_ | (_) |  / _ \ || |  _/ _ \/ _ \/ _/ _/ -_) '_ \  _/ _ \ '_|
  \___|___/\___|\___/  /_/ \_\_,_|\__\___/_/ \_\__\__\___| .__/\__\___/_|  
                               written by Elliot Potts   |_|               
                                                         """


SETTINGS = {'key': None}
CONFIG = configparser.ConfigParser()
PROJ_PATH = "C:\Potts' Software\CSGO Autoaccept"


def settingsInit():
    if os.path.isdir(PROJ_PATH):
        if os.path.isfile(PROJ_PATH+"\settings.ini"):
            CONFIG.read(PROJ_PATH+"\settings.ini")
            SETTINGS['key'] = CONFIG.get("Settings", "hotkey")
        else:
            os.chdir(PROJ_PATH)
            intConf = open("settings.ini", "w")
            CONFIG.add_section("Settings")
            CONFIG.set("Settings", "hotkey", "N")
            CONFIG.write(intConf)
            intConf.close()
    else:
        os.makedirs(PROJ_PATH)


def run_program():
    if SETTINGS['key'] is None:
        print(" [-] You have't configured your hotkey.")
        getHotKey = input("  [!] Enter a single key: ")
        print(" [+] Hotkey changed to {}.".format(getHotKey))

        SETTINGS['key'] = getHotKey

        openConf = open(PROJ_PATH+"\settings.ini", "w")
        CONFIG.add_section("Settings")
        CONFIG.set("Settings", "hotkey", getHotKey)
        CONFIG.write(openConf)
        openConf.close()
    else:
        pass

    print(" [+] Press {} to start the program.".format(SETTINGS['key']))

    toggled = False

    urllib.request.urlretrieve("https://i.imgur.com/nsjO50f.png",
                               "accept_image.png")

    while True:

        if keyboard.is_pressed(SETTINGS['key']):
            if not toggled:
                toggled = True
                print(" [+] Toggled on.")
                time.sleep(1)
            else:
                toggled = False
                print(" [-] Toggled off.")
                time.sleep(1)

        if toggled is True:
            try:
                val = pyautogui.locateCenterOnScreen("accept_image.png")

                if str(type(val)) == "<class 'NoneType'>":
                    pass
                else:
                    print(" [+] ACCEPT found at {}, accepting!".format(str(val)))
                    pyautogui.click(val)
            except TypeError:
                pass


if __name__ == '__main__':
    print(ASCII_ART)
    settingsInit()
    run_program()


