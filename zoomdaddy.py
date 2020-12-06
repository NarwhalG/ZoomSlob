import subprocess
import time
import os
import logging
import traceback
import glob
import urllib
import sys
import urllib.request
from datetime import date, datetime

def death():
    os.system('cls')
    if os.path.isfile("ignore\skull.txt"):
        f = open('ignore\skull.txt', 'r', encoding='utf-8')
        print(f.read())
        f.close()

def default_print():
    print(f"{Fore.GREEN}Modules imported succesfully! {Style.RESET_ALL}ZoomSlob {Fore.LIGHTYELLOW_EX}Version 1.1{Style.RESET_ALL}")
    title = Fore.LIGHTBLUE_EX + r'''
 ________  ________  ________  _____ ______   ________  ___       ________  ________
|\_____  \|\   __  \|\   __  \|\   _ \  _   \|\   ____\|\  \     |\   __  \|\   __  \
 \|___/  /\ \  \|\  \ \  \|\  \ \  \\\__\ \  \ \  \___|\ \  \    \ \  \|\  \ \  \|\ /_
     /  / /\ \  \\\  \ \  \\\  \ \  \\|__| \  \ \_____  \ \  \    \ \  \\\  \ \   __  \
    /  /_/__\ \  \\\  \ \  \\\  \ \  \    \ \  \|____|\  \ \  \____\ \  \\\  \ \  \|\  \
   |\________\ \_______\ \_______\ \__\    \ \__\____\_\  \ \_______\ \_______\ \_______\
    \|_______|\|_______|\|_______|\|__|     \|__|\_________\|_______|\|_______|\|_______|
                                                \|_________|
    ''' + Style.RESET_ALL
    print(title)
    trash = "csv\\"
    print(f"Reading: {Fore.CYAN}{csvList[choiceNum - 1].replace(trash, '')}{Style.RESET_ALL}")
    if len(csv.index) > 0:
        print("Found " + str(len(csv.index)) + " class(es), time will be checked regularly in the background.")
version = 1.3
def update_checker():
    try:
        print("Checking for updates...")
        stream = urllib.request.urlopen("https://raw.githubusercontent.com/NarwhalG/ZoomSlob/main/version.txt")
        streamBytes = stream.read()
        streamText = streamBytes.decode('utf8')
        stream.close()
        os.system('cls')
        if float(streamText) > version:
            print(f"The newer version of ZoomSlob ({Fore.YELLOW}{streamText}{Style.RESET_ALL}) is available")
            upChoice = ""
            while upChoice == "":
                tempChoice = input(f'Would you like to update now? ({Fore.GREEN}y{Style.RESET_ALL}/{Fore.RED}n{Style.RESET_ALL}) ').lower()
                if tempChoice == "y":
                    upChoice = tempChoice
                elif tempChoice == "n":
                    upChoice = tempChoice
            if upChoice == "y":
                app_path = os.path.realpath(sys.argv[0])
                dl_path = os.path.realpath(sys.argv[0]) + ".new"
                backup_path = os.path.realpath(sys.argv[0]) + ".old"
                try:
                    dl_file = open(dl_path, 'w')
                    dl_stream = urllib.request.urlopen("https://raw.githubusercontent.com/NarwhalG/ZoomSlob/main/zoomdaddy.py")
                    dl_file.write(dl_stream.read().decode('utf-8'))
                    dl_stream.close()
                    dl_file.close()
                except IOError as errno:
                    print(f"{Fore.LIGHTRED_EX}Download Failed{Style.RESET_ALL}")
                    print(errno)
                    input('\nPress enter to continue anyway')
                try:
                    if os.path.isfile(backup_path):
                        os.remove(backup_path)
                    os.rename(app_path, backup_path)
                    os.rename(dl_path, app_path)
                    try:
                        import shutil
                        shutil.copymode(backup_path, app_path)
                    except:
                        os.chmod(app_path, 775)
                    os.system('cls')
                    print(f"{Fore.GREEN}Updated ZoomSlob to version {streamText}{Style.RESET_ALL}")
                    input('Press enter to reload')
                    if os.path.isfile("zoomdaddy.py"):
                        os.system('cls')
                        subprocess.call(['python', 'zoomdaddy.py'])
                    exit()
                except:
                    print(f"{Fore.YELLOW}Something went wrong renaming the files.{Style.RESET_ALL}")
                    input()
        else:
            print(f"Your version of ZoomSlob ({Fore.LIGHTYELLOW_EX}{version}{Style.RESET_ALL}) is up to date :)")
            time.sleep(4)
    except Exception:
        print(f"{Fore.LIGHTRED_EX}Failed to check for updates.")
        logging.error(traceback.format_exc())
        input('\nPress enter to continue anyway') 
