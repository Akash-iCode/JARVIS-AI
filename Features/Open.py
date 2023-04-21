import os
import keyboard
import pyautogui
import webbrowser
from time import sleep

def OpenExe(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        Nameofweb = Query.replace("visit","").strip()
        Link = f"https://www.{Nameofweb}.com/"
        webbrowser.open(Link)

    elif "launch" in Query:
        Nameofweb = Query.replace("launch","").strip()
        Link = f"https://www.{Nameofweb}.com/"
        webbrowser.open(Link)
        return True
    
    elif "open" in Query:
        NameofApp = Query.replace("open","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(NameofApp)
        sleep(1)
        keyboard.press("enter")
        sleep(0.5)
        return True
    
    elif "start" in Query:
        NameofApp = Query.replace("start","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(NameofApp)
        sleep(1)
        keyboard.press("enter")
        sleep(0.5)
        return True

# OpenExe("start chrome")
