########################################################################
## IMPORTS
########################################################################
import threading
import urllib.request
########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################
import main1
########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
########################################################################
from youtubeDownloader import downloadYtVid, downloadYtAudio
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

import sys

########################################################################
# MAIN WINDOW CLASS
########################################################################

class dragEffect(QtWidgets.QLabel, QMainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self)
        super(dragEffect, self).__init__(*args, **kwargs)
        self.setFrameShape(QtWidgets.QFrame.Box) #type: ignore
        self.setAcceptDrops(True)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()
            file_path = e.mimeData().urls()[0].toLocalFile()
            #print(file_path)
            #detect(file_path, ".mkv")
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
                if i in file_path:
                    print("valid format")
                    input_format = i
            try:
                if input_format == ".mp3" or input_format == ".wac" or input_format == ".acc" or input_format == ".flac" or input_format == ".aiff":
                    msg = QMessageBox()
                    msg.setWindowTitle("Alert")
                    msg.setText("No audio files accepted")
                    msg.setIcon(QMessageBox.Information)
                    x = msg.exec_()

                else:
                    popup = main1.MainWindow1()
                    popup.get_path(idk=file_path)
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Alert")
                msg.setText("No other files accepted")
                msg.setIcon(QMessageBox.Information)
                x = msg.exec_()
            
            
        else:
            e.ignore()

class HyperlinkLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('font-size: 35px')
        self.setOpenExternalLinks(True)


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self) # type: ignore
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label_18 = dragEffect("label_17")
        self.ui.label_18.setObjectName(u"label_17")
        font8 = QFont()
        font8.setPointSize(12)
        self.ui.label_18.setFont(font8)
        self.ui.label_18.setStyleSheet(u"border: 2px dashed #fff;\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color: #2c313c\n"
        )
        self.ui.label_18.setAlignment(Qt.AlignCenter)
        self.ui.label_18.setText(QCoreApplication.translate("MainWindow", u"Drag your File Here!", None))
        self.ui.label_18.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        self.ui.verticalLayout_21.addWidget(self.ui.label_18)



        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################

        ########################################################################

        self.show()

        # EXPAND CENTER MENU WIDGET SIZE
        self.ui.HelpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.InfoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())

        # CLOSE CENTER MENU WIDGET SIZE
        self.ui.closeMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())
        self.ui.pushButton_2.clicked.connect(self.clickedDownload)
        self.ui.pushButton_4.clicked.connect(self.clickedDownloadM)

        linkTemplate = '<a href={0}>{1}</a>'
        self.ui.label_17 = HyperlinkLabel()
        self.ui.label_17.setText(linkTemplate.format('https://Google.com', 'Google.com'))
        timer = QTimer(self)

        # adding action to timer
        timer.timeout.connect(self.showTime)

        # update the timer every second
        timer.start(1000)




    def clickedDownload(self):
        text = self.ui.textEdit.toPlainText()
        response = QFileDialog.getExistingDirectory(
            self,
            caption='Select a folder'
        )
        validation = None
        try:
            urllib.request.urlopen('http://google.com') #Python 3.x
            validation = True
        except:
            validation = False
        print('connected' if validation else 'no internet!')
        if validation:
            try:
                downloadYtVid(text, response)
                msg = QMessageBox()
                msg.setWindowTitle("Alert")
                msg.setText("Your video is downloaded!")
                msg.setInformativeText("Thanks for Using MyCatDownloader")
                msg.setIcon(QMessageBox.Information)
                x = msg.exec_()

            except:
                self.ui.textEdit.setPlainText("Put a valid Url!")

    def clickedDownloadM(self):
        text = self.ui.textEdit_2.toPlainText()
        response = QFileDialog.getExistingDirectory(
            self,
            caption='Select a folder'
        )
        validation = None
        try:
            urllib.request.urlopen('http://google.com')
            validation = True
        except:
            validation = False
        if validation:
            try:
                downloadYtAudio(text, response)
                msg = QMessageBox()
                msg.setWindowTitle("Alert")
                msg.setText("Your music is downloaded!")
                msg.setInformativeText("Thanks for Using MyCatDownloader")
                msg.setIcon(QMessageBox.Information)
                x = msg.exec_()

            except:
                self.ui.textEdit_2.setPlainText("Put a valid Url!")

    def showTime(self):

        # getting current time
        current_time = QTime.currentTime()

        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')

        # showing it to the label
        self.ui.clock.setText(label_time)

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

########################################################################
## END
########################################################################  