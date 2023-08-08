# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:/Shaswata/Robotics/rover/ui_app/qt_ui_files/ui_layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdir)
sys.path.append(currentdir + "/../..")
from drive_layout import Ui_DriveTab
from arm_layout import Ui_Arm
from science_tab_layout import Ui_Science
from power_layout import Ui_Power
from gps_layout import Ui_GPS

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1460,900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.Systemsview = QtWidgets.QTabWidget(self.centralwidget)
        # self.Systemsview.setGeometry(QtCore.QRect(470, 10, 301, 531))
        self.Systemsview.setGeometry(QtCore.QRect(1050, 10, 400, 880))
        self.Systemsview.setObjectName("Systemsview")
        #
        self.Arm = Ui_Arm()
        self.Arm.setupUi(self.Arm)
        self.Systemsview.addTab(self.Arm, "")
        #
        self.Drive = Ui_DriveTab()
        self.Drive.setupUi(self.Drive)
        self.Systemsview.addTab(self.Drive, "")
        #
        self.Science = Ui_Science()
        self.Science.setupUi(self.Science)
        self.Science.setObjectName("Science")
        self.Systemsview.addTab(self.Science, "")
        #
        self.Power = Ui_Power()
        self.Power.setupUi(self.Power)
        self.Power.setObjectName("Power")
        self.Systemsview.addTab(self.Power, "")
        #
        self.GPS = Ui_GPS()
        self.GPS.setupUi(self.GPS)
        self.GPS.setObjectName("GPS")
        self.Systemsview.addTab(self.GPS, "")

        self.camera_selector = QtWidgets.QComboBox(self.centralwidget)
        self.camera_selector.setGeometry(QtCore.QRect(10, 585, 131, 31))
        self.camera_selector.setObjectName("camera_selector")
        self.camera_selector.addItem("")
        self.camera_selector.addItem("")
        self.camera_selector.addItem("")
        self.camera_selector.addItem("")
        self.camera_selector.addItem("")
        self.camera_selector.addItem("")
        # camera showbox
        self.Camera = QtWidgets.QLabel(self.centralwidget)
        self.Camera.setGeometry(QtCore.QRect(10, 10, 1000, 562))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Camera.setFont(font)
        self.Camera.setFrameShape(QtWidgets.QFrame.Box)
        self.Camera.setLineWidth(2)
        self.Camera.setObjectName("Camera")
        self.OverallFeedback = QtWidgets.QWidget(self.centralwidget)
        self.OverallFeedback.setGeometry(QtCore.QRect(10, 360, 311, 191))
        self.OverallFeedback.setObjectName("OverallFeedback")
        self.label = QtWidgets.QLabel(self.centralwidget)
        # self.label.setGeometry(QtCore.QRect(10, 340, 151, 17))
        self.label.setGeometry(QtCore.QRect(320, 585, 200, 17))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.overall_feedback_messagebox = QtWidgets.QTextBrowser(self.centralwidget)
        self.overall_feedback_messagebox.setGeometry(QtCore.QRect(320, 620, 410, 220))
        self.overall_feedback_messagebox.setObjectName("text_browser")
        self.overall_feedback_messagebox.clear()



        self.control_selector = QtWidgets.QComboBox(self.centralwidget)
        self.control_selector.setGeometry(QtCore.QRect(160, 585, 150, 31))
        self.control_selector.setObjectName("control_selector")
        self.control_selector.addItem("")
        self.control_selector.addItem("")
        self.control_selector.addItem("")
        self.control_selector.addItem("")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(5, 5, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Systemsview.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rover UI"))
        self.Systemsview.setTabText(self.Systemsview.indexOf(self.Arm), _translate("MainWindow", "Arm"))
        self.Systemsview.setTabText(self.Systemsview.indexOf(self.Drive), _translate("MainWindow", "Drive "))
        self.Systemsview.setTabText(self.Systemsview.indexOf(self.Science), _translate("MainWindow", "Science"))
        self.Systemsview.setTabText(self.Systemsview.indexOf(self.Power), _translate("MainWindow", "Power"))
        self.Systemsview.setTabText(self.Systemsview.indexOf(self.GPS), _translate("MainWindow", "GPS"))
        self.camera_selector.setCurrentText(_translate("MainWindow", "Cam 1"))
        self.camera_selector.setItemText(0, _translate("MainWindow", "Cam 1"))
        self.camera_selector.setItemText(1, _translate("MainWindow", "Cam 2"))
        self.camera_selector.setItemText(2, _translate("MainWindow", "Cam 3"))
        self.camera_selector.setItemText(3, _translate("MainWindow", "Cam 4"))
        self.camera_selector.setItemText(4, _translate("MainWindow", "Cam 5"))
        self.camera_selector.setItemText(5, _translate("MainWindow", "Cam 6"))
        self.Camera.setText(_translate("MainWindow", "Camera (add pixmap)"))
        self.label.setText(_translate("MainWindow", "Overall Feedback"))
        self.control_selector.setItemText(0, _translate("MainWindow", "Arm"))
        self.control_selector.setItemText(1, _translate("MainWindow", "Drive"))
        self.control_selector.setItemText(2, _translate("MainWindow", "Science"))
        self.control_selector.setItemText(3, _translate("MainWindow", "Power"))
