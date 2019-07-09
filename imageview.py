import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from thumbview import ThumbView
from thumbnail import Thumbnail
from fullimageview import FullImageView

class ImageView(QFrame):
	""" ImageViewer widget derived from QFrame which contains a main 
		image frame to show selected image and small thumbnail frames
	"""
	def __init__(self, parent = None):
		QFrame.__init__(self, parent)

		self.mFullImageView = FullImageView()
		self.mFullImageView.prevRequested.connect(self.OnPrevRequested)
		self.mFullImageView.nextRequested.connect(self.OnNextRequested)

		self.mLayout = QVBoxLayout(self)
		self.mLayout.setSpacing(10)
		self.mLayout.setAlignment(Qt.AlignTop|Qt.AlignHCenter)

		self.mPresenter = Thumbnail(self)
		self.mPresenter.setFixedSize(496, 280)
		self.mPresenter.clicked.connect(self.onFullscreenView)

		self.mThumbs = ThumbView(self)
		self.mThumbs.thumbChanged.connect(self.onItemChanged)

		self.mLayout.addWidget(self.mPresenter, 0, Qt.AlignCenter|Qt.AlignTop)
		self.mLayout.addWidget(self.mThumbs, 0, Qt.AlignCenter|Qt.AlignTop)

	def setPresenterSize(self, w, h):
		self.mPresenter.setFixedSize(w, h)
		self.mThumbs.setFixedSize(w, h)

	# sets spacing between presenter and thumbview
	def setSpacingBetween(self, spacing):
		self.mLayout.setSpacing(spacing)

	# adds a new thumbnail to thumbview
	def addThumbnail(self, pix, uri = "", thumb_type = 0):
		self.mThumbs.addThumbnailByInfo(pix, uri, thumb_type)
		if self.mThumbs.count() == 1:
			self.mThumbs.setActiveThumbByIndex(0)

	# this slot is called when user click on thumbnail of thumbview
	@pyqtSlot(int)
	def onItemChanged(self, id):
		imgPath, uri, thumb_type = self.mThumbs.getThumbInfo(id)
		self.mPresenter.setId(id)
		self.mPresenter.setPixmap(imgPath)
		self.mPresenter.setUri(uri)
		self.mPresenter.setType(thumb_type)

	def OnPrevRequested(self):
		self.mThumbs.prevThumb()

	def OnNextRequested(self):
		self.mThumbs.nextThumb()

	# this slot is called when user click on presenter
	@pyqtSlot()
	def onFullscreenView(self):
		if len(self.mPresenter.getImagePath()) == 0:
			return

		infolist = self.mThumbs.getThumbInfoList()
		self.mFullImageView.setInfoList(infolist)
		self.mFullImageView.setCurrentId(self.mPresenter.getId())
		self.mFullImageView.setResource(self.mPresenter.getImagePath(), self.mPresenter.getUri(), self.mPresenter.getType())
		self.mFullImageView.exec()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QWidget()
	vbox = QVBoxLayout(widget)
	iv = ImageView(widget)
	iv.setPresenterSize(640, 480)
	iv.addThumbnail("./img/bird.png", "https://www.youtube.com/embed/b99UVkWzYTQ?rel=0&amp;showinfo=0", 1)
	iv.addThumbnail("./img/large.png")
	iv.addThumbnail("./img/microsoft_preferred.png")
	iv.addThumbnail("./img/phantom.jpg")
	iv.addThumbnail("./img/spectre.jpg")
	iv.addThumbnail("./img/bird.png")
	iv.addThumbnail("./img/large.png")
	iv.addThumbnail("./img/microsoft_preferred.png")
	iv.addThumbnail("./img/phantom.jpg")
	iv.addThumbnail("./img/spectre.jpg")
	vbox.addWidget(iv)
	widget.show()
	sys.exit(app.exec())