import tkinter as tk
from pynput import keyboard, mouse

# Global variable to store recorded events
recorded_events = []

# Function to start recording
def start_recording():
    global keyboard_listener, mouse_listener, recorded_events
    recorded_events = []

    # Define keyboard event handlers
    def on_press(key):
        try:
            recorded_events.append(('keyboard', 'press', key.char))
        except AttributeError:
            recorded_events.append(('keyboard', 'press', key.name))

    def on_release(key):
        recorded_events.append(('keyboard', 'release', key))
        if key == keyboard.Key.esc:
            stop_recording()  # Stop recording when 'esc' is pressed
            return False

    # Define mouse event handlers
    def on_move(x, y):
        recorded_events.append(('mouse', 'move', (x, y)))

    def on_click(x, y, button, pressed):
        event_type = 'press' if pressed else 'release'
        recorded_events.append(('mouse', event_type, (x, y, button)))

    def on_scroll(x, y, dx, dy):
        recorded_events.append(('mouse', 'scroll', (x, y, dx, dy)))

    # Set up listeners
    keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)

    # Start listeners
    keyboard_listener.start()
    mouse_listener.start()

    status_label.config(text="Recording... Press ESC to stop.")

# Function to stop recording
def stop_recording():
    keyboard_listener.stop()
    mouse_listener.stop()
    status_label.config(text="Recording stopped. Events recorded.")

    # Print recorded events (for debugging purposes)
    for event in recorded_events:
        print(event)

    # Save recorded events to a file
    with open('recorded_events.txt', 'w') as f:
        for event in recorded_events:
            f.write(f"{event}\n")

# Set up the Tkinter interface
root = tk.Tk()
root.title("Macro Recorder")

start_button = tk.Button(root, text="Start Recording", command=start_recording)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Recording", command=stop_recording)
stop_button.pack(pady=10)

status_label = tk.Label(root, text="Press 'Start Recording' to begin.")
status_label.pack(pady=10)

root.mainloop()
