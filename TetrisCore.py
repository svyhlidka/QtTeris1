
from PyQt5.QtWidgets import * #QWidget, QApplication, QFrame, QMessageBox, QLabel, QDesktopWidget,  QMainWindow, QDialog
import sys, random
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, pyqtSlot, QRect
from PyQt5.QtGui import *
import winsound         # for sound  

class Terminoe(object):
    
    terminoesCoords = [
             [(0,0)],                           #NoShape 
             [((-2,0),(-1,0),(0,0),(1,0)), ((0,2),(0,1),(0,0),(0,-1)), ((2,0),(1,0),(0,0),(-1,0)), ((0,-2),(0,-1),(0,0),(0,1))],                  # 1 I-Shape
             [((-1,0), (-2,0), (0,0), (0,1)), ((-1,0), (0,-1), (0,-2), (0,0)), ((0,-1), (0,0), (1,0), (2,0)),((1,0), (0,0), (0,1), (0,2))],       # 2 J-Shape
             [((0,-1), (0,0), (-1,0), (-1,1)),((1,0), (0,0), (0,-1), (-1,-1)), ((0,1), (0,0), (1,0), (1,-1)), ((-1,0), (0,0), (0,1), (1,1))],     # 3 Z-Shape
             [((-1,0), (-1,1), (0,0), (0,1)), ((-1,0), (-1,1), (0,0), (0,1)), ((-1,0), (-1,1), (0,0), (0,1)), ((-1,0), (-1,1), (0,0), (0,1))],    # 4 O-Shape
             [((0,0), (1,0), (-1,1), (0,1)),  ((0,0), (0,-1), (1,1), (1,0)), ((0,0), (1,0), (-1,1), (0,1)), ((0,0), (0,1), (-1,-1), (-1,0))],     # 5 S-Shape
             [((0,0), (1,0), (-1,0), (0,1)),  ((0,0), (0,1), (-1,0), (0,-1)), ((0,0), (1,0), (-1,0), (0,-1)), ((0,0), (1,0), (0,-1), (0,1))],     # 6 T-Shape
             [((0,0), (-1,0), (1,-1), (1,0)),  ((0,0), (0,-1), (0,1), (1,1)), ((0,0), (1,0), (-1,0), (-1,1)), ((0,0), (0,1), (0,-1), (-1,-1))]]   # 7 L-Shape

    transform = {
        (-2-2):(2,-2), (-1,-2):(2,-1), (0,-2):(2,0), (1,-2):(2,1), (2,-2):(2,2),
        (-2,-1):(1-2), (-1,-1):(1,-1), (0,-1):(1,0), (1,-1):(1,1), (2,-1):(1,2),
        (-2,0):(0,-2), (-1,0):(0,-1), (0,0):(0,0), (1,0):(0,1), (2,0):(0,2),
        (2,-1):(-1,-2), (-1,1):(-1,-1), (0,1):(-1,0), (1,1):(-1,1), (2,1):(-1,2),
        (-2,2):(2,2), (-1,2):(-2,-1), (0,2):(-2,0), (1,2):(-2,1), (2,2):(-2,2)
        }
                                             
    def __init__(self):
        super().__init__()
        self.terminoesColors = []
        self.terminoesColors.append(Qt.lightGray)
        self.terminoesColors.append(Qt.blue)
        self.terminoesColors.append(Qt.darkRed)
        self.terminoesColors.append(Qt.cyan)
        self.terminoesColors.append(Qt.red)
        self.terminoesColors.append(Qt.green)
        self.terminoesColors.append(Qt.yellow)
        self.terminoesColors.append(Qt.magenta)

        self.currentTermino = 1
        self.status = 0  # 0 = 0, 1 = 90, 2 = 180, 3 = 270  -rotation
        self.currentTerminoMaxX = 0
        self.currentTerminoMaxY = 0

    def setCurrentTermino(self,i,rnd):
        if rnd:
            self.currentTermino = (random.randint(1, 7))
            self.currentColor   = (random.randint(1, 7))
        else:
            self.currentTermino = i
            self.currentColor   = i
        self.setMinMax()

    def setMinMax(self):
        self.currentTerminoMaxX = self.getMaxX()
        self.currentTerminoMaxY = self.getMaxY()
        self.currentTerminoMinX = self.getMinX()
        self.currentTerminoMinY = self.getMinY()

    def getMaxX(self):
        xMax=0
        for item in self.terminoesCoords[self.currentTermino][self.status]:
            if item[0] > xMax: xMax = item[0]
        return abs(xMax)

    def getMaxY(self):
        yMax=0
        for item in self.terminoesCoords[self.currentTermino][self.status]:
            if item[1] > yMax: yMax = item[1]
        return abs(yMax)

    def getMinX(self):
        xMin=100
        for item in self.terminoesCoords[self.currentTermino][self.status]:
            if item[0] < xMin: xMin = item[0]
        return abs(xMin)

    def getMinY(self):
        yMin=100
        for item in self.terminoesCoords[self.currentTermino][self.status]:
            if item[1] < yMin: yMin = item[1]
        return abs(yMin)
       
    def setRotateRight(self):
        if self.status == 3: self.status = 0
        else: self.status += 1
        self.setMinMax()

    def setRotateLeft(self):
        if self.status == 0: self.status = 3
        else: self.status -= 1
        self.setMinMax()

    def newShape(self):
        self.setCurrentTermino(0,True)


class Board(QWidget):

    terminoe_signal = pyqtSignal(int)
    line_signal = pyqtSignal(int)
    Speed = 300
    block_size = 20
    BLOCK_OUTLINE_WIDTH = 2
    board_width  = 15
    board_height = 22
    AlreadyStarted = False
    generation = 0

    def __init__(self):
        super(Board,self).__init__() #(win)
        self.currDict = {}
        self.initUI()
        self.step = 0
        self.max  = 1000
        self.timer = QBasicTimer()
        self.timer.start(self.max, self)
        self.curentShape = 4
        self.currentX = 4
        self.currentY = 1
        self.started  = False
        self.paused   = False
        self.itemDown = False
        self.shape = Terminoe()
        self.counter = 0
        self.totalShapes = 0
        self.totalLines = 0
        self.totalFullLines = 0

    def initUI(self):
        pass
    #    self.setFocusPolicy(Qt.StrongFocus)

    def start_game_again(self):
        self.currDict = {}
        self.step = 0
        self.max  = 1000
        self.timer.start(self.max, self)
        self.curentShape = 4
        self.currentX = 4
        self.currentY = 1
        self.started  = False
        self.paused   = False
        self.itemDown = False
        self.shape = Terminoe()
        self.counter = 0
        self.totalShapes = 0
        self.totalLines = 0
        self.totalFullLines = 0

    def paintEvent(self, event):
        qp = QPainter(self)
        self.update_set(qp)

    def draw_square(self, x, y, w, h, color, qp ) :
        qp.fillRect(self.block_size*x,self.block_size*y, w, h, color)
        qp.setPen(Qt.black)
        qp.drawRect(self.block_size*x,self.block_size*y, w, h)
   
    def clearDict(self):
        self.currDict={}
        for j in range(1,self.board_height+1):
           for i in range(1,self.board_width+1):
               self.currDict.update({(i,j):0})

    def update_set(self , qp):
        if not self.started: 
            self.gameOver()
            self.checkFullLine()
            self.shape.setCurrentTermino(0,True) #(1,False)
            self.setCurrentX(0,True) #(1,False)
            self.setCurrentY(self.shape.getMinY()+1,False)
            self.started = True
        for j in range(1,self.board_height+1):
           for i in range(1,self.board_width+1):
               self.draw_square(i, j, self.block_size, self.block_size, self.shape.terminoesColors[self.currDict[i,j]],qp) 
        for item in self.shape.terminoesCoords[self.shape.currentTermino][self.shape.status]:
            self.draw_square(self.currentX+item[0], self.currentY+item[1], self.block_size, self.block_size, self.shape.terminoesColors[self.shape.currentColor],qp)
        self.lineDown()

###############  testing area
#        term = 3
#        self.currentX =5
#        self.currentY = 5
#        for item in self.shape.terminoesCoords[term][self.counter]:
#            self.draw_square(self.currentX+item[0], self.currentY+item[1], self.block_size, self.block_size, self.shape.terminoesColors[term],qp)
#        self.currentX =5
#        self.currentY = 11
#        for item in self.shape.terminoesCoords[term][1]:
#            titem = transform()
#            self.draw_square(self.currentX+titem[0], self.currentYt+item[1], self.block_size, self.block_size, self.shape.terminoesColors[term],qp)
#        if self.counter == 3: self.counter = 0
#        else: self.counter += 1
#########################################

    def checkRotation(self):
        if self.currentX+self.shape.currentTerminoMaxX > self.board_width:  return False
        if self.currentX-self.shape.currentTerminoMinX < 1:                 return False
        if self.currentY+self.shape.currentTerminoMaxY > self.board_height: return False
        for item in self.shape.terminoesCoords[self.shape.currentTermino][self.shape.status]:
            if self.currDict[self.currentX+item[0],self.currentY+item[1]] > 0: return False
        return True
               
    def checkPos(self, x):
        for item in self.shape.terminoesCoords[self.shape.currentTermino][self.shape.status]:
           if (x != 0):
              if (x ==  1 and self.currentX+item[0]+1 > self.board_width): return False
              if (x == -1 and self.currentX+item[0]-1 < 1): return False
              if (self.currDict[self.currentX+item[0]+x,self.currentY+item[1]] > 0): return False
           else:
               if (self.currentY+self.shape.currentTerminoMaxY >= self.board_height) \
                  or (self.currDict[self.currentX+item[0],self.currentY+item[1]+1] > 0):
                  self.addTerminou()
                  return False              
        return True

    def moveItem(self,left):
        if left: 
            if self.checkPos(-1): self.setCurrentX(self.currentX-1,False)
            return
        else:  
          if self.checkPos(1): self.setCurrentX(self.currentX+1,False)

    def setCurrentX(self,i, rnd): 
        if rnd: 
            xx = random.randint(1,self.board_width)
            if xx+self.shape.getMaxX() > self.board_width: xx = self.board_width-self.shape.getMaxX()
            if xx-self.shape.getMinX() < 1: xx = self.shape.getMinX()+1
            self.currentX = xx
        else: self.currentX = i

    def setCurrentY(self,i,rnd):
        if rnd: self.currentY  = (random.randint(1,self.board_height))
        else: self.currentY = i

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.step += 1
            self.update()
        else:
            super(Board, self).timerEvent(event)

    def lineDown(self):
        if self.checkPos(0): self.setCurrentY(self.currentY+1,False)


    def addTerminou(self):
        for item in self.shape.terminoesCoords[self.shape.currentTermino][self.shape.status]:
            self.currDict.update({(item[0]+self.currentX,item[1]+self.currentY):self.shape.currentColor})
        self.started = False
        self.totalShapes += 1
        self.terminoe_signal.emit(self.totalShapes)

    def goDown(self):
        while self.checkPos(0):
            self.setCurrentY(self.currentY+1,False)


    def pause(self):
        pass

    def gameOver(self):
        for i in range(self.board_width):
           if self.currDict[i+1,1] > 0: 
               self.timer.stop()
               self.started = False
              # self.start_game()
           else: return

    def checkFullLine(self):
        for i in range(1,self.board_width+1):  
            if (self.currDict[i,self.board_height] == 0): return
        self.totalFullLines += 1
        self.line_signal.emit(self.totalFullLines)
        winsound.Beep(4040, 100) # frequency, duration
        self.deleteHistoryLine()

    def deleteHistoryLine(self):
        oldDict = self.currDict
        line = self.board_height
        while line > 1:
            for i in range(1,self.board_width+1,1): self.currDict[i,line]=oldDict[i,line-1]
            line -=1
        for i in range(1,self.board_width+1,1): self.currDict[i,1]=0



    def keyPressEvent(self, event):
        '''processes key press events'''
        
        #if not self.started: # or self.curPiece.shape() == Tetrominoe.NoShape:
        #    super(Board, self).keyPressEvent(event)
        #    return

        key = event.key()
 
        if key == Qt.Key_P:
            self.pause()
            return
            
        if self.paused:
            return
        
        elif key == Qt.Key_Space:
            self.goDown()

        elif key == Qt.Key_Left:
            self.moveItem(True)
            
        elif key == Qt.Key_Right:
            self.moveItem(False)
            
        elif key == Qt.Key_Down:
            self.shape.setRotateRight()
            if not self.checkRotation(): self.shape.setRotateLeft() 

        elif key == Qt.Key_Up:
            self.shape.setRotateLeft()
            if not self.checkRotation(): self.shape.setRotateRight()
                     
        elif key == Qt.Key_D:
         #  self.lineDown()
            pass
            
        else:
            super(Board, self).keyPressEvent(event)

    def change_speed(self, new_value):
        self.timer.start(new_value, self)

    def new_game(self):
        reply = QMessageBox.question(self, 'End of Game?',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:

            sys.exit(app.exec_())
        else:
            event.ignore() 

