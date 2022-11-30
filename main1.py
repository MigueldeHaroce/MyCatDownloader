########################################################################
## IMPORTS
########################################################################


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

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow1(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

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

    def passInfo(self):
        my_path = my_path_to_pass
        threading.Thread(target=detect, args=(my_path, self.format,)).start()


        
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