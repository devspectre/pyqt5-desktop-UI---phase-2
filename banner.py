import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from link import Link

class Banner(QFrame):
	""" Banner widget derived from QFrame to contain a preferred sign, brief desc, etc
	"""

	def __init__(self, parent = None):
		QFrame.__init__(self, parent)

		self.mIcon = QLabel(self)
		self.mIcon.setScaledContents(True)
		self.mIcon.setObjectName("BannerIcon")
		self.mIcon.setPixmap(QPixmap("./img/microsoft_preferred.png"))
		self.mIcon.setFixedSize(90, 85)
		self.mText = QLabel(self)
		self.mText.setFont(QFont("SegeoUI", 12, QFont.Light))
		self.mText.setText("Microsoft preferred solution")
		self.mText.setObjectName("BannerText")
		self.mText.setStyleSheet("#BannerText{color: white;}")
		self.mLink = Link(self, "Learn more >")
		self.mLink.setDefaultColor("white;")
		self.mLink.setHoverColor("white;")

		self.mTextLayout = QVBoxLayout()
		self.mTextLayout.setContentsMargins(15, 0, 15, 0)
		self.mTextLayout.addWidget(self.mText, 0, Qt.AlignLeft|Qt.AlignBottom)
		self.mTextLayout.addWidget(self.mLink, 0, Qt.AlignLeft|Qt.AlignTop)

		self.mLayout = QHBoxLayout(self)
		self.mLayout.setContentsMargins(0, 0, 0, 0)
		self.mLayout.addWidget(self.mIcon)
		self.mLayout.addLayout(self.mTextLayout)

		self.setObjectName("Banner")
		self.setAutoFillBackground(True)
		self.setStyleSheet("#Banner{background-color: rgba(0, 125, 215, 255);}")

	def setFixedHeight(self, ah):
		QFrame.setFixedHeight(self, ah)
		pixmap = self.mIcon.pixmap()
		pw, ph = pixmap.width(), pixmap.height()
		# resize the logo icon according to the resized widget, keeping its aspect ratio
		self.mIcon.setFixedSize(int(ah * (pw / ph)), ah)

	# set icon of the banner, parameter icon should be a QPixmap 
	def setBannerIcon(self, icon):
		self.mIcon.setPixmap(icon)

	# var color should be a string value ends with semicolon(;), ex: rgba(0, 125, 225, 255); or white;
	def setBackgroundColor(self, color):
		self.setStyleSheet("#Banner{background-color: " + color + "}")

	def setBannerText(self, text):
		self.mText.setText(text)

	def setBannerTextFont(self, font):
		self.mText.setFont(font)

	# var color should be a string value ends with semicolon(;), ex: rgba(0, 125, 225, 255); or white;
	def setBannerTextColor(self, color):
		self.mText.setStyleSheet("#BannerText{color: " + color + "}")

	def setBannerLinkText(self, text):
		self.mLink.setText(text)

	def setBannerLinkFont(self, font):
		self.mLink.setFont(font)

	# var color should be a string value ends with semicolon(;), ex: rgba(0, 125, 225, 255); or white;
	def setBannerLinkColor(self, color):
		self.mLink.setDefaultColor(color)
		self.mLink.setHoverColor(color)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QWidget()
	vbox = QVBoxLayout(widget)
	ba = Banner(widget)
	#ba.setBannerTextColor("green;")
	#ba.setBannerLinkColor("red;")
	#ba.setBannerLinkFont(QFont("Comic Sans MS", 15))
	vbox.addWidget(ba)
	widget.show()
	sys.exit(app.exec())


