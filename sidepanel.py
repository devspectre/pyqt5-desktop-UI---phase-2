import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from applogo import AppLogo
from detailbutton import DetailButton
from link import Link
from linklist import LinkList
from starrating import StarRating
from verticalscrollarea import VerticalScrollArea
from verticalscrollarea import VSCROLL_STYLE

class SidePanel(QFrame):
	def __init__(self, parent = None):
		super().__init__(parent)

		self.setObjectName("SidePanel")
		self.setStyleSheet("#SidePanel{background: white;}")
		self.setAutoFillBackground(True)

		self.mAppLogo = AppLogo(self)
		self.mAppLogo.setPixmap(QPixmap("./img/large.png"))

		self.mButtonFrame = QFrame(self)
		self.mButtonLayout = QVBoxLayout(self.mButtonFrame)
		self.mButtonLayout.setContentsMargins(0, 0, 0, 0)

		self.mBtnInstall = DetailButton("Install Now", self.mButtonFrame)
		self.mBtnContact = DetailButton("Contact", self.mButtonFrame)

		self.mButtonLayout.addWidget(self.mBtnInstall, 0, Qt.AlignCenter)
		self.mButtonLayout.addWidget(self.mBtnContact, 0, Qt.AlignCenter)

		self.mContentArea = VerticalScrollArea(self)
		self.mContentArea.setStyle(VSCROLL_STYLE.THIN.value)
		self.mContentArea.setFrameShape(QFrame.NoFrame)
		self.mContentArea.setObjectName("ContentArea")
		self.mContentArea.setStyleSheet("#ContentArea{background-color: white;}")
	
		self.mContentFrame = QFrame(self.mContentArea)
		self.mContentFrame.setObjectName("ContentFrame")
		self.mContentFrame.setStyleSheet("#ContentFrame{background-color: white;}")
		self.mContentLayout = QVBoxLayout(self.mContentFrame)
		self.mContentLayout.setSpacing(15)
		self.mContentLayout.setContentsMargins(0, 0, 0, 0)
		self.mContentLayout.setAlignment(Qt.AlignLeft)

		self.mLinkWhat = Link(self.mContentFrame, "What's Test Drive?", "https://deepcognition.ai/")

		self.mTestDuration = QLabel("Test Drive duration", self.mContentFrame)
		self.mTestDurationValue = QLabel("1 hour", self.mContentFrame)
		self.mTestLayout = QVBoxLayout()
		self.mTestLayout.setContentsMargins(0, 0, 0, 0)
		self.mTestLayout.setSpacing(5)
		self.mTestLayout.addWidget(self.mTestDuration)
		self.mTestLayout.addWidget(self.mTestDurationValue)

		self.mRating = StarRating(self.mContentFrame)
		self.mRating.adjustWidthByHeight(21)

		self.mFeedback = QLabel("(3)", self.mContentFrame)
		self.mFeedback.setFont(QFont("Roboto", 12, QFont.Normal))
		self.mFeedback.setFixedWidth(50)

		self.mRatingLayout = QHBoxLayout()
		self.mRatingLayout.setSpacing(5)
		self.mRatingLayout.setAlignment(Qt.AlignLeft)
		self.mRatingLayout.setContentsMargins(0, 5, 0, 5)
		self.mRatingLayout.addWidget(self.mRating)
		self.mRatingLayout.addWidget(self.mFeedback)

		self.mProducts = LinkList(self.mContentFrame, "Products")
		self.mProducts.addLinkByText("Undefined", "https://deepcognition.ai/")

		self.mPublisher = QLabel("Publisher", self.mContentFrame)
		self.mPublisherValue = QLabel("Undefined", self.mContentFrame)
		self.mPublisherLayout = QVBoxLayout()
		self.mPublisherLayout.setContentsMargins(0, 0, 0, 0)
		self.mPublisherLayout.setSpacing(5)
		self.mPublisherLayout.addWidget(self.mPublisher)
		self.mPublisherLayout.addWidget(self.mPublisherValue)

		self.mAcquire = QLabel("Acquire Using", self.mContentFrame)
		self.mAcquireValue = QLabel("Undefined", self.mContentFrame)
		self.mAcquireLayout = QVBoxLayout()
		self.mAcquireLayout.setContentsMargins(0, 0, 0, 0)
		self.mAcquireLayout.setSpacing(5)
		self.mAcquireLayout.addWidget(self.mAcquire)
		self.mAcquireLayout.addWidget(self.mAcquireValue)

		self.mVersion = QLabel("Version", self.mContentFrame)
		self.mVersionValue = QLabel("1", self.mContentFrame)
		self.mVersionLayout = QVBoxLayout()
		self.mVersionLayout.setContentsMargins(0, 0, 0, 0)
		self.mVersionLayout.setSpacing(5)
		self.mVersionLayout.addWidget(self.mVersion)
		self.mVersionLayout.addWidget(self.mVersionValue)

		self.mCategories = LinkList(self.mContentFrame, "Categories")
		self.mCategories.addLinkByText("Undefined.", "https://deepcognition.ai/")

		self.mIndustries = LinkList(self.mContentFrame, "Industries")
		self.mIndustries.addLinkByText("Undefined", "https://deepcognition.ai/")

		self.mSupport = LinkList(self.mContentFrame, "Support")
		self.mSupport.addLinkByText("Undefined", "https://deepcognition.ai/")

		self.mLegal = LinkList(self.mContentFrame, "Legal")
		self.mLegal.addLinkByText("Undefined", "https://deepcognition.ai/")

		self.mContentLayout.addWidget(self.mLinkWhat)
		self.mContentLayout.addLayout(self.mTestLayout)
		self.mContentLayout.addLayout(self.mRatingLayout)
		self.mContentLayout.addWidget(self.mProducts)
		self.mContentLayout.addLayout(self.mPublisherLayout)
		self.mContentLayout.addLayout(self.mAcquireLayout)
		self.mContentLayout.addLayout(self.mVersionLayout)
		self.mContentLayout.addWidget(self.mCategories)
		self.mContentLayout.addWidget(self.mIndustries)
		self.mContentLayout.addWidget(self.mSupport)
		self.mContentLayout.addWidget(self.mLegal)
		self.mContentLayout.addSpacerItem(QSpacerItem(10, 1000, QSizePolicy.Fixed, QSizePolicy.Expanding))

		self.mContentArea.setWidget(self.mContentFrame)
		self.mContentArea.setWidgetResizable(True)

		self.mLayout = QVBoxLayout(self)
		self.mLayout.setContentsMargins(5, 5, 5, 5)
		self.mLayout.setSpacing(15)
		self.mLayout.setAlignment(Qt.AlignHCenter)

		self.mLayout.addWidget(self.mAppLogo)
		self.mLayout.addWidget(self.mButtonFrame)
		self.mLayout.addWidget(self.mContentArea)

		self.setItemCaptionFont(QFont("Roboto", 10, QFont.Normal))
		self.setItemContentFont(QFont("Roboto", 10, QFont.Light))

	def setProduct(self, text):
		self.mProducts.setText(text)

	def setPublisher(self, text):
		self.mPublisher.setText(text)

	def setAcquireUsing(self, text):
		self.mAcquire.setText(text)

	def setVersion(self, version):
		self.mVersion.setText(version)

	def setRating(self, rating):
		self.mRating.setRating(rating)

	def setFeedback(self, feedback):
		self.mFeedback.setText(str(feedback))

	def setTestDuration(self, duration):
		self.mTestDuration.setText(duration)

	def autoAdjust(self):
		self.mLayout.mProducts.autoAdjust();

	def setItemCaptionFont(self, font):
		self.mLinkWhat.setFont(font)
		self.mTestDuration.setFont(font)
		self.mPublisher.setFont(font)
		self.mAcquire.setFont(font)
		self.mVersion.setFont(font)
		self.mProducts.setCaptionFont(font)
		self.mCategories.setCaptionFont(font)
		self.mIndustries.setCaptionFont(font)
		self.mSupport.setCaptionFont(font)
		self.mLegal.setCaptionFont(font)

	def setItemContentFont(self, font):
		self.mTestDurationValue.setFont(font)
		self.mPublisherValue.setFont(font)
		self.mAcquireValue.setFont(font)
		self.mVersionValue.setFont(font)
		self.mProducts.setLinkFont(font)
		self.mCategories.setLinkFont(font)
		self.mIndustries.setLinkFont(font)
		self.mSupport.setLinkFont(font)
		self.mLegal.setLinkFont(font)

	def adjustFixedWidth(self, aw):
		ml, mt, mr, mb = self.mLayout.getContentsMargins()
		mx = ml + mr
		self.setFixedWidth(aw)
		self.mAppLogo.setFixedSize(aw - mx, aw - mx)
		self.mBtnInstall.setFixedWidth(aw - mx)
		self.mBtnContact.setFixedWidth(aw - mx)
		scroll_width = 0
		scroll_style = self.mContentArea.getStyle()
		if scroll_style == VSCROLL_STYLE.THIN.value:
			scroll_width = 5
		elif scroll_style == VSCROLL_STYLE.NARROW.value:
			scroll_width = 10
		elif scroll_style == VSCROLL_STYLE.NORMAL.value:
			scroll_width = 15

		self.mContentFrame.setMaximumWidth(aw - mx - scroll_width)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QWidget()
	widget.setFixedSize(300, 1000)
	vbox = QVBoxLayout(widget)
	side = SidePanel(widget)
	side.adjustFixedWidth(200)
	vbox.addWidget(side)
	#side.setStyleSheet("#Side{background-color: white}")
	widget.show()
	sys.exit(app.exec())
