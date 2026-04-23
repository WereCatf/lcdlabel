# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'example.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QMenuBar, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

from lcdlabel import LcdLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(731, 477)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.clock1 = LcdLabel(self.frame)
        self.clock1.setObjectName(u"clock1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clock1.sizePolicy().hasHeightForWidth())
        self.clock1.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"DSEG7 Classic Mini"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.clock1.setFont(font1)
        self.clock1.setProperty(u"alignment", Qt.AlignmentFlag.AlignCenter)
        self.clock1.setProperty(u"foregroundColor", QColor(0, 255, 0))
        self.clock1.setProperty(u"backgroundColor", QColor(60, 60, 60))

        self.verticalLayout.addWidget(self.clock1)

        self.clock2 = LcdLabel(self.frame)
        self.clock2.setObjectName(u"clock2")
        sizePolicy.setHeightForWidth(self.clock2.sizePolicy().hasHeightForWidth())
        self.clock2.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"DSEG14 Classic Mini"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.clock2.setFont(font2)
        self.clock2.setProperty(u"alignment", Qt.AlignmentFlag.AlignCenter)
        self.clock2.setProperty(u"foregroundColor", QColor(255, 0, 255))
        self.clock2.setProperty(u"backgroundColor", QColor(60, 60, 60))

        self.verticalLayout.addWidget(self.clock2)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        palette = QPalette()
        brush = QBrush(QColor(166, 169, 159, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        self.frame_2.setPalette(palette)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lcdLabel_3 = LcdLabel(self.frame_2)
        self.lcdLabel_3.setObjectName(u"lcdLabel_3")
        font3 = QFont()
        font3.setFamilies([u"DSEG7 Classic Mini"])
        font3.setPointSize(32)
        font3.setBold(True)
        self.lcdLabel_3.setFont(font3)
        self.lcdLabel_3.setProperty(u"alignment", Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lcdLabel_3.setProperty(u"foregroundColor", QColor(0, 0, 0))
        self.lcdLabel_3.setProperty(u"backgroundColor", QColor(0, 0, 0, 20))

        self.verticalLayout_2.addWidget(self.lcdLabel_3)

        self.lcdLabel_4 = LcdLabel(self.frame_2)
        self.lcdLabel_4.setObjectName(u"lcdLabel_4")
        font4 = QFont()
        font4.setFamilies([u"DSEG14 Classic Mini"])
        font4.setPointSize(32)
        font4.setBold(True)
        self.lcdLabel_4.setFont(font4)
        self.lcdLabel_4.setProperty(u"alignment", Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lcdLabel_4.setProperty(u"foregroundColor", QColor(0, 0, 0))
        self.lcdLabel_4.setProperty(u"backgroundColor", QColor(0, 0, 0, 20))

        self.verticalLayout_2.addWidget(self.lcdLabel_4)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        brush1 = QBrush(QColor(255, 85, 0, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        self.frame_3.setPalette(palette1)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lcdLabel_2 = LcdLabel(self.frame_3)
        self.lcdLabel_2.setObjectName(u"lcdLabel_2")
        font5 = QFont()
        font5.setFamilies([u"DSEG14 Classic Mini"])
        font5.setPointSize(18)
        font5.setBold(False)
        self.lcdLabel_2.setFont(font5)
        self.lcdLabel_2.setProperty(u"alignment", Qt.AlignmentFlag.AlignCenter)
        self.lcdLabel_2.setProperty(u"foregroundColor", QColor(0, 0, 0))
        self.lcdLabel_2.setProperty(u"backgroundColor", QColor(0, 0, 0, 20))

        self.horizontalLayout.addWidget(self.lcdLabel_2)

        self.lcdLabel = LcdLabel(self.frame_3)
        self.lcdLabel.setObjectName(u"lcdLabel")
        sizePolicy.setHeightForWidth(self.lcdLabel.sizePolicy().hasHeightForWidth())
        self.lcdLabel.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setFamilies([u"DSEG Weather"])
        font6.setPointSize(64)
        self.lcdLabel.setFont(font6)
        self.lcdLabel.setProperty(u"alignment", Qt.AlignmentFlag.AlignCenter)
        self.lcdLabel.setProperty(u"foregroundColor", QColor(0, 0, 0))
        self.lcdLabel.setProperty(u"backgroundColor", QColor(0, 0, 0, 20))

        self.horizontalLayout.addWidget(self.lcdLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 731, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.clock1.setProperty(u"text", QCoreApplication.translate("MainWindow", u"12:34.56", None))
        self.clock1.setProperty(u"backgroundText", QCoreApplication.translate("MainWindow", u"8.88888", None))
        self.clock2.setProperty(u"text", QCoreApplication.translate("MainWindow", u"12:34.56", None))
        self.clock2.setProperty(u"backgroundText", QCoreApplication.translate("MainWindow", u"~~:~~.~~", None))
        self.lcdLabel_3.setProperty(u"text", QCoreApplication.translate("MainWindow", u"LEFT!7seg", None))
        self.lcdLabel_3.setProperty(u"backgroundText", QCoreApplication.translate("MainWindow", u"888888888", None))
        self.lcdLabel_4.setProperty(u"text", QCoreApplication.translate("MainWindow", u"14SEG!RIGHT", None))
        self.lcdLabel_4.setProperty(u"backgroundText", QCoreApplication.translate("MainWindow", u"~~~~~~~~~~~", None))
        self.lcdLabel_2.setProperty(u"text", QCoreApplication.translate("MainWindow", u"PARTIALLY!CLOUDY", None))
        self.lcdLabel_2.setProperty(u"backgroundText", QCoreApplication.translate("MainWindow", u"~~~~~~~~~~~~~~~~", None))
        self.lcdLabel.setProperty(u"text", QCoreApplication.translate("MainWindow", u"9", None))
        self.lcdLabel.setProperty(u"backgroundText", QCoreApplication.translate("MainWindow", u"~", None))
    # retranslateUi

