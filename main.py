import psutil
from colorama import Fore, Back ,init
from pathlib import Path

ROBLOX_PATH = Path.home() / "AppData\\Local\\Roblox"
USER_TEMP = Path.home() / "AppData\\Local\\Temp"

init()

print(Fore.RED + "Killing Roblox process")

for proc in psutil.process_iter():
    if proc.name() == "RobloxPlayerBeta.exe":
        proc.kill()

print(Fore.GREEN + "Killed process\n")

print(Fore.WHITE + "--------------------\n")

print(Fore.GREEN + "Trying Method #1 - Deleting GlobalBasicSettings_13.xml")
if Path(ROBLOX_PATH / "GlobalBasicSettings_13.xml").is_file():
    Path.unlink(ROBLOX_PATH / "GlobalBasicSettings_13.xml")
    print(Fore.GREEN + "File successfully deleted\n")
else:
    print(Fore.RED + "File doesn't exist\n")

print(Fore.WHITE + "--------------------\n")

print(Fore.RED + "If doesn't work remove your Roblox client" + Fore.RESET)
input("Press any key for exit")
