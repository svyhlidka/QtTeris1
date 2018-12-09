###  GIT
from TetrisCore import *
app = QApplication(sys.argv)
class Dialog(QDialog):

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        mainQGridLayout = QGridLayout()
        mainQGridLayout.setSpacing(10)

        self.section1QVBoxLayout = QVBoxLayout()
        self.section2GridLayout  = QGridLayout()
    #    self.section2GridLayout.setSpacing(2)
        self.section3QHBoxLayout = QVBoxLayout()
        self.section4QHBoxLayout = QHBoxLayout()

        mainQGridLayout.addLayout(self.section1QVBoxLayout, 0, 0)
        mainQGridLayout.addLayout(self.section2GridLayout, 0, 1)
        mainQGridLayout.addLayout(self.section3QHBoxLayout, 1, 0)
        mainQGridLayout.addLayout(self.section4QHBoxLayout, 1, 1)

        self.tboard = Board()
 
        self.tboard.clearDict()

        self.section1QVBoxLayout.addWidget(self.tboard)
        self.lineEdit = QLabel()
        self.lineEdit4 = QLineEdit()

        self.label0 = QLabel()
        self.label0.setFont(QFont('Tahoma', 20))
        self.label0.setText("<font color='DarkGreen'>T E T R I S</font>")
        self.label0.setAlignment(Qt.AlignCenter)
        self.section2GridLayout.addWidget(self.label0,0,0)

        self.label1 = QLabel()
        self.label1.setFont(QFont('Tahoma', 10, italic=True))
        self.label1.setText("<font color='DarkGreen'>Bear's Services Co.</font>")
        self.label1.setAlignment(Qt.AlignCenter)
        self.section2GridLayout.addWidget(self.label1,1,0)

        self.label2 = QLabel()
        self.label2.setFont(QFont('Tahoma', 14))
        self.label2.setText("<font color='Blue'>Lines removed:</font>")
        self.label2.setAlignment(Qt.AlignLeft)
        self.section2GridLayout.addWidget(self.label2,8,0)
        
        self.label3 = QLabel()
        self.label3.setFont(QFont('Tahoma', 12))
        self.label3.setText("<font color='Black'>Total terminoes generated:</font>")
        self.section2GridLayout.addWidget(self.label3,9,0)


###########   Slider######################
        self.slider1 = QSlider(Qt.Horizontal)
        self.slider1.setMinimum(1)
        self.slider1.setMaximum(self.tboard.max)
        self.slider1.setValue(int(0.2*self.tboard.max))
        self.slider1.setTickInterval(int(self.tboard.max/10))
        self.slider1.setTickPosition(QSlider.TicksBelow)
        self.slider1.valueChanged.connect(self.v_change)
########################### 


        self.section3QHBoxLayout.addWidget(self.lineEdit)
        self.section3QHBoxLayout.addWidget(self.slider1)

        self.setLayout(mainQGridLayout)
        self.section4QHBoxLayout.addWidget(self.lineEdit4)
        self.lineEdit.setText("Change the speed!")
    #    self.lineEdit4.setText("Čekám!")
        self.setWindowTitle("Bear's Services Co. presents TETRIS")
        self.setWindowIcon(QIcon('BearPaw.png'))
        self.resize(700, 600)
        self.tboard.setFocus(Qt.ActiveWindowFocusReason)
        self.tboard.terminoe_signal.connect(on_terminoe_signal)
        self.tboard.line_signal.connect(on_line_signal)



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
      #  self.tboard.max  = new_value
        self.tboard.change_speed(int(self.tboard.max-new_value))
        self.lineEdit.setText("Current speed:"+str(int(new_value)))
        self.tboard.setFocus(Qt.ActiveWindowFocusReason)

    def label2_change(self, text):
        dialog.label2.setText(text)

    def label3_change(self, text):
        dialog.label3.setText(text)

@pyqtSlot(int)
def on_terminoe_signal(value):
    dialog.label3_change("Total terminoes generated: "+str(value))

@pyqtSlot(int)
def on_line_signal(value):
    dialog.label2_change("<font color='Blue'>Lines removed:"+str(value)+"</font>")

@pyqtSlot(int)
def on_end_of_game_signal(value):
    print("signal!!!!")
    ui.end_of_game()

if __name__ == '__main__':
    import sys
    dialog = Dialog()
    dialog.show();
    sys.exit(app.exec_()) 

