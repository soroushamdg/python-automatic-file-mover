from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time,os

class fileHandler(FileSystemEventHandler):
    def __init__(self):
        pass

    def on_modified(self, event):
        for filename in os.listdir(folderToTrack):
            source = folderToTrack + "/" + filename
            newDes = folderDes + "/" + filename
            os.rename(source,newDes)


folderToTrack = input("enter source folder : ")
folderDes = input("enter destination folder : ")

eventHandler = fileHandler()
observer = Observer()
observer.schedule(eventHandler, folderToTrack, recursive= True)
observer.start()

try:
    while True:
        time.sleep(50)
except KeyboardInterrupt:
    observer.stop()

observer.join()
