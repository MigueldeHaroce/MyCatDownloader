# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledFzatnd.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomStackedWidget
from Custom_Widgets.Widgets import QCustomSlideMenu


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(361, 329)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color:transparent;\n"
"	background:transparent;\n"
"	padding:0;\n"
"	margin:0;\n"
"	color:fff;\n"
"\n"
"}\n"
"#leftContainer{\n"
"	background-color:#16191d;\n"
"}\n"
"#leftContainer QPushButton{\n"
"	text-align:left;\n"
"	padding:5px 10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"background-color: #2c313c;\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftContainer = QWidget(self.centralwidget)
        self.leftContainer.setObjectName(u"leftContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftContainer.sizePolicy().hasHeightForWidth())
        self.leftContainer.setSizePolicy(sizePolicy1)
        self.leftContainer.setMaximumSize(QSize(45, 16777215))
        self.leftContainer.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.leftContainer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.leftContainer)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.widget.setStyleSheet(u"background-color:#16191d")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 9, 0, 9)
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setStyleSheet(u"font: 8pt \"Franklin Gothic Medium\";\n"
"color: rgb(255, 255, 255);background-color:#1f232a;")
        icon = QIcon()
        icon.addFile(u"logois/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.homeBtn)

        self.vidBtn = QPushButton(self.frame_2)
        self.vidBtn.setObjectName(u"vidBtn")
        icon1 = QIcon()
        icon1.addFile(u"logois/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.vidBtn.setIcon(icon1)
        self.vidBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.vidBtn)

        self.imgBtn = QPushButton(self.frame_2)
        self.imgBtn.setObjectName(u"imgBtn")
        icon2 = QIcon()
        icon2.addFile(u"logois/image.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.imgBtn.setIcon(icon2)
        self.imgBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.imgBtn)

        self.musBtn = QPushButton(self.frame_2)
        self.musBtn.setObjectName(u"musBtn")
        icon3 = QIcon()
        icon3.addFile(u"logois/music.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.musBtn.setIcon(icon3)
        self.musBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.musBtn)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        icon4 = QIcon()
        icon4.addFile(u"logois/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon4)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_11.addWidget(self.infoBtn)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.widget, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftContainer)

        self.mainContainer = QWidget(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainContainer.sizePolicy().hasHeightForWidth())
        self.mainContainer.setSizePolicy(sizePolicy3)
        self.mainContainer.setStyleSheet(u"background-color:#1f232a;\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.mainContainer)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.topContainer = QFrame(self.mainContainer)
        self.topContainer.setObjectName(u"topContainer")
        self.topContainer.setStyleSheet(u"background-color: #2c313c;\n"
"")
        self.topContainer.setFrameShape(QFrame.StyledPanel)
        self.topContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.topContainer)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_7 = QFrame(self.topContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(34, 34))
        self.label_4.setPixmap(QPixmap(u"unnamed.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_4, 0, Qt.AlignLeft)

        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label_5, 0, Qt.AlignLeft)


        self.horizontalLayout_7.addWidget(self.frame_7, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.topContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.minusBtn = QPushButton(self.frame_6)
        self.minusBtn.setObjectName(u"minusBtn")
        icon5 = QIcon()
        icon5.addFile(u"logois/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minusBtn.setIcon(icon5)

        self.horizontalLayout_5.addWidget(self.minusBtn)

        self.exitBtn = QPushButton(self.frame_6)
        self.exitBtn.setObjectName(u"exitBtn")
        icon6 = QIcon()
        icon6.addFile(u"logois/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exitBtn.setIcon(icon6)
        self.exitBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.exitBtn)


        self.horizontalLayout_7.addWidget(self.frame_6, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.topContainer)

        self.widget_7 = QCustomSlideMenu(self.mainContainer)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QCustomStackedWidget(self.widget_7)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.horizontalLayout_10 = QHBoxLayout(self.homePage)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widget_10 = QWidget(self.homePage)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"*{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.widget_10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.widget_10)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QSize(200, 150))
        self.label_8.setPixmap(QPixmap(u"kindpng_2099181.png"))
        self.label_8.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.label_9 = QLabel(self.widget_10)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)

        self.verticalLayout_8.addWidget(self.label_9, 0, Qt.AlignBottom)

        self.label_10 = QLabel(self.widget_10)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setFamily(u"Corbel")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_10.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_10, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.clockLab = QLabel(self.widget_10)
        self.clockLab.setObjectName(u"clockLab")

        self.verticalLayout_8.addWidget(self.clockLab, 0, Qt.AlignHCenter)


        self.horizontalLayout_10.addWidget(self.widget_10, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.stackedWidget_2.addWidget(self.homePage)
        self.vidPage = QWidget()
        self.vidPage.setObjectName(u"vidPage")
        self.verticalLayout_5 = QVBoxLayout(self.vidPage)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 0)
        self.widget_2 = QWidget(self.vidPage)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy5)
        self.verticalLayout_15 = QVBoxLayout(self.widget_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_21 = QWidget(self.widget_2)
        self.widget_21.setObjectName(u"widget_21")
        sizePolicy5.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy5)
        self.horizontalLayout_17 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_21)
        self.label_11.setObjectName(u"label_11")
        font2 = QFont()
        font2.setPointSize(15)
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_17.addWidget(self.label_11, 0, Qt.AlignTop)


        self.verticalLayout_15.addWidget(self.widget_21, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.widget_2, 0, Qt.AlignHCenter)

        self.widget_6 = QWidget(self.vidPage)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy4.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy4)
        self.horizontalLayout_8 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 6, 0, 0)
        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"* {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #2c313c;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.widget_9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.checkBox_2 = QCheckBox(self.widget_9)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_6.addWidget(self.checkBox_2, 0, Qt.AlignLeft)

        self.checkBox_3 = QCheckBox(self.widget_9)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_6.addWidget(self.checkBox_3, 0, Qt.AlignLeft)

        self.checkBox = QCheckBox(self.widget_9)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_6.addWidget(self.checkBox, 0, Qt.AlignLeft)


        self.horizontalLayout_8.addWidget(self.widget_9, 0, Qt.AlignTop)

        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"* {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #2c313c;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.widget_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.checkBox_4 = QCheckBox(self.widget_8)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setTristate(False)

        self.verticalLayout_7.addWidget(self.checkBox_4, 0, Qt.AlignLeft)

        self.checkBox_5 = QCheckBox(self.widget_8)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setTristate(False)

        self.verticalLayout_7.addWidget(self.checkBox_5, 0, Qt.AlignLeft)

        self.pushButton_5 = QPushButton(self.widget_8)
        self.pushButton_5.setObjectName(u"pushButton_5")
        font3 = QFont()
        font3.setPointSize(8)
        self.pushButton_5.setFont(font3)

        self.verticalLayout_7.addWidget(self.pushButton_5, 0, Qt.AlignLeft)


        self.horizontalLayout_8.addWidget(self.widget_8, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.widget_6, 0, Qt.AlignTop)

        self.stackedWidget_2.addWidget(self.vidPage)
        self.imgPage = QWidget()
        self.imgPage.setObjectName(u"imgPage")
        self.horizontalLayout_11 = QHBoxLayout(self.imgPage)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.widget_11 = QWidget(self.imgPage)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_9 = QVBoxLayout(self.widget_11)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_22 = QWidget(self.widget_11)
        self.widget_22.setObjectName(u"widget_22")
        self.verticalLayout_16 = QVBoxLayout(self.widget_22)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_23 = QWidget(self.widget_22)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(9, 9, 9, 9)
        self.label_14 = QLabel(self.widget_23)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_18.addWidget(self.label_14, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.widget_23)

        self.widget_24 = QWidget(self.widget_22)
        self.widget_24.setObjectName(u"widget_24")
        sizePolicy4.setHeightForWidth(self.widget_24.sizePolicy().hasHeightForWidth())
        self.widget_24.setSizePolicy(sizePolicy4)
        self.horizontalLayout_19 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 6, 0, 0)
        self.widget_25 = QWidget(self.widget_24)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setStyleSheet(u"* {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #2c313c;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"\n"
"}")
        self.verticalLayout_17 = QVBoxLayout(self.widget_25)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, -1, 0, -1)
        self.checkBox_16 = QCheckBox(self.widget_25)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.verticalLayout_17.addWidget(self.checkBox_16, 0, Qt.AlignLeft)

        self.checkBox_17 = QCheckBox(self.widget_25)
        self.checkBox_17.setObjectName(u"checkBox_17")

        self.verticalLayout_17.addWidget(self.checkBox_17, 0, Qt.AlignLeft)

        self.checkBox_18 = QCheckBox(self.widget_25)
        self.checkBox_18.setObjectName(u"checkBox_18")

        self.verticalLayout_17.addWidget(self.checkBox_18, 0, Qt.AlignLeft)


        self.horizontalLayout_19.addWidget(self.widget_25, 0, Qt.AlignTop)

        self.widget_26 = QWidget(self.widget_24)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setStyleSheet(u"* {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #2c313c;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"\n"
"}")
        self.verticalLayout_18 = QVBoxLayout(self.widget_26)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, -1, 0, -1)
        self.checkBox_19 = QCheckBox(self.widget_26)
        self.checkBox_19.setObjectName(u"checkBox_19")
        self.checkBox_19.setTristate(False)

        self.verticalLayout_18.addWidget(self.checkBox_19, 0, Qt.AlignLeft)

        self.checkBox_20 = QCheckBox(self.widget_26)
        self.checkBox_20.setObjectName(u"checkBox_20")
        self.checkBox_20.setTristate(False)

        self.verticalLayout_18.addWidget(self.checkBox_20, 0, Qt.AlignLeft)

        self.pushButton_9 = QPushButton(self.widget_26)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font3)

        self.verticalLayout_18.addWidget(self.pushButton_9, 0, Qt.AlignLeft)


        self.horizontalLayout_19.addWidget(self.widget_26, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.widget_24)


        self.verticalLayout_9.addWidget(self.widget_22)


        self.horizontalLayout_11.addWidget(self.widget_11)

        self.stackedWidget_2.addWidget(self.imgPage)
        self.audPage = QWidget()
        self.audPage.setObjectName(u"audPage")
        self.horizontalLayout_14 = QHBoxLayout(self.audPage)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 9, -1, 0)
        self.widget_16 = QWidget(self.audPage)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_14 = QVBoxLayout(self.widget_16)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.widget_20 = QWidget(self.widget_16)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(9, 9, 9, 9)
        self.label_13 = QLabel(self.widget_20)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_16.addWidget(self.label_13, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_14.addWidget(self.widget_20)

        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy4.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy4)
        self.horizontalLayout_15 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 6, 0, 0)
        self.widget_18 = QWidget(self.widget_17)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setStyleSheet(u"* {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #2c313c;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.widget_18)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, 0, -1)
        self.checkBox_11 = QCheckBox(self.widget_18)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.verticalLayout_12.addWidget(self.checkBox_11, 0, Qt.AlignLeft)

        self.checkBox_12 = QCheckBox(self.widget_18)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.verticalLayout_12.addWidget(self.checkBox_12, 0, Qt.AlignLeft)

        self.checkBox_13 = QCheckBox(self.widget_18)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.verticalLayout_12.addWidget(self.checkBox_13, 0, Qt.AlignLeft)


        self.horizontalLayout_15.addWidget(self.widget_18, 0, Qt.AlignTop)

        self.widget_19 = QWidget(self.widget_17)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setStyleSheet(u"* {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #2c313c;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.widget_19)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, -1, 0, -1)
        self.checkBox_14 = QCheckBox(self.widget_19)
        self.checkBox_14.setObjectName(u"checkBox_14")
        self.checkBox_14.setTristate(False)

        self.verticalLayout_13.addWidget(self.checkBox_14, 0, Qt.AlignLeft)

        self.checkBox_15 = QCheckBox(self.widget_19)
        self.checkBox_15.setObjectName(u"checkBox_15")
        self.checkBox_15.setTristate(False)

        self.verticalLayout_13.addWidget(self.checkBox_15, 0, Qt.AlignLeft)

        self.pushButton_8 = QPushButton(self.widget_19)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font3)

        self.verticalLayout_13.addWidget(self.pushButton_8, 0, Qt.AlignLeft)


        self.horizontalLayout_15.addWidget(self.widget_19, 0, Qt.AlignTop)


        self.verticalLayout_14.addWidget(self.widget_17)


        self.horizontalLayout_14.addWidget(self.widget_16)

        self.stackedWidget_2.addWidget(self.audPage)

        self.horizontalLayout_12.addWidget(self.stackedWidget_2)


        self.verticalLayout_4.addWidget(self.widget_7)


        self.horizontalLayout.addWidget(self.mainContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.homeBtn.setText("")
        self.vidBtn.setText("")
        self.imgBtn.setText("")
        self.musBtn.setText("")
        self.infoBtn.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"MyCat Downloader", None))
        self.minusBtn.setText("")
        self.exitBtn.setText("")
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"________________________________________", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"FORMAT MENU", None))
        self.clockLab.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Video Formats!</p></body></html>", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u".mp4", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u".mkv", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u".avi", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u".webp", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u".mov", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Convert!", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Image Formats!</p></body></html>", None))
        self.checkBox_16.setText(QCoreApplication.translate("MainWindow", u".png", None))
        self.checkBox_17.setText(QCoreApplication.translate("MainWindow", u".jpg", None))
        self.checkBox_18.setText(QCoreApplication.translate("MainWindow", u".jpeg", None))
        self.checkBox_19.setText(QCoreApplication.translate("MainWindow", u".webp", None))
        self.checkBox_20.setText(QCoreApplication.translate("MainWindow", u".tiff", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Convert!", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Audio Formats!</p></body></html>", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u".mp3", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u".wav", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u".aac", None))
        self.checkBox_14.setText(QCoreApplication.translate("MainWindow", u".flac", None))
        self.checkBox_15.setText(QCoreApplication.translate("MainWindow", u".aiff", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Convert!", None))
    # retranslateUi

