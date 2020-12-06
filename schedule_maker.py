import os
import time
import re
import subprocess
from urllib.parse import urlparse

def death():
    os.system('cls')
    if os.path.isfile("ignore\skull.txt"):
        f = open('ignore\skull.txt', 'r', encoding='utf-8')
        print(f.read())
        f.close()
try:
    from colorama import Fore
    from colorama import Style
    import pandas as pd
    os.system('color')
except ModuleNotFoundError as err:
    death()
    time.sleep(2)
    if os.path.isfile("module_installer.py"):
        subprocess.call(['python', 'module_installer.py'])
        if os.path.isfile("schedule_maker.py"):
            os.system('cls')
            subprocess.call(['python', 'schedule_maker.py'])
    else:
        print("Some modules are missing, please run module_installer.py and restart the program!")
        input()
    exit()

layout = {'MeetingTime': [],
        'MeetingID': [],
        'MeetingPassword': [],
        'MeetingDays': []
        }
df = pd.DataFrame(layout)
def url_val(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc, result.path])
    except:
        return False

completed = False

acceptable = ["y", "yes", "n", "no"]
skippedThrough = False
while not completed:
    os.system('cls')
    skippedThrough = False
    if(df.empty):
        print(f"{Fore.CYAN}Welcome to the schedule maker, let's get started!{Style.RESET_ALL}\n")
    else:
        print(Fore.LIGHTYELLOW_EX)
        print(df)
        print(Style.RESET_ALL)
    url = ""
    while url == "" and not skippedThrough:
        tempUrl = input(f'Enter the {Fore.LIGHTBLUE_EX}Zoom link{Style.RESET_ALL} of your class:')
        if tempUrl == "" and not df.empty:
            skippedThrough = True
        if not skippedThrough and url_val(tempUrl):
            meetID = ""
            try:
                if "/j/" in tempUrl:
                    meetID = tempUrl.split("/j/")[1].split("?")[0]
                elif "/w/" in tempUrl:
                    meetID = tempUrl.split("/w/")[1].split("?")[0]
                password = tempUrl.split("pwd=")[1]
                url = tempUrl
            except:
                pass

    urlVal = ""
    while urlVal != "y" and not skippedThrough:
        os.system('cls')
        print(f"{Fore.LIGHTBLUE_EX}{url}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTYELLOW_EX}ID{Style.RESET_ALL}: " + str(meetID) + f" {Fore.LIGHTYELLOW_EX}Password{Style.RESET_ALL}: " + str(password))
        valTemp = input(f'Is this correct? ({Fore.GREEN}y{Style.RESET_ALL}/{Fore.RED}n{Style.RESET_ALL}) ').lower()
        if valTemp in acceptable:
            if valTemp == "yes":
                valTemp = "y"
            if valTemp == "no":
                valTemp = "n"
            urlVal = valTemp
        if urlVal == "n":
            newChange = ""
            options = ["1", "2"]
            while newChange == "":
                print(f"What do you want to change?\n[{Fore.GREEN}1{Style.RESET_ALL}] ID\n[{Fore.GREEN}2{Style.RESET_ALL}] Password")
                tempChange = input()
                if tempChange in options:
                    newChange = tempChange
                elif tempChange == "":
                    break
            if newChange == "1":
                newID = ""
                while newID == "":
                    tempID = input('Type the correct ID: ')
                    if tempID == "":
                        break
                    try:
                        tempID = int(tempID)
                        meetID = str(tempID)
                        newID = str(tempID)
                    except:
                        pass
            elif newChange == "2":
                newPass = ""
                while newPass == "":
                    tempPass = input('Type the correct password: ')
                    try:
                        password = tempPass
                        newPass = tempPass
                    except:
                        pass

    def time_val(input = ""):
        try:
            time.strptime(input, '%H:%M')
            return True
        except:
            return False

    if urlVal == "y" or skippedThrough:
        meetTime = ""
        while meetTime == "" and not skippedThrough:
            print("At what time is the meeting? 00:00-23:59")
            tempTime = input()
            if time_val(tempTime):
                meetTime = tempTime
        meetDays = ""
        days = ["su", "mo", "tu", "we", "th", "fr", "sa"]
        while meetDays == "" and not skippedThrough:
            print("What days of the week does the meeting occur? Mo-Fr Monday-Friday")
            tempDays = input().lower()
            squabble = ""
            if not ',' in tempDays and not ' ' in tempDays:
                if tempDays[:2] in days:
                    meetDays = tempDays[:2]
            else:
                if ',' in tempDays:
                    tempDays.replace(' ', '').split(',')
                elif ' ' in tempDays:
                    tempDays = re.sub(' +', ' ', tempDays).split(' ')
                for day in tempDays:
                    if day[:2] in days:
                        squabble = squabble + day[:2] + ","
                if len(squabble) >= 0:
                    if squabble[len(squabble) - 1] == ",":
                        squabble = squabble[:-1]
                meetDays = squabble
        if not skippedThrough:
            classRow = {'MeetingTime':str(meetTime), 'MeetingID':str(meetID), 'MeetingPassword': str(password), 'MeetingDays':str(meetDays)}
            df = df.append(classRow, ignore_index=True)
        doneVal = ""
        while doneVal == "" and not skippedThrough:
            valTemp = input(f'Would you like to add another class? ({Fore.GREEN}y{Style.RESET_ALL}/{Fore.RED}n{Style.RESET_ALL}) ').lower()
            if valTemp in acceptable:
                if valTemp == "yes":
                    valTemp = "y"
                if valTemp == "no":
                    valTemp = "n"
                doneVal = valTemp
        if doneVal == "y":
            continue
        fullyDone = False
        while not fullyDone:
            doneVal = ""
            while doneVal == "":
                os.system('cls')
                print(Fore.YELLOW)
                print(df)
                print(Style.RESET_ALL)
                valTemp = input(f'This is your schedule result, do you want to save it? ({Fore.GREEN}y{Style.RESET_ALL}/{Fore.RED}n{Style.RESET_ALL}) ').lower()
                if valTemp in acceptable:
                    if valTemp == "yes":
                        valTemp = "y"
                    if valTemp == "no":
                        valTemp = "n"
                    doneVal = valTemp
            if doneVal == "y":
                while True and not completed:
                    tempName = input('Give this schedule file a name: ').replace(' ', '_').lower()
                    if tempName != "":
                        if not os.path.isfile(f'csv\{tempName}.csv'):
                            df.to_csv(f"csv\{tempName}.csv", encoding='utf-8', index=False)
                            print('Your schedule has been saved. Press enter to exit')
                            fullyDone = True
                            completed = True
                            break
                        else:
                            while True and not completed:
                                tempOver = input(f"{Fore.LIGHTYELLOW_EX}{tempName}.csv{Style.RESET_ALL} already exists, do you want to overwrite it? ({Fore.GREEN}y{Style.RESET_ALL}/{Fore.RED}n{Style.RESET_ALL}) ").lower()
                                if tempOver == "y":
                                    df.to_csv(f"csv\{tempName}.csv", encoding='utf-8', index=False)
                                    print('Your schedule has been saved. Press enter to exit')
                                    fullyDone = True
                                    completed = True
                                    break
                                elif tempOver == "n":
                                    break
                    else:
                        break

            else:
                print("What would you like to do?")
                print(f"[{Fore.GREEN}1{Style.RESET_ALL}] Add a meeting\n[{Fore.GREEN}2{Style.RESET_ALL}] Remove a meeting")
                choiceVal = ""
                choices = ["1", "2"]
                while choiceVal == "":
                    valTemp = input().lower()
                    if valTemp == "":
                        break
                    if valTemp in choices:
                        choiceVal = valTemp
                if choiceVal == "1":
                    skippedThrough = False
                    completed = False
                    break
                elif choiceVal == "2":
                    choosed = False
                    os.system('cls')
                    print(Fore.YELLOW)
                    print(df)
                    print(Style.RESET_ALL)
                    while not choosed:
                        print("Which meeting would you like to remove? Type the index number")
                        choice = input()
                        if choice == "":
                            break
                        try:
                            indexNum = int(choice)
                            df.drop(indexNum, inplace=True)
                            skippedThrough = False
                            choosed = True
                        except:
                            pass
        continue
input()