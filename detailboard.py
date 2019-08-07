import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from sidepanel import SidePanel
from tabwidget import TabWidget
from reviewcontainer import ReviewContainer
from introframe import IntroFrame
from imageview import ImageView
from navigationbar import NavigationBar

class DetailBoard(QFrame):
	""" Detail page widget derived from QFrame. 
		I hope you to customize it totally.
	"""
	def __init__(self, parent = None):
		QFrame.__init__(self, parent)

		self.mLayout = QVBoxLayout(self)
		self.mLayout.setContentsMargins(0, 0, 0, 0)
		self.mLayout.setSpacing(0)
		self.mHLayout = QHBoxLayout()
		self.mHLayout.setSpacing(20)

		self.mVLayout = QVBoxLayout()
		self.mVLayout.setContentsMargins(5, 5, 5, 5)

		self.mNavigation = NavigationBar(self)
		self.mNavigation.pushNavigation("Apps", 0)
		self.mNavigation.pushNavigation("Neal Analytics SKU Assortment Optimization", 1)
		self.mNavigation.pushNavigation("Neal Analytics", 2)

		self.mSidePanel = SidePanel(self)
		self.mHeaderFrame = QFrame(self)
		self.mAppName = QLabel(self.mHeaderFrame)
		self.mAppName.setFont(QFont("SegeoUI", 20))
		self.mAppName.setText("Neal Analytics SKU Assortment Optimization")
		self.mAppNameBrief = QLabel(self.mHeaderFrame)
		self.mAppNameBrief.setFont(QFont("SegeoUI", 14))
		self.mAppNameBrief.setText("Neal Analytics")
		self.mHeaderLayout = QVBoxLayout(self.mHeaderFrame)
		self.mHeaderLayout.addWidget(self.mAppName, 0, Qt.AlignLeft)
		self.mHeaderLayout.addWidget(self.mAppNameBrief, 0, Qt.AlignLeft)

		self.mTab = TabWidget(self)
		self.mTab.addItemByText("Overview", 0)
		self.mTab.addItemByText("Reviews", 1)
		self.mTab.tabChanged.connect(self.onTabChanged)

		self.mOverviewFrame = QFrame(self)

		self.mIntroFrame = IntroFrame(self.mOverviewFrame)
		self.mIntroFrame.setIntroDescHtmlFile("./html/example.html")

		self.mImageView = ImageView(self.mOverviewFrame)
		self.mImageView.setPresenterSize(640, 480)
		self.mImageView.addThumbnail("./img/phantom.jpg")
		self.mImageView.addThumbnail("./img/spectre.jpg")
		self.mImageView.addThumbnail("./img/deeplearning.png", "https://www.youtube.com/embed/b99UVkWzYTQ?rel=0&amp;showinfo=0", 1)
		self.mImageView.addThumbnail("./img/large.png")
		self.mImageView.addThumbnail("./img/microsoft_preferred.png")
		self.mImageView.addThumbnail("./img/phantom.jpg")
		self.mImageView.addThumbnail("./img/spectre.jpg")

		self.mOverviewLayout = QHBoxLayout(self.mOverviewFrame)
		self.mOverviewLayout.setSpacing(40)
		self.mOverviewLayout.setContentsMargins(0, 0, 0, 0)
		self.mOverviewLayout.addWidget(self.mIntroFrame)
		self.mOverviewLayout.addWidget(self.mImageView)

		self.mReviewFrame = ReviewContainer(self)	

		self.mVLayout.addWidget(self.mHeaderFrame, 0)
		self.mVLayout.addWidget(self.mTab, 0)
		self.mVLayout.addWidget(self.mReviewFrame, 10)
		self.mVLayout.addWidget(self.mOverviewFrame, 10)

		self.mHLayout.addWidget(self.mSidePanel)
		self.mHLayout.addLayout(self.mVLayout)

		self.mLayout.addWidget(self.mNavigation, 0, Qt.AlignLeft)
		self.mLayout.addLayout(self.mHLayout)
		self.mSidePanel.adjustFixedWidth(200)

		self.mTab.setActiveItemByIndex(0)

		self.setObjectName("DetailPage")
		self.setStyleSheet("#DetailPage{background-color: white;}")
		self.setAutoFillBackground(True)
		self.onTabChanged(0)

	def setAppName(self, text):
		self.mAppName.setText(text)

	def setAppNameFont(self, font):
		self.mAppName.setFont(font)

	def setAppNameBrief(self, text):
		self.mAppNameBrief.setText(text)

	def setAppNameBriefFont(self, font):
		self.mAppNameBrief.setFont(font)

	@pyqtSlot(int)
	def onTabChanged(self, id):
		if id == 0:
			self.mReviewFrame.hide()
			self.mOverviewFrame.show()
		elif id == 1:
			self.mReviewFrame.show()
			self.mOverviewFrame.hide()


