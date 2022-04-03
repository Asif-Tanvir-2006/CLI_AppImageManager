# CLI_AppImageManager

## Usage

### Flags

* exec (required during installation of AppImage/Executable)
* icon (required during installation of AppImage/Executable)
* name (required during installation of AppImage/Executable)
* category (required during installation of AppImage/Executable **optional, need not necessarily include this flag during installation)
* uninstall (required during uninstallation)
* ls (lists all the AppImages/executables that had been installed via the AIM.py python script)

### Installation
python AIM.py "exec=/path/to/executable/file" "icon=/path/to/icon/file" "name=the name of your program(can be anything)" "category=Internet/Gaming or anything else(u get it right? :))"
### Listing all AppImages that had been installed via the script
python AIM.py ls
### Uninstallation
python AIM.py ls
(Check the list of programs that's been installed (will only list those programs that were installed using AIM.py script))
**Example output**
Brave_Browser
python AIM.py "uninstall=Brave_Browser"
## Note
**For further clarification, refer to this YouTube Video - https://www.youtube.com/watch?v=NZY4Pzg7pFk**

#### Thank you

