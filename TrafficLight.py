# Traffic Light Instructions
# Ask the user to enter a traffic light color (red, yellow, or green). Print what action to take based on the color. If the color is invalid, print an error message.

Red = "Stop"
Yellow = "Ready"
Green = "Go"

light = input("Enter a Traffic Light1 Color: ")

if light == "red":
 print("Stop")
elif light == "yellow":
 print("Ready")
else:
 print("Go")
