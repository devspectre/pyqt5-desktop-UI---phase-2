import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from enum import Enum

#styles for customized horizontal scroll bar
class HSCROLL_STYLE(Enum):
	SILENT = """
		QScrollBar:horizontal {
			border: none;
			background: none;
			width: 0px;
			margin: 0px 0 0px 0;
		}

		QScrollBar::handle:horizontal {
			background: #ddd;
            min-height: 0px;
		}

		QScrollBar::handle:horizontal:hover {
			background: #bbb;
            min-height: 0px;
		}


		QScrollBar::add-line:horizontal {
			background: none;
			height: 10px;
			subcontrol-position: bottom;
			subcontrol-origin: margin;
		}

		QScrollBar::sub-line:horizontal {
			background: none;
			height: 10px;
			subcontrol-position: top left;
			subcontrol-origin: margin;
			position: absolute;
		}

		QScrollBar:up-arrow:horizontal, QScrollBar::down-arrow:horizontal {
			width: 5px;
			height: 5px;
			background: none;
			image: url('./img/glass.png');
        }

        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
            background: none;
		}"""
	THIN = """
		QScrollBar:horizontal {
			border: none;
			background: none;
			height: 5px;
			margin: 0px 0 0px 0;
		}

		QScrollBar::handle:horizontal {
			background: #ddd;
            min-width: 5px;
		}

		QScrollBar::handle:horizontal:hover {
			background: #bbb;
            min-width: 5px;
		}


		QScrollBar::add-line:horizontal {
			background: none;
			width: 10px;
			subcontrol-position: right;
			subcontrol-origin: margin;
		}

		QScrollBar::sub-line:horizontal {
			background: none;
			width: 10px;
			subcontrol-position: top left;
			subcontrol-origin: margin;
			position: absolute;
		}

		QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {
			width: 5px;
			height: 5px;
			background: none;
			image: url('./img/glass.png');
        }

        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
            background: none;
		}"""
	NARROW = """
		QScrollBar:horizontal {
			border: none;
			background: none;
			height: 10px;
			margin: 0px 0 0px 0;
		}

		QScrollBar::handle:horizontal {
			background: #ddd;
            min-width: 10px;
		}

		QScrollBar::handle:horizontal:hover {
			background: #bbb;
            min-width: 10px;
		}

		QScrollBar::add-line:horizontal {
			background: none;
			width: 10px;
			subcontrol-position: bottom;
			subcontrol-origin: margin;
		}

		QScrollBar::sub-line:horizontal {
			background: none;
			width: 10px;
			subcontrol-position: top left;
			subcontrol-origin: margin;
			position: absolute;
		}

		QScrollBar:up-arrow:horizontal, QScrollBar::down-arrow:horizontal {
			width: 10px;
			height: 10px;
			background: none;
			image: url('./img/glass.png');
        }

        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
            background: none;
        }"""

class HorizontalScrollArea(QScrollArea):
	"""Scroll area derived from QScrollArea only shows horizontal scroll bar whose
		width has to be adjusted to fit the screen resolution"""

	def __init__(self, parent = None):
		QScrollArea.__init__(self, parent)

		self.style = HSCROLL_STYLE.NARROW.value

		self.setWidgetResizable(True)
		self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
		self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.verticalScrollBar().setEnabled(False)
		self.horizontalScrollBar().setStyleSheet(self.style)
		self.horizontalScrollBar().setEnabled(True)

	#this is necessary for users to scroll horizontally with mouse on frame.
	def wheelEvent(self, event: QWheelEvent):
		self.horizontalScrollBar().wheelEvent(event)
		
	#set scroll bar style
	def setStyle(self, newstyle):
		self.style = newstyle
		self.setStyleSheet(self.style)

	#calculate exact minimum width within the area and set it
	def eventFilter(self, object, event):
		if object is not None:
			if object == self.widget():
				if event.type() == QEvent.Resize:
					self.setMinimumHeight(self.widget().minimumSizeHint().height() + self.horizontalScrollBar().height())
		return QScrollArea.eventFilter(self, object, event)