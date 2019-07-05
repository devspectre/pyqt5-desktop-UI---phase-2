import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from link import Link
from elidelabel import ElideLabel

class LinkList(QFrame):
	"""Widget contains list of links, derived from QFrame which contains a caption and list of links"""

	#this signal is emitted when user click one of links
	itemClicked = pyqtSignal(str)
	def __init__(self, parent = None, text = ""):
		QFrame.__init__(self, parent)

		self.mList = []
		self.mListFont = QFont("SegeoUI", 10, QFont.Light)

		self.mListLayout = QVBoxLayout()
		self.mListLayout.setContentsMargins(0, 0, 0, 0)
		self.mListLayout.setSpacing(5)

		self.mLayout = QVBoxLayout(self)
		self.mLayout.setAlignment(Qt.AlignTop|Qt.AlignLeft)
		self.mLayout.setContentsMargins(0, 5, 0, 5)
		self.mLayout.setSpacing(5)

		self.mCaption = ElideLabel(self, text)
		self.mCaption.setObjectName("Caption")
		self.mCaption.setFont(QFont("SegeoUI", 15, QFont.Light))

		self.mLayout.addWidget(self.mCaption)
		self.mLayout.addLayout(self.mListLayout)

		self.setObjectName("LinkList")
		self.setStyleSheet("#LinkList{background-color: white}")
		self.setAutoFillBackground(True)
		self.setContentsMargins(0, 0, 0, 0)

	#add a new link with a given text
	def addLinkByText(self, text, uri = ""):
		newLink = Link(self, text, uri)
		self.addLink(newLink)

	#add a new link with an instance of link
	def addLink(self, newLink):
		newLink.setFont(self.mListFont)
		newLink.clicked.connect(self.onItemClicked)
		self.mList.append(newLink)
		self.mListLayout.addWidget(newLink)

	#remove a link by text
	def removeLink(self, text):
		for link in self.mList:
			if text == link.text():
				self.mListLayout.removeWidget(link)
				self.mList.remove(link)
				link.setParent(None)

	#adjust widget height to fit the total height of elements
	def autoAdjust(self):
		ml, mt, mr, mb = self.mLayout.getContentsMargins()
		mLinkHeight = 0
		if len(self.mList) > 0:
			mLinkHeight = QFontMetrics(self.mListFont).height() * len(self.mList)
		self.setFixedHeight(mt + mb + self.mCaption.height() + mLinkHeight + self.mLayout.spacing() + self.mListLayout.spacing() * (len(self.mList) - 1))

	#set the alignment of widget
	def setAlignment(self, align):
		self.mLayout.setAlignment(align)

	#set caption on top of links
	def setCaption(self, text):
		self.mCaption.setText(text)

	#set the font of caption
	def setCaptionFont(self, font):
		self.mCaption.setFont(font)

	#set font of links
	def setLinkFont(self, font):
		self.mListFont = font
		for each in self.mList:
			each.setFont(self.mListFont)
	#set spacing between caption and links
	def setSpacing(self, spacing):
		self.mLayout.setSpacing(spacing)

	#this slot is called when a link is clicked
	@pyqtSlot(str)
	def onItemClicked(self, txt):
		self.itemClicked.emit(txt)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QWidget()
	widget.setFixedSize(500, 500)
	ll = LinkList(widget, "Products")
	ll.setObjectName("XXX")
	ll.setStyleSheet("#XXX{background-color: white}")
	ll.setAutoFillBackground(True)
	ll.setFont(QFont("Roboto", 10))
	ll.addLinkByText("Web AppsTicTacTicTac", "https://deepcognition.ai/")
	ll.addLinkByText("Analytics", "https://deepcognition.ai/")
	ll.autoAdjust()
	widget.show()
	sys.exit(app.exec())