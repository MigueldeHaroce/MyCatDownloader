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
from converter import detect
import time


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
        self.ui.pushButton_5.clicked.connect(self.passInfo)
        self.ui.pushButton_9.clicked.connect(self.passInfo)
        self.ui.pushButton_8.clicked.connect(self.passInfo)

        self.ui.checkBox.stateChanged.connect(self.uncheck)
        self.ui.checkBox_2.stateChanged.connect(self.uncheck)
        self.ui.checkBox_3.stateChanged.connect(self.uncheck)
        self.ui.checkBox_4.stateChanged.connect(self.uncheck)
        self.ui.checkBox_5.stateChanged.connect(self.uncheck)
        self.ui.checkBox_11.stateChanged.connect(self.uncheck)
        self.ui.checkBox_12.stateChanged.connect(self.uncheck)
        self.ui.checkBox_13.stateChanged.connect(self.uncheck)
        self.ui.checkBox_14.stateChanged.connect(self.uncheck)
        self.ui.checkBox_15.stateChanged.connect(self.uncheck)
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
            if self.sender() == self.ui.checkBox:

                # making other check box to uncheck
                self.ui.checkBox_2.setChecked(False)
                self.ui.checkBox_3.setChecked(False)
                self.ui.checkBox_4.setChecked(False)
                self.ui.checkBox_5.setChecked(False)
                self.ui.checkBox_11.setChecked(False)
                self.ui.checkBox_12.setChecked(False)
                self.ui.checkBox_13.setChecked(False)
                self.ui.checkBox_14.setChecked(False)
                self.ui.checkBox_15.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".avi"

            # if second check box is selected
            elif self.sender() == self.ui.checkBox_2:

                # making other check box to uncheck
                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_3.setChecked(False)
                self.ui.checkBox_4.setChecked(False)
                self.ui.checkBox_5.setChecked(False)
                self.ui.checkBox_11.setChecked(False)
                self.ui.checkBox_12.setChecked(False)
                self.ui.checkBox_13.setChecked(False)
                self.ui.checkBox_14.setChecked(False)
                self.ui.checkBox_15.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".mp4"

            # if third check box is selected
            elif self.sender() == self.ui.checkBox_3:

                # making other check box to uncheck
                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_2.setChecked(False)
                self.ui.checkBox_4.setChecked(False)
                self.ui.checkBox_5.setChecked(False)
                self.ui.checkBox_11.setChecked(False)
                self.ui.checkBox_12.setChecked(False)
                self.ui.checkBox_13.setChecked(False)
                self.ui.checkBox_14.setChecked(False)
                self.ui.checkBox_15.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".mkv"

            # if third check box is selected
            elif self.sender() == self.ui.checkBox_4:

                # making other check box to uncheck
                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_2.setChecked(False)
                self.ui.checkBox_3.setChecked(False)
                self.ui.checkBox_5.setChecked(False)
                self.ui.checkBox_11.setChecked(False)
                self.ui.checkBox_12.setChecked(False)
                self.ui.checkBox_13.setChecked(False)
                self.ui.checkBox_14.setChecked(False)
                self.ui.checkBox_15.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".webm"
            # if third check box is selected
            elif self.sender() == self.ui.checkBox_5:

                # making other check box to uncheck
                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_2.setChecked(False)
                self.ui.checkBox_3.setChecked(False)
                self.ui.checkBox_4.setChecked(False)
                self.ui.checkBox_11.setChecked(False)
                self.ui.checkBox_12.setChecked(False)
                self.ui.checkBox_13.setChecked(False)
                self.ui.checkBox_14.setChecked(False)
                self.ui.checkBox_15.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".mov"
            # if third check box is selected
            elif self.sender() == self.ui.checkBox_11:

                # making other check box to uncheck
                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_2.setChecked(False)
                self.ui.checkBox_3.setChecked(False)
                self.ui.checkBox_4.setChecked(False)
                self.ui.checkBox_5.setChecked(False)
                self.ui.checkBox_12.setChecked(False)
                self.ui.checkBox_13.setChecked(False)
                self.ui.checkBox_14.setChecked(False)
                self.ui.checkBox_15.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".mp3"
                # if third check box is selected
            elif self.sender() == self.ui.checkBox_12:

                # making other check box to uncheck
                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_2.setChecked(False)
                self.ui.checkBox_3.setChecked(False)
                self.ui.checkBox_4.setChecked(False)
                self.ui.checkBox_5.setChecked(False)
                self.ui.checkBox_11.setChecked(False)
                self.ui.checkBox_13.setChecked(False)
                self.ui.checkBox_14.setChecked(False)
                self.ui.checkBox_15.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".wac"
                # if third check box is selected
            elif self.sender() == self.ui.checkBox_13:

                # making other check box to uncheck
                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_2.setChecked(False)
                self.ui.checkBox_3.setChecked(False)
                self.ui.checkBox_4.setChecked(False)
                self.ui.checkBox_5.setChecked(False)
                self.ui.checkBox_11.setChecked(False)
                self.ui.checkBox_12.setChecked(False)
                self.ui.checkBox_14.setChecked(False)
                self.ui.checkBox_15.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".acc"
                # if third check box is selected
            elif self.sender() == self.ui.checkBox_14:

                # making other check box to uncheck
                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_2.setChecked(False)
                self.ui.checkBox_3.setChecked(False)
                self.ui.checkBox_4.setChecked(False)
                self.ui.checkBox_5.setChecked(False)
                self.ui.checkBox_11.setChecked(False)
                self.ui.checkBox_12.setChecked(False)
                self.ui.checkBox_13.setChecked(False)
                self.ui.checkBox_15.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".flac"
                # if third check box is selected
            elif self.sender() == self.ui.checkBox_15:

                # making other check box to uncheck
                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_2.setChecked(False)
                self.ui.checkBox_3.setChecked(False)
                self.ui.checkBox_4.setChecked(False)
                self.ui.checkBox_5.setChecked(False)
                self.ui.checkBox_11.setChecked(False)
                self.ui.checkBox_12.setChecked(False)
                self.ui.checkBox_13.setChecked(False)
                self.ui.checkBox_14.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".aiff"
                # if third check box is selected
            elif self.sender() == self.ui.checkBox_16:

                # making other check box to uncheck
                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_2.setChecked(False)
                self.ui.checkBox_3.setChecked(False)
                self.ui.checkBox_4.setChecked(False)
                self.ui.checkBox_5.setChecked(False)
                self.ui.checkBox_11.setChecked(False)
                self.ui.checkBox_12.setChecked(False)
                self.ui.checkBox_13.setChecked(False)
                self.ui.checkBox_14.setChecked(False)
                self.ui.checkBox_15.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".png"
                # if third check box is selected
            elif self.sender() == self.ui.checkBox_17:

                # making other check box to uncheck
                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_2.setChecked(False)
                self.ui.checkBox_3.setChecked(False)
                self.ui.checkBox_4.setChecked(False)
                self.ui.checkBox_5.setChecked(False)
                self.ui.checkBox_11.setChecked(False)
                self.ui.checkBox_12.setChecked(False)
                self.ui.checkBox_13.setChecked(False)
                self.ui.checkBox_14.setChecked(False)
                self.ui.checkBox_15.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".jpg"
                # if third check box is selected
            elif self.sender() == self.ui.checkBox_18:

                # making other check box to uncheck
                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_2.setChecked(False)
                self.ui.checkBox_3.setChecked(False)
                self.ui.checkBox_4.setChecked(False)
                self.ui.checkBox_5.setChecked(False)
                self.ui.checkBox_11.setChecked(False)
                self.ui.checkBox_12.setChecked(False)
                self.ui.checkBox_13.setChecked(False)
                self.ui.checkBox_14.setChecked(False)
                self.ui.checkBox_15.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_19.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".jpeg"
                # if third check box is selected
            elif self.sender() == self.ui.checkBox_19:

                # making other check box to uncheck
                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_2.setChecked(False)
                self.ui.checkBox_3.setChecked(False)
                self.ui.checkBox_4.setChecked(False)
                self.ui.checkBox_5.setChecked(False)
                self.ui.checkBox_11.setChecked(False)
                self.ui.checkBox_12.setChecked(False)
                self.ui.checkBox_13.setChecked(False)
                self.ui.checkBox_14.setChecked(False)
                self.ui.checkBox_15.setChecked(False)
                self.ui.checkBox_16.setChecked(False)
                self.ui.checkBox_17.setChecked(False)
                self.ui.checkBox_18.setChecked(False)
                self.ui.checkBox_20.setChecked(False)
                self.format = ".webp"
            # if third check box is selected
            elif self.sender() == self.ui.checkBox_20:

                # making other check box to uncheck
                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_2.setChecked(False)
                self.ui.checkBox_3.setChecked(False)
                self.ui.checkBox_4.setChecked(False)
                self.ui.checkBox_5.setChecked(False)
                self.ui.checkBox_11.setChecked(False)
                self.ui.checkBox_12.setChecked(False)
                self.ui.checkBox_13.setChecked(False)
                self.ui.checkBox_14.setChecked(False)
                self.ui.checkBox_15.setChecked(False)
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
        time.sleep(1)
        #self.thread1 = threading.Thread(target=self.set_Myprogress).start()
        my_path = my_path_to_pass
        detect(my_path, self.format)

    def showTime(self):

        # getting current time
        current_time = QTime.currentTime()

        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')

        # showing it to the label
        self.ui.clockLab.setText(label_time)


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
