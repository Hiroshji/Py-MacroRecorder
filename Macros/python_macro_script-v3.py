import tkinter as tk
from pynput import keyboard, mouse
import time

# Global variables to store recorded events and listeners
recorded_events = []
keyboard_listener = None
mouse_listener = None

# Function to start recording
def start_recording():
    global keyboard_listener, mouse_listener, recorded_events
    recorded_events = []

    # Define keyboard event handlers
    def on_press(key):
        try:
            recorded_events.append(('keyboard', 'press', key.char, time.time()))
        except AttributeError:
            recorded_events.append(('keyboard', 'press', key.name, time.time()))

    def on_release(key):
        recorded_events.append(('keyboard', 'release', key, time.time()))
        if key == keyboard.Key.esc:
            stop_recording()
            return False

    # Define mouse event handlers
    def on_move(x, y):
        recorded_events.append(('mouse', 'move', (x, y), time.time()))

    def on_click(x, y, button, pressed):
        event_type = 'press' if pressed else 'release'
        recorded_events.append(('mouse', event_type, (x, y, button), time.time()))

    def on_scroll(x, y, dx, dy):
        recorded_events.append(('mouse', 'scroll', (x, y, dx, dy), time.time()))

    # Set up listeners
    keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)

    # Start listeners
    keyboard_listener.start()
    mouse_listener.start()

    status_label.config(text="Recording... Press ESC to stop.")

# Function to stop recording
def stop_recording():
    global keyboard_listener, mouse_listener
    keyboard_listener.stop()
    mouse_listener.stop()
    status_label.config(text="Recording stopped. Events recorded.")

    # Save recorded events to a file
    with open('recorded_events.txt', 'w') as f:
        for event in recorded_events:
            f.write(f"{event}\n")

# Function to replay recorded events
def replay_events():
    status_label.config(text="Replaying events...")

    # Load recorded events from the file (optional, can be skipped if using the same session)
    with open('recorded_events.txt', 'r') as f:
        lines = f.readlines()

    loaded_events = [eval(line.strip()) for line in lines]

    # Get the time offset to synchronize the events
    start_time = loaded_events[0][3]

    for event in loaded_events:
        event_type, action, details, event_time = event
        time.sleep(event_time - start_time)
        start_time = event_time

        if event_type == 'keyboard':
            if action == 'press':
                if len(details) == 1:
                    keyboard.Controller().press(details)
                else:
                    keyboard.Controller().press(getattr(keyboard.Key, details))
            elif action == 'release':
                if len(details) == 1:
                    keyboard.Controller().release(details)
                else:
                    keyboard.Controller().release(getattr(keyboard.Key, details))

        elif event_type == 'mouse':
            if action == 'move':
                mouse.Controller().position = details
            elif action == 'press':
                mouse.Controller().press(details[2])
            elif action == 'release':
                mouse.Controller().release(details[2])
            elif action == 'scroll':
                mouse.Controller().scroll(details[2], details[3])

    status_label.config(text="Replay finished.")

# Set up the Tkinter interface
root = tk.Tk()
root.title("Macro Recorder")

start_button = tk.Button(root, text="Start Recording", command=start_recording)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Recording", command=stop_recording)
stop_button.pack(pady=10)

replay_button = tk.Button(root, text="Replay Events", command=replay_events)
replay_button.pack(pady=10)

status_label = tk.Label(root, text="Press 'Start Recording' to begin.")
status_label.pack(pady=10)

root.mainloop()
