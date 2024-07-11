# Import the keyboard library, which allows us to control and monitor keyboard events
import keyboard

# Define the first custom function to be executed when its hotkey is pressed
def custom_function_1():
    print("Custom Function 1 executed")

# Define the second custom function to be executed when its hotkey is pressed
def custom_function_2():
    print("Custom Function 2 executed")

# Map the custom_function_1 to the key combination 'ctrl+shift+a'
# When this key combination is pressed, custom_function_1 will be executed
keyboard.add_hotkey('ctrl+shift+a', custom_function_1)

# Map the custom_function_2 to the key combination 'ctrl+shift+b'
# When this key combination is pressed, custom_function_2 will be executed
keyboard.add_hotkey('ctrl+shift+b', custom_function_2)

# Print a message indicating how to stop the script
print("Press ESC to stop the script")

# Wait indefinitely until the 'esc' key is pressed, which will stop the script
keyboard.wait('esc')
