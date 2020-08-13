import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from banner import Banner
from linklist import LinkList
from enum import Enum

# styles for customized vertical scroll bar
class VSCROLL_STYLE(Enum):
	THIN = """
		QScrollBar:vertical {
			border: none;
			background: none;
			width: 5px;
			margin: 0px 0 0px 0;
		}

		QScrollBar::handle:vertical {
			background: lightgray;
            min-height: 5px;
		}

		QScrollBar::handle:vertical:hover {
			background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(215, 215, 225, 225), stop:1 rgba(155, 155, 175, 255));
            min-height: 5px;
		}


		QScrollBar::add-line:vertical {
			background: none;
			height: 10px;
			subcontrol-position: bottom;
			subcontrol-origin: margin;
		}

		QScrollBar::sub-line:vertical {
			background: none;
			height: 10px;
			subcontrol-position: top left;
			subcontrol-origin: margin;
			position: absolute;
		}

		QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {
			width: 5px;
			height: 5px;
			background: none;
			image: url('./img/glass.png');
        }

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
		}"""
	NARROW = """
		QScrollBar:vertical {
			border: none;
			background: none;
			width: 10px;
			margin: 0px 0 0px 0;
		}

		QScrollBar::handle:vertical {
			background: #ddd;
            min-height: 10px;
		}

		QScrollBar::handle:vertical:hover {
			background: #bbb;
            min-height: 10px;
		}

		QScrollBar::add-line:vertical {
			background: none;
			height: 10px;
			subcontrol-position: bottom;
			subcontrol-origin: margin;
		}

		QScrollBar::sub-line:vertical {
			background: none;
			height: 10px;
			subcontrol-position: top left;
			subcontrol-origin: margin;
			position: absolute;
		}

		QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {
			width: 10px;
			height: 10px;
			background: none;
			image: url('./img/glass.png');
        }

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
        }"""

class IntroFrame(QFrame):
	""" Customized widget derived from QFrame which contains placeholder for banner, 
		app intro and app description as well as learn more
		app description widget is capable of both loading plain text and html file
	"""
	def __init__(self, parent = None):
		super().__init__(parent)

		self.mBanner = Banner(self)

		self.mIntroTitle = QLabel(self)
		self.mIntroTitle.setFont(QFont("SegeoUI", 15, QFont.Light))
		self.mIntroTitle.setWordWrap(True)
		self.mIntroTitle.setObjectName("IntroTitle")
		self.mIntroTitle.setText("Put the right products on every shelf at every outlet to satisfy ever-evolving customer demands")

		self.mIntroDesc = QTextBrowser(self)
		self.mIntroDesc.verticalScrollBar().setStyleSheet(VSCROLL_STYLE.NARROW.value)
		self.mIntroDesc.setFrameShape(QFrame.NoFrame)
		self.mIntroDesc.setOpenExternalLinks(True)

		self.mLearnMore = LinkList(self, "Learn more")
		self.mLearnMore.setSpacing(20)
		self.mLearnMore.addLinkByText("Solution Overview", "https://deepcognition.ai/")
		self.mLearnMore.addLinkByText("Sample Data Specifications", "https://deepcognition.ai/")
		self.mLearnMore.addLinkByText("Arca Continental Case Study", "https://deepcognition.ai/")

		self.mLayout = QVBoxLayout(self)
		self.mLayout.setContentsMargins(0, 0, 0, 0)
		self.mLayout.addWidget(self.mBanner)
		self.mLayout.addWidget(self.mIntroTitle)
		self.mLayout.addWidget(self.mIntroDesc)
		self.mLayout.addWidget(self.mLearnMore, 0, Qt.AlignLeft|Qt.AlignTop)

		self.setObjectName("IntroFrame")
		self.setStyleSheet("#IntroFrame{background-color: white;}")
		self.setAutoFillBackground(True)

	def setBannerIcon(self, icon):
		self.mBanner.setBannerIcon(icon)

	# var color should be a string value ends with semicolon(;), ex: rgba(0, 125, 225, 255); or white;
	def setBackgroundColor(self, color):
		self.mBanner.setBackgroundColor(color)

	def setBannerText(self, text):
		self.mBanner.setBannerText(text)

	def setBannerTextFont(self, font):
		self.mBanner.setBannerTextFont(font)

	# var color should be a string value ends with semicolon(;), ex: rgba(0, 125, 225, 255); or white;
	def setBannerTextColor(self, color):
		self.mBanner.setBannerTextColor

	def setBannerLinkText(self, text):
		self.mBanner.setBannerLinkText(text)

	def setBannerLinkFont(self, font):
		self.mBanner.setBannerLinkFont(font)

	# var color should be a string value ends with semicolon(;), ex: rgba(0, 125, 225, 255); or white;
	def setBannerLinkColor(self, color):
		self.mBanner.setBannerLinkColor(color)

	def setIntroTitleText(self, text):
		self.mIntroTitle.setText(text)

	def setIntroTitleFont(self, font):
		self.mIntroTitle.setFont(font)

	def setIntroTitleColor(self, color):
		self.mIntroTitle.setStyleSheet("#IntroTitle{color: " + color + "}")

	# set plain text as description
	def setIntroDescText(self, text):
		self.mIntroDesc.setText(text)

	# set html string rather than plain text
	def setIntroDescHtml(self, html):
		self.mIntroDesc.setHtml(html)

	# load html from a file instead of plain text
	def setIntroDescHtmlFile(self, filePath):
		file = QFile(filePath)
		if file.open(QIODevice.ReadOnly):
			stream = QTextStream(file)
			self.mIntroDesc.setHtml(stream.readAll())
			file.close()
		else:
			fileInfo = QFileInfo(file)
			print("Failed to open: " + fileInfo.absolutePath() + "/" + fileInfo.fileName())

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QWidget()
	vbox = QVBoxLayout(widget)
	intro = IntroFrame(widget)
	intro.setIntroDescHtmlFile("./html/example.html")
	vbox.addWidget(intro)
	widget.show()
	sys.exit(app.exec())