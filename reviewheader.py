import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from reviewbutton import ReviewButton
from enum import Enum

class ReviewHeader(QFrame):
	""" Customized Header Widget derived from QFrame for Reviews"""

	# this signal is emitted when the button is clicked
	writeReviewClicked = pyqtSignal()
	def __init__(self, parent = None):
		super().__init__(parent)

		self.mCaption = QLabel("User Reviews", self)
		self.mCaption.setFont(QFont("SegoeUI", 12, QFont.Normal))

		self.mBtnReview = ReviewButton(self, "Write a review")
		self.mBtnReview.clicked.connect(self.onReviewButton)

		self.mLayout = QHBoxLayout(self)
		self.mLayout.setContentsMargins(10, 20, 10, 20)
		self.mLayout.addWidget(self.mCaption, 0, Qt.AlignLeft|Qt.AlignVCenter)
		self.mLayout.addWidget(self.mBtnReview, 0, Qt.AlignRight|Qt.AlignVCenter)

		self.setFixedHeight(80)
		self.setObjectName("ReviewFrame")
		self.setStyleSheet("#ReviewFrame{background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:1, stop:0 rgba(225, 225, 225, 255), stop:1 rgba(243, 243, 243, 255));}")

	# this slot is called when the button is called
	@pyqtSlot()
	def onReviewButton(self):
		self.writeReviewClicked.emit()

	# set the caption
	def setCaption(self, caption):
		self.mCaption.setText(caption)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QWidget()
	#widget.setFixedSize(1000, 800)
	header = ReviewHeader(widget)
	hbox = QHBoxLayout(widget)
	hbox.addWidget(header, 0, Qt.AlignCenter)
	widget.show()
	sys.exit(app.exec())
