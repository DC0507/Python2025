#Imports
import os
import msvcrt 
import secrets
import string
import sys

#Functions
def clearConsole():
    os.system("cls" if os.name=="nt" else "clear")

def waitKey():
    if os.name == 'nt':
        #For Windows OS
        msvcrt.getch() #Reads a single character from console
    else:
        #For other systems
        import termios #Provide an interface to control terminal I/O
        import tty #Provide functions to handle terminal modes
        fd = sys.stdin.fileno() #This store the file descriptor associated to the terminal
        old_settings = termios.tcgetattr(fd) #Stores the current attributes for the terminal
        #A try...finally block to ensure the terminal recover the previous state even if an error happens
        try:
            tty.setraw(sys.stdin.fileno()) #Sets the terminal to "raw" mode
            ch = sys.stdin.read(1) #Reads a single character and store it
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) #Set the terminal attributes to the original ones
        return ch #Return the character

def pws_generator(pwsLen):
    charBase = string.ascii_letters + string.digits + string.punctuation #Stores a string with all the allowed characters for the password
    pws = "".join(secrets.choice(charBase) for i in range(pwsLen)) #Generate the password taking random character of the charBase string
    return pws #Returns the password

#Main Program
while True:
    pwsLen = int(input("Type the password lenght:")) #Asks the password lenght
    clearConsole()
    if pwsLen < 15: #If the lenght is less than 15, then you need to type the lenght again
        print("The password lenght must be greater than 14 chararters. Please try again!")
        print("Press a key to continue...")
        waitKey() #Calls the function to wait for a key
        clearConsole() #Calls the function to clear the terminal
    else:break
print("Your password is: " + pws_generator(pwsLen)) #Calls the function to generate the password and prints the value