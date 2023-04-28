"""
Counter Strike: Global Offensive Auto Acceptor
    A program which automatically accepts competitive matches for you
        Update: 7/10/2018 - Panorama support added.

Written by Elliot Potts
    https://github.com/Elliot-Potts
"""

import time
import pyautogui
import keyboard
import configparser
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
            SETTINGS['max_tries'] = CONFIG.get("Settings", "max_tries")
        else:
            os.chdir(PROJ_PATH)
            intConf = open("settings.ini", "w")
            CONFIG.add_section("Settings")
            CONFIG.set("Settings", "hotkey", "N")
            CONFIG.set("Settings", "max_tries", 2)
            CONFIG.write(intConf)
            intConf.close()
    else:
        os.makedirs(PROJ_PATH)


def run_program():
    if not SETTINGS['key']:
        print(" [-] You have't configured your hotkey.")
        new_hot_key = input("  [!] Enter a single key: ")
        print(" [+] Hotkey changed to {}.".format(new_hot_key))

        SETTINGS['key'] = new_hot_key

        openConf = open(PROJ_PATH+"\settings.ini", "w")
        CONFIG.add_section("Settings")
        CONFIG.set("Settings", "hotkey", new_hot_key)
        CONFIG.write(openConf)
        openConf.close()

    print(" [+] Press {} to start the program.".format(SETTINGS['key']))

    toggled = False

    while True:
        if keyboard.is_pressed(SETTINGS['key']):
            if not toggled:
                toggled = True
                print(" [+] Toggled on.")
            else:
                toggled = False
                print(" [-] Toggled off.")

            time.sleep(1)

        if toggled:
            try:
                accept_btn = pyautogui.locateCenterOnScreen("pan_accept_btn.png")
                assert accept_btn is not None
            except Exception:
                pass
            else:
                for i in range(SETTINGS["max_tries"]):
                    print(" [+] ACCEPT found at {}, accepting! ({}/{}).".format(str(accept_btn), str(i + 1), SETTINGS["max_tries"]))
                    pyautogui.click(accept_btn)
                    time.sleep(0.5)

print(ASCII_ART)
settingsInit()
run_program()
