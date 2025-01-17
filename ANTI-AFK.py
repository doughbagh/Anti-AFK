from pynput.keyboard import Key, Listener, Controller
import time
import threading
import tkinter as tk

# Initialize the controller for keyboard actions
keyboard = Controller()

# Global flag to control the space bar clicking
running = False

def on_press(key):
    global running
    try:
        if key == Key.f5:
            running = not running
            if running:
                print("Space bar clicking activated.")
                status_label.config(text="Activated")
            else:
                print("Space bar clicking deactivated.")
                status_label.config(text="Deactivated")
    except AttributeError:
        pass

def click_space():
    while True:
        if running:
            keyboard.press(Key.space)
            time.sleep(0.1)  # Small delay to ensure the key press is recognized
            keyboard.release(Key.space)
            time.sleep(300)  # 5 minutes = 300 seconds
        else:
            time.sleep(1)  # Check every second if we should start clicking

# Tkinter setup
root = tk.Tk()
root.title("Space Bar Clicker Status")
root.geometry("200x100")

status_label = tk.Label(root, text="Deactivated", font=("Arial", 14))
status_label.pack(expand=True)

# Start the thread for clicking space bar
thread = threading.Thread(target=click_space)
thread.daemon = True  # Daemonize thread so it terminates when main program ends
thread.start()

# Collect events until released
listener = Listener(on_press=on_press)
listener.start()

root.mainloop()
listener.stop()