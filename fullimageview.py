import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from closebutton import CloseButton
from movabledialog import MovableDialog
from youtube import YoutubeFrame

class FullImageView(MovableDialog):
	""" View widget derived from MovableDialog to show full screen image/video
	"""

	# this signal is emitted when user clicks on the left arrow button,
	# or press left key, down key or pagedown
	prevRequested = pyqtSignal()

	# this signal is emitted when user clicks on the right arrow button,
	# or press right key, up key or pageup
	nextRequested = pyqtSignal()

	def __init__(self, parent = None):
		QDialog.__init__(self, parent)

		self.mMaxWidth = 1280
		self.mMaxHeight = 800
		self.mInfoList = []
		self.mCurrentId = -1

		self.mTitle = QLabel(self)
		self.mTitle.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
		self.mBtnClose = CloseButton(self)
		self.mBtnClose.clicked.connect(self.close)

		self.mTitleBarLayout = QHBoxLayout()
		self.mTitleBarLayout.setContentsMargins(0, 0, 0, 0)
		self.mTitleBarLayout.addWidget(self.mTitle, 0 ,Qt.AlignLeft)
		self.mTitleBarLayout.addWidget(self.mBtnClose, 0, Qt.AlignRight)

		self.mImageFrame = QFrame(self)
		self.mImageFrame.setFixedSize(self.mMaxWidth, self.mMaxHeight)
		self.mImageFrame.setObjectName("FullImageFrame")
		self.mImageFrame.setStyleSheet("#FullImageFrame{border: none; background-color: grey}")
		self.mImageFrame.setAutoFillBackground(True)

		self.mImage = QLabel(self.mImageFrame)
		self.mImageLayout = QHBoxLayout(self.mImageFrame)
		self.mImageLayout.setContentsMargins(0, 0, 0, 0)
		self.mImageLayout.addWidget(self.mImage, 0, Qt.AlignCenter)

		self.mYoutube = YoutubeFrame(self)
		self.mYoutube.setFixedSize(self.mMaxWidth, self.mMaxHeight)
		self.mYoutube.hide()

		self.mBtnPrev = QPushButton(self)
		self.mBtnPrev.setFocusPolicy(Qt.NoFocus)
		self.mBtnPrev.setObjectName("ButtonPrev")
		self.mBtnPrev.setStyleSheet("""#ButtonPrev{border-radius: 32px; border: none; background-color: rgba(225, 225, 225, 55); background-image: url(./img/arrow_prev.png); padding: 10px;}
										#ButtonPrev:hover{ background-color: rgba(225, 225, 225, 155);}""")
		self.mBtnPrev.setFixedSize(64, 64)
		self.mBtnPrev.clicked.connect(self.onPrev)

		self.mBtnNext = QPushButton(self)
		self.mBtnNext.setFocusPolicy(Qt.NoFocus)
		self.mBtnNext.setObjectName("ButtonNext")
		self.mBtnNext.setStyleSheet("""#ButtonNext{border-radius: 32px; border: none; background-color: rgba(225, 225, 225, 55); background-image: url(./img/arrow_next.png); padding: 10px;}
										#ButtonNext:hover{ background-color: rgba(225, 225, 225, 155);}""")
		self.mBtnNext.setFixedSize(64, 64)
		self.mBtnNext.clicked.connect(self.onNext)

		self.mPageNumber = QLabel(self)
		self.mPageNumber.setAlignment(Qt.AlignCenter)
		self.mPageNumber.setObjectName("Number")
		self.mPageNumber.setStyleSheet("#Number{color: rgba(215, 215, 215, 215);}")
		self.setPageNumberFont(QFont("SegeoUI", 48))

		self.mLayout = QVBoxLayout(self)
		self.mLayout.setContentsMargins(0, 0, 0, 0)
		self.mLayout.setSpacing(0)

		self.mLayout.addLayout(self.mTitleBarLayout)
		self.mLayout.addWidget(self.mImageFrame)
		self.mLayout.addWidget(self.mYoutube)

		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setMaximumSize(self.mMaxWidth, self.mMaxHeight)
		self.setObjectName("FullView")
		self.setStyleSheet("#FullView{border: 1px solid lightgrey; background-color: white}")
		self.setAutoFillBackground(True)

	# relocates prev button, next button and page number
	def resizeEvent(self, event):
		QDialog.resizeEvent(self, event)
		self.mBtnPrev.setGeometry(20, (self.height() - self.mBtnClose.height() - self.mBtnPrev.height()) / 2, self.mBtnPrev.width(), self.mBtnPrev.height())
		self.mBtnNext.setGeometry(self.width() - self.mBtnNext.width() - 20, (self.height() - self.mBtnClose.height() - self.mBtnNext.height()) / 2, self.mBtnNext.width(), self.mBtnNext.height())
		self.mPageNumber.setGeometry((self.width() - self.mPageNumber.width()) / 2, self.height() - self.mPageNumber.height() - 20, self.mPageNumber.width(), self.mPageNumber.height())

	def closeEvent(self, event):
		self.mYoutube.setSourceUrl("")
		QDialog.closeEvent(self, event)
	
	# sets current id to id and show/hide navigate buttons and updates page number
	def setCurrentId(self, id):
		self.mCurrentId = id
		if self.mCurrentId == self.mInfoList[0][0]:
			self.mBtnPrev.hide()
			self.mBtnNext.show()
		elif self.mCurrentId == self.mInfoList[len(self.mInfoList) - 1][0]:
			self.mBtnPrev.show()
			self.mBtnNext.hide()
		else:
			self.mBtnPrev.show()
			self.mBtnNext.show()

		for info in self.mInfoList:
			if info[0] == self.mCurrentId:
				number = self.mInfoList.index(info) + 1
				self.mPageNumber.setText(str(number))

	# determines whether to show/hide page number widget
	def setPageNumberEnabled(self, flag):
		if flag:
			self.mPageNumber.show()
		else:
			self.mPageNumber.hide()

	# sets font of page number
	def setPageNumberFont(self, font):
		self.mPageNumber.setFont(font)
		self.mPageNumber.setFixedHeight(QFontMetrics(font).height())

	# sets list of informations of portfolios such as id, imagePath, uri, type
	def setInfoList(self, ilist):
		self.mInfoList = ilist

	# sets resource information and updates view
	def setResource(self, imgPath, uri = "", type = 0):
		if type == 0:# uri indicates an image
			self.mYoutube.hide()
			self.mYoutube.setSourceUrl("")
			self.mImageFrame.show()
			if len(uri) == 0:
				uri = imgPath

			# adjust frame size keeping aspect ratio of the image to remove white space
			pixmap = QPixmap(uri)
			pw, ph = pixmap.width(), pixmap.height()
			if pw > self.mMaxWidth or ph > self.mMaxHeight:
				pixmap = pixmap.scaledToHeight(self.mMaxHeight, Qt.SmoothTransformation)
				pw = pixmap.width()
				if pw > self.mMaxWidth:
					pixmap = pixmap.scaledToWidth(self.mMaxWidth, Qt.SmoothTransformation)
				self.setFixedSize(pixmap.width(), pixmap.height() + self.mBtnClose.height())
				self.mImageFrame.setFixedSize(pixmap.width(), pixmap.height())
				self.mImage.setFixedSize(pixmap.width(), pixmap.height())
				self.mImage.setPixmap(pixmap)
			else:
				self.mImageFrame.setFixedSize(self.width(), self.height() - self.mBtnClose.height())
				self.mImage.setFixedSize(pw, ph)
				self.mImage.setPixmap(pixmap.scaledToWidth(pw))
		elif type == 1:# uri indicates a video, in this case, it must be directed to youtubeframe
			w, h = self.mYoutube.getFrameSize()
			# e do not change youtube frame's original size and adjust fullimageviewer's size to fit it
			self.setFixedSize(w, h + self.mBtnClose.height())
			self.mYoutube.setSourceUrl(uri)
			self.mImageFrame.hide()
			self.mYoutube.show()

	# navigates previous image/video
	@pyqtSlot()
	def onPrev(self):
		for info in self.mInfoList:
			if info[0] == self.mCurrentId:
				index = self.mInfoList.index(info)
				if index != 0:
					self.mBtnNext.show()
					prevInfo = self.mInfoList[index - 1]
					self.setCurrentId(prevInfo[0])
					self.setResource(prevInfo[1], prevInfo[2], prevInfo[3])
					return
				else:
					return
	# navigates to next image/video
	@pyqtSlot()
	def onNext(self):
		for info in self.mInfoList:
			if info[0] == self.mCurrentId:
				index = self.mInfoList.index(info)
				if index != len(self.mInfoList) - 1:
					self.mBtnPrev.show()
					nextInfo = self.mInfoList[index + 1]
					self.setCurrentId(nextInfo[0])
					self.setResource(nextInfo[1], nextInfo[2], nextInfo[3])
					return
				else:
					return
	# handles key event
	# instead of clicking on arrow buttons we can navigate with some keys
	def keyPressEvent(self, event):
		pkey = event.key()
		if pkey == Qt.Key_Left or pkey == Qt.Key_Up or pkey == Qt.Key_PageUp:
			self.onPrev()
		elif pkey == Qt.Key_Right or pkey == Qt.Key_Down or pkey == Qt.Key_PageDown:
			self.onNext()
