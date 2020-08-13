import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from enum import Enum

class DetailButton(QPushButton):
	""" Button widget derived from QPushButton 
		with styles and used on left side panel
	"""

	# predefined styles to stylize the button
	class BUTTON_STYLE(Enum):
		NORMAL = "#Button{color: white; background-color: rgba(0, 120, 215, 255); border: 1px solid rgba(0, 120, 215, 255); padding: 9px auto 9px auto}"
		HOVER = "#Button{color: white; background-color: rgba(0, 108, 194, 255); border: 1px solid rgba(25, 25, 25, 0.5); padding: 9px auto 9px auto}"
		DOWN = "#Button{color: white; background-color: rgba(0, 84, 151, 255); border: 1px solid rgba(0, 120, 215, 255); padding: 9px auto 9px auto}"

	def __init__(self, text = "", parent = None):
		super().__init__(text, parent)

		self.isUpper = True
		
		self.setText(text)
		self.setObjectName("Button")
		self.setFont(QFont("Roboto", 10, 400))
		self.setStyleSheet(self.BUTTON_STYLE.NORMAL.value)
		self.setFixedHeight(40)

	# button effect
	def enterEvent(self,event):
		self.setStyleSheet(self.BUTTON_STYLE.HOVER.value)

	# button effect
	def leaveEvent(self,event):
		self.setStyleSheet(self.BUTTON_STYLE.NORMAL.value)

	# button effect
	def mousePressEvent(self, event):
		QPushButton.mousePressEvent(self, event)
		self.setStyleSheet(self.BUTTON_STYLE.DOWN.value)

	# button effect
	def mouseReleaseEvent(self, event):
		QPushButton.mouseReleaseEvent(self, event)	
		self.setStyleSheet(self.BUTTON_STYLE.NORMAL.value)	

	def setText(self, text):
		QPushButton.setText(self, text.upper() if self.isUpper else text)
