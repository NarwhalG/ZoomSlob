import os, sys
import time
import re, glob
import subprocess
import logging, traceback
import urllib.request
from urllib.parse import urlparse

updt = None
modules = None
try:
    from zoomdaddy import Updates
    from zoomdaddy import Modules
except ImportError:
    pass
else:
    updt = Updates(1.22)
    modules = Modules()
try:
    from colorama import Fore
    from colorama import Style
    import pandas as pd
except ImportError as err:
    if modules:
        os.system('cls')
        modules.initiate()
        if os.path.isfile("schedule_maker.py"):
            os.system('cls')
            subprocess.call(['python', 'schedule_maker.py'])
    else:
        print("Some modules are missing, please run zoomdaddy.py and restart the program!")
        input()
    exit()
else:
    os.system('color')
if not os.path.isfile('hahasecret'):
    if updt:
        updt.update_checker("ScheduleSlob", 1, os.path.realpath(sys.argv[0]))
        tmp = "ScheduleSlob (Update Error)"
        os.system(f"title {updt.title or tmp}")

#pd.options.display.float_format = '{:.2f}'.format
def time_val(input = ""):
    try:
        time.strptime(input, '%H:%M')
        return True
    except:
        return False

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

def make_choice(choices, desc = [], skippable = False, title = "", clear = True):
    list = ""
    if desc:
        for i, d in enumerate(desc):
            list = list + f"[{Fore.GREEN}{i+1}{Style.RESET_ALL}] {d}"
    while True:
        if clear:
            os.system('cls')
        if title != "":
            print(title)
        if list != "":
            print(list)
        theChoice = input()
        if theChoice in choices:
            break
        elif theChoice == "" and skippable:
            break
    return theChoice
actionChoice = ""
csvList = glob.glob('csv\*.{}'.format('csv'))
if len(csvList) == 0:
    actionChoice = "1"

completed = False

acceptable = ["y", "n"]
skippedThrough = False
loadedCSV = False
loadThrough = False
editChoice = ""
editRow = None
editIndex = None
# Finish the functionality of editing a meeting from a loaded CSV
while not completed:
    os.system('cls')
    skippedThrough = False
    if not df.empty and editChoice == "":
        print(Fore.LIGHTYELLOW_EX)
        print(df)
        print(Style.RESET_ALL)
    actions = ["1", "2"]
    if actionChoice == "":
        title = f"{Fore.CYAN}Welcome to the schedule maker, let's get started!{Style.RESET_ALL}\n\nWhat would you like to do?"
        actionChoice = make_choice(actions, ["Create a schedule\n", "Edit a schedule"], False, title)
        #tempAct = input()
    if actionChoice == "2" and not loadedCSV:
        print("Choose a .csv to edit")
        # [f.path for f in os.scandir("C:\\Users") if f.is_dir()]
        choices = []
        trash = "csv\\"
        for idx in range(len(csvList)):
            print(f"[{Fore.CYAN}{str(idx + 1)}{Style.RESET_ALL}] {csvList[idx].replace(trash, '')}")
            choices.append(int(idx))
        while not loadedCSV:
            csvChoice = input()
            try:
                choiceNum = int(csvChoice)
                if choiceNum - 1 in choices:
                    df = pd.read_csv(csvList[choiceNum - 1])
                    loadedCSV = True
                    loadThrough = True
                    break
            except:
                pass
        continue
    url = ""
    while url == "" and not skippedThrough and not loadThrough and editChoice == "":
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
                password = tempUrl.split("pwd=")[1].replace('#success','')
                url = tempUrl
            except:
                pass

    urlVal = ""
    if editChoice == "1" or editChoice == "3":
        urlVal = "y"
    while urlVal != "y" and not skippedThrough and not loadThrough:
        os.system('cls')
        if editChoice == "" and editIndex == None:
            print(f"{Fore.LIGHTBLUE_EX}{url}{Style.RESET_ALL}")
        else:
            editRow = df.loc[[editIndex]]
            meetID = editRow.iloc[0,1]
            password = editRow.iloc[0,2]
            print(f"{Fore.YELLOW}{str(editRow)}{Style.RESET_ALL}\n")

        print(f"{Fore.LIGHTYELLOW_EX}ID{Style.RESET_ALL}: " + str(meetID) + f" {Fore.LIGHTYELLOW_EX}Password{Style.RESET_ALL}: " + str(password))
        if editChoice == "":
            valTemp = input(f'Is this correct? ({Fore.GREEN}y{Style.RESET_ALL}/{Fore.RED}n{Style.RESET_ALL}) ').lower()
            if valTemp in acceptable:
                urlVal = valTemp
            else:
                continue
        if urlVal == "n" or editChoice == "2":
            newChange = ""
            options = ["1", "2"]
            newChange = make_choice(actions, ["ID\n", "Password"], True, "What do you want to change?", False)
            if newChange == "1":
                while True:
                    tempID = input('Type the correct ID: ')
                    if tempID == "":
                        break
                    try:
                        tempID = int(tempID)
                        meetID = str(tempID)
                        if editChoice != "":
                            df.at[editIndex, 'MeetingID'] = meetID
                        break
                    except:
                        pass
            elif newChange == "2":
                while True:
                    tempPass = input('Type the correct password: ')
                    try:
                        password = tempPass
                        if editChoice != "":
                            df.at[editIndex, 'MeetingPassword'] = password
                        break
                    except:
                        pass
            if editChoice != "":
                editChoice = ""
                skippedThrough = True

    if urlVal == "y" or skippedThrough or loadThrough or editChoice != "":
        meetTime = ""
        if editChoice != "":
            print(f"{Fore.YELLOW}{str(editRow)}{Style.RESET_ALL}\n")
        while True and not skippedThrough and not loadThrough and editChoice != "3":
            print("At what time is the meeting? 00:00-23:59")
            tempTime = input()
            if time_val(tempTime):
                meetTime = tempTime
                if editChoice == "1":
                    df.at[editIndex, 'MeetingTime'] = meetTime
                    editChoice = ""
                    skippedThrough = True
                break
        meetDays = ""
        days = ["su", "mo", "tu", "we", "th", "fr", "sa"]
        while True and not skippedThrough and not loadThrough or editChoice == "3":
            if editChoice == "3":
                os.system('cls')
                print(f"{Fore.YELLOW}{str(editRow)}{Style.RESET_ALL}\n")
            print("What days of the week does the meeting occur? Mo-Fr Monday-Friday")
            tempDays = input().lower()
            squabble = ""
            if not ' ' in tempDays:
                if tempDays[:2] in days:
                    meetDays = tempDays[:2]
            else:
                tempDays = re.sub(' +', ' ', tempDays).split(' ')
                for day in tempDays:
                    if day[:2] in days:
                        squabble = squabble + day[:2] + ","
                if len(squabble) >= 0:
                    if squabble[len(squabble) - 1] == ",":
                        squabble = squabble[:-1]
                meetDays = squabble
            if meetDays != "":
                if editChoice == "3":
                    df.at[editIndex, 'MeetingDays'] = meetDays
                    editChoice = ""
                    skippedThrough = True
                break
        if not skippedThrough and not loadThrough:
            classRow = {'MeetingTime':str(meetTime), 'MeetingID':str(meetID), 'MeetingPassword': str(password), 'MeetingDays':str(meetDays)}
            df = df.append(classRow, ignore_index=True)
        doneVal = ""
        if skippedThrough and editIndex != None:
            doneVal = "n"
            editIndex = None
            skippedThrough = False
        while doneVal == "" and not skippedThrough and not loadThrough:
            valTemp = input(f'Would you like to add another class? ({Fore.GREEN}y{Style.RESET_ALL}/{Fore.RED}n{Style.RESET_ALL}) ').lower()
            if valTemp in acceptable:
                doneVal = valTemp
        if doneVal == "y":
            continue
        fullyDone = False
        while not fullyDone:
            doneVal = ""
            if loadThrough:
                doneVal = "n"
            while doneVal == "" and editChoice == "":
                os.system('cls')
                print(Fore.YELLOW)
                print(df)
                print(Style.RESET_ALL)
                valTemp = input(f'This is your schedule result, do you want to save it? ({Fore.GREEN}y{Style.RESET_ALL}/{Fore.RED}n{Style.RESET_ALL}) ').lower()
                if valTemp in acceptable:
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
                choiceVal = ""
                choices = ["1", "2", "3"]
                while choiceVal == "" and editChoice == "":
                    choiceVal = make_choice(choices, ["Add a meeting\n", "Remove a meeting\n", "Edit a meeting"], True, "What would you like to do?\n", False)
                    if choiceVal == "":
                        break
                loadThrough = False
                if choiceVal == "1":
                    skippedThrough = False
                    completed = False
                    break
                elif choiceVal == "2":
                    os.system('cls')
                    print(Fore.YELLOW)
                    print(df)
                    print(Style.RESET_ALL)
                    while True:
                        print("Which meeting(s) would you like to remove? Type the index number(s)")
                        choice = input()
                        if choice == "":
                            break
                        try:
                            if ' ' in choice:
                                meetings = choice.split(' ')
                                for m in meetings:
                                    try:
                                        indexNum = int(m)
                                        df.drop(indexNum, inplace=True)
                                    except:
                                        pass
                            else:
                                indexNum = int(choice)
                                df.drop(indexNum, inplace=True)
                            skippedThrough = False
                            break
                        except:
                            pass
                elif choiceVal == "3":
                    os.system('cls')
                    print(Fore.YELLOW)
                    print(df)
                    print(Style.RESET_ALL)
                    while True:
                        print("Which meeting would you like to edit? Type the index number")
                        choice = input()
                        if choice == "":
                            break
                        try:
                            indexNum = int(choice)
                            editRow = df.loc[[indexNum]]
                            editIndex = indexNum
                            os.system('cls')
                            title = f"{Fore.LIGHTYELLOW_EX}{str(editRow)}{Style.RESET_ALL}\n\nWhat would you like to edit?"
                            editChoice = make_choice(["1", "2", "3"], ["Meeting Time\n", "Credentials\n", "Meeting Days"], True, title, False)
                            break
                        except:
                            pass
                    skippedThrough = False
                    loadThrough = False
                    completed = False
                    if editChoice != "":
                        break
        continue
input()