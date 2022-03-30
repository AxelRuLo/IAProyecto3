import sys
from controller.principalControler import ControllerPrincipal
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = ControllerPrincipal()
    myApp.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("closing")
        