import serial                     # pyserial import
import pyautogui                  # pyautogui import

comPort = "COM3"

ser = serial.Serial(comPort, 9600) # References relevant COM port and Baud Rate

while True: 
    acceleration_x =int(ser.readline())   # defines var as an int variable of the ser object's '.readline()' function
    if acceleration_x > 1000:
        # click gui
        
    else:
        #sleep