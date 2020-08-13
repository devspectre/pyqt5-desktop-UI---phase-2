import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from thumbnail import Thumbnail
from horizontalscrollarea import HorizontalScrollArea

class ThumbView(HorizontalScrollArea):
	""" Thumbnail viewer widget derived from QFrame which contains several thumbnails horizontally arragned"""

	thumbChanged = pyqtSignal(int)
	def __init__(self, parent = None):
		super().__init__(parent)

		self.mCurrentId = -1
		self.mAssignedId = 0
		self.mThumbList = []

		self.mFrame = QFrame(self)
		self.mFrame.setObjectName("ThumbViewFrame")
		self.mFrame.setStyleSheet("#ThumbViewFrame{border: none; background: transparent;}")

		self.mLayout = QHBoxLayout(self.mFrame)
		self.mLayout.setContentsMargins(0, 0, 0, 0)
		self.mLayout.setSpacing(15)

		# this let the inner frame automatically resize itself to fit the content 
		self.setWidget(self.mFrame)
		self.setWidgetResizable(True)
		self.setObjectName("ThumbView")
		self.setStyleSheet("#ThumbView{border: none; background-color: white;}")

	# return count of thumbnails
	def count(self):
		return len(self.mThumbList)

	# set alignment of widget
	def setAlignment(self, align):
		self.mLayout.setAlignment

	# set active thumbnail and promote it to presenter with its id
	def setActiveThumbById(self, id):
		self.onThumbClicked(id)

	# set active thumbnail and promote it to presenter with its index
	def setActiveThumbByIndex(self, index):
		self.onThumbClicked(self.mThumbList[index].getId())

	# add new thumbnail with an instance
	def addThumbnail(self, thumb):
		self.mThumbList.append(thumb)
		self.mLayout.addWidget(thumb)
		thumb.clicked.connect(self.onThumbClicked)

	# add new thumbnail with details
	def addThumbnailByInfo(self, imgPath, uri = "", thumb_type = 0):
		newThumb = Thumbnail(self, self.mAssignedId)
		self.mAssignedId += 1
		newThumb.setPixmap(imgPath)
		if len(uri) == 0:
			uri = imgPath
		newThumb.setUri(uri)
		newThumb.setType(thumb_type)
		self.addThumbnail(newThumb)

	# remove a thumbnail with its id
	def removeThumbnail(self, id):
		for thumb in self.mThumbList:
			if thumb.getId() == id:
				self.mThumbList.remove(thumb)
				self.mLayout.removeWidget(thumb)
				thumb.setParent(None)

	# remove all thumbnails
	def removeAll(self):
		for thumb in self.mThumbList:
			self.mThumbList.remove(thumb)
			self.mLayout.removeWidget(thumb)
			thumb.setParent(None)		

	# return thumb info whose id is equal to "id"
	def getThumbInfo(self, id):
		for thumb in self.mThumbList:
			if thumb.getId() == id:
				return thumb.getInfo()

	# return uri with thumb's id
	def getUriFromThumb(self, id):
		for thumb in self.mThumbList:
			if thumb.getId() == id:
				return thumb.getUri()

	# return image path with thumb's id
	def getImagePathFromThumb(self, id):
		for thumb in self.mThumbList:
			if thumb.getId() == id:
				return thumb.getImagePath()

	# return type with thumb's id
	def getThumbType(self, id):
		for thumb in self.mThumbList:
			if thumb.getId() == id:
				return thumb.getType()

	# return id of previous thumb of current thumb
	def prevThumbId(self, id):
		for thumb in self.mThumbList:
			if thumb.getId() == id:
				if self.mThumbList.index(thumb) == 0:
					return -1
				return self.mThumbList[self.mThumbList.index(thumb) - 1].getID()
		return -1

	# return id of next thumb of current thumb
	def nextThumbId(self, id):
		for thumb in self.mThumbList:
			if thumb.getId() == id:
				if self.mThumbList.index(thumb) == len(self.mThumbList) - 1:
					return -1
				return self.mThumbList[self.mThumbList.index(thumb) + 1].getID()
		return -1

	# activate previous thumb and promote it
	def prevThumb(self):
		id = self.prevThumbId(self.mCurrentId)
		if id != -1:
			self.onThumbClicked(id)

	# activate next thumb and promote it
	def nextThumb(self):
		id = self.nextThumbId(self.mCurrentId)
		if id != -1:
			self.onThumbClicked(id)

	# return all information of all thumbnails
	def getThumbInfoList(self):
		infolist = []
		for thumb in self.mThumbList:
			info = (thumb.getId(), thumb.getImagePath(), thumb.getUri(), thumb.getType())
			infolist.append(info)

		return infolist

	# this slot is called when a thumb is clicked
	# promote it to presenter and emit a signal
	@pyqtSlot(int)
	def onThumbClicked(self, id):
		self.mCurrentId = id
		for thumb in self.mThumbList:
			if thumb.getId() == id:
				thumb.setActive(True)
			else:
				thumb.setActive(False)
		self.thumbChanged.emit(id)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QWidget()
	vbox = QVBoxLayout(widget)
	tv = ThumbView(widget)
	tv.addThumbnailByInfo("./img/bird.png")
	tv.addThumbnailByInfo("./img/spectre.jpg")
	tv.addThumbnailByInfo("./img/phantom.jpg")
	vbox.addWidget(tv)
	widget.show()
	sys.exit(app.exec())