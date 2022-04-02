import sys
from sys import exit
import os
i = 1
exe = ""
ico = ""
name = ""
category = ""
II = ""
IE = ""

try:
    while i < 4:
        if "exec=" in sys.argv[i]:
            exe = sys.argv[i].replace("exec=", "")
            if os.path.exists(exe):
                print("executable's path is OK")
            else:
                IE = "X"
                print("Invalid executable path!")
                exit()
        if "icon=" in sys.argv[i]:
            ico = sys.argv[i].replace("icon=", "")
            if os.path.exists(ico):
                print("icon's path is OK")
                
            else:
                II = "X"
                print("Invalid icon path!")
                exit()
        if "name=" in sys.argv[i]:
            name = sys.argv[i].replace("name=", "")
        if "category=" in sys.argv[i]:
            category = sys.argv[i].replace("category=", "")

        i = i + 1
except:
    pass
if II == "X":
    quit()
if IE == "X":
    quit()
if name == "":
    print("Please specify a name for your AppImage")
    exit()
if ico == "":
    print("Please specify an icon path")
    exit()
if exe == "":
    print("Please specify the path to your AppImage")
    exit()
try:
    os.chdir("/var/opt/AppImgz")
except:
    os.system("sudo mkdir /var/opt/AppImgz")
    os.chdir("/var/opt/AppImgz")
os.system("sudo mkdir " + "'" + name + "'")
os.chdir(name)
exe_i = "'" + "/var/opt/" + "AppImgz/" + name + "/" + os.path.basename(exe) + "'"
ico_i = "'" + "/var/opt/" + "AppImgz/" + name + "/" + os.path.basename(ico) + "'"
ico_ii = "/var/opt/" + "AppImgz/" + name + "/" + os.path.basename(ico)

exe = "'" + exe + "'"
ico = "'" + ico + "'"
os.system("sudo mv " + exe + " " + exe_i)
os.system("sudo cp " + ico + " " + ico_i)
os.system("sudo chmod +x " + exe_i)


Textfile = ["[Desktop Entry]","Version=1.0","Type=Application","Terminal=false","Exec=" + exe_i,"Name=" + name,"Icon=" + ico_ii,"Category=" + category]
for i in Textfile:
    os.chdir("/tmp")
    de_file = name + ".desktop"
    f = open(de_file, "a")
    f.write(i + "\n")
    f.close()
os.system("sudo mv " + "'" + "/tmp/" + de_file + "' " + "/usr/share/applications/")
os.system("sudo chmod +x " + "'" + "/usr/share/applications/" + de_file + "'")
