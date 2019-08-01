import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from starrating import StarRating
from link import Link
from elidelabel import ElideLabel
from autotextview import AutoTextView

class ReviewCard(QFrame):
	""" Review Card widget derived from QFrame which contains star rating, reviewed date, reviewer, title, comment and two text buttons"""
	def __init__(self, parent = None):
		QFrame.__init__(self, parent)

		self.mShowAll = False

		self.mRatingFrame = QFrame(self)
		self.mRatingFrame.setFixedWidth(200)

		self.mRating = StarRating(self.mRatingFrame)
		self.mRating.adjustWidthByHeight(21)
		self.mRatedDate = QLabel("Sat, Jun 17, 2017", self.mRatingFrame)
		self.mRatedDate.setFont(QFont("SegeoUI", 12, QFont.Light))
		self.mRater = QLabel("Anonymous", self.mRatingFrame)
		self.mRater.setFont(QFont("SegeoUI", 12, QFont.Light))

		self.mRatingLayout = QVBoxLayout(self.mRatingFrame)
		self.mRatingLayout.setContentsMargins(10, 5, 10, 5)
		self.mRatingLayout.setAlignment(Qt.AlignTop)
		self.mRatingLayout.setSpacing(15)
		self.mRatingLayout.addWidget(self.mRating, 0, Qt.AlignLeft|Qt.AlignTop)
		self.mRatingLayout.addWidget(self.mRatedDate, 0, Qt.AlignLeft|Qt.AlignTop)
		self.mRatingLayout.addWidget(self.mRater, 0, Qt.AlignLeft|Qt.AlignTop)

		self.mTxtFrame = QFrame(self)

		self.mTitle = ElideLabel(self.mTxtFrame, "Undefined")
		self.mTitle.setContentsMargins(0, 0, 0, 0)
		self.mTitle.setFont(QFont("SegeoUI", 14, QFont.Light))

		self.mComment = AutoTextView(self.mTxtFrame)
		self.mComment.setFont(QFont("SegeoUI", 12, QFont.Light))
		self.mComment.lessThanLimit.connect(self.onLessThanLimit)
		self.mComment.moreThanLimit.connect(self.onMoreThanLimit)
		self.mComment.setAutoFillBackground(True)

		self.mBtnMore = Link(self.mTxtFrame, "Read More")
		self.mBtnMore.setHoverColor("rgba(25, 55, 155, 255);")
		self.mBtnMore.setHoverStyle("")
		self.mBtnMore.setFont(QFont("SegeoUI", 12, QFont.Light))
		self.mBtnMore.setContentsMargins(0, 0, 0, 0)
		self.mBtnMore.clicked.connect(self.onReadMore)

		self.mBtnReport = Link(self.mTxtFrame, "Report this review")
		self.mBtnReport.setDefaultColor("rgba(0, 0, 0, 255);")
		self.mBtnReport.clicked.connect(self.onReport)

		self.mCaptionLayout = QHBoxLayout()
		self.mCaptionLayout.setContentsMargins(0, 0, 0, 0)
		self.mCaptionLayout.setAlignment(Qt.AlignLeft|Qt.AlignTop)
		self.mCaptionLayout.addWidget(self.mTitle)

		self.mTxtLayout = QVBoxLayout(self.mTxtFrame)
		self.mTxtLayout.setAlignment(Qt.AlignLeft|Qt.AlignTop)
		self.mTxtLayout.setContentsMargins(5, 5, 5, 5)
		self.mTxtLayout.setSpacing(5)
		self.mTxtLayout.addLayout(self.mCaptionLayout, 0)
		self.mTxtLayout.addWidget(self.mComment)
		self.mTxtLayout.addWidget(self.mBtnMore, 0, Qt.AlignLeft|Qt.AlignTop)
		self.mTxtLayout.addWidget(self.mBtnReport, 0, Qt.AlignLeft|Qt.AlignTop)

		self.mLayout = QHBoxLayout(self)
		self.mLayout.setAlignment(Qt.AlignLeft|Qt.AlignTop)
		self.mLayout.addWidget(self.mRatingFrame)
		self.mLayout.addWidget(self.mTxtFrame)

		self.setObjectName("ReviewCard")

	@pyqtSlot()
	def onLessThanLimit(self):
		self.mBtnMore.hide()

	@pyqtSlot()
	def onMoreThanLimit(self):
		self.mBtnMore.show()

	def setReviewRating(self, rating):
		self.mRating.setRating(float(rating))

	# set rated text with formatted QDateTime variable
	def setReviewDate(self, date):
		self.mRatedDate.setText(date.toString("ddd, MMM d, yyyy"))
	# set rated text with pure string
	def setReviewDateString(self, str):
		self.mRatedDate.setText(str)

	def setReviewTitle(self, str):
		self.mTitle.setText(str)

	def setReviewComment(self, str):
		self.mComment.setText(str)

	def showComment(self, showAll = False):
		if showAll:
			self.mComment.showAll()
			self.mBtnMore.setText("Read Less")
		else:
			self.mComment.showLess()
			self.mBtnMore.setText("Read More")

	def onReadMore(self):
		self.mShowAll = not self.mShowAll
		self.showComment(self.mShowAll)

	def onReport(self):
		QMessageBox.information(self, "", "User reported the review")


if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QWidget()
	card = ReviewCard(widget)
	card.setObjectName("Side")
	card.setStyleSheet("#Side{background-color: white}")
	card.setReviewDate(QDate.fromString("2017-09-23", "yyyy-MM-d"))
	desc_str = "Dave from Neal Analytics replied within hours of my email despite the time difference between Singapore and the US. We also managed to set up a call easily and he was accommodating of our schedules and client's timing.Unfortunately, the solution was not really what our spare parts / after-sales service - manufacturing customer was looking for"
	card.setReviewComment(desc_str)
	hbox = QHBoxLayout(widget)
	hbox.addWidget(card)
	widget.show()
	sys.exit(app.exec())