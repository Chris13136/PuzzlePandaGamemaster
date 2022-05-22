# PuzzlePandaGamemaster
Gamemaster Program framework that communicates to microcontrollers in the rooms to trigger puzzles
Config File lay out is as follows
for the control buttons X is the number of the button
Button should be 1-15
NameWantShown currently has a 25 char max
ButtonX = {NameWantShown} = {ControlCode}
Exmpl:
    Button1 = Hello = 1
