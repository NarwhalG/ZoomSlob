import subprocess
import sys
import logging
import os
import traceback

modules = ["numpy==1.19.3", "pyautogui", "colorama", "pillow", "pandas"]

def install(pckg):
    print("Please wait while this checks through all of the modules.")
    subprocess.check_call([sys.executable, "-m", "pip", "install", pckg])

try:
    for pckg in modules:
        install(pckg)
        os.system('cls')
    print("All modules checked. Press enter to exit.")
    if os.path.isfile("ignore\doge.txt"):
        f = open('ignore\doge.txt', 'r', encoding='utf-8')
        print(f.read())
        f.close()
except Exception as e:
    logging.error(traceback.format_exc())
input()