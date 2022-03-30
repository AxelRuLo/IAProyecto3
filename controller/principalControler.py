
from convolucional import convolucionar, convolucionarGuardado
from view.main_view import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt



class ControllerPrincipal(QMainWindow):
   def __init__(self):
      super(ControllerPrincipal, self).__init__()
      self.ui = Ui_MainWindow()
      self.ui.setupUi(self)
      self.ruta = ""
      self.label_img = QLabel()
      self.ui.buttonAbrir.clicked.connect(self.openFileNameDialog)
      self.ui.buttonPredictNuevo.clicked.connect(self.entrenarNuevo)
      self.ui.buttonpredictGuardado.clicked.connect(self.entrenarGuardado)
      # self.ui.lineRuta.setDisabled(True)
      self.ui.buttonpredictGuardado.setDisabled(True)
      self.ui.buttonPredictNuevo.setDisabled(True)
      
      
      
   def openFileNameDialog(self):
        global text_file
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        "(*jpg);(*jpeg);(*png);(*bmp);(*tiff)"
        fileName, _ = QFileDialog.getOpenFileName(self,"Cargar Imagen", "","JPG(*jpg);;JPEG(*jpeg);;PNG(*png);;BMP(*bmp);;TIFF(*tiff);;ALL FILES(*)", options=options)
        if fileName:
            self.ruta = fileName
            self.ui.lineRuta.setText(fileName)
            self.setImage()
            self.ui.prediccion.setText("")
            self.ui.buttonpredictGuardado.setDisabled(False)
            self.ui.buttonPredictNuevo.setDisabled(False)
            
            
            
   def setImage(self):
      self.ui.Imagen.removeWidget(self.label_img)
      self.label_img = QLabel()
      pixmap=QPixmap(self.ruta)
      pixmap_resized = pixmap.scaled(400, 400, Qt.KeepAspectRatio)
      self.label_img.setPixmap(pixmap_resized)
      self.label_img.adjustSize()
      self.ui.Imagen.addWidget(self.label_img,alignment=Qt.AlignCenter)
      
   def entrenarNuevo(self):
      categoria = convolucionar(self.ruta)
      self.ui.prediccion.setText(categoria)
   
   def entrenarGuardado(self):
      categoria = convolucionarGuardado(self.ruta)
      self.ui.prediccion.setText(categoria)
            