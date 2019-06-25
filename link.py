import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from elidelabel import ElideLabel

class Link(ElideLabel):
	"""Link widget with text that is simliar to <a> tag in html"""

	#this signal is emitted when user click on the link with its text as a parameter
	clicked = pyqtSignal(str)

	#this signal is emitted when user click on the link with its id as a parameter
	linkActivated = pyqtSignal(int)

	def __init__(self, parent = None, text = "", uri = ""):
		ElideLabel.__init__(self, parent, text)

		self.mId = -1;
		self.mUri = uri
		self.mNormalColor = "rgba(0, 120, 215, 255);"
		self.mHoverColor = "rgba(0, 120, 255, 255);"
		self.mHoverStyle = "text-decoration: underline;"
		self.mEnabled = True

		self.setElideMode(1)
		self.setText(text)
		self.setObjectName("Link")
		self.setStyleSheet("#Link{color: " + self.mNormalColor + "" + "}")
		self.setAlignment(Qt.AlignLeft)
		self.setCursor(Qt.PointingHandCursor)

	#enable/disable mouse effect
	def setEnabled(self, flag):
		self.mEnabled = flag

	def setId(self, id):
		self.mId = id

	def getId(self):
		return self.mId

	def setUri(self, txt):
		self.mUri = txt

	def getUri(self):
		return self.mUri

	def setDefaultColor(self, cl):
		self.mNormalColor = cl
		self.mHoverColor = cl
		self.setStyleSheet("#Link{color: " + self.mNormalColor + "" + "}")

	def setHoverColor(self, cl):
		self.mHoverColor = cl

	def setHoverStyle(self, style):
		self.mHoverStyle = style

	def enterEvent(self, event):
		if not self.mEnabled:
			return
		self.setStyleSheet("#Link{color: " + self.mHoverColor + self.mHoverStyle + "}")

	def leaveEvent(self, event):
		if not self.mEnabled:
			return
		self.setStyleSheet("#Link{color: " + self.mNormalColor + "" + "}")

	def mousePressEvent(self, event):
		if not self.mEnabled:
			return
		QLabel.mousePressEvent(self, event)
		self.setStyleSheet("#Link{color: " + self.mNormalColor + "" + "}")

	def mouseReleaseEvent(self, event):
		if not self.mEnabled:
			return
		QLabel.mouseReleaseEvent(self, event)

		if len(self.mUri) > 0:
			url = QUrl(self.mUri)
			try:
				QDesktopServices.openUrl(url)
			except:
				print("Network error: No connection. Please check your network connection.")
		self.clicked.emit(self.text())
		self.linkActivated.emit(self.mId)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QWidget()
	widget.setFixedSize(500, 500)

	logo = Link(widget, "chicky chicky", "https://deepcognition.ai/")
	logo.setGeometry(100, 100, logo.width(), logo.height())

	widget.show()

	sys.exit(app.exec())
