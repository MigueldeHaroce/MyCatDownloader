import threading
from pathlib import Path
import moviepy.editor as moviepy
from PySide2.QtWidgets import QMessageBox
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PIL import Image
from os import path
from pydub import AudioSegment
import re
import subprocess



def detect(myPath, myOutput):
    formats = [".mp4",
               ".avi",
               ".mkv",
               ".webm",
               ".mov",
               ".png",
               ".jpg",
               ".jpeg",
               ".webp",
               ".tiff",
               ".mp3",
               ".wac",
               ".acc",
               ".flac",
               ".aiff"]
    for i in formats:
        if i in myPath:
            print("valid format")
            input_format = i

    nameFile = Path(myPath).name
    print(input_format)
    threading.Thread(target=convert, args=(nameFile, myPath, input_format, myOutput,)).start()
def call_warn_popup():
    QtWidgets.QMessageBox.information(None, "Error", "Random value above limit",
                                      QtWidgets.QMessageBox.Ok)
def convert(name, myPath, myInput, output):
    formatsDict = len(myInput)
    print(formatsDict)
    nameOnly = name[:formatsDict]
    pathOnly = myPath[:-formatsDict]
    formatOnly = re.sub(r'.', '', output, count = 1)
    print(pathOnly)
    print(nameOnly, formatOnly)
    print(myPath)

    if myInput == ".mp4" or myInput == ".avi" or myInput == ".mkv" or myInput == ".webm" or myInput == ".mov":
        if output == ".mp4" or output == ".avi" or output == ".mkv" or output == ".mov":
            if output != ".webp":
                if myInput != output:
                    clip = moviepy.VideoFileClip(r"" + myPath)
                    result = moviepy.CompositeVideoClip([clip])
                    result.write_videofile(pathOnly + output, codec='mpeg4')
                    #msg = QMessageBox()
                    #msg.setWindowTitle("Alert")
                    #msg.setText("Your video is converted!")
                    #msg.setInformativeText("Thanks for Using MyCatDownloader")
                    #msg.setIcon(QMessageBox.Information)
                    #sys.exit(msg.exec_())
                else:
                    # TODO POPUP
                    print("NO VALID")
                    # threading.Thread(target=call_warn_popup).start()

        elif output == ".webm":
            if myInput != output:
                clip = moviepy.VideoFileClip(r"" + myPath)
                result = moviepy.CompositeVideoClip([clip])
                result.write_videofile(pathOnly + output, codec='libvpx')
        else:

            print("NO VALID")
            #threading.Thread(target=call_warn_popup).start()

    elif myInput == ".png" or myInput == ".jpg" or myInput == ".jpeg" or myInput == ".webp" or myInput == ".tiff":
        if output == ".png" or output == ".jpg" or output == ".jpeg" or output == ".webp" or output == ".tiff":
            if myInput != output:
                im1 = Image.open(myPath)
                im1.save(f"{pathOnly}{output}")
            else:
                print("NO VALID")
        else:
            print("NO VALID")
    elif myInput == ".mp3" or myInput == ".wac" or myInput == ".acc" or myInput == ".flac" or myInput == ".aiff":
        if output == ".mp3" or output == ".wac" or output == ".acc" or output == ".flac" or output == ".aiff":
            if myInput != output:
                # TODO
                pass

            else:
                print("NO VALID")
        else:
            print("NO VALID")
    else:
        print("NO VALID")

        


if __name__ == "__main__":
    detect(r"C:\Users\migue\Desktop\myapp\test.avi", ".mkv")