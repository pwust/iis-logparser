# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QMainWindow

from .Ui_LogParser import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_btnParse_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSlot()
    def on_actionOpen_log_file_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSlot()
    def on_actionQuit_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSlot()
    def on_actionAbout_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
