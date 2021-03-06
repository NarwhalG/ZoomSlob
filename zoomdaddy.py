import time
import os, sys, subprocess
import logging, traceback
import glob
import urllib, urllib.request
import shutil
from datetime import date, datetime

class Updates:
    def __init__(self, version:float, path):
        self.version = version
        self.title = None
        self.path = path
    def update_checker(self, title:str=None, index:int=0):
        print("Checking for updates...")
        time.sleep(1.5)
        try:
            stream = urllib.request.urlopen("https://raw.githubusercontent.com/NarwhalG/ZoomSlob/main/version.txt")
        except Exception:
            self.title = f"{title} (No internet access)"
            os.system(f"title {self.title}")
            return
        streamBytes = stream.readlines()
        streamText = streamBytes[index].decode('utf8')
        streamText = str(streamText).split(' ')
        stream.close()
        streamName = str(streamText[2])
        streamVer = float(streamText[0])
        os.system('cls')
        if self.version < streamVer:
            app_path = self.path
            dl_path = self.path + ".new"
            backup_path = self.path + ".old"
            try:
                dl_file = open(dl_path, 'w')
                dl_stream = urllib.request.urlopen(f"https://raw.githubusercontent.com/NarwhalG/ZoomSlob/main/{streamName}.py")
                dl_file.write(dl_stream.read().decode('utf-8'))
                dl_stream.close()
                dl_file.close()
            except IOError as errno:
                self.title = f"{title} (Update Failed)"
                os.system(f"title {self.title}")
                return
            try:
                if os.path.isfile(backup_path):
                    os.remove(backup_path)
                os.rename(app_path, backup_path)
                os.rename(dl_path, app_path)
                try:
                    shutil.copymode(backup_path, app_path)
                except Exception:
                    os.chmod(app_path, 775)
                self.title = f"{title} (Update v{streamVer})"
                os.system(f"title {self.title}")
                if os.path.isfile(f"{streamName}.py"):
                    os.system('cls')
                    subprocess.call(['python', f'{streamName}.py'])
                exit()
            except Exception:
                print("Something went wrong renaming the files.")
                input('\nPress enter to continue anyway')
        else:
            self.title = f"{title} is up to date :)"
            os.system(f"title {self.title}")

class Modules():
    def __init__(self):
        self.modules = ["numpy==1.19.3", "pyautogui", "colorama", "pillow", "pandas"]

    def install(self, pckg):
        print("Please wait while this checks through all of the modules.")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pckg])

    def initiate(self):
        try:
            for pckg in self.modules:
                self.install(pckg)
                os.system('cls')
            print("All modules checked. Press enter to exit.")
            if os.path.isfile("ignore\doge.txt"):
                f = open('ignore\doge.txt', 'r', encoding='utf-8')
                print(f.read())
                f.close()
        except Exception as e:
            logging.error(traceback.format_exc())
        input()

def default_print():
    if updt.msg != "":
        tmp = f"ZoomSlob (Update Error)"
        os.system(f"title {updt.title or tmp}")
        print(updt.msg + "\n")
    print(f"{Fore.GREEN}Modules imported succesfully! {Style.RESET_ALL}ZoomSlob {Fore.LIGHTYELLOW_EX}Version {updt.version}{Style.RESET_ALL}")
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
    time.sleep(1)
    if len(csv.index) > 0:
        print("Found " + str(len(csv.index)) + " class(es), time will be checked regularly in the background.")
        row = csv.iloc[0]
        print(f"Next class begins at {row[0]}")

