{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a7935b4b-1d78-49af-aa5b-4426b01c2d7e",
   "metadata": {},
   "source": [
    "## SMART GIS FILE ORGANIZER\n",
    "### Beginner Python + GIS Practice Project"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "758af89d-3bc7-4c80-8666-4218dadd296e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# WHAT THIS PROJECT DOES:\n",
    "# 1. Reads files from a folder\n",
    "# 2. Detects file types\n",
    "# 3. Creates folders automatically\n",
    "# 4. Moves files into correct folders\n",
    "# GIS FILES:\n",
    "# .shp .geojson .kml .tif\n",
    "#\n",
    "# NORMAL FILES:\n",
    "# .pdf .jpg .png .docx"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6cf7f797-5907-46da-9bc5-129be36fbee4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import shutil"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a906be0-4fc4-41b3-97b1-12ee23590f61",
   "metadata": {},
   "outputs": [],
   "source": [
    "folderPath = input(\"Enter Folder Path: \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68e13746-311b-4f2f-8620-a3f02d5d5bf1",
   "metadata": {},
   "outputs": [],
   "source": [
    "r\"C:\\Users\\dell\\Desktop\\AI using Python\\Projects\\File Organizer\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "403fb0b3-6d77-44d4-92f0-3252be9439be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Folder doesn't Exist\n",
      "\n",
      "Scanning folder...\n",
      "\n"
     ]
    }
   ],
   "source": [
    "if not os.path.exists(folderPath):\n",
    "    print(\"Folder doesn't Exist\")\n",
    "    exit()\n",
    "print (\"\\nScanning folder...\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7aacc23d-a765-484d-bd26-f38e41d56e12",
   "metadata": {},
   "outputs": [],
   "source": [
    "gisFiles=[\".shp\",\".geojson\",\".kml\",\".tif\"]\n",
    "images=[\".jpg\",\".jpeg\",\".png\"]\n",
    "documents=[\".pdf\",\".docx\",\".txt\"]\n",
    "csvFile=[\".csv\"]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b8cb9a2b-c0e2-4b7c-a732-28bd2272207d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def createFolder(folderName):\n",
    "    newFolder=os.path.join(folderName,folderName)\n",
    "    if not os.path.exists(newFolder):\n",
    "        os.mkdir(newFolder)\n",
    "    return newFolder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "62e98040-64be-4a09-b269-1bd9fa2ebd0a",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[WinError 3] The system cannot find the path specified: 'GIS Files\\\\GIS Files'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[7], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m gisFolder\u001b[38;5;241m=\u001b[39mcreateFolder(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mGIS Files\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      2\u001b[0m imageFolder\u001b[38;5;241m=\u001b[39mcreateFolder(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mImages\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      3\u001b[0m docsFolder\u001b[38;5;241m=\u001b[39mcreateFolder(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mDocs Files\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "Cell \u001b[1;32mIn[6], line 4\u001b[0m, in \u001b[0;36mcreateFolder\u001b[1;34m(folderName)\u001b[0m\n\u001b[0;32m      2\u001b[0m newFolder\u001b[38;5;241m=\u001b[39mos\u001b[38;5;241m.\u001b[39mpath\u001b[38;5;241m.\u001b[39mjoin(folderName,folderName)\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m os\u001b[38;5;241m.\u001b[39mpath\u001b[38;5;241m.\u001b[39mexists(newFolder):\n\u001b[1;32m----> 4\u001b[0m     os\u001b[38;5;241m.\u001b[39mmkdir(newFolder)\n\u001b[0;32m      5\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m newFolder\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [WinError 3] The system cannot find the path specified: 'GIS Files\\\\GIS Files'"
     ]
    }
   ],
   "source": [
    "gisFolder=createFolder(\"GIS Files\")\n",
    "imageFolder=createFolder(\"Images\")\n",
    "docsFolder=createFolder(\"Docs Files\")\n",
    "csvFolder=createFolder(\"CSV Files\")\n",
    "otherForlder=createFolder(\"Other\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca0069cc-d265-4a77-b777-ab246c1f1a33",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
