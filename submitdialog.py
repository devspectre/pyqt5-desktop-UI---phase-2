import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from reviewbutton import ReviewButton
from starrating import StarRating
from closebutton import CloseButton
from movabledialog import MovableDialog

class SubmitDialog(MovableDialog):

	def __init__(self, parent = None):
		super().__init__(parent)

		self.mIsPressed = False

		self.mStar = StarRating(self)
		self.mStar.setClickable(True)
		self.mStar.adjustWidthByHeight(25)

		self.separator = QFrame(self)
		self.separator.setObjectName("Separator")
		self.separator.setFixedHeight(2)
		self.separator.setFrameShape(QFrame.HLine)
		self.separator.setFrameShadow(QFrame.Sunken)

		self.mTitleEdit = QLineEdit(self)
		self.mTitleEdit.setObjectName("BriefEdit")
		self.mTitleEdit.setStyleSheet("#BriefEdit{border: 1px solid lightgrey;}")
		self.mTitleEdit.setPlaceholderText("Title")
		self.mTitleEdit.setFont(QFont("SegeoUI", 12))
		self.mTitleEdit.textChanged.connect(self.onTitleChanged)

		self.mTitleWarning = QLabel(self)
		self.mTitleWarning.setObjectName("BriefWarning")
		self.mTitleWarning.setStyleSheet("#BriefWarning{border: none; color: red; background: transparent;}")
		self.mTitleWarning.setText("This field is required!")
		self.mTitleWarning.hide()

		self.mComment = QTextEdit(self)
		self.mComment.setPlaceholderText("Comment")
		self.mComment.setObjectName("DescEdit")
		self.mComment.setStyleSheet("#DescEdit{border: 1px solid lightgrey}")
		self.mComment.setFont(QFont("SegeoUI", 10, QFont.Light))

		self.mTextLayout = QVBoxLayout()
		self.mTextLayout.setContentsMargins(0, 0, 0, 0)
		self.mTextLayout.setSpacing(5)
		self.mTextLayout.addWidget(self.mTitleWarning)
		self.mTextLayout.addWidget(self.mTitleEdit)
		self.mTextLayout.addWidget(self.mComment)

		self.mBtnSubmit = ReviewButton(self, "Submit")
		self.mBtnSubmit.setFixedWidth(150)
		self.mBtnSubmit.clicked.connect(self.accept)

		self.mBtnClose = CloseButton(self)
		self.mBtnClose.setFixedWidth(self.mBtnClose.height())
		self.mBtnClose.clicked.connect(self.reject)
		self.mBtnClose.setGeometry(self.width() - self.mBtnClose.width() - 1, 1, self.mBtnClose.width(), self.mBtnClose.height())

		self.mBtnLayout = QHBoxLayout()
		self.mBtnLayout.setContentsMargins(30, 10, 30, 20)
		self.mBtnLayout.addWidget(self.mBtnSubmit)

		self.mLayout = QVBoxLayout(self)
		self.mLayout.setContentsMargins(10, 20, 10, 10)
		self.mLayout.setSpacing(20)
		self.mLayout.addWidget(self.mStar, 0, Qt.AlignCenter)
		self.mLayout.addWidget(self.separator)
		self.mLayout.addLayout(self.mTextLayout)
		self.mLayout.addLayout(self.mBtnLayout)

		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setFixedSize(400, 400)
		self.setObjectName("SubmitDialog")
		self.setStyleSheet("#SubmitDialog{border: 1px solid lightgrey; background-color: white;}")

	#QDialog.accept, check whether everything is okay and close the dialog successfully
	def accept(self):
		if len(self.mTitleEdit.text()) < 1:
			self.mTitleWarning.show()
			self.mTitleEdit.setFocus()
			return
		QDialog.accept(self)

	#hide warning for title if there's any user input
	def onTitleChanged(self):
		if self.mTitleWarning.isVisible():
			self.mTitleWarning.hide()

	#set geometry of close button when resize event is activated
	def resizeEvent(self, event):
		self.mBtnClose.setGeometry(self.width() - self.mBtnClose.width() - 1, 1, self.mBtnClose.width(), self.mBtnClose.height())

	#return the whole information of dialog , rating, title and comment
	def getReviewInformation(self):
		return (self.mStar.getRating(), self.mTitleEdit.text(), self.mComment.toPlainText())
	
if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QWidget()
	dlg = SubmitDialog()
	flist = ["Nice!", "Great ever!", "Flawless performance"]
	dlg.addFeedbackExampleList(flist)
	widget.show()
	if dlg.exec() == QDialog.Accepted:
		rating, brief, desc = dlg.getReviewInformation()
		QMessageBox.information(dlg, "Submit", rating + "\n" + brief + "\n" + desc)
	sys.exit(app.exec())
