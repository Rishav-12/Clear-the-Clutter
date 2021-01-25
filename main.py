import os
import shutil

ImgExts = [".jpg", ".jpeg", ".bmp", ".png"]
DocExts = [".txt", ".doc", ".docx", ".pdf"]
OfficeExts = [".xlsx", ".pptx", ".accdb"]
MediaExts = [".mp4", ".mp3", ".m4a", ".flv", ".mkv", ".avi"]

def createFolder(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)

createFolder('Images')
createFolder('Docs')
createFolder('Office')
createFolder('Media')
createFolder('Others')

contents = os.listdir()
contents.remove("main.py")
files = []
for content in contents:
    if os.path.isfile(content):
        files.append(content)

for file in files:
    if os.path.splitext(file)[1].lower() in ImgExts:
        shutil.move(file, 'Images')
    elif os.path.splitext(file)[1].lower() in DocExts:
        shutil.move(file, 'Docs')
    elif os.path.splitext(file)[1].lower() in OfficeExts:
        shutil.move(file, 'Office')
    elif os.path.splitext(file)[1].lower() in MediaExts:
        shutil.move(file, 'Media')
    else:
        shutil.move(file, 'Others')
