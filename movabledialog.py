
from PyQt5.QtGui import *
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QDialog

class MovableDialog(QDialog):
	"""Dialog widget derived from Dialog which is movable with mouse dragging"""
	def __init__(self, parent = None):
		self.mIsPressed = False
		self.mXDiff = 0
		self.mYDiff = 0

	def mousePressEvent(self, event):
		self.mIsPressed = True
		pressedPoint = QCursor.pos()
		appPos = self.pos()
		self.mXDiff = pressedPoint.x() - appPos.x()
		self.mYDiff = pressedPoint.y() - appPos.y()

	def mouseReleaseEvent(self, event):
		self.mIsPressed = False

	def mouseMoveEvent(self, event):
		if self.mIsPressed:
			appNewPos = QPoint()
			appNewPos.setX(QCursor.pos().x() - self.mXDiff)
			appNewPos.setY(QCursor.pos().y() - self.mYDiff)
			self.move(appNewPos.x(), appNewPos.y())