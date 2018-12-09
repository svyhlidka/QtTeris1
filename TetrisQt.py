# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

#from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import * #QWidget, QApplication, QFrame, QMessageBox, QLabel, QDesktopWidget,  QMainWindow, QDialog
import sys, random
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, pyqtSlot, QRect, QCoreApplication, QMetaObject
from PyQt5.QtGui import *
import winsound         # for sound  
from TetrisCore import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(845, 645)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 551, 503))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QRect(630, 10, 201, 74))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_1 = QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setAlignment(Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_2.addWidget(self.label_1)
        self.line_2 = QFrame(self.verticalLayoutWidget_2)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QRect(630, 420, 208, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_removed = QLabel(self.verticalLayoutWidget)
        font = QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.label_removed.setFont(font)
        self.label_removed.setObjectName("label_removed")
        self.verticalLayout.addWidget(self.label_removed)
        self.label_term_generated = QLabel(self.verticalLayoutWidget)
        font = QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setItalic(False)
        self.label_term_generated.setFont(font)
        self.label_term_generated.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_term_generated.setObjectName("label_term_generated")
        self.verticalLayout.addWidget(self.label_term_generated)
        self.line = QFrame(self.centralwidget)
        self.line.setGeometry(QRect(580, 10, 20, 561))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QRect(630, 169, 201, 141))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.widget = QWidget(self.verticalLayoutWidget_3)
        self.widget.setObjectName("widget")
        self.verticalLayout_3.addWidget(self.widget)

        font = QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 845, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.tboard = Board()
        self.tboard.clearDict()
        self.gridLayout.addWidget(self.tboard,0,0)

        self.slider1 = QSlider(self.centralwidget)
        self.slider1.setGeometry(QRect(10, 560, 361, 22))
        self.slider1.setOrientation(Qt.Horizontal)
        self.slider1.setObjectName("slider1")
        self.slider_label = QLabel(self.centralwidget)
        self.slider_label.setGeometry(QRect(10, 530, 211, 21))

        font = QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.slider_label.setFont(font)
        self.slider_label.setObjectName("slider_label")

        ###########   Slider######################
        self.slider1.setMinimum(1)
        self.slider1.setMaximum(self.tboard.max)
        self.slider1.setValue(int(0.2*self.tboard.max))
        self.slider1.setTickInterval(int(self.tboard.max/10))
        self.slider1.setTickPosition(QSlider.TicksBelow)
        self.slider1.valueChanged.connect(self.v_change)

########################### 

        self.tboard.setFocus(Qt.ActiveWindowFocusReason)

################  signal connect ######################################
        self.tboard.terminoe_signal.connect(on_terminoe_signal)
        self.tboard.line_signal.connect(on_line_signal)
        self.tboard.game_over_signal.connect(on_game_over_signal)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "<font color=\'DarkGreen\'>T E T R I S</font>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#006400;\">Bear\'s Services Co. - 2018</span></p></body></html>"))
        self.label_removed.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0000ff;\">Lines removed: 0</span></p></body></html>"))
        self.label_term_generated.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Total terminoes generated: 0</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Next terminoe:"))
        self.slider_label.setText(_translate("MainWindow", "Change the speed!"))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()   

    def v_change(self):
        new_value = self.slider1.value()
        self.tboard.change_speed(int(self.tboard.max-new_value))
        self.slider_label.setText("Current speed:"+str(int(new_value)))
        self.tboard.setFocus(Qt.ActiveWindowFocusReason)

    def label_remove_change(self, text):
        self.label_removed.setText(text)

    def label_term_generated_change(self, text):
        self.label_term_generated.setText(text)

    def end_of_game(self):
        reply = QMessageBox.question(self, "G A M E   O V E R!",
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            print('slot yes!!!!!!!!!!!!')
            sys.exit(QApplication.exec_())
        else:
            print('no!!!!!!!!!!!!!1')
#            self.start_game_again()
#            return
            event.ignore() 


@pyqtSlot(int)
def on_terminoe_signal(value):
    ui.label_term_generated_change("Total terminoes generated: "+str(value))

@pyqtSlot(int)
def on_line_signal(value):
    ui.label_remove_change("<font color='Blue'>Lines removed:"+str(value)+"</font>")

@pyqtSlot()
def on_game_over_signal():
    print("signal!!!!")
#    ui.end_of_game()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

