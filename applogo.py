import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class AppLogo(QLabel):
	""" Image widget derived from QLabel to show an app logo"""

	def __init__(self, parent = None):
		super().__init__(parent)

		self.img = None
		self.title = "Undefined"
		self.setFixedSize(200, 200)
		self.setScaledContents(True)
		self.setObjectName("AppLogo")
		self.setStyleSheet("#AppLogo{border: 1px solid lightgrey; padding: 5px;}")

