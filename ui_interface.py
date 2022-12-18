# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceJvUqxE.ui'
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
        MainWindow.resize(726, 584)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
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
"\n"
"#mainBodyContainer{\n"
"	background-color:#1f232a;\n"
"}\n"
"#leftMenuContainer{\n"
"	background-color:#16191d;\n"
"}\n"
"#leftMenuContainer QPushButton{\n"
"	text-align:left;\n"
"	padding:5px 10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"#centerMenuContainer {\n"
"	background-color: #2c313c;\n"
"}\n"
"#frame_4{\n"
"	background-color: #16191d;\n"
"	border-radius: 10px;\n"
"}\n"
"#headerContainer{\n"
"	background-color: #2c313c;\n"
"}\n"
"#foot{\n"
"	background-color: #2c313c;\n"
"}\n"
"#fileContainer{\n"
"	background-color: #2c313c;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"}")
        self.centralwidget = QCustomSlideMenu(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMinimumSize(QSize(0, 487))
        self.leftMenuContainer.setMaximumSize(QSize(45, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftmenu = QWidget(self.leftMenuContainer)
        self.leftmenu.setObjectName(u"leftmenu")
        self.leftmenu.setStyleSheet(u"background-color:#16191d")
        self.verticalLayout_2 = QVBoxLayout(self.leftmenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.leftmenu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(22, 25, 29);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.menuBtn = QPushButton(self.frame_2)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setStyleSheet(u"background-color: rgb(22, 25, 29);")
        icon = QIcon()
        icon.addFile(u"logois/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame = QFrame(self.leftmenu)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame)
        self.homeBtn.setObjectName(u"homeBtn")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(31, 35, 42, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.homeBtn.setPalette(palette)
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeBtn.setStyleSheet(u"font: 8pt \"Franklin Gothic Medium\";\n"
"color: rgb(255, 255, 255);background-color:#1f232a;")
        icon1 = QIcon()
        icon1.addFile(u"logois/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.homeBtn)

        self.ytBtn = QPushButton(self.frame)
        self.ytBtn.setObjectName(u"ytBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ytBtn.sizePolicy().hasHeightForWidth())
        self.ytBtn.setSizePolicy(sizePolicy2)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush5 = QBrush(QColor(22, 25, 29, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush5)
        brush6 = QBrush(QColor(255, 255, 255, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        brush7 = QBrush(QColor(255, 255, 255, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        brush8 = QBrush(QColor(255, 255, 255, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.ytBtn.setPalette(palette1)
        font = QFont()
        font.setFamily(u"Franklin Gothic Medium")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ytBtn.setFont(font)
        self.ytBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ytBtn.setStyleSheet(u"font: 8pt \"Franklin Gothic Medium\";\n"
"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u"logois/youtube.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ytBtn.setIcon(icon2)
        self.ytBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.ytBtn)

        self.vidBtn = QPushButton(self.frame)
        self.vidBtn.setObjectName(u"vidBtn")
        self.vidBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.vidBtn.setStyleSheet(u"font: 8pt \"Franklin Gothic Medium\";\n"
"color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u"logois/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.vidBtn.setIcon(icon3)
        self.vidBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.vidBtn)

        self.musBtn = QPushButton(self.frame)
        self.musBtn.setObjectName(u"musBtn")
        self.musBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.musBtn.setStyleSheet(u"font: 8pt \"Franklin Gothic Medium\";\n"
"color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u"logois/music.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.musBtn.setIcon(icon4)
        self.musBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.musBtn)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftmenu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.HelpBtn = QPushButton(self.frame_3)
        self.HelpBtn.setObjectName(u"HelpBtn")
        self.HelpBtn.setStyleSheet(u"font: 8pt \"Franklin Gothic Medium\";\n"
"color: rgb(255, 255, 255);")
        icon5 = QIcon()
        icon5.addFile(u"logois/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.HelpBtn.setIcon(icon5)
        self.HelpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.HelpBtn)

        self.InfoBtn = QPushButton(self.frame_3)
        self.InfoBtn.setObjectName(u"InfoBtn")
        self.InfoBtn.setStyleSheet(u"font: 8pt \"Franklin Gothic Medium\";\n"
"color: rgb(255, 255, 255);")
        icon6 = QIcon()
        icon6.addFile(u"logois/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.InfoBtn.setIcon(icon6)
        self.InfoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.InfoBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftmenu)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setToolTipDuration(4)
        self.centerMenuContainer.setAutoFillBackground(False)
        self.centerMenuContainer.setStyleSheet(u"background-color: #2c313c;")
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.centerMenuContainer)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.widget_2.setMinimumSize(QSize(200, 100))
        self.widget_2.setMaximumSize(QSize(16777215, 600))
        self.widget_2.setStyleSheet(u"background-color: #2c313c;")
        self.verticalLayout_7 = QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.widget_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"	background-color: #16191d;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Franklin Gothic Medium")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"font: 10pt \"Franklin Gothic Medium\";\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.closeMenuBtn = QPushButton(self.frame_4)
        self.closeMenuBtn.setObjectName(u"closeMenuBtn")
        icon7 = QIcon()
        icon7.addFile(u"logois/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeMenuBtn.setIcon(icon7)
        self.closeMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.closeMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.centerMenuPages = QCustomStackedWidget(self.widget_2)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        sizePolicy1.setHeightForWidth(self.centerMenuPages.sizePolicy().hasHeightForWidth())
        self.centerMenuPages.setSizePolicy(sizePolicy1)
        self.centerMenuPages.setStyleSheet(u"background-color: #2c313c;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_17 = QVBoxLayout(self.page)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_8 = QWidget(self.page)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Infornation_2 = QLabel(self.widget_8)
        self.Infornation_2.setObjectName(u"Infornation_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Infornation_2.sizePolicy().hasHeightForWidth())
        self.Infornation_2.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setPointSize(13)
        self.Infornation_2.setFont(font2)
        self.Infornation_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Infornation_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.Infornation_2, 0, Qt.AlignTop)

        self.pushButton_3 = QPushButton(self.widget_8)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setIcon(icon6)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.pushButton_3)


        self.verticalLayout_17.addWidget(self.widget_8, 0, Qt.AlignTop)

        self.widget_9 = QWidget(self.page)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy1.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy1)
        self.verticalLayout_18 = QVBoxLayout(self.widget_9)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_13 = QLabel(self.widget_9)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setMinimumSize(QSize(0, 100))
        self.label_13.setMaximumSize(QSize(160, 360))
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_18.addWidget(self.label_13)


        self.verticalLayout_17.addWidget(self.widget_9)

        self.centerMenuPages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget = QWidget(self.page_2)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_8 = QHBoxLayout(self.widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Infornation = QLabel(self.widget)
        self.Infornation.setObjectName(u"Infornation")
        sizePolicy4.setHeightForWidth(self.Infornation.sizePolicy().hasHeightForWidth())
        self.Infornation.setSizePolicy(sizePolicy4)
        self.Infornation.setFont(font2)
        self.Infornation.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Infornation.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.Infornation, 0, Qt.AlignTop)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.pushButton)


        self.verticalLayout_8.addWidget(self.widget, 0, Qt.AlignTop)

        self.widget_4 = QWidget(self.page_2)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy5)
        self.horizontalLayout_9 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.widget_4)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setMinimumSize(QSize(0, 100))
        self.label_10.setMaximumSize(QSize(160, 360))
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_9.addWidget(self.label_10, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.widget_4)

        self.centerMenuPages.addWidget(self.page_2)

        self.verticalLayout_7.addWidget(self.centerMenuPages, 0, Qt.AlignLeft)


        self.verticalLayout_6.addWidget(self.widget_2)

        self.widget_15 = QWidget(self.centerMenuContainer)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_22 = QVBoxLayout(self.widget_15)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_17 = QLabel(self.widget_15)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color:rgb(255, 255, 255);")

        self.verticalLayout_22.addWidget(self.label_17, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_6.addWidget(self.widget_15)


        self.horizontalLayout.addWidget(self.centerMenuContainer, 0, Qt.AlignLeft)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        self.mainBodyContainer.setEnabled(True)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QFrame(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(30, 30))
        self.label_3.setPixmap(QPixmap(u"unnamed.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignLeft)

        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label_4)


        self.horizontalLayout_4.addWidget(self.frame_7, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.minusBtn = QPushButton(self.frame_6)
        self.minusBtn.setObjectName(u"minusBtn")
        icon8 = QIcon()
        icon8.addFile(u"logois/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minusBtn.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.minusBtn)

        self.restoreBtn = QPushButton(self.frame_6)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon9 = QIcon()
        icon9.addFile(u"logois/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.restoreBtn)

        self.exitBtn = QPushButton(self.frame_6)
        self.exitBtn.setObjectName(u"exitBtn")
        icon10 = QIcon()
        icon10.addFile(u"logois/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exitBtn.setIcon(icon10)
        self.exitBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.exitBtn)


        self.horizontalLayout_4.addWidget(self.frame_6, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.headerContainer)

        self.widget_3 = QWidget(self.mainBodyContainer)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy6)
        self.widget_3.setToolTipDuration(0)
        self.verticalLayout_15 = QVBoxLayout(self.widget_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 9, 0, 0)
        self.mainMenu = QWidget(self.widget_3)
        self.mainMenu.setObjectName(u"mainMenu")
        self.verticalLayout_11 = QVBoxLayout(self.mainMenu)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.mainPages = QCustomStackedWidget(self.mainMenu)
        self.mainPages.setObjectName(u"mainPages")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_10 = QVBoxLayout(self.page_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_10 = QWidget(self.page_3)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_19 = QVBoxLayout(self.widget_10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_2 = QLabel(self.widget_10)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(350, 350))
        self.label_2.setPixmap(QPixmap(u"unnamed.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_19.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.label_14 = QLabel(self.widget_10)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_19.addWidget(self.label_14, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_5 = QLabel(self.widget_10)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setFamily(u"Corbel")
        font4.setPointSize(30)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.verticalLayout_19.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.clock = QLabel(self.widget_10)
        self.clock.setObjectName(u"clock")
        self.clock.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_19.addWidget(self.clock, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.widget_10)

        self.mainPages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_12 = QVBoxLayout(self.page_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_5 = QWidget(self.page_4)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_16 = QVBoxLayout(self.widget_5)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, -1, -1, 0)
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setPointSize(35)
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_16.addWidget(self.label_6)

        self.label_11 = QLabel(self.widget_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(400, 40))
        font6 = QFont()
        font6.setPointSize(10)
        self.label_11.setFont(font6)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_16.addWidget(self.label_11)

        self.textEdit = QTextEdit(self.widget_5)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy7)
        self.textEdit.setMinimumSize(QSize(0, 35))
        self.textEdit.setMaximumSize(QSize(16777215, 34))
        font7 = QFont()
        font7.setPointSize(9)
        self.textEdit.setFont(font7)
        self.textEdit.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"background-color:#2c313c;\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-top-left-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"border-bottom-right-radius:5px;")

        self.verticalLayout_16.addWidget(self.textEdit)

        self.pushButton_2 = QPushButton(self.widget_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"color:rgb(255, 255, 255);")
        icon11 = QIcon()
        icon11.addFile(u"logois/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon11)

        self.verticalLayout_16.addWidget(self.pushButton_2, 0, Qt.AlignRight)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_2)


        self.verticalLayout_12.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.page_4)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_10.setSpacing(9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.frame_8 = QFrame(self.widget_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_12.setSpacing(8)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy8)
        self.label_12.setPixmap(QPixmap(u"PngItem_200678.png"))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.label_12)


        self.horizontalLayout_11.addWidget(self.frame_8)


        self.horizontalLayout_10.addWidget(self.widget_7)


        self.verticalLayout_12.addWidget(self.widget_6)

        self.mainPages.addWidget(self.page_4)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_13 = QVBoxLayout(self.page_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_14 = QWidget(self.page_7)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_21 = QVBoxLayout(self.widget_14)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_7 = QLabel(self.widget_14)
        self.label_7.setObjectName(u"label_7")
        font8 = QFont()
        font8.setPointSize(30)
        self.label_7.setFont(font8)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_21.addWidget(self.label_7, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.widget_14)

        self.mainPages.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_14 = QVBoxLayout(self.page_8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_11 = QWidget(self.page_8)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_20 = QVBoxLayout(self.widget_11)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, -1, -1, 0)
        self.label_8 = QLabel(self.widget_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_20.addWidget(self.label_8)

        self.label_15 = QLabel(self.widget_11)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(400, 40))
        self.label_15.setFont(font6)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_20.addWidget(self.label_15)

        self.textEdit_2 = QTextEdit(self.widget_11)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy7.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy7)
        self.textEdit_2.setMinimumSize(QSize(0, 35))
        self.textEdit_2.setMaximumSize(QSize(16777215, 34))
        self.textEdit_2.setFont(font7)
        self.textEdit_2.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"background-color:#2c313c;\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-top-left-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"border-bottom-right-radius:5px;")

        self.verticalLayout_20.addWidget(self.textEdit_2)

        self.pushButton_4 = QPushButton(self.widget_11)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.pushButton_4.setIcon(icon11)

        self.verticalLayout_20.addWidget(self.pushButton_4, 0, Qt.AlignRight)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_3)


        self.verticalLayout_14.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.page_8)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_13.setSpacing(9)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_2 = QSpacerItem(150, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_2)

        self.frame_9 = QFrame(self.widget_13)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_15.setSpacing(8)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_16 = QLabel(self.frame_9)
        self.label_16.setObjectName(u"label_16")
        sizePolicy8.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy8)
        self.label_16.setMaximumSize(QSize(235, 224))
        self.label_16.setPixmap(QPixmap(u"musical-note-portable-network-graphics-computer-icons-clip-art-png-favpng-nzc8dcUd1hT9ETrZQV5C1LbUv.png"))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_16, 0, Qt.AlignRight)


        self.horizontalLayout_14.addWidget(self.frame_9)


        self.horizontalLayout_13.addWidget(self.widget_13)


        self.verticalLayout_14.addWidget(self.widget_12)

        self.mainPages.addWidget(self.page_8)

        self.verticalLayout_11.addWidget(self.mainPages)


        self.verticalLayout_15.addWidget(self.mainMenu)


        self.verticalLayout_9.addWidget(self.widget_3)

        self.foot = QWidget(self.mainBodyContainer)
        self.foot.setObjectName(u"foot")
        self.foot.setMinimumSize(QSize(30, 30))
        self.horizontalLayout_7 = QHBoxLayout(self.foot)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, 0, 0, 0)
        self.label_9 = QLabel(self.foot)
        self.label_9.setObjectName(u"label_9")
        font9 = QFont()
        font9.setBold(True)
        font9.setWeight(75)
        self.label_9.setFont(font9)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.sizeGrip = QFrame(self.foot)
        self.sizeGrip.setObjectName(u"sizeGrip")
        sizePolicy1.setHeightForWidth(self.sizeGrip.sizePolicy().hasHeightForWidth())
        self.sizeGrip.setSizePolicy(sizePolicy1)
        self.sizeGrip.setMinimumSize(QSize(10, 10))
        self.sizeGrip.setMaximumSize(QSize(10, 10))
        self.sizeGrip.setBaseSize(QSize(0, 0))
        self.sizeGrip.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.sizeGrip, 0, Qt.AlignBottom)


        self.verticalLayout_9.addWidget(self.foot)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(1)
        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Open the menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to main page", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.ytBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Download videos from Youtube", None))
#endif // QT_CONFIG(tooltip)
        self.ytBtn.setText(QCoreApplication.translate("MainWindow", u"Youtube Downloader ", None))
#if QT_CONFIG(tooltip)
        self.vidBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Convert your videos to different extensions", None))
#endif // QT_CONFIG(tooltip)
        self.vidBtn.setText(QCoreApplication.translate("MainWindow", u"Converter", None))
#if QT_CONFIG(tooltip)
        self.musBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Download music from Youtube", None))
#endif // QT_CONFIG(tooltip)
        self.musBtn.setText(QCoreApplication.translate("MainWindow", u"Music Downloader", None))
#if QT_CONFIG(tooltip)
        self.HelpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.HelpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(tooltip)
        self.InfoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information about the app", None))
#endif // QT_CONFIG(tooltip)
        self.InfoBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
#if QT_CONFIG(tooltip)
        self.closeMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeMenuBtn.setText("")
        self.Infornation_2.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.pushButton_3.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/>To use this app properly you </p><p>should to copy all the url from</p><p>only youtube.</p><p><br/></p><p>(It's only works from youtube</p><p>links and downloads the file in</p><p>mp4 at the max resolution. If </p><p>you want other format use the </p><p>convertor tool)</p><p><br/></p><p>The Converter tool only works</p><p>with video formats and image</p><p>formats</p></body></html>", None))
        self.Infornation.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.pushButton.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/>Wellcome to my App! This app</p><p>was made 100% in python. It's</p><p>was developed for my Pi project.</p><p>I hope this app help you!</p><p><br/></p><p>(Licensed by GNU)</p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"GitHub Repository Link", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"MyCat Downloader", None))
        self.minusBtn.setText("")
        self.restoreBtn.setText("")
        self.exitBtn.setText("")
        self.label_2.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"_______________________________________________________________________", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"HOME PAGE", None))
        self.clock.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Youtube Downloader", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Insert your Youtube Url!", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Youtube Url</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"Download to mp4 your Video!", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_12.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" vertical-align:super;\">Converter</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Music Downloader", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Insert your Youtube Url! (It will only download a mp3 file)", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Youtube Url</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.pushButton_4.setToolTip(QCoreApplication.translate("MainWindow", u"Download to mp4 your Video!", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_16.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Made By: MiguelDeHaroce", None))
    # retranslateUi