if __name__ == '__main__':
    updt = Updates(1.7, os.path.realpath(sys.argv[0]))
    modules = Modules()
    try:
        import pyautogui
        from PIL import Image
        from colorama import Fore
        from colorama import Style
        import pandas as pd
    except ImportError as err:
        os.system('cls')
        time.sleep(2)
        modules.initiate()
        if os.path.isfile("zoomdaddy.py"):
            os.system('cls')
            subprocess.call(['python', 'zoomdaddy.py'])
        exit()
    else:
        pyautogui.FAILSAFE = True
        os.system('color')

    try:
        residue = glob.glob('*.{}'.format('old'))
        if len(residue) > 0:
            for r in residue:
                os.remove(r)
        if os.path.exists("module_installer.py") and os.path.isfile("module_installer.py"):
            os.remove("module_installer.py")
    except Exception:
        pass
    if not os.path.isfile('hahasecret'):
        updt.update_checker("ZoomSlob", 0)
        os.system(f"title {updt.title}")
    dir_path = 'ignore'
    zoom_path = ""
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        txt_path = dir_path + '\\zoomDir.txt'
        if os.path.exists(txt_path) and os.path.isfile(txt_path):
            f = open(txt_path, 'r', encoding='utf-8')
            zoom_dir = f.read()
            f.close()
            if os.path.exists(zoom_dir) and os.path.isfile(zoom_dir) and zoom_dir.endswith('Zoom.exe'):
                zoom_path = zoom_dir
        else:
            try:
                subfolders = [f.path for f in os.scandir("C:\\Users") if f.is_dir()]
                for i in subfolders:
                    if os.path.isfile(i + "\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"):
                        zoom_path = i + "\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
                        dir_file = open('ignore\\zoomDir.txt', 'w')
                        dir_file.write(zoom_path)
                        dir_file.close()
                        break
            except:
                pass
    while zoom_path == "":
        os.system('cls')
        tempPath = input(f'Please enter your Zoom directory, it should end with something like {Fore.LIGHTBLUE_EX}Zoom\\bin\\Zoom.exe{Style.RESET_ALL}\n')
        if tempPath != "" and os.path.exists(tempPath):
            if os.path.isdir(tempPath) and os.path.exists(tempPath + '\\Zoom.exe') and os.path.isfile(tempPath + '\\Zoom.exe'):
                dir_file = open('ignore\\zoomDir.txt', 'w')
                dir_file.write(tempPath + '\\Zoom.exe')
                dir_file.close()
                zoom_path = tempPath + '\\Zoom.exe'
            elif os.path.isfile(tempPath) and tempPath.endswith('Zoom.exe'):
                dir_file = open('ignore\\zoomDir.txt', 'w')
                dir_file.write(tempPath)
                dir_file.close()
                zoom_path = tempPath
    # Chooses the csv to use with automation
    csv = None
    csvDir = 'csv/'
    if os.path.exists(csvDir) and os.path.isdir(csvDir):
        csvList = glob.glob('csv\*.{}'.format('csv'))
        if not os.listdir(csvDir) or len(csvList) == 0:
            if os.path.isfile("schedule_maker.py"):
                print("You do not have any schedules setup. Let's make one!")
                time.sleep(3.5)
                subprocess.call(['python', 'schedule_maker.py'])
                if os.path.isfile("zoomdaddy.py"):
                    os.system('cls')
                    subprocess.call(['python', 'zoomdaddy.py'])
                exit()
            else:
                print("You are missing 'schedule_maker.py'. Please make sure it's in the same directory or redownload ZoomSlob.\n")
                input('Press enter to exit')
                exit()
        else:
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

    def time_difference(theTime):
        curt = time.localtime()
        curTime = time.strftime('%H:%M:%S', curt)

        delta1 = datetime.strptime(theTime, '%H:%M').time()
        m1 = datetime.strptime(str(delta1), '%H:%M:%S').time()
        tdelta = datetime.strptime(curTime, '%H:%M:%S') - datetime.strptime(str(m1), '%H:%M:%S')
        return tdelta.total_seconds()

    # gets rid of meetings older than 5 minutes
    curDay = datetime.today().strftime('%A').lower()[:2]
    for index, row in csv.iterrows():
        meetingDays = row['MeetingDays']
        splitDays = meetingDays.lower().replace(" ", "").split(',')
        if not curDay in splitDays:
            csv.drop(index, inplace = True)
        else:
            timeDif = time_difference(row['MeetingTime'])
            if timeDif > 300:
                #more than 5 minutes late, remove the meeting
                csv.drop(index, inplace = True)

    default_print()
    def process_exists(process):
        call = ['TASKLIST', '/FI', f'imagename eq {process}']
        output = subprocess.check_output(call).decode()
        last = output.strip().split('\r\n')[-1]
        return last.lower().startswith(process.lower())
    def start_zoom(notif = True):
        if process_exists('Zoom.exe'):
            try:
                os.system("taskkill /f /im Zoom.exe")
                time.sleep(2)
            except Exception:
                pass
        try:
            subprocess.Popen(zoom_path)
            if notif:
                print("Launching Zoom")
        except Exception as e:
            os.system('cls')
            print(f"{Fore.RED}There was a problem finding the directory for Zoom.exe!{Style.RESET_ALL}")
            logging.error(traceback.format_exc())
            input('Press enter to close the program.')
            exit()

    def manual_sign_in(meetid, passwd = ""):
        print(f"{Fore.BLUE}Do not touch keyboard or mouse during automation.{Style.RESET_ALL}")
        time.sleep(10)

        join_btn = pyautogui.locateCenterOnScreen('ignore\join_button.png')
        if join_btn != None:
            pyautogui.moveTo(join_btn)
            pyautogui.click()
        else:
            print(f"Zoom not on foreground. {Fore.LIGHTRED_EX}Retrying...{Style.RESET_ALL}")
            start_zoom(False)
            time.sleep(4)
            join_btn = pyautogui.locateCenterOnScreen('ignore\join_button.png')
            if join_btn != None:
                pyautogui.moveTo(join_btn)
                pyautogui.click()
            else:
                print(f"{Fore.RED}Failed to keep Zoom on the foreground.{Style.RESET_ALL}\n")
                input('Press enter to exit')
                exit()

        time.sleep(3)
        pyautogui.write(meetid)

        time.sleep(1)
        #pyautogui.press('enter')
        join2_btn = pyautogui.locateCenterOnScreen('ignore\join_final.png')
        pyautogui.moveTo(join2_btn)
        pyautogui.click()

        time.sleep(2)
        #pass_input = pyautogui.locateCenterOnScreen('ignore\meetingPASS_input.png')
        #pyautogui.moveTo(pass_input)
        #pyautogui.click()
        if passwd != "":
            pyautogui.write(passwd)
            pyautogui.press('enter')

    # check for a recently missed meeting and join it
    if not csv.empty:
        for index, row in csv.iterrows():
            # if less than 5 minutes late: join
            timeDif = time_difference(row['MeetingTime'])
            if timeDif <= 300 and timeDif >= 0:
                print(str(row['MeetingTime']) + " " + str(timeDif))
                m_id = str(row['MeetingID'])
                m_id.replace(" ", "") #just makes life less complicated
                m_pswd = str(row['MeetingPassword'])
                m_pswd.replace(" ", "")
                try:
                    start_zoom()
                    manual_sign_in(m_id, m_pswd)
                    csv.drop(index, inplace = True)
                    os.system('cls')
                    default_print()
                except Exception as e:
                    print(f"{Fore.RED}Something went wrong with the automation!{Style.RESET_ALL}")
                    logging.error(traceback.format_exc())
                break # prevent madness
    # checks the remaining meetings every 10 seconds
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