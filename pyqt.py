import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from Analyzer import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
 
 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Tweet Analysis    '
        self.left = 500
        self.top = 500
        self.width = 1000
        self.height = 1000
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(70,70)
        button.clicked.connect(self.on_click)
        

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        
        self.show()
        
    def on_click(self):
        self.textboxValue = self.textbox.text()
        print(self.textboxValue)
        #print('PyQt5 button click')
        sa.DownloadData(self.textboxValue)
        self.show()
        plt.show()
        #PlotCanvas1.plot(self)

# class PlotCanvas1(FigureCanvas):
 
#     def __init__(self, parent=None, width=5, height=4, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
 
#         FigureCanvas.__init__(self, fig)
#         self.setParent(parent)
 
#         FigureCanvas.setSizePolicy(self,
#                 QSizePolicy.Expanding,
#                 QSizePolicy.Expanding)
#         FigureCanvas.updateGeometry(self)
    
#     def plot(self):
#         sa.plotPieChart(sa.positive,sa.wpositive, sa.spositive, sa.negative, sa.wnegative, sa.snegative, sa.neutral, sa.searchTerm, sa.NoOfTerms)
 
#self.plotPieChart(positive, wpositive, spositive, negative, wnegative, snegative, neutral, searchTerm, NoOfTerms)

    # def plot(self):
    #     #self.plt.show()
    #     label = QLabel(self)
    #     pixmap = QPixmap('img.png')
    #     label.setPixmap(pixmap)
    #     self.resize(pixmap.width(),pixmap.height())
    #     ax.set_title('PyQt Matplotlib Example')
    #     #self.show()
    #     self.draw()



 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
sys.exit(app.exec_())
