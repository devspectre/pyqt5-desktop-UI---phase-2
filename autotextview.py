import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class AutoTextView(QPlainTextEdit):
	""" TextView widget derived from QPlainTextEdit 
		which automatically adjust its height due to the width
	"""

	# this signal is emitted when current text
	# has less lines than default line count.
	lessThanLimit = pyqtSignal()

	# this signal is emitted when current text 
	# has more lines than default line count.
	moreThanLimit = pyqtSignal()

	def __init__(self, parent = None):
		super().__init__(parent)
		
		self.mDefaultLineCount = 3
		self.mShowAll = False
		
		self.setObjectName("AutoTextView")
		self.setStyleSheet("#AutoTextView{border: none; margin: 0; background-color: white;}")
		self.setAutoFillBackground(True)
		self.setTextInteractionFlags(Qt.TextEditable)
		self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.verticalScrollBar().setDisabled(True)
		self.setFont(QFont("SegeoUI", 10, QFont.Light))
		self.setContentsMargins(0, 0, 0, 0)
		self.setCursor(QCursor(Qt.ArrowCursor))
		self.setReadOnly(True)
		self.hide()

	# set content text of wiget
	def setText(self, text):
		self.setPlainText(text)
		if len(text) > 0:
			self.show()
		else:
			self.hide()

	# set text font and adjust show
	def setFont(self, font):
		QPlainTextEdit.setFont(self, font)
		if self.mShowAll:
			self.showAll()
		else:
			self.showLess()

	# set line limit to show when self.mShowAll is false
	def setDefaultLineCount(self, count):
		self.mDefaultLineCount = count

	# important, in case the widget size is changed, it computes real height of text 
	# and adjust widget height based on the mShowAll flag
	def resizeEvent(self, event):
		QPlainTextEdit.resizeEvent(self, event)

		# adjust show based on the flag
		if self.mShowAll:
			self.showAll()
		else:
			self.showLess()

		# computes real height of text within the given width
		# and checks whether the text if overflooded or not
		# and also emit signal 
		doc = self.document()
		layout = doc.documentLayout()
		h = 0
		b = doc.begin()
		while b != doc.end():
			h += layout.blockBoundingRect(b).height()
			b = b.next()
		fh = h + doc.documentMargin() + 2 * self.frameWidth() + 1

		fm = QFontMetrics(self.font())
		minh = fm.height() * (self.mDefaultLineCount + 1) + 2 * self.frameWidth() + doc.documentMargin() + 3
		if fh < minh:
			self.lessThanLimit.emit()
		else:
			self.moreThanLimit.emit()

	# show whole text
	def showAll(self):
		self.mShowAll = True

		doc = self.document()
		layout = doc.documentLayout()
		h = 0
		b = doc.begin()
		while b != doc.end():
			h += layout.blockBoundingRect(b).height()
			b = b.next()

		self.setFixedHeight(h + doc.documentMargin() + 2 * self.frameWidth() + 1)

	# show fixed lines of text only, line count is equal to self.mDefaultLineCount
	def showLess(self):
		self.mShowAll = False

		doc = self.document()
		layout = doc.documentLayout()
		h = 0
		b = doc.begin()
		while b != doc.end():
			h += layout.blockBoundingRect(b).height()
			b = b.next()
		fh = h + doc.documentMargin() + 2 * self.frameWidth() + 1

		fm = QFontMetrics(self.font())
		minh = fm.height() * self.mDefaultLineCount + 2 * self.frameWidth() + doc.documentMargin() + 3
		if fh < minh:
			self.setFixedHeight(fh)
		else:
			self.setFixedHeight(minh)

		# scroll to top
		self.moveCursor(QTextCursor.Start)
		self.ensureCursorVisible()
