import time

import pyautogui

# Get screen size
screen_size = pyautogui.size()
print(f"Screen size: {screen_size}")

# Display mouse position for a short period
print("Move your mouse to see its position (Press Ctrl+C to stop)...")
try:
    while True:
        x, y = pyautogui.position()
        print(f"Mouse position: (X: {x}, Y: {y})", end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopped displaying mouse position.")
