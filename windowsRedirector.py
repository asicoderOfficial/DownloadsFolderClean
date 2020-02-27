import os
import time
import magic
from watchdog.events import FileSystemEventHandler


class MainHandler(FileSystemEventHandler):
    def getTypeOfFiles(self):
        for filename in os.listdir(originFolder):
            currentfile = originFolder + "/" + filename
            if not os.path.isdir(currentfile):
                typeoffile = magic.from_file(currentfile)
                switcher = {
                    "PDF": "pdfs",
                    "JPG": "imgs",
                    "PNG": "imgs",
                    "TXT": "txts",
                    "ZIP": "zip",
                    "DOCX": "docx",
                    "EXE": "exe",
                    "XSLX": "xlsx",
                    "PPTX": "pptx",
                    "SCI": "sci",
                    "ISO": "iso",
                    "C": "programmingFiles/C",
                }
                key = typeoffile.split(" ")[0].upper()
                if key not in switcher:
                    os.rename(currentfile, destFolder + "/OTHERS/" + filename)
                else:
                    folderoftype = switcher[key]
                    os.rename(currentfile, destFolder + "/" + folderoftype + "/" + filename)
            else:
                os.rename(currentfile, destFolder + "/FOLDERS/" + filename)


originFolder = "C:/Users/asico/Downloads"
destFolder = "C:/Users/asico/Desktop/DownloadsRedirected"


try:
    while True:
        MainHandler.getTypeOfFiles(MainHandler())
        time.sleep(60)
except KeyboardInterrupt:
    MainHandler.getTypeOfFiles(MainHandler())
