# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #F5F7F6;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #263A35;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #2E7D6B;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 8px 20px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #246554;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #B8C9C3;\n"
"    border-radius: 7px;\n"
"    padding: 7px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: white;\n"
"    border: 1px solid #B8C9C3;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(140, 64, 258, 351))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_topic = QLabel(self.gridLayoutWidget)
        self.label_topic.setObjectName(u"label_topic")
        self.label_topic.setStyleSheet(u"QLabel {\n"
"    background-color: white;\n"
"    border: 2px solid #A8C5BC;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"}")

        self.gridLayout.addWidget(self.label_topic, 1, 0, 1, 1)

        self.comboBox_topic = QComboBox(self.gridLayoutWidget)
        self.comboBox_topic.addItem("")
        self.comboBox_topic.addItem("")
        self.comboBox_topic.addItem("")
        self.comboBox_topic.addItem("")
        self.comboBox_topic.addItem("")
        self.comboBox_topic.addItem("")
        self.comboBox_topic.setObjectName(u"comboBox_topic")
        self.comboBox_topic.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 2px solid #A8C5BC;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"}")

        self.gridLayout.addWidget(self.comboBox_topic, 1, 1, 1, 1)

        self.textEdit_result = QTextEdit(self.gridLayoutWidget)
        self.textEdit_result.setObjectName(u"textEdit_result")
        self.textEdit_result.setStyleSheet(u"QTextEdit {\n"
"    background-color: white;\n"
"    border: 2px solid #A8C5BC;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}")

        self.gridLayout.addWidget(self.textEdit_result, 5, 0, 1, 2)

        self.pushButton_show = QPushButton(self.gridLayoutWidget)
        self.pushButton_show.setObjectName(u"pushButton_show")

        self.gridLayout.addWidget(self.pushButton_show, 3, 0, 1, 2)

        self.label_result_title = QLabel(self.gridLayoutWidget)
        self.label_result_title.setObjectName(u"label_result_title")
        self.label_result_title.setStyleSheet(u"QLabel {\n"
"    color: #183C35;\n"
"}")

        self.gridLayout.addWidget(self.label_result_title, 4, 0, 1, 1)

        self.label_title = QLabel(self.gridLayoutWidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setStyleSheet(u"QLabel {\n"
"    color: #183C35;\n"
"}")

        self.gridLayout.addWidget(self.label_title, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_topic.setText(QCoreApplication.translate("MainWindow", u"Select a topic:", None))
        self.comboBox_topic.setItemText(0, QCoreApplication.translate("MainWindow", u"Select a topic", None))
        self.comboBox_topic.setItemText(1, QCoreApplication.translate("MainWindow", u"Funny", None))
        self.comboBox_topic.setItemText(2, QCoreApplication.translate("MainWindow", u"Motivational", None))
        self.comboBox_topic.setItemText(3, QCoreApplication.translate("MainWindow", u"Tech News", None))
        self.comboBox_topic.setItemText(4, QCoreApplication.translate("MainWindow", u"Movie", None))
        self.comboBox_topic.setItemText(5, QCoreApplication.translate("MainWindow", u"Game", None))

        self.pushButton_show.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.label_result_title.setText(QCoreApplication.translate("MainWindow", u"Result:", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Random Info ", None))
    # retranslateUi

