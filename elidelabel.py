import sys
from PyQt5.QtCore import (QSize, QPoint, Qt)
from PyQt5.QtGui import (QPainter, QFont, QTextLayout)
from PyQt5.QtWidgets import (QApplication, QFrame, QWidget, QLabel)

class ElideLabel(QLabel):
	"""A Label widget derived from QLabel and implementing its
       own paintEvent to prevent text overflowing"""
	def __init__(self, parent = None, txt = ""):
		QLabel.__init__(self, txt, parent)

		self.elideMode = 0
		self.lines = 0

	#set whether to elide text or not
	def setElideMode(self, mode):
		if mode != self.elideMode:
			self.elideMode = mode
		self.update()

	def paintEvent(self, event):
		if self.elideMode == 0:#if not set then behave as a normal label
			QLabel.paintEvent(self, event)
		else:
			QFrame.paintEvent(self, event)
			painter = QPainter(self)
			painter.setFont(self.font())

			#gets the spacing between lines
			lineSpacing = self.fontMetrics().lineSpacing()
			y = 0

			textLayout = QTextLayout(self.text(), self.font())
			textLayout.beginLayout()

			#loops  til the end of line
			while True:
				#create a line
				line = textLayout.createLine()

				if line.isValid() != True:
					break
				self.lines += 1
				#set limit of line width
				line.setLineWidth(self.width())
				#calculate position of next line
				nextLineY = y + lineSpacing

				if self.height() >= nextLineY + lineSpacing:
					line.draw(painter, QPoint(0, y))
					y = nextLineY
				else:#regenerate each line so that they do not overflow the width of widget
					lastLine = self.text()[line.textStart(): len(self.text())]
					elidedLastLine = self.fontMetrics().elidedText(lastLine, Qt.ElideRight, self.width())
					painter.drawText(QPoint(0, y + self.fontMetrics().ascent()), elidedLastLine)
					line = textLayout.createLine()
					break
			textLayout.endLayout()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	widget = QWidget()
	widget.setFixedSize(500, 500)
	el = ElideLabel(widget, "Able was I ere I saw Elba")

	el.setGeometry(100, 100, 100, 30)
	el.setElideMode(1)
	widget.show()
	sys.exit(app.exec())
