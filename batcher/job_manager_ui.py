# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'job_manager.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelIterInfo = QLabel(self.centralwidget)
        self.labelIterInfo.setObjectName(u"labelIterInfo")

        self.verticalLayout.addWidget(self.labelIterInfo)

        self.lineEditIterableInput = QLineEdit(self.centralwidget)
        self.lineEditIterableInput.setObjectName(u"lineEditIterableInput")

        self.verticalLayout.addWidget(self.lineEditIterableInput)

        self.labelScriptInfo = QLabel(self.centralwidget)
        self.labelScriptInfo.setObjectName(u"labelScriptInfo")

        self.verticalLayout.addWidget(self.labelScriptInfo)

        self.textEditJobInput = QTextEdit(self.centralwidget)
        self.textEditJobInput.setObjectName(u"textEditJobInput")

        self.verticalLayout.addWidget(self.textEditJobInput)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonAddJob = QPushButton(self.centralwidget)
        self.pushButtonAddJob.setObjectName(u"pushButtonAddJob")

        self.horizontalLayout.addWidget(self.pushButtonAddJob)

        self.pushButtonRemoveJob = QPushButton(self.centralwidget)
        self.pushButtonRemoveJob.setObjectName(u"pushButtonRemoveJob")

        self.horizontalLayout.addWidget(self.pushButtonRemoveJob)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listWidgetJobs = QListWidget(self.centralwidget)
        self.listWidgetJobs.setObjectName(u"listWidgetJobs")
        self.listWidgetJobs.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listWidgetJobs.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout.addWidget(self.listWidgetJobs)

        self.pushButtonStartExecution = QPushButton(self.centralwidget)
        self.pushButtonStartExecution.setObjectName(u"pushButtonStartExecution")

        self.verticalLayout.addWidget(self.pushButtonStartExecution)

        self.plainTextEditResults = QPlainTextEdit(self.centralwidget)
        self.plainTextEditResults.setObjectName(u"plainTextEditResults")

        self.verticalLayout.addWidget(self.plainTextEditResults)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.labelIterInfo.setText(QCoreApplication.translate("MainWindow", u"Python script to generate: iterable = ...", None))
        self.labelScriptInfo.setText(QCoreApplication.translate("MainWindow", u"Python script to run on the iterable:", None))
        self.pushButtonAddJob.setText(QCoreApplication.translate("MainWindow", u"Add Job", None))
        self.pushButtonRemoveJob.setText(QCoreApplication.translate("MainWindow", u"Remove Selected Job", None))
        self.pushButtonStartExecution.setText(QCoreApplication.translate("MainWindow", u"Start Execution", None))
        pass
    # retranslateUi

