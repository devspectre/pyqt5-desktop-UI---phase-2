import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from enum import Enum

class CloseButtonStyle(Enum):
	Normal = "#Close{border: none;}"
	Hover = "#Close{background-color: rgba(200, 50, 34, 255); border: 1px solid lightgrey}"
	Down = "#Close{background-color: rgba(200, 50, 34, 25); border: 1px solid lightgrey}"

class CloseButton(QFrame):
	"""Button widget derived from QLabel for close"""

	clicked = pyqtSignal()
	def __init__(self, parent = None):
		super().__init__(parent)

		self.mStyle = ""
		self.mIsIn = False
		
		self.mPix = QLabel(self)
		self.mPix.setScaledContents(True)
		self.mPix.setFixedSize(15, 15)
		self.mPix.setPixmap(QPixmap("./img/close.png"))
		self.mLayout = QHBoxLayout(self)
		self.mLayout.setContentsMargins(0, 0, 0, 0)
		self.mLayout.setAlignment(Qt.AlignCenter)
		self.mLayout.addWidget(self.mPix, 0, Qt.AlignCenter)

		self.setObjectName("Close")
		self.setStyleSheet(CloseButtonStyle.Normal.value)
		self.setFixedSize(50, 30)

	def enterEvent(self, event):
		QFrame.enterEvent(self, event)
		self.setStyleSheet(CloseButtonStyle.Hover.value)
		self.mIsIn = True

	def leaveEvent(self, event):
		QFrame.leaveEvent(self, event)
		self.setStyleSheet(CloseButtonStyle.Normal.value)
		self.mIsIn = False

	def mousePressEvent(self, event):
		QFrame.mousePressEvent(self, event)
		self.setStyleSheet(CloseButtonStyle.Down.value)

	def mouseReleaseEvent(self, event):
		QFrame.mouseReleaseEvent(self, event)
		self.setStyleSheet(CloseButtonStyle.Normal.value)
		if self.mIsIn:
			self.clicked.emit()
