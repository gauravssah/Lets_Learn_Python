import pyautogui
import time
import pyperclip

# Optionally: Activate the target window (if needed)
time.sleep(2)  # Pause to allow the user to focus the correct window

# Step 1: Click at a specified point (761, 1054) to focus the target window (adjust this if needed)
pyautogui.click(x=761, y=1054)
time.sleep(2)  # Delay to ensure the window is active

# Step 2: Click and hold the left mouse button at the starting position of the text (705, 289)
pyautogui.moveTo(x=705, y=289)
pyautogui.mouseDown(button='left')

# Step 3: Drag to the end position of the text (1847, 1010) while holding the mouse button down
pyautogui.moveTo(x=1847, y=1010, duration=1)
pyautogui.mouseUp(button='left')  # Release the mouse button to complete the selection

time.sleep(2)  # Small delay after selecting text

# Step 4: Copy the selected text to the clipboard using Ctrl + C
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)  # Give the system time to process the copy command

# Step 5: Get and print the clipboard content
copied_text = pyperclip.paste()  # Get the clipboard content
print("Selected data:", copied_text)
