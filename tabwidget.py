import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from tabitem import TabItem
from enum import Enum

class TabWidget(QFrame):
	""" Customized tab widget derived from QFrame which would contains several TabItem instances"""
	# this signal is emitted when one of tab items is clicked
	tabChanged = pyqtSignal(int)
	def __init__(self, parent = None):
		QFrame.__init__(self, parent)

		self.mAssignedId = 0
		self.mList = []

		self.mLayout = QHBoxLayout(self)
		self.mLayout.setContentsMargins(0, 0, 20, 0)
		self.mLayout.setSpacing(10)
		self.mLayout.setAlignment(Qt.AlignLeft|Qt.AlignBottom)

		self.setObjectName("TabWidget")
		self.setStyleSheet("#TabWidget{background-color: white;}")
		self.setAutoFillBackground(True)

	# add new item with text and id
	def addItemByText(self, text, nid = -1):
		if nid == -1:
			nid = self.mAssignedId 
			self.mAssignedId += 1
		newItem = TabItem(self, text, nid)
		self.addItem(newItem)

	# add item with an instance of tab item
	def addItem(self, item):
		item.clicked.connect(self.itemClicked)
		self.mList.append(item)
		self.mLayout.addWidget(item, 0, Qt.AlignLeft)

	# get item id with its index
	def getIDByIndex(self, index):
		if index <= len(self.mList):
			return self.mList[index].getId()

	# set active item with its index
	def setActiveItemByIndex(self, index):
		if index <= len(self.mList):
			self.itemClicked(self.getIDByIndex(index))

	# set active item with its id
	def setActiveItemByID(self, id):
		if index <= len(self.mList):
			self.itemClicked(id)

	# this slot is called when a tab item is clicked,
	# activate that item and emit a signal
	@pyqtSlot(int)
	def itemClicked(self, id):
		#print("Item(" + str(id) + ") clicked!")
		for item in self.mList:
			if item.getId() != id:
				item.setActive(False)
			else:
				item.setActive(True)
		self.tabChanged.emit(id)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QWidget()
	#widget.setFixedSize(500, 250)
	hbox = QHBoxLayout(widget)
	tab = TabWidget(widget)
	tab.addItemByText("Overview", 1)
	tab.addItemByText("Reviews", 2)
	hbox.addWidget(tab)
	widget.show()
	sys.exit(app.exec())

