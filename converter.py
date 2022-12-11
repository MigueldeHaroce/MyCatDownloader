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
from ui_interface1 import *

class Convert(QMainWindow):
    def __init__(self, myPath, myOutput):
        super().__init__()
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label_to_change.setText(QCoreApplication.translate("MainWindow", u"Working", None))
        self.ui.label_to_change1.setText(QCoreApplication.translate("MainWindow", u"Working", None))

    ### BIG ERROR ####### TO SOLUCIONATE ###
    def detect(self, myPath, myOutput):
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
        threading.Thread(target=self.convert, args=(self, nameFile, myPath, input_format, myOutput,)).start()

    def convert(self, name, myPath, myInput, output):
        formatsDict = len(myInput)
        nameOnly = name[:formatsDict]
        pathOnly = myPath[:-formatsDict]
        formatOnly = re.sub(r'.', '', output, count = 1)

        if myInput == ".mp4" or myInput == ".avi" or myInput == ".mkv" or myInput == ".webm" or myInput == ".mov":
            if output == ".mp4" or output == ".avi" or output == ".mkv" or output == ".mov":
                if output != ".webp":
                    if myInput != output:
                        clip = moviepy.VideoFileClip(r"" + myPath)
                        result = moviepy.CompositeVideoClip([clip])
                        result.write_videofile(pathOnly + output, codec='mpeg4')
                        self.ui.label_to_change.setText(QCoreApplication.translate("Mainwindow", u"Done!", None))
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
                    self.ui.label_to_change.setText(QCoreApplication.translate("Mainwindow", u"Done!", None))
            else:

                print("NO VALID")
                #threading.Thread(target=call_warn_popup).start()

        elif myInput == ".png" or myInput == ".jpg" or myInput == ".jpeg" or myInput == ".webp" or myInput == ".tiff":
            if output == ".png" or output == ".jpg" or output == ".jpeg" or output == ".webp" or output == ".tiff":
                if myInput != output:
                    im1 = Image.open(myPath)
                    im1.save(f"{pathOnly}{output}")
                    self.ui.label_to_change1.setText(QCoreApplication.translate("Mainwindow", u"Done!", None))
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




