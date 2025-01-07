# Automatic Discord Status Updater
## Update your custom status automatically on a customizable timer

### How to Install
It's a very simple installation.
1. Download the Automated-Statuses.zip from [releases.](https://github.com/meilaleinalainengithub/Automated-Status/releases/tag/discord)
2. Unzip the folder.

If you want to add this program to Windows Startup (automatically run this when your PC boots up):
1. Move the folder to ```%appdata%\\roaming```.
2. Run ```.reg```.

```.reg``` adds ```main.py``` to the Windows Registry and runs the script on startup. 

### How to Use
1. Import your desired statuses into ```statuses.txt```.
2. Open ```main.py``` inside a text editor, even notepad works.
3. Inside ```main.py```, you will see this code at the top: 
```
TIMER = 3  # In seconds
TOKEN = "your-token" # Replace with your Discord token 
```
4. Replace the number next to ```TIMER``` with the amount of time between status changes, and replace ```"your-token``` with your discord token.

3. Run ```RUNME.bat```.

That's it! You are now cycling between custom status messages! To add more, just add them into ```statuses.txt``` and the program will automatically use them.