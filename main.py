import tkinter as tk
from tkinter import ttk
import re

# Puzzle Panda Gamemaster software
# Author: Chris Brinkley, Neil Sing
# Goal: This is a program that is designed to provide a framework for
#       escape room control, focused around the idea of having microcontrollers
#       that control most of the specific elements of the game. This program requires that the config
#       file (included in package), to be filled out with most of the specific info regarding the room
#       and its micro controllers.


# Sets up the timer frame
# Configs:
#          TimerTitle -> the title you want on your timer
def timerSetup(window):
    #print(dic)
    TimerFrame = tk.Frame(master=window)
    TimerLabel = tk.Label(master=TimerFrame,
                          text=dic["TimerTitle"],
                          fg="white",
                          bg="black",
                          width=80,
                          height=15)
    TimerLabel.pack()
    TimerFrame.grid(row=0, column=0)


# This is the event called when a control button is pressed
def controlTrigger(event):
    buttonName = event.widget.cget('text')
    print(f"control code {dic[buttonName.strip()]}")


# This handles setting up the buttons in their frame
# Configs: ControlTitle -> the title you want above your buttons
#          Button1-15   -> the names for the buttons you want to use, no dups
def controlSetup(window):
    # ToDO redo the way that i group the buttons so i can have proper spacing
    ButtonsFrame = tk.Frame(master=window)
    col = 0
    row = 1
    controlTitle = tk.Label(master=ButtonsFrame, text=dic["ControlTitle"])
    controlTitle.grid(row=0, column=3)

    # Looks for Button1-15 in the dic and gets their mapping
    for i in range(1, 16):
        search = "Button" + str(i)
        buttonName = dic[search]
        if len(buttonName) < 25:
            buttonName = buttonName + (" " * (25 - len(buttonName)))

        # Button for triggering X puzzle
        newButton1 = ttk.Button(master=ButtonsFrame,
                                text=buttonName)
        newButton1.grid(row=row, column=col + 1)
        newButton1.bind('<Double-1>', controlTrigger)

        # If checked then was triggered
        hasBeenTriggered = ttk.Checkbutton(master=ButtonsFrame)
        hasBeenTriggered.grid(row=row, column=col)

        # Iterator math
        if row == 5:
            row = 1
            col += 2
        else:
            row += 1
    ButtonsFrame.grid(row=1, column=0, columnspan=2)


# This builds the overarching dictionary from the configs
# in the config file
def configLoadIn():
    di = {}
    buttonSearch = re.compile(r'.* = .* = .*')
    file = open("config.txt", "r")
    for line in file:
        if len(line) > 1:
            if buttonSearch.search(line) is not None:
                lineSplit = line.strip().split(" = ")
                di[lineSplit[0].strip()] = lineSplit[1].strip()
                di[lineSplit[1].strip()] = lineSplit[2].strip()
            else:
                lineSplit = line.strip().split(" = ")
                di[lineSplit[0].strip()] = lineSplit[1].strip()
    return di


# This will handle setting up the frame where the buttons for
# Start, Pause, addTime (TimeConfig1, TimeConfig2), Win
# Configs:
#           StartPic     -> the path to the picture you want shown
#                           under the start button will default to white
#           PausePic     -> the path to the picture you want shown
#                           under the pause button will default to white
#           AddTimePic   -> the path to the picture you want shown
#                           under the AddTimeButton button will default to white
#           WinPic       -> the path to the picture you want shown
#                           under the win button will default to white
#           StartControl -> The start control code
#           PauseControl -> The pause control code
#           TimeControl  -> The time control code
#           WinControl   -> The win control code
#           TimeConfig1  -> The Low end of time you want added
#           TimeConfig2  -> The High end of time you want added
#
def gameControlSetup(window):
    gameControlFrame = tk.Frame(master=window)

    StartButton = ttk.Button(master=gameControlFrame, text="Start", width=20)
    StartButton.grid(row=0, column=0)

    WinButton = ttk.Button(master=gameControlFrame, text="Win", width=20)
    WinButton.grid(row=0, column=1, sticky="SW")

    addLowButton = ttk.Button(master=gameControlFrame, text="Add 5 sec", width=20)
    addLowButton.grid(row=1, column=0)

    addHighButton = ttk.Button(master=gameControlFrame, text="Add 60 sec", width=20)
    addHighButton.grid(row=1, column=1)

    PauseButton = ttk.Button(master=gameControlFrame, text="Pause", width=45)
    PauseButton.grid(row=2, column=0, columnspan=2)

    gameControlFrame.grid(row=0, column=1)


def hintPicSetup(window):
    picFrame = tk.Frame(master=window)

    picLabel = tk.Label(master=picFrame,
                          fg="white",
                          bg="white",
                          width=80,
                          height=15)
    picLabel.pack()

    picFrame.grid(row=0, column=3)


def main():
    # This is the frame that holds all the individual elements of the gui
    window = tk.Tk()
    # Sets up the timer framing
    timerSetup(window)
    # Sets up the buttons in a grid
    controlSetup(window)
    # Sets up the game control buttons like start, stop, win
    gameControlSetup(window)
    # Sets up where the hints will be shown
    hintPicSetup(window)
    # Starts the loop
    window.mainloop()


# Takes the config file, parses it, and creates a dictionary with various mappings
# Leaves dic as a global variable for the other functions to access
dic = configLoadIn()
main()

