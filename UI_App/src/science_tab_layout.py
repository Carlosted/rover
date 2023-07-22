# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_ui_files/science_tab_layout.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class Ui_Science(QtWidgets.QWidget):
    def setupUi(self, Science):
        Science.setObjectName("Science")
        Science.resize(500, 747)
        font = QtGui.QFont()
        font.setPointSize(10)
        Science.setFont(font)
        self.gridLayout_10 = QtWidgets.QGridLayout(Science)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.scrollArea = QtWidgets.QScrollArea(Science)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 480, 727))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_22 = QtWidgets.QGridLayout()
        self.gridLayout_22.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.linear_guide_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.linear_guide_label.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.linear_guide_label.setFont(font)
        self.linear_guide_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.linear_guide_label.setTextFormat(QtCore.Qt.AutoText)
        self.linear_guide_label.setAlignment(QtCore.Qt.AlignCenter)
        self.linear_guide_label.setObjectName("linear_guide_label")
        self.gridLayout_22.addWidget(self.linear_guide_label, 4, 0, 1, 3)
        self.auger_speed_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auger_speed_label.sizePolicy().hasHeightForWidth())
        self.auger_speed_label.setSizePolicy(sizePolicy)
        self.auger_speed_label.setMaximumSize(QtCore.QSize(60, 35))
        self.auger_speed_label.setObjectName("auger_speed_label")
        self.gridLayout_22.addWidget(self.auger_speed_label, 9, 0, 1, 1)
        self.linear_guide_fb_lcd = QtWidgets.QLCDNumber(self.scrollAreaWidgetContents)
        self.linear_guide_fb_lcd.setMaximumSize(QtCore.QSize(500, 16777215))
        self.linear_guide_fb_lcd.setObjectName("linear_guide_fb_lcd")
        self.gridLayout_22.addWidget(self.linear_guide_fb_lcd, 6, 2, 1, 1)
        self.carousel_position_inc_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carousel_position_inc_label.sizePolicy().hasHeightForWidth())
        self.carousel_position_inc_label.setSizePolicy(sizePolicy)
        self.carousel_position_inc_label.setMaximumSize(QtCore.QSize(60, 35))
        self.carousel_position_inc_label.setObjectName("carousel_position_inc_label")
        self.gridLayout_22.addWidget(self.carousel_position_inc_label, 2, 0, 1, 1)
        self.linear_guide_speed_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linear_guide_speed_label.sizePolicy().hasHeightForWidth())
        self.linear_guide_speed_label.setSizePolicy(sizePolicy)
        self.linear_guide_speed_label.setMaximumSize(QtCore.QSize(60, 35))
        self.linear_guide_speed_label.setObjectName("linear_guide_speed_label")
        self.gridLayout_22.addWidget(self.linear_guide_speed_label, 6, 0, 1, 1)
        self.linear_guide_slider = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.linear_guide_slider.setMinimum(-100)
        self.linear_guide_slider.setMaximum(100)
        self.linear_guide_slider.setPageStep(1)
        self.linear_guide_slider.setOrientation(QtCore.Qt.Horizontal)
        self.linear_guide_slider.setObjectName("linear_guide_slider")
        self.gridLayout_22.addWidget(self.linear_guide_slider, 6, 1, 1, 1)
        self.carousel_position_inc_spinbox = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.carousel_position_inc_spinbox.setDecimals(0)
        self.carousel_position_inc_spinbox.setMinimum(-360.0)
        self.carousel_position_inc_spinbox.setMaximum(360.0)
        self.carousel_position_inc_spinbox.setSingleStep(1.0)
        self.carousel_position_inc_spinbox.setProperty("value", 0.0)
        self.carousel_position_inc_spinbox.setObjectName("carousel_position_inc_spinbox")
        self.gridLayout_22.addWidget(self.carousel_position_inc_spinbox, 2, 1, 1, 1)
        self.auger_speed_fb_lcd = QtWidgets.QLCDNumber(self.scrollAreaWidgetContents)
        self.auger_speed_fb_lcd.setMaximumSize(QtCore.QSize(500, 16777215))
        self.auger_speed_fb_lcd.setObjectName("auger_speed_fb_lcd")
        self.gridLayout_22.addWidget(self.auger_speed_fb_lcd, 9, 2, 1, 1)
        self.carousel_position_fb_lcd = QtWidgets.QLCDNumber(self.scrollAreaWidgetContents)
        self.carousel_position_fb_lcd.setMaximumSize(QtCore.QSize(500, 16777215))
        self.carousel_position_fb_lcd.setSmallDecimalPoint(False)
        self.carousel_position_fb_lcd.setDigitCount(7)
        self.carousel_position_fb_lcd.setMode(QtWidgets.QLCDNumber.Dec)
        self.carousel_position_fb_lcd.setObjectName("carousel_position_fb_lcd")
        self.gridLayout_22.addWidget(self.carousel_position_fb_lcd, 2, 2, 1, 1)
        self.auger_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auger_label.sizePolicy().hasHeightForWidth())
        self.auger_label.setSizePolicy(sizePolicy)
        self.auger_label.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.auger_label.setFont(font)
        self.auger_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.auger_label.setAlignment(QtCore.Qt.AlignCenter)
        self.auger_label.setObjectName("auger_label")
        self.gridLayout_22.addWidget(self.auger_label, 7, 0, 1, 3)
        self.carousel_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.carousel_label.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.carousel_label.setFont(font)
        self.carousel_label.setAlignment(QtCore.Qt.AlignCenter)
        self.carousel_label.setObjectName("carousel_label")
        self.gridLayout_22.addWidget(self.carousel_label, 0, 0, 1, 3)
        self.auger_speed_slider = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.auger_speed_slider.setMinimum(-100)
        self.auger_speed_slider.setMaximum(100)
        self.auger_speed_slider.setPageStep(1)
        self.auger_speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.auger_speed_slider.setObjectName("auger_speed_slider")
        self.gridLayout_22.addWidget(self.auger_speed_slider, 9, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_22, 2, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.moisture_sampleCnt_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.moisture_sampleCnt_label.setFont(font)
        self.moisture_sampleCnt_label.setObjectName("moisture_sampleCnt_label")
        self.gridLayout_7.addWidget(self.moisture_sampleCnt_label, 5, 1, 1, 1)
        self.send_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.send_button.setFont(font)
        self.send_button.setObjectName("send_button")
        self.gridLayout_7.addWidget(self.send_button, 1, 1, 1, 1)
        self.moisture_sampleCnt_spinbox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.moisture_sampleCnt_spinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.moisture_sampleCnt_spinbox.setMinimum(100)
        self.moisture_sampleCnt_spinbox.setMaximum(10000000)
        self.moisture_sampleCnt_spinbox.setSingleStep(100)
        self.moisture_sampleCnt_spinbox.setProperty("value", 10000)
        self.moisture_sampleCnt_spinbox.setObjectName("moisture_sampleCnt_spinbox")
        self.gridLayout_7.addWidget(self.moisture_sampleCnt_spinbox, 6, 1, 1, 1)
        
        self.moisture_data_fig = plt.figure()
        self.moisture_data_canvas = FigureCanvas(self.moisture_data_fig)
        self.moisture_plotter = self.moisture_data_canvas
        self.moisture_plotter.setMinimumSize(QtCore.QSize(0, 400))
        self.moisture_plotter.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.moisture_plotter.setObjectName("moisture_plotter")
        self.gridLayout_7.addWidget(self.moisture_plotter, 3, 1, 1, 1)
        self.moisture_plotter_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.moisture_plotter_label.setFont(font)
        self.moisture_plotter_label.setAlignment(QtCore.Qt.AlignCenter)
        self.moisture_plotter_label.setObjectName("moisture_plotter_label")
        self.gridLayout_7.addWidget(self.moisture_plotter_label, 2, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_10.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Science)
        QtCore.QMetaObject.connectSlotsByName(Science)

    def retranslateUi(self, Science):
        _translate = QtCore.QCoreApplication.translate
        Science.setWindowTitle(_translate("Science", "Form"))
        self.linear_guide_label.setText(_translate("Science", "Linear Guide Control"))
        self.auger_speed_label.setText(_translate("Science", "Speed"))
        self.carousel_position_inc_label.setText(_translate("Science", "Position"))
        self.linear_guide_speed_label.setText(_translate("Science", "Speed"))
        self.auger_label.setText(_translate("Science", "Auger Control"))
        self.carousel_label.setText(_translate("Science", "Carousel Position"))
        self.moisture_sampleCnt_label.setText(_translate("Science", "Samples to display"))
        self.send_button.setText(_translate("Science", "Send"))
        self.moisture_plotter_label.setText(_translate("Science", "Moisture Sensors Plots"))