try:
    import pyautogui
    from PIL import Image
    from colorama import Fore
    from colorama import Style
    import pandas as pd

    pyautogui.FAILSAFE = True
    os.system('color')
    update_checker()
    csv = None

    csvDir = 'csv/'
    if os.path.exists(csvDir) and os.path.isdir(csvDir):
        if not os.listdir(csvDir):
            print("You do not have any schedules setup. Let's make one!")
            time.sleep(4)
            if os.path.isfile("schedule_maker.py"):
                subprocess.call(['python', 'schedule_maker.py'])
            if os.path.isfile("zoomdaddy.py"):
                os.system('cls')
                subprocess.call(['python', 'zoomdaddy.py'])
            exit()
        else:
            csvList = glob.glob('csv\*.{}'.format('csv'))
            if len(csvList) == 1:
                choiceNum = 0
                csv = pd.read_csv(csvList[0])
            else:
                print("Multiple .csv files found, choose one")
                choices = []
                trash = "csv\\"
                for idx in range(len(csvList)):
                    print(f"[{Fore.CYAN}{str(idx + 1)}{Style.RESET_ALL}] {csvList[idx].replace(trash, '')}")
                    choices.append(int(idx))
                while True:
                    csvChoice = input()
                    try:
                        choiceNum = int(csvChoice)
                        if choiceNum - 1 in choices:
                            csv = pd.read_csv(csvList[choiceNum - 1])
                            break
                    except:
                        pass
    os.system('cls')
except ModuleNotFoundError as err:
    death()
    time.sleep(2)
    if os.path.isfile("module_installer.py"):
        subprocess.call(['python', 'module_installer.py'])
        if os.path.isfile("zoomdaddy.py"):
            os.system('cls')
            subprocess.call(['python', 'zoomdaddy.py'])
    else:
        print("Some modules are missing, please run module_installer.py and restart the program!")
        input()
    exit()

curDay = datetime.today().strftime('%A').lower()[:2]
curt = time.localtime()
curTime = time.strftime('%H:%M:%S', curt)
for index, row in csv.iterrows():
    meetingDays = row['MeetingDays']
    splitDays = meetingDays.lower().replace(" ", "").split(',')
    if not curDay in splitDays:
        csv.drop(index, inplace = True)
    else:
        meetingTime = datetime.strptime(row['MeetingTime'], '%H:%M').time()
        m1 = datetime.strptime(str(meetingTime), '%H:%M:%S').time()
        tdelta = datetime.strptime(curTime, '%H:%M:%S') - datetime.strptime(str(m1), '%H:%M:%S')
        #print(str(curTime) + " - " + str(m1) + "\n" + str(tdelta))
        if tdelta.total_seconds() >= 300:
            #more than 5 minutes late, remove the meeting
            csv.drop(index, inplace = True)

default_print()

startTime = time.time()
def start_zoom():
    try:
        os.system("taskkill /f /im Zoom.exe")
    except Exception:
        pass
        
    subfolders = [f.path for f in os.scandir("C:\\Users") if f.is_dir()]
    try:
        for i in subfolders:
            if os.path.isfile(i + "\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"):
                subprocess.Popen(i + "\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
                print("Launching Zoom")
                break
    except Exception as e:
        death()
        print(f"{Fore.RED}There was a problem finding the directory for Zoom.exe!{Style.RESET_ALL}")
        logging.error(traceback.format_exc())
        input('Press enter to close the program.')
        exit()

def manual_sign_in(meetid, passwd = ""):
    print(f"{Fore.BLUE}Do not touch keyboard or mouse during automation.{Style.RESET_ALL}")
    time.sleep(10)

    join_btn = pyautogui.locateCenterOnScreen('ignore\join_button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    #time.sleep(1)
    #id_btn = pyau6921371120zomb6togui.locateCenterOnScreen('ignore\meetingID_input.png')
    #pyautogui.moveTo(id_btn)
    #pyautogui.click()
    time.sleep(1)
    pyautogui.write(meetid)

    time.sleep(1)
    #pyautogui.press('enter')
    join2_btn = pyautogui.locateCenterOnScreen('ignore\join_final.png')
    pyautogui.moveTo(join2_btn)
    pyautogui.click()

    time.sleep(1)
    #pass_input = pyautogui.locateCenterOnScreen('ignore\meetingPASS_input.png')
    #pyautogui.moveTo(pass_input)
    #pyautogui.click()
    if passwd != "":
        pyautogui.write(passwd)
        pyautogui.press('enter')

while True:
    if len(csv.index) == 0:
        break
    now = datetime.now().strftime("%H:%M")
    if now in str(csv['MeetingTime']):
        row = csv.loc[csv['MeetingTime'] == now]
        m_id = str(row.iloc[0,1])
        m_id.replace(" ", "") #just makes life less complicated
        m_pswd = str(row.iloc[0,2])
        m_pswd.replace(" ", "")

        try:
            start_zoom()
            manual_sign_in(m_id, m_pswd)
            csv.drop(row.index, inplace = True)
            os.system('cls')
            print("BOOFBOOF")
            default_print()
            if len(csv.index) == 0:
                break
        except Exception as e:
            print(f"{Fore.RED}Something went wrong with the automation!{Style.RESET_ALL}")
            logging.error(traceback.format_exc())
        time.sleep(60)
    else:
        time.sleep(10 - time.time() % 10)
input('No classes left to automate. Press enter to exit.')