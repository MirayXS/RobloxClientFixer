import os # You're insecure :)
import psutil
from colorama import Fore, Back, init
import shutil
from time import sleep

# CONSTANTS
HOME_PATH = os.path.expanduser("~")
ROBLOX_PATH = HOME_PATH + "\\AppData\\Local\\Roblox"
USER_TEMP = HOME_PATH + "\\AppData\\Local\\Temp"
PREFETCH = "C:\\Windows\\Prefetch"
SYS_TEMP = "C:\\Windows\\Temp"

print("Special thanks to Sirmeme for making a video!")
sleep(2)

os.system("cls")

init()  # Colorama init

print(Fore.RED + "Killing Roblox process")

for proc in psutil.process_iter():
    if proc.name() == "RobloxPlayerBeta.exe":
        proc.kill()

print(Fore.GREEN + "Killed process\n")

print(Fore.WHITE + "--------------------\n")

print(Fore.GREEN + "Trying Method #1 - Deleting GlobalBasicSettings_13.xml")

if os.path.exists(ROBLOX_PATH + "GlobalBasicSettings_13.xml"):
    os.remove(ROBLOX_PATH + "GlobalBasicSettings_13.xml")
    print(Fore.GREEN + "File successfully deleted\n")
else:
    print(Fore.RED + "File doesn't exist\n")

print(Fore.WHITE + "--------------------\n")

print(Fore.GREEN + "Trying Method #2 - Deleting Temp files")

try:
    shutil.rmtree(USER_TEMP, ignore_errors=True)
    shutil.rmtree(PREFETCH, ignore_errors=True)
    shutil.rmtree(SYS_TEMP, ignore_errors=True)
    print(Fore.GREEN + "Temporary files deleted successfully\n")
except:
    print(Fore.RED + "An error ocurred - Please make sure you run this tool as Administrator\n")

print(Fore.WHITE + "--------------------\n")


print(Fore.YELLOW + "If doesn't work remove your Roblox client" + Fore.RESET)
input("Press any key for exit...")