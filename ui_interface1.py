# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledKbsPGf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomStackedWidget
from Custom_Widgets.Widgets import QCustomSlideMenu


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(321, 346)
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
        self.verticalLayout.setContentsMargins(0, 9, 0, 0)
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
        self.vidBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"logois/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.vidBtn.setIcon(icon1)
        self.vidBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.vidBtn)

        self.imgBtn = QPushButton(self.frame_2)
        self.imgBtn.setObjectName(u"imgBtn")
        self.imgBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"logois/image.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.imgBtn.setIcon(icon2)
        self.imgBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.imgBtn)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        icon3 = QIcon()
        icon3.addFile(u"logois/arrow-down-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.pushButton)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

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
        self.minusBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"logois/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minusBtn.setIcon(icon4)

        self.horizontalLayout_5.addWidget(self.minusBtn)

        self.exitBtn = QPushButton(self.frame_6)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"logois/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exitBtn.setIcon(icon5)
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
        self.stackedWidget_2.setCursor(QCursor(Qt.ArrowCursor))
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
        self.verticalLayout_2 = QVBoxLayout(self.widget_22)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_23 = QWidget(self.widget_22)
        self.widget_23.setObjectName(u"widget_23")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_23.sizePolicy().hasHeightForWidth())
        self.widget_23.setSizePolicy(sizePolicy4)
        self.horizontalLayout_18 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(9, 9, 9, 9)
        self.label_14 = QLabel(self.widget_23)
        self.label_14.setObjectName(u"label_14")
        font1 = QFont()
        font1.setPointSize(15)
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_18.addWidget(self.label_14, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.widget_23, 0, Qt.AlignTop)

        self.widget_24 = QWidget(self.widget_22)
        self.widget_24.setObjectName(u"widget_24")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_24.sizePolicy().hasHeightForWidth())
        self.widget_24.setSizePolicy(sizePolicy5)
        self.widget_24.setLayoutDirection(Qt.LeftToRight)
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
        font2 = QFont()
        font2.setPointSize(8)
        self.pushButton_9.setFont(font2)
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_18.addWidget(self.pushButton_9, 0, Qt.AlignLeft)


        self.horizontalLayout_19.addWidget(self.widget_26, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.widget_24)

        self.widget_3 = QWidget(self.widget_22)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_to_change1 = QLabel(self.widget_3)
        self.label_to_change1.setObjectName(u"label_to_change1")
        self.label_to_change1.setStyleSheet(u"color:rgb(255,255,255);\n"
"font:45px;")

        self.horizontalLayout_3.addWidget(self.label_to_change1, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.verticalLayout_9.addWidget(self.widget_22, 0, Qt.AlignTop)


        self.horizontalLayout_11.addWidget(self.widget_11)

        self.stackedWidget_2.addWidget(self.imgPage)
        self.vidPage = QWidget()
        self.vidPage.setObjectName(u"vidPage")
        self.verticalLayout_5 = QVBoxLayout(self.vidPage)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.widget_2 = QWidget(self.vidPage)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_27 = QWidget(self.widget_2)
        self.widget_27.setObjectName(u"widget_27")
        self.verticalLayout_3 = QVBoxLayout(self.widget_27)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_28 = QWidget(self.widget_27)
        self.widget_28.setObjectName(u"widget_28")
        sizePolicy4.setHeightForWidth(self.widget_28.sizePolicy().hasHeightForWidth())
        self.widget_28.setSizePolicy(sizePolicy4)
        self.horizontalLayout_20 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(9, 9, 9, 9)
        self.label_15 = QLabel(self.widget_28)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_20.addWidget(self.label_15, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.widget_28, 0, Qt.AlignTop)

        self.widget_29 = QWidget(self.widget_27)
        self.widget_29.setObjectName(u"widget_29")
        sizePolicy5.setHeightForWidth(self.widget_29.sizePolicy().hasHeightForWidth())
        self.widget_29.setSizePolicy(sizePolicy5)
        self.widget_29.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_21 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 6, 0, 0)
        self.widget_30 = QWidget(self.widget_29)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setStyleSheet(u"* {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #2c313c;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"\n"
"}")
        self.verticalLayout_19 = QVBoxLayout(self.widget_30)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, -1, 0, -1)
        self.checkBox_21 = QCheckBox(self.widget_30)
        self.checkBox_21.setObjectName(u"checkBox_21")

        self.verticalLayout_19.addWidget(self.checkBox_21, 0, Qt.AlignLeft)

        self.checkBox_22 = QCheckBox(self.widget_30)
        self.checkBox_22.setObjectName(u"checkBox_22")

        self.verticalLayout_19.addWidget(self.checkBox_22, 0, Qt.AlignLeft)

        self.checkBox_23 = QCheckBox(self.widget_30)
        self.checkBox_23.setObjectName(u"checkBox_23")

        self.verticalLayout_19.addWidget(self.checkBox_23, 0, Qt.AlignLeft)


        self.horizontalLayout_21.addWidget(self.widget_30, 0, Qt.AlignTop)

        self.widget_31 = QWidget(self.widget_29)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setStyleSheet(u"* {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #2c313c;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"\n"
"}")
        self.verticalLayout_20 = QVBoxLayout(self.widget_31)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, -1, 0, -1)
        self.checkBox_24 = QCheckBox(self.widget_31)
        self.checkBox_24.setObjectName(u"checkBox_24")
        self.checkBox_24.setTristate(False)

        self.verticalLayout_20.addWidget(self.checkBox_24, 0, Qt.AlignLeft)

        self.checkBox_25 = QCheckBox(self.widget_31)
        self.checkBox_25.setObjectName(u"checkBox_25")
        self.checkBox_25.setTristate(False)

        self.verticalLayout_20.addWidget(self.checkBox_25, 0, Qt.AlignLeft)

        self.pushButton_10 = QPushButton(self.widget_31)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font2)
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_20.addWidget(self.pushButton_10, 0, Qt.AlignLeft)


        self.horizontalLayout_21.addWidget(self.widget_31, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.widget_29, 0, Qt.AlignTop)

        self.widget_4 = QWidget(self.widget_27)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_to_change = QLabel(self.widget_4)
        self.label_to_change.setObjectName(u"label_to_change")
        self.label_to_change.setStyleSheet(u"color:rgb(255,255,255);\n"
"font:45px;")

        self.horizontalLayout_4.addWidget(self.label_to_change, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.widget_4)


        self.horizontalLayout_8.addWidget(self.widget_27, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.stackedWidget_2.addWidget(self.vidPage)
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
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy6)

        self.verticalLayout_8.addWidget(self.label_9, 0, Qt.AlignBottom)

        self.label_10 = QLabel(self.widget_10)
        self.label_10.setObjectName(u"label_10")
        sizePolicy6.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy6)
        font3 = QFont()
        font3.setFamily(u"Corbel")
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_10.setFont(font3)

        self.verticalLayout_8.addWidget(self.label_10, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.clockLab = QLabel(self.widget_10)
        self.clockLab.setObjectName(u"clockLab")

        self.verticalLayout_8.addWidget(self.clockLab, 0, Qt.AlignHCenter)


        self.horizontalLayout_10.addWidget(self.widget_10, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.stackedWidget_2.addWidget(self.homePage)

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
        self.pushButton.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"MyCat Downloader", None))
        self.minusBtn.setText("")
        self.exitBtn.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Image Formats!</p></body></html>", None))
        self.checkBox_16.setText(QCoreApplication.translate("MainWindow", u".png", None))
        self.checkBox_17.setText(QCoreApplication.translate("MainWindow", u".jpg", None))
        self.checkBox_18.setText(QCoreApplication.translate("MainWindow", u".jpeg", None))
        self.checkBox_19.setText(QCoreApplication.translate("MainWindow", u".webp", None))
        self.checkBox_20.setText(QCoreApplication.translate("MainWindow", u".tiff", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Convert!", None))
        self.label_to_change1.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Video Formats!</p></body></html>", None))
        self.checkBox_21.setText(QCoreApplication.translate("MainWindow", u".mp4", None))
        self.checkBox_22.setText(QCoreApplication.translate("MainWindow", u".mkv", None))
        self.checkBox_23.setText(QCoreApplication.translate("MainWindow", u".avi", None))
        self.checkBox_24.setText(QCoreApplication.translate("MainWindow", u".webm", None))
        self.checkBox_25.setText(QCoreApplication.translate("MainWindow", u".mov", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Convert!", None))
        self.label_to_change.setText("")
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"________________________________________", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"FORMAT MENU", None))
        self.clockLab.setText("")
    # retranslateUi

