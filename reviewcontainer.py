import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from reviewheader import ReviewHeader
from reviewcard import ReviewCard
from submitdialog import SubmitDialog
from verticalscrollarea import *

class ReviewContainer(QFrame):
	"""Review Container widget derived from QFrame which contains a header with a text and a button and serveral review cards"""
	def __init__(self, parent = None):
		QFrame.__init__(self, parent)

		self.mCardList = []

		self.mHeader = ReviewHeader(self)
		self.mHeader.writeReviewClicked.connect(self.onWriteReview)

		self.mLayout = QVBoxLayout(self)
		self.mLayout.setAlignment(Qt.AlignTop)
		self.mLayout.setContentsMargins(0, 0, 0, 0)
		self.mLayout.setSpacing(0)

		self.mCardArea = VerticalScrollArea(self)
		self.mCardArea.verticalScrollBar().setStyleSheet(VSCROLL_STYLE.THIN.value)
		self.mCardArea.setFrameShape(QFrame.NoFrame)
		self.mCardArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

		self.mCardFrame = QFrame(self.mCardArea)
		self.mCardFrame.setObjectName("ReviewCardFrame")
		self.mCardFrame.setStyleSheet("#ReviewCardFrame{border: none; background-color: white;}")

		self.mCardLayout = QVBoxLayout(self.mCardFrame)
		self.mCardLayout.setAlignment(Qt.AlignTop)
		self.mCardLayout.setContentsMargins(0, 0, 0, 0)
		self.mCardLayout.setSpacing(0)

		self.mCardArea.setWidget(self.mCardFrame)
		self.mCardArea.setWidgetResizable(True)

		self.mLayout.addWidget(self.mHeader)
		self.mLayout.addWidget(self.mCardArea)

		self.setObjectName("ReviewContainer")
		self.setAutoFillBackground(True)
		self.setStyleSheet("#ReviewContainer{background-color: white;}")

	#this slot is called when the "Write Review" button is clicked
	@pyqtSlot()
	def onWriteReview(self):
		dlg = SubmitDialog()
		if dlg.exec() == QDialog.Accepted:
			rating, title, desc = dlg.getReviewInformation()
			newCard = ReviewCard(self.mCardFrame)
			newCard.setReviewTitle(title)
			newCard.setReviewRating(rating)
			newCard.setReviewComment(desc)
			newCard.setReviewDate(QDate.currentDate())
			self.addCard(newCard)

	#add new card with an instance
	def addCard(self, card):
		self.mCardList.append(card)
		self.mCardLayout.addWidget(card, 0, Qt.AlignTop)
		card.showComment()

	#add new card with detailed info
	def addCardByText(self, rating = 5.0, title = "", desc = ""):
		newCard = ReviewCard(self.mCardFrame)
		newCard.setReviewTitle(title)
		newCard.setReviewRating(rating)
		newCard.setReviewComment(desc)
		self.addCard(newCard)

	#remove all cards
	def removeAll(self):
		for card in self.mCardList:
			self.mCardLayout.removeWidget(card)
			card.setParent(None)

		self.mCardList.clear()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QWidget()

	vbox = QVBoxLayout(widget)
	con = ReviewContainer(widget)
	con.addCardByText(4.3, "Very good", "It was a good experience")
	con.addCardByText(4.3, "Very good", "It was a good experience.Dave from Neal Analytics replied within hours of my email despite the time difference between Singapore and the US. We also managed to set up a call easily and he was accommodating of our schedules and client's timing. Unfortunately, the solution was not really what our spare parts after-sales service - manufacturing customer was looking for")
	vbox.addWidget(con)
	con.removeAll()
	widget.show()
	sys.exit(app.exec())


