########################################################################
## IMPORTS
########################################################################
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import PyQt5 as qt
########################################################################
# IMPORT GUI FILE
from ui_interface1 import *
########################################################################
import threading
########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
########################################################################
from converter import Convert
import time
from pathlib import Path
import moviepy.editor as moviepy
from PIL import Image
import re
from os import path
from pydub import AudioSegment
import sys
import subprocess

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow1(QMainWindow):
    #finished = qt.QtCore.pyqtSignal()
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.running = False
        #self.kill_reason = None
        #self.lock = threading.Lock()
        #self.finished.connect(self.set_Myprogress)
        #QGraphicsObject()


        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui, jsonFiles={
            "style1.json",
            "style1.json"
        })
        ########################################################################
        self.format = None
        self.ui.pushButton_10.clicked.connect(self.passInfo)
        self.ui.pushButton_9.clicked.connect(self.passInfo)

        self.ui.checkBox_21.stateChanged.connect(self.uncheck)
        self.ui.checkBox_22.stateChanged.connect(self.uncheck)
        self.ui.checkBox_23.stateChanged.connect(self.uncheck)
        self.ui.checkBox_24.stateChanged.connect(self.uncheck)
        self.ui.checkBox_25.stateChanged.connect(self.uncheck)
        self.ui.checkBox_16.stateChanged.connect(self.uncheck)
        self.ui.checkBox_17.stateChanged.connect(self.uncheck)
        self.ui.checkBox_18.stateChanged.connect(self.uncheck)
        self.ui.checkBox_19.stateChanged.connect(self.uncheck)
        self.ui.checkBox_20.stateChanged.connect(self.uncheck)

        self.show()

        timer = QTimer(self)

        # adding action to timer
        timer.timeout.connect(self.showTime)

        # update the timer every second
        timer.start(1000)

    def uncheck(self, state):

        # checking if state is checked
        if state == Qt.Checked:

            # if first check box is selected
            if self.sender() == self.ui.checkBox_23:

                # making other check box to uncheck
                self.ui.checkBox_21.setChecked(False)
                self.ui.checkBox_22.setChecked(False)
                self.ui.checkBox_24.setChecked(False)
                self.ui.checkBox_25.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".avi"

            # if second check box is selected
            elif self.sender() == self.ui.checkBox_21:

                # making other check box to uncheck
                self.ui.checkBox_23.setChecked(False)
                self.ui.checkBox_22.setChecked(False)
                self.ui.checkBox_24.setChecked(False)
                self.ui.checkBox_25.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".mp4"

            # if third check box is selected
            elif self.sender() == self.ui.checkBox_22:

                # making other check box to uncheck
                self.ui.checkBox_23.setChecked(False)
                self.ui.checkBox_21.setChecked(False)
                self.ui.checkBox_24.setChecked(False)
                self.ui.checkBox_25.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".mkv"

            # if third check box is selected
            elif self.sender() == self.ui.checkBox_24:

                # making other check box to uncheck
                self.ui.checkBox_23.setChecked(False)
                self.ui.checkBox_21.setChecked(False)
                self.ui.checkBox_22.setChecked(False)
                self.ui.checkBox_25.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".webm"
            # if third check box is selected
            elif self.sender() == self.ui.checkBox_25:

                # making other check box to uncheck
                self.ui.checkBox_23.setChecked(False)
                self.ui.checkBox_21.setChecked(False)
                self.ui.checkBox_22.setChecked(False)
                self.ui.checkBox_24.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".mov"
            # if third check box is selected
            elif self.sender() == self.ui.checkBox_16:

                # making other check box to uncheck
                self.ui.checkBox_23.setChecked(False)
                self.ui.checkBox_21.setChecked(False)
                self.ui.checkBox_22.setChecked(False)
                self.ui.checkBox_24.setChecked(False)
                self.ui.checkBox_25.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".png"
                # if third check box is selected
            elif self.sender() == self.ui.checkBox_17:

                # making other check box to uncheck
                self.ui.checkBox_23.setChecked(False)
                self.ui.checkBox_21.setChecked(False)
                self.ui.checkBox_22.setChecked(False)
                self.ui.checkBox_24.setChecked(False)
                self.ui.checkBox_25.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".jpg"
                # if third check box is selected
            elif self.sender() == self.ui.checkBox_18:

                # making other check box to uncheck
                self.ui.checkBox_23.setChecked(False)
                self.ui.checkBox_21.setChecked(False)
                self.ui.checkBox_22.setChecked(False)
                self.ui.checkBox_24.setChecked(False)
                self.ui.checkBox_25.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".jpeg"
                # if third check box is selected
            elif self.sender() == self.ui.checkBox_19:

                # making other check box to uncheck
                self.ui.checkBox_23.setChecked(False)
                self.ui.checkBox_21.setChecked(False)
                self.ui.checkBox_22.setChecked(False)
                self.ui.checkBox_24.setChecked(False)
                self.ui.checkBox_25.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".webp"
            # if third check box is selected
            elif self.sender() == self.ui.checkBox_20:

                # making other check box to uncheck
                self.ui.checkBox_23.setChecked(False)
                self.ui.checkBox_21.setChecked(False)
                self.ui.checkBox_22.setChecked(False)
                self.ui.checkBox_24.setChecked(False)
                self.ui.checkBox_25.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.format = ".tiff"

    @staticmethod
    def get_path(idk):
        global my_path_to_pass
        my_path_to_pass = idk
        return my_path_to_pass

    def set_Myprogress(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alert")
        msg.setText("Your music is downloaded!")
        msg.setInformativeText("Thanks for Using MyCatDownloader")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    # https://stackoverflow.com/questions/33081529/in-pyqt-what-is-the-best-way-to-share-data-between-the-main-window-and-a-thread
    ##############################################################################################################################
    def passInfo(self):
        self.ui.label_to_change.setText(QCoreApplication.translate("MainWindow", u"Working", None))
        self.ui.label_to_change1.setText(QCoreApplication.translate("MainWindow", u"Working", None))
        #self.thread1 = threading.Thread(target=self.set_Myprogress).start()
        self.my_path = my_path_to_pass
        self.detect(self.my_path, self.format)
        #self.ui.label_to_change.setText("Done!")
        #time.sleep(1)
        #self.ui.label_to_change.setText("")




    def showTime(self):

        # getting current time
        current_time = QTime.currentTime()

        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')

        # showing it to the label
        self.ui.clockLab.setText(label_time)
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
        threading.Thread(target=self.convert, args=(nameFile, myPath, input_format, myOutput,)).start()

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
                        self.ui.label_to_change.setText(QCoreApplication.translate("Mainwindow", u"ERROR!", None))

            elif output == ".webm":
                if myInput != output:
                    clip = moviepy.VideoFileClip(r"" + myPath)
                    result = moviepy.CompositeVideoClip([clip])
                    result.write_videofile(pathOnly + output, codec='libvpx')
                    self.ui.label_to_change.setText(QCoreApplication.translate("Mainwindow", u"Done!", None))
            else:

                print("NO VALID")
                self.ui.label_to_change.setText(QCoreApplication.translate("Mainwindow", u"ERROR!", None))

        elif myInput == ".png" or myInput == ".jpg" or myInput == ".jpeg" or myInput == ".webp" or myInput == ".tiff":
            if output == ".png" or output == ".jpg" or output == ".jpeg" or output == ".webp" or output == ".tiff":
                if myInput != output:
                    im1 = Image.open(myPath)
                    im1.save(f"{pathOnly}{output}")
                    self.ui.label_to_change1.setText(QCoreApplication.translate("Mainwindow", u"Done!", None))
                else:
                    self.ui.label_to_change1.setText(QCoreApplication.translate("Mainwindow", u"ERROR!", None))
            else:
                self.ui.label_to_change1.setText(QCoreApplication.translate("Mainwindow", u"ERROR!", None))
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
            self.ui.label_to_change.setText(QCoreApplication.translate("Mainwindow", u"ERROR!", None))
            self.ui.label_to_change1.setText(QCoreApplication.translate("Mainwindow", u"ERROR!", None))


########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow1()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################
