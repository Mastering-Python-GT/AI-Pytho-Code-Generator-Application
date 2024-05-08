# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pycode.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(863, 600)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
#         self.centralwidget.setStyleSheet(u"QWidget{\n"
# "	background-color: #090B10;\n"
# "}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(10, 0, 10, 10)
        self.result = QTextEdit(self.centralwidget)
        self.result.setObjectName(u"result")
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(14)
        self.result.setFont(font)
#         self.result.setStyleSheet(u"QTextEdit{\n"
# "	border: 1px solid #1E212D;\n"
# "	color: white;\n"
# "	background-color: #0F111A;\n"
# "}")
        self.result.setReadOnly(False)

        self.gridLayout.addWidget(self.result, 2, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 65))
        self.widget.setMaximumSize(QSize(16777215, 65))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.text = QPlainTextEdit(self.widget)
        self.text.setObjectName(u"text")
        self.text.setMinimumSize(QSize(0, 64))
        self.text.setMaximumSize(QSize(16777215, 64))
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(12)
        self.text.setFont(font1)
#         self.text.setStyleSheet(u"QPlainTextEdit{\n"
# "	border: 1px solid #1E212D;\n"
# "	color: white;\n"
# "	background-color: #0F111A;\n"
# "\n"
# "}")

        self.horizontalLayout.addWidget(self.text)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.generate = QPushButton(self.widget)
        self.generate.setObjectName(u"generate")
        self.generate.setMinimumSize(QSize(64, 64))
        self.generate.setMaximumSize(QSize(64, 64))
        self.generate.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icon/1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.generate.setIcon(icon)
        self.generate.setIconSize(QSize(50, 50))
        self.generate.setCheckable(True)

        self.horizontalLayout.addWidget(self.generate)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 25))
        self.widget_2.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(756, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(25, 25))
        self.pushButton_3.setMaximumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/chrome-minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.maximize_btn = QPushButton(self.widget_2)
        self.maximize_btn.setObjectName(u"maximize_btn")
        self.maximize_btn.setMinimumSize(QSize(25, 25))
        self.maximize_btn.setMaximumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/chrome-maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/icon/chrome-restore.svg", QSize(), QIcon.Normal, QIcon.On)
        self.maximize_btn.setIcon(icon2)
        self.maximize_btn.setIconSize(QSize(16, 16))
        self.maximize_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.widget_2)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(25, 25))
        self.close_btn.setMaximumSize(QSize(25, 25))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/chrome-close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon3)
        self.close_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.close_btn)


        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.result.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your generated code will be shown here .", None))
        self.text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Describe your code here, then press the generate button .", None))
        self.generate.setText("")
        self.pushButton_3.setText("")
        self.maximize_btn.setText("")
        self.close_btn.setText("")
    # retranslateUi

