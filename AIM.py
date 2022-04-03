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
IL = ""
IU = ""
try:
    while i < 5:
        if "ls" in sys.argv[i]:
            IL = "X"
            print("List of AppImages installed:")
            os.system("ls /var/opt/AppImgz/")
            quit()
        if "uninstall=" in sys.argv[i]:
            IU = "X"
            folder = sys.argv[i].replace("uninstall=", "")
            os.system("sudo mv " + "/var/opt/AppImgz/" + folder + "/" + "name.txt " + "/tmp/name.txt")
            file = open("/tmp/name.txt")
            line = file.readlines()
            for i in line:
                de_rm = i
            os.system("sudo rm -rf " + "'" + "/var/opt/AppImgz/" + folder + "'")
            os.chdir("/usr/share/applications")
            os.system("sudo rm " + de_rm) 
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
if IL == "X":
    quit()
if IU == "X":
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
os.system("sudo mkdir " + "'" + name.replace(" ", "_") + "'")
os.chdir(name.replace(" ", "_"))
exe_i = "/var/opt/" + "AppImgz/" + name.replace(" ", "_") + "/" + "exec"
ico_i = "/var/opt/" + "AppImgz/" + name.replace(" ", "_") + "/" + "icon" 
exe = "'" + exe + "'"
ico = "'" + ico + "'"
os.system("sudo mv " + exe + " " + exe_i)
os.system("sudo cp " + ico + " " + ico_i)
os.chdir("/tmp")
os.system("echo '" + "\"" + name + ".desktop" + "\"" + "'" + " >> name.txt" )
os.system("sudo mv /tmp/name.txt " + "'" + "/var/opt/AppImgz/" + name.replace(" ", "_") + "/'")
os.system("sudo chmod +x " + exe_i)
Textfile = ["[Desktop Entry]","Version=1.0","Type=Application","Terminal=false","Exec=" + exe_i,"Name=" + name,"Icon=" + ico_i,"Category=" + category]
for i in Textfile:
    os.chdir("/tmp")
    de_file = name + ".desktop"
    f = open(de_file, "a")
    f.write(i + "\n")
    f.close()
os.system("sudo mv " + "'" + "/tmp/" + de_file + "' " + "/usr/share/applications/")
os.system("sudo chmod +x " + "'" + "/usr/share/applications/" + de_file + "'")
