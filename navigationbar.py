import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from link import Link

class MiddleArrow(QLabel):
	""" Widget Only for {>} without any action"""

	def __init__(self, parent = None):
		QLabel.__init__(self, parent)

		self.setPixmap(QPixmap("./img/arrow.png"))
		self.setScaledContents(True)
		self.setFixedSize(20, 20)
		self.setFont(QFont("SegeoUI", 15))
		self.setAlignment(Qt.AlignCenter)

class NavigationBar(QFrame):
	""" Navigation widget derived from QFrame which contains several link widgets to navigate between pages"""

	# this signal is emitted one of links are clicked
	navigationChanged = pyqtSignal(int)
	def __init__(self, parent = None):
		QFrame.__init__(self, parent)

		self.mAssignedId = -1;
		self.mNavList = []
		self.mArrowList = []
		self.mFont = QFont("SegeoUI", 10, QFont.Light)

		self.mLayout = QHBoxLayout(self)
		self.mLayout.setContentsMargins(10, 5, 10, 5)
		self.mLayout.setAlignment(Qt.AlignLeft)

		self.setObjectName("NavigationBar")
		self.setStyleSheet("#NavigationBar{background-color: white;}")
		self.setAutoFillBackground(True)

	# add a navigation link with text, id and uri
	def pushNavigation(self, text, nid = -1, uri = ""):
		h = QFontMetrics(self.mFont).height()
		# add an arrow behind the previous navigation, before the current navigation link
		if len(self.mNavList) != 0:
			arrow = MiddleArrow(self)
			arrow.setFixedSize(h, h)
			self.mLayout.addWidget(arrow, 0, Qt.AlignLeft)
			self.mArrowList.append(arrow)

		# By default, the last navigation link is disabled
		# So you need to enable previous navigation link when a new one is attached to it
		if len(self.mNavList) > 0:
			self.mNavList[len(self.mNavList) - 1].setEnabled(True)

		if nid == -1:
			self.mAssignedId += 1
			nid = self.mAssignedId

		# add a new link for navigation
		newNav = Link(self, text)
		newNav.setId(nid)
		newNav.setUri(uri)
		newNav.setDefaultColor("black;")
		newNav.setHoverColor("rgba(0, 125, 215, 255);")
		newNav.setElideMode(0)
		newNav.setFont(self.mFont)
		newNav.setAlignment(Qt.AlignBottom)
		newNav.setEnabled(False)
		newNav.linkActivated.connect(self.onNavigationClicked)
		self.mNavList.append(newNav)
		self.mLayout.addWidget(newNav, 0, Qt.AlignLeft)

	# remove all navigation links whose indices are equal or bigger than given index
	def popNavigation(self, index):
		# remove the navigation link first
		if len(self.mNavList) > index:
			for nav in reversed(self.mNavList):
				if self.mNavList.index(nav) == index:
					break
				self.mLayout.removeWidget(nav)
				self.mNavList.remove(nav)
				nav.setParent(None)

		# remove the arrow then
		if len(self.mArrowList) > index - 1:
			for arrow in reversed(self.mArrowList):
				if self.mArrowList.index(arrow) == index - 1:
					break
				self.mLayout.removeWidget(arrow)
				self.mArrowList.remove(arrow)
				arrow.setParent(None)

	# this slot is called when a navigation is clicked
	# it removes all the links behind it
	@pyqtSlot(int)
	def onNavigationClicked(self, id):
		for nav in self.mNavList:
			if nav.getId() == id:
				index = self.mNavList.index(nav)
				self.popNavigation(index)
				self.navigationChanged.emit(nav.getId())

	# set the font of all links inside navigation bar
	def setFont(self, font):
		self.mFont = font
		for nav in self.mNavList:
			nav.setFont(font)

		h = QFontMetrics(font).height()
		for arrow in self.mArrowList:
			arrow.setFixedSize(h, h)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QWidget()
	vbox = QVBoxLayout(widget)
	link = Link(widget)
	nv = NavigationBar(widget)
	nv.setFont(QFont("SegeoUI", 15))
	nv.pushNavigation("Apps")
	nv.pushNavigation("Neal Analytics SKU Assortment Optimization")
	nv.pushNavigation("123")
	vbox.addWidget(nv)
	widget.show()
	sys.exit(app.exec())