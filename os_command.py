import shutil as sh
import os
import time




def listOption():
	'''This function display the operations'''
	
	print("1. Copy")
	print("2. Move")
	print("3. Delete")
	print("4. File Properties")
	return "xxxxxxxxxxxxxxxxxxxx"

currentDir  = os.getcwd()
print("You are in ", currentDir)
listDir = os.listdir('.')
print('Files: ', listDir)




while True:
        print(listOption())
        userChoice = input("Enter your choice ")
        userChoice = int(userChoice)
        if userChoice == 1:
                print(listDir)
                fileName= input("Enter file name to be copy ")
                newFilename = input("Enter filename for copied file")
                sh.copy(fileName,newFilename)
                print("\nFile copied successfull")
                print("xxxxxxxxxxxxxxxxxxxx")
        elif userChoice == 2:
                print(listDir)
                fileName= input("Enter file name ")
                dirName = input("Enter the dir name ")
                sh.move(fileName,dirName)
                print('File Move Successfully')
                print("xxxxxxxxxxxxxxxxxxxx")
        elif userChoice == 3:
                print(listDir)
                fileName= input("Enter file name  ")
                os.remove(fileName)
        elif userChoice == 4:
                fileName= input("Enter file name  ")
                print("xxxxxxxxxxxxxxxxxxxx")
                file_status = os.stat(fileName)
                fileStatusList = [file_status]
                print('File size: ',int(fileStatusList[0][6]/1024)," kb")
                TimeFormat = time.strftime("%d-%m-%y", time.localtime(fileStatusList[0][9]))
                
                print("File created on ", TimeFormat)
                print("xxxxxxxxxxxxxxxxxxxx")
                






