"""The program moves the files in the root directory to different directories, based on the extension"""

#Imports
import os
import shutil

#Functions
def organize_files(rootPath):
    files = os.listdir(rootPath) #Create a list with all the files in the root path
    for file in files:
        if os.path.isfile(rootPath + file): #Confirm if the file is not a directory
            filename = file.split(".") #Split the file in name and extension
            ext = filename[1] #Stores the extension
            source = rootPath + file #Source path
            dest = rootPath + ext #Destination directory
            if not os.path.exists(dest): #Confirms if the destination directory exists
                os.mkdir(dest) #If no, creates the directory
            shutil.move(source,dest,copy_function="copy2") #Moves the file
            print("{} was copied successfully!".format(file)) #Prints the confirmation and the name of the file

#Sample Case
# rootPath = "./Files/"
# organize_files(rootPath)