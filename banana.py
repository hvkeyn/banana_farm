import subprocess as sp
import time
import psutil
import random
import pyautogui

def run_banana(path, process_banana):
    # Start the Banana.exe process
    process = sp.Popen(path)
    time.sleep(10)  # Wait for 69 seconds

    print(f'sleep 10!')

    # Generate random coordinates within a specified range
    x = random.randint(300, 450)
    y = random.randint(610, 650)
    # Perform a mouse click at the generated coordinates
    pyautogui.click(x, y)

    time.sleep(30)
    print(f'sleep 30!')

    # Iterate over all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        #print(proc.info['name'])
        # If the process name matches the target process
        if proc.info['name'] == process_banana:
            # Terminate the process
            proc.terminate()

# Path to the Banana.exe file
banana_path = r"D:\SteamLibrary\steamapps\common\Banana\Banana.exe"
# Name of the Banana.exe process
banana_process = "Banana.exe"

# Set the pause duration for pyautogui actions
pyautogui.PAUSE = 0.00001

pint = 0

# Infinite loop to run the game
while True:
    print(f'Start '+str(pint)+'...')
    pint = pint+1
    # Run the Banana.exe game
    run_banana(banana_path, banana_process)
    # Wait for 10800 seconds (3 hours) before restarting the game
    time.sleep(3600)