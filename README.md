# Python---Macro-Recorder
MacroRecorder - A Python-based tool to record and replay keyboard and mouse actions with a simple Tkinter interface.


# MacroRecorder

## Overview
MacroRecorder is a Python-based tool designed to record and replay keyboard and mouse actions. This project leverages the `pynput` library for capturing and simulating input events and provides a simple user interface using `Tkinter`. The tool is ideal for automating repetitive tasks and can be customized to suit various automation needs.

## Features
- **Record Keyboard and Mouse Events**: Capture all keyboard presses/releases and mouse movements/clicks.
- **Replay Recorded Events**: Accurately replay the recorded actions, including precise timing. (at this time of writing v1-v5 doesnt acutally support this feature)
- **Tkinter Interface**: User-friendly GUI to control recording and replaying.
- **Toggle Recording with F6**: Start and stop recording using the F6 key.
- **Replay with F7**: Trigger replay of recorded events using the F7 key. (at this time of writing v1-v5 doesnt acutally support this feature)


## Iterations
### Initial Start - v1
- **No inbuilt Recording**: Have to type in each individual key
- **only supports Keyboard**: The inintial start used the Keyboard library found out about pyinput in the second iteration

### Second Version - v2
- **Basic Recording and Stopping**: The initial script allowed for basic recording of keyboard and mouse events with separate start and stop buttons.
- **Replay Functionality**: Added the capability to replay recorded events on a txt file.
- **Tkinter Interface**: Introduced a basic Tkinter interface with start and stop buttons.

### Third Iteration - v3
- **Key Press Handling**: Updated to handle key presses and releases more accurately.
- **Mouse Actions**: Included more detailed mouse event handling (clicks, movements, scrolls).
- **Enhanced Interface**: Improved the Tkinter interface with better status updates and button controls.

### Forth Iteration 
- **Toggle Recording with F6**: Implemented functionality to start and stop recording with the F6 key.
- **Replay with F7**: Enabled replaying of recorded events using the F7 key (Doesnt has intended yet).
- **Interface Updates**: Updated the interface to reflect changes in the recording state (button text changes dynamically).

### Fifth Version
- **Comprehensive Event Handling**: Ensured that both keyboard and mouse events are recorded and replayed accurately.
- **Global Key Listener**: Added a global key listener to handle F6 and F7 key presses for more intuitive control.
- **File Handling**: Save and load recorded events to/from a file for persistent storage.
- **User Feedback**: Enhanced status labels to provide clear feedback to the user regarding the current state (recording, stopped, replaying) (This still have some bugs that will be changed and updated on v6).
  (Note: it doesnt work that well and you may find some bugs with this iteration compared to the other previous iterations)

## Future Enhancements
- **Customizable Hotkeys**: Allow users to customize hotkeys for starting, stopping, and replaying.
- **Advanced Event Editing**: Provide an interface to edit recorded events before replaying.
- **Event Filtering**: Enable filtering of specific types of events (e.g., only keyboard or only mouse).
  - **color recognition**: Select a point/area of the screen for when it sees a specific color it starts a specific action decided previously by the user.

## Contributing
Contributions are welcome! If you have any ideas, feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.
