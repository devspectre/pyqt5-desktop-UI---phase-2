import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from enum import Enum

class ReviewButton(QPushButton):
	""" Button with customized styles"""

	# predefined styles to stylize the button
	class BUTTON_STYLE(Enum):
		NORMAL = "#Button{color: rgba(0, 120, 215, 255); border: 1px solid rgba(0, 120, 215, 255); padding: 9px 25px 9px 25px}"
		HOVER = "#Button{color: white; background: rgba(0, 108, 194, 255); border: 1px solid rgba(0, 120, 215, 255); padding: 9px 25px 9px 25px}"
		DOWN = "#Button{color: rgba(0, 120, 215, 255); background-color: rgb(243, 243, 243); border: 1px solid rgba(0, 120, 215, 255); padding: 9px 25px 9px 25px;}"
		CANCEL_HOVER = "#Button{color: white; background: rgba(194, 58, 0, 255); border: 1px solid rgba(215, 120, 0, 255); padding: 9px 25px 9px 25px}"
		CANCEL_DOWN = "#Button{color: rgba(215, 120, 0, 255); background-color: rgb(243, 243, 243); border: 1px solid rgba(215, 120, 0, 255); padding: 9px 25px 9px 25px;}"

	def __init__(self, parent = None, txt = ""):
		QPushButton.__init__(self, parent)

		self.mGraphicsEffect = QGraphicsDropShadowEffect(self)
		self.mGraphicsEffect.setBlurRadius(5)
		self.mGraphicsEffect.setOffset(0, 0)
		self.mGraphicsEffect.setColor(QColor(0, 125, 215, 255))
		self.mGraphicsEffect.setEnabled(False)

		self.setAutoFillBackground(True)
		self.setText(txt)
		self.setObjectName("Button")
		self.setFont(QFont("Roboto", 12, QFont.Light))
		self.setStyleSheet(self.BUTTON_STYLE.NORMAL.value)
		self.setFixedHeight(40)
		self.setGraphicsEffect(self.mGraphicsEffect)

	# button hover effect
	def enterEvent(self,event):
		txt = self.text().lower()
		if txt == "cancel" or txt == "close" or txt == "exit" or txt == "reject":
			self.setStyleSheet(self.BUTTON_STYLE.CANCEL_HOVER.value)
		else:
			self.setStyleSheet(self.BUTTON_STYLE.HOVER.value)

	# button effect
	def leaveEvent(self,event):
		self.setStyleSheet(self.BUTTON_STYLE.NORMAL.value)
		self.mGraphicsEffect.setEnabled(False)

	# button press effect
	def mousePressEvent(self, event):
		QPushButton.mousePressEvent(self, event)
		txt = self.text().lower()
		if txt == "cancel" or txt == "close" or txt == "exit" or txt == "reject":
			self.mGraphicsEffect.setColor(QColor(215, 125, 0, 255))
			self.setStyleSheet(self.BUTTON_STYLE.CANCEL_DOWN.value)
		else:
			self.mGraphicsEffect.setColor(QColor(0, 125, 215, 255))
			self.setStyleSheet(self.BUTTON_STYLE.DOWN.value)
		self.mGraphicsEffect.setEnabled(True)

	# button effect
	def mouseReleaseEvent(self, event):
		QPushButton.mouseReleaseEvent(self, event)	
		self.setStyleSheet(self.BUTTON_STYLE.NORMAL.value)	
		self.mGraphicsEffect.setEnabled(False)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QWidget()
	widget.setFixedSize(500, 500)
	button = ReviewButton(widget, "Write a review")
	button.setGeometry(190, 235, 150, 40)
	widget.show()
	sys.exit(app.exec())