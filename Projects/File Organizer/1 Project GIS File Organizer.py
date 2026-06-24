import os
import shutil
folderPath = input("Enter Folder Path: ")
# r"C:\Users\dell\Desktop\AI using Python\Projects\File Organizer"

if not os.path.exists(folderPath):
    print("Folder doesn't Exist")
    exit()
print ("\nScanning folder...\n")

gisFiles=[".shp",".geojson",".kml",".tif"]
images=[".jpg",".jpeg",".png"]
documents=[".pdf",".docx",".txt"]
csvFile=[".csv"]

def createFolder(folderName):
    newFolder=os.path.join(folderName,folderName)
    if not os.path.exists(newFolder):
        os.mkdir(newFolder)
    return newFolder

gisFolder=createFolder("GIS Files")
imageFolder=createFolder("Images")
docsFolder=createFolder("Docs Files")
csvFolder=createFolder("CSV Files")
otherForlder=createFolder("Other")