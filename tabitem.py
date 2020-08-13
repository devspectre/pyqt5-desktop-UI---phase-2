import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from enum import Enum

class TabItem(QFrame):
	""" Customized Tab Item derived from QFrame to be embedded into TabWidget"""

	# tab item styles
	class TabItemStyle(Enum):
		Normal = "#TabItem{background-color: white; border: none; border-bottom: 3px solid rgba(255, 255, 255, 255)}"
		Hover = "#TabItem{background-color: white; border: none; border-bottom: 3px solid rgba(0, 125, 215, 255);}"
		Down = "#TabItem{background-color: white; border: none; border-bottom: 3px solid rgba(0, 125, 215, 255);}"
		Active_Normal = "#TabItem{color: rgba(0, 25, 25, 255); background-color: white; border: none; border-bottom: 3px solid rgba(25, 25, 25, 255);}"
		Active_Hover = "#TabItem{color: rgba(0, 25, 25, 255); background-color: white; border: none; border-bottom: 3px solid rgba(0, 125, 215, 255);}"
		Active_Down = "#TabItem{color: rgba(0, 25, 25, 255); background-color: white; border: none; border-bottom: 3px solid rgba(0, 125, 215, 255);}"


	# this signal is emitted when click
	clicked = pyqtSignal(int)
	def __init__(self, parent = None, text = "", id = -1):
		super().__init__(parent)

		self.mId = id
		self.mIsIn = False
		self.mIsActive = False

		self.mText = QLabel(self)
		self.mText.setFont(QFont("SegeoUI", 15, QFont.Normal))
		self.mText.setText(text)
		self.mText.setObjectName("TabText")
		self.mLayout = QHBoxLayout(self)
		self.mLayout.setAlignment(Qt.AlignCenter)
		self.mLayout.setContentsMargins(10, 15, 10, 15)
		self.mLayout.addWidget(self.mText, 0, Qt.AlignTop|Qt.AlignLeft)
		self.mText.setAlignment(Qt.AlignCenter)

		self.mText.setStyleSheet("#TabText{color: rgba(0, 125, 215, 255);}")

		self.setObjectName("TabItem")
		self.setAutoFillBackground(True)
		self.setAttribute(Qt.WA_StyledBackground)
		self.setStyleSheet(self.TabItemStyle.Normal.value)	

	# return idetifier of tab item, id, to its caller
	def getId(self):
		return self.mId

	# set it to be active , when clicked by default
	def setActive(self, flag):
		self.mIsActive = flag
		if self.mIsActive:
			self.mText.setStyleSheet("#TabText{color: black;}")
			self.setStyleSheet(self.TabItemStyle.Active_Normal.value)
		else:
			self.mText.setStyleSheet("#TabText{color: rgba(0, 125, 215, 255);}")
			self.setStyleSheet(self.TabItemStyle.Normal.value)

	# hover effect
	def enterEvent(self, event):
		QFrame.enterEvent(self, event)
		if self.mIsActive:
			self.setStyleSheet(self.TabItemStyle.Active_Hover.value)	
		else:
			self.setStyleSheet(self.TabItemStyle.Hover.value)
		self.mIsIn = True

	# effect
	def leaveEvent(self, event):
		QFrame.leaveEvent(self, event)
		if self.mIsActive:
			self.setStyleSheet(self.TabItemStyle.Active_Normal.value)
		else:
			self.setStyleSheet(self.TabItemStyle.Normal.value)
		self.mIsIn = False

	# effect
	def mousePressEvent(self, event):
		QFrame.mousePressEvent(self, event)
		if self.mIsActive:
			self.setStyleSheet(self.TabItemStyle.Active_Down.value)
		else:
			self.setStyleSheet(self.TabItemStyle.Down.value)
	# effect, emit "clicked" signal
	def mouseReleaseEvent(self, event):
		QFrame.mouseReleaseEvent(self, event)
		if self.mIsActive:
			if self.mIsIn:
				self.setStyleSheet(self.TabItemStyle.Active_Hover.value)	
			else:
				self.setStyleSheet(self.TabItemStyle.Active_Normal.value)
		else:
			if self.mIsIn:
				self.setStyleSheet(self.TabItemStyle.Hover.value)	
			else:
				self.setStyleSheet(self.TabItemStyle.Normal.value)
		if self.mIsIn:
			self.clicked.emit(self.mId)