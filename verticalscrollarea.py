import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from enum import Enum

# styles for customized vertical scroll bar
class VSCROLL_STYLE(Enum):
	SILENT = """
		QScrollBar:vertical {
			border: none;
			background: none;
			width: 0px;
			margin: 0px 0 0px 0;
		}

		QScrollBar::handle:vertical {
			background: lightgray;
            min-height: 0px;
		}

		QScrollBar::handle:vertical:hover {
			background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(215, 215, 225, 225), stop:1 rgba(155, 155, 175, 255));
            min-height: 0px;
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
	THIN = """
		QScrollBar:vertical {
			border: none;
			background: none;
			width: 5px;
			margin: 0px 0 0px 0;
		}

		QScrollBar::handle:vertical {
			background: #ddd;
            min-height: 5px;
		}

		QScrollBar::handle:vertical:hover {
			background: #bbb;
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
	NORMAL = """
		QScrollBar:vertical {
			border: none;
			background: none;
			width: 15px;
			margin: 0px 0 0px 0;
		}

		QScrollBar::handle:vertical {
			background: lightgray;
            min-height: 15px;
		}

		QScrollBar::handle:vertical:hover {
			background: #ddd;
            min-height: 15px;
		}

		QScrollBar::add-line:vertical {
			background: none;
			height: 15px;
			subcontrol-position: bottom;
			subcontrol-origin: margin;
		}

		QScrollBar::sub-line:vertical {
			background: none;
			height: 15px;
			subcontrol-position: top left;
			subcontrol-origin: margin;
			position: absolute;
		}

		QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {
			width: 15px;
			height: 15px;
			background: none;
			image: url('./img/glass.png');
        }

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
        }"""
	THICK = """
		QScrollBar:vertical {
			border: none;
			background: none;
			width: 20px;
			margin: 0px 0 0px 0;
		}

		QScrollBar::handle:vertical {
			background: lightgray;
            min-height: 20px;
		}


		QScrollBar::add-line:vertical {
			background: none;
			height: 20px;
			subcontrol-position: bottom;
			subcontrol-origin: margin;
		}

		QScrollBar::sub-line:vertical {
			background: none;
			height: 20px;
			subcontrol-position: top left;
			subcontrol-origin: margin;
			position: absolute;
		}

		QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {
			width: 20px;
			height: 20px;
			background: none;
			image: url('./img/glass.png');
        }

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
        }"""

class VerticalScrollArea(QScrollArea):
	""" Scroll area derived from QScrollArea only shows vertical scroll bar whose
		width has to be adjusted to fit the screen resolution"""

	def __init__(self, parent = None):
		QScrollArea.__init__(self, parent)

		self.style = VSCROLL_STYLE.NARROW.value

		self.setWidgetResizable(True)
		self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
		self.verticalScrollBar().setStyleSheet(self.style)

	# set scroll bar style
	def setStyle(self, newstyle):
		self.style = newstyle
		self.verticalScrollBar().setStyleSheet(self.style)

	def getStyle(self):
		return self.style

	# calculate exact minimum width within the area and set it
	def eventFilter(self, object, event):
		if object is not None:
			if object == self.widget():
				if event.type() == QEvent.Resize:
					self.setMinimumWidth(self.widget().minimumSizeHint().width() + self.verticalScrollBar().width())
		return QScrollArea.eventFilter(self, object, event)