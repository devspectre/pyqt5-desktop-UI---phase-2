import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class AppLogo(QLabel):
	"""Image widget derived from QLabel to show an app logo"""

	def __init__(self, parent = None):
		QLabel.__init__(self, parent)

		self.img = None
		self.title = "Undefined"
		self.setFixedSize(200, 200)
		self.setScaledContents(True)
		self.setObjectName("AppLogo")
		self.setStyleSheet("#AppLogo{border: 1px solid lightgrey; padding: 5px;}")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QWidget()
	widget.setFixedSize(500, 500)

	logo = AppLogo(widget)
	logo.setPixmap(QPixmap("./img/large.png"))
	logo.setGeometry(100, 100, 300, 300)
	logo.setAutoFillBackground(True)

	widget.show()

	sys.exit(app.exec())
