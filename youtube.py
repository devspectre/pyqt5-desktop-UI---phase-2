from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys, time
from PyQt5.QtCore import Qt,QUrl
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtWebEngineCore
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from closebutton import CloseButton
from movabledialog import MovableDialog

class YoutubeFrame(QFrame):
	""" Youtube frame derived from QFrame to show online videos"""

	def __init__(self, parent = None):
		QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled,True)
		super().__init__(parent)

		self.mSrcUrl = ""
		self.mMaxWidth = 720
		self.mMaxHeight = 480
		self.baseUrl = "local"

		self.mLayout = QVBoxLayout(self)
		self.mLayout.setContentsMargins(0, 0, 0, 0)
		self.mLayout.setSpacing(0)

		self.mWebView = QWebEngineView(self)
		self.mWebView.setContentsMargins(0, 0, 0, 0)
		self.mWebView.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
		self.mWebView.page().fullScreenRequested.connect(lambda request: request.accept())

		self.mLayout.addWidget(self.mWebView)

		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setFixedSize(self.mMaxWidth + 20, self.mMaxHeight + 20)
		self.setObjectName("YTB")
		self.setStyleSheet("#YTB{background-color: white; border: 1px solid lightgrey;}")
		self.setAutoFillBackground(True)
		self.setContentsMargins(0, 0, 0, 0)
		self.show()

	# set url of video
	def setSourceUrl(self, srcUrl):
		self.mSrcUrl = srcUrl
		self.update()		

	# set frame size and adjust content size
	def setFixedSize(self, w, h):
		QFrame.setFixedSize(self, w, h)
		self.mMaxWidth, self.mMaxHeight = w - 20, h - 20
		
	# return widget size
	def getFrameSize(self):
		return (self.mMaxWidth + 20, self.mMaxHeight + 20)

	# update content with given url
	def update(self):
		iframe_String = "<iframe width='" + str(self.mMaxWidth) + "' height='" + str(self.mMaxHeight) + "' src='" + str(self.mSrcUrl) + "' frameborder='0' style='background-color: black; padding: 0' allowfullscreen></iframe>" 
		htmlString = """<html><body style="margin: 0, padding: 0">""" + iframe_String + """</body></html>"""
		self.mWebView.setHtml(htmlString, QUrl(self.baseUrl))

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QWidget()

	dlg = YoutubeFrame(widget)
	url = "https://www.youtube.com/embed/b99UVkWzYTQ?rel=0&amp;showinfo=0"
	dlg.setFixedSize(480, 360)
	dlg.setSourceUrl(url)

	widget.setFixedSize(600, 700)
	widget.show()
	
	sys.exit(app.exec_())