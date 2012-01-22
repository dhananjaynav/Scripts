import sys
from PyQt4 import QtCore, QtGui
from gui import Ui_Dialog
from helicopter import copter

class mainWindow(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)
    self.device = copter('/dev/ttyUSB0', 115200)
    
    QtCore.QObject.connect(self.ui.verticalSlider, QtCore.SIGNAL("sliderMoved(int)"), self.adjust_rotor)
    
  def adjust_rotor(self, value):
    self.ui.label_2.setText(str(value))
    self.device.adjust_rotor(value)  

def main():
  app = QtGui.QApplication(sys.argv)
  heliapp = mainWindow()
  heliapp.show()
  sys.exit(app.exec_())
  
  
if __name__ == '__main__':
  main()

    