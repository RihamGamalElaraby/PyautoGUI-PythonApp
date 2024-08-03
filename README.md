PyAutoGUI Automation Script
This Python script leverages the pyautogui library to automate a series of GUI interactions on a Windows computer. It simulates mouse clicks, cursor movements, typing, and key presses to perform specific tasks, such as opening a command prompt and installing a Python package.

Features
Mouse Click Simulation: Clicks at specific screen coordinates to activate windows or applications.
Typing Automation: Types predefined paths or commands into active windows.
Key Press Simulation: Presses keys such as 'Enter' to execute commands.
Automated Delays: Uses time.sleep() to ensure proper timing between actions.
Usage
Initial Setup:

Imports necessary libraries: time and pyautogui.
Clicking on a Specific Position:

Simulates a mouse click at the coordinates (69, 750) to activate a specific application or window.
Typing a Path:

Defines and types a file path: C:\\Users\\mohamed\\AppData\\Local\\Programs\\Python\\Python311\\Scripts.
Presses 'Enter' to execute any command or action associated with the typed path.
Opening Command Prompt:

Simulates a mouse click at the coordinates (851, 62) to focus or open a specific application or command prompt.
Types 'cmd' to open the Command Prompt and presses 'Enter'.
Installing a Python Package:

Types the command pip install pyautogui into the Command Prompt to install the pyautogui package.
Important Notes
Ensure that the screen coordinates in the script match your screen's positions. Adjust them based on your screen resolution and layout if necessary.
Test the script in a controlled environment to avoid unexpected behavior, especially if other applications or dialogs might interfere.
Be cautious with automated scripts that involve typing and clicking, as they can perform unintended actions if the active window or application changes during execution.
Requirements
Python 3.x
PyAutoGUI library (pip install pyautogui)
