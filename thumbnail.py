import sys, os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from enum import Enum

class Thumbnail(QLabel):
	""" Thumbnail derived from QLabel which shows an image and emit signal when clicked"""

	# styles for thumbnail
	class THUMB_STYLE(Enum):
		Normal = "#Thumbnail{border: 1px solid lightgrey; background-color: grey;}"
		Hover = "#Thumbnail{border: 1px solid rgba(0, 125, 215, 255); background-color: grey;}"
		Down = "#Thumbnail{border: 1px solid black; background-color: grey;}"
		Active = "#Thumbnail{border: 2px solid rgba(0, 125, 215, 255); background-color: grey;}"

	# this signal is emitted when clicked on
	clicked = pyqtSignal(int)
	def __init__(self, parent = None, id = -1, imgPath = ""):
		super().__init__(parent)

		self.mImg = imgPath
		self.mUri = ""# this is only useful when mType is 1
		self.mType = 0# 0: image, 1: video
		self.mID = id;
		self.mIsIn = False
		self.mIsActive = False

		self.setFixedSize(80, 46)
		self.setObjectName("Thumbnail")
		self.setAlignment(Qt.AlignCenter)
		self.setCursor(Qt.PointingHandCursor)
		self.setStyleSheet(self.THUMB_STYLE.Normal.value)
		self.setAutoFillBackground(True)

	# note that param imgPath is just a string rather than QPixmap
	def setPixmap(self, imgPath):
		# this transformation is to keep aspect ratio of the image
		# Parameter Qt.SmoothTransformation is very necessary to show perfect pixmap after scale

		file = QFile(imgPath)
		if not file.exists():
			print("Image file does not exist.")
			return
		pixmap = QPixmap(imgPath).scaledToHeight(self.height(), Qt.SmoothTransformation)
		QLabel.setPixmap(self, pixmap)
		self.mImg = imgPath

	def setId(self, id):
		self.mID = id

	def getId(self):
		return self.mID

	# we use this uri when we want to show a video when the thumbnail is selected
	# for image thumbnails, it is the same as imgPath
	def setUri(self, uri):
		self.mUri = uri

	def getUri(self):
		return self.mUri

	def getImagePath(self):
		return self.mImg

	# set whether to show an image or video when thumbnail is promoted on presenter
	def setType(self, type):
		self.mType = type

	def getType(self):
		return self.mType

	# return information
	def getInfo(self):
		return (self.mImg, self.mUri, self.mType)

	# this method is for when the thumbnail is selected for showing
	def setActive(self, flag):
		self.mIsActive = flag
		if self.mIsActive:
			self.setStyleSheet(self.THUMB_STYLE.Active.value)
		else:
			if self.mIsIn:
				self.setStyleSheet(self.THUMB_STYLE.Hover.value)
			else:
				self.setStyleSheet(self.THUMB_STYLE.Normal.value)

	# effect
	def enterEvent(self, event):	
		if self.mIsActive:
			self.setStyleSheet(self.THUMB_STYLE.Active.value)
		else:
			self.setStyleSheet(self.THUMB_STYLE.Hover.value)
		self.mIsIn = True

	# effect
	def leaveEvent(self, event):
		if self.mIsActive:
			self.setStyleSheet(self.THUMB_STYLE.Active.value)
		else:
			self.setStyleSheet(self.THUMB_STYLE.Normal.value)
		self.mIsIn = False

	# effect
	def mousePressEvent(self, event):
		QLabel.mousePressEvent(self, event)
		self.setStyleSheet(self.THUMB_STYLE.Down.value)

	# show effect and emit the signal with its own id
	def mouseReleaseEvent(self, event):
		QLabel.mouseReleaseEvent(self, event)
		if self.mIsIn:
			self.setStyleSheet(self.THUMB_STYLE.Hover.value)
		else:
			self.setStyleSheet(self.THUMB_STYLE.Normal.value)

		self.clicked.emit(self.mID)

	# use QLabel.pixmap() to get the pixmap of Thumbnail

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QWidget()
	vbox = QVBoxLayout(widget)
	t1 = Thumbnail(widget)

	file  = sys.argv[0]
	dirname = os.path.dirname(file)
	t1.setPixmap(os.path.join(dirname, "/img/spectre.jpg"))
	vbox.addWidget(t1)
	widget.show()
	t1.setActive(True)
	sys.exit(app.exec())