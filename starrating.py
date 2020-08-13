import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QToolTip
from PyQt5.QtGui import QPixmap, QImage, QPainter, QCursor
from PyQt5.QtCore import QRectF, Qt, QSize, pyqtSignal

class StarRating(QFrame):
	"""Star rating widget derived from QFrame based on two different images, one for grey stars and one for colored and possessed stars"""

	#this signal is emitted with rating when the widget is clicked
	ratingChangedByClicking = pyqtSignal(float)
	def __init__(self, parent = None):
		super().__init__(parent)

		self.onImage = QPixmap("./img/star_on.png", "PNG")#this should be colored stars at back
		self.offImage = QPixmap("./img/star_off.png", "PNG")#grey stars at the back
		self.rating = 5#current rating
		self.max = 5
		self.clickable = False

		self.setMouseTracking(True)

	#set active blue star image
	def setOnImage(self, onimg):
		self.onImage = onimg
		self.update()

	#set greyed star image
	def setOffImage(self, offpix):
		self.offImage = offimg
		self.update()

	#adjust widget size keeping the aspect ratio
	def adjustWidthByHeight(self, ah):
		pw, ph = self.offImage.width(), self.offImage.height()
		aw = ah * (pw / ph)
		self.setFixedSize(aw, ah)

	#set rating and update view
	def setRating(self, rating):
		if int(rating) != self.rating:
			self.rating = int(rating)
			self.update()
	#return rating
	def getRating(self):
		return str(self.rating)

	#enable/disable setting rating by mouse clicking
	def setClickable(self, flag):
		self.clickable = flag

	#if clickable is set True, then sets rating based on mouse clicked position
	def mousePressEvent(self, event):
		QFrame.mousePressEvent(self, event)
		if self.clickable == False:
			return

		if event.button() == Qt.LeftButton:
			x = event.pos().x()
			rating = int(x  / self.width() * 5.0) + 1
		elif event.button() == Qt.RightButton:
			rating = 5
		self.setRating(rating)
		self.ratingChangedByClicking.emit(rating)

	#this event is overrided to show tooltips
	def mouseMoveEvent(self, event):
		QFrame.mouseMoveEvent(self, event)
		x = event.pos().x()
		rating = int(x  / self.width() * 5.0) + 1
		QToolTip.showText(QCursor.pos(), str(rating), self)

	#actually draws the stars according to the rating value
	def paintEvent(self, event):
		painter = QPainter(self)
		#actually, this does not work at all, it should work to render pixmap transform smoothly
		painter.setRenderHints(QPainter.SmoothPixmapTransform|QPainter.HighQualityAntialiasing)
		
		painter.drawPixmap(QRectF(0, 0, self.width(), self.height()), self.offImage, QRectF(0, 0, self.offImage.width(), self.offImage.height()))
		#real width of enabled stars
		rw = self.width() * self.rating / self.max
		painter.drawPixmap(QRectF(0, 0, rw, self.height()), self.onImage, QRectF(0, 0, self.onImage.width() * self.rating / self.max , self.onImage.height()))
		painter.end()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	widget = QWidget()
	widget.setFixedSize(500, 500)
	starrating = StarRating(widget)
	starrating.adjustWidthByHeight(25)
	starrating.setGeometry(100, 100, starrating.width(), starrating.height())
	starrating.setRating(3.5)
	
	widget.show()
	sys.exit(app.exec())