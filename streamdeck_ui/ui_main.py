# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QTextEdit, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QProgressBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 639)
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionDocs = QAction(MainWindow)
        self.actionDocs.setObjectName(u"actionDocs")
        self.actionGithub = QAction(MainWindow)
        self.actionGithub.setObjectName(u"actionGithub")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, -1, -1, 3)
        self.main_horizontalLayout = QHBoxLayout()
        self.main_horizontalLayout.setSpacing(12)
        self.main_horizontalLayout.setObjectName(u"main_horizontalLayout")
        self.main_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_verticalLayout = QVBoxLayout()
        self.left_verticalLayout.setSpacing(6)
        self.left_verticalLayout.setObjectName(u"left_verticalLayout")
        self.left_verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.left_verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.deviceSettings_horizontalLayout = QHBoxLayout()
        self.deviceSettings_horizontalLayout.setObjectName(u"deviceSettings_horizontalLayout")
        self.deviceSettings_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.device_list = QComboBox(self.centralwidget)
        self.device_list.setObjectName(u"device_list")
        self.device_list.setMinimumSize(QSize(400, 0))

        self.deviceSettings_horizontalLayout.addWidget(self.device_list)

        self.settingsButton = QPushButton(self.centralwidget)
        self.settingsButton.setObjectName(u"settingsButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsButton.sizePolicy().hasHeightForWidth())
        self.settingsButton.setSizePolicy(sizePolicy)
        self.settingsButton.setMinimumSize(QSize(0, 0))
        self.settingsButton.setMaximumSize(QSize(30, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/icons/gear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsButton.setIcon(icon)

        self.deviceSettings_horizontalLayout.addWidget(self.settingsButton)

        self.cpu_usage = QProgressBar(self.centralwidget)
        self.cpu_usage.setObjectName(u"cpu_usage")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cpu_usage.sizePolicy().hasHeightForWidth())
        self.cpu_usage.setSizePolicy(sizePolicy1)
        self.cpu_usage.setMaximumSize(QSize(25, 25))
        self.cpu_usage.setMaximum(130)
        self.cpu_usage.setValue(0)
        self.cpu_usage.setOrientation(Qt.Vertical)

        self.deviceSettings_horizontalLayout.addWidget(self.cpu_usage)


        self.left_verticalLayout.addLayout(self.deviceSettings_horizontalLayout)

        self.pages = QTabWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy2)
        self.pages.setAutoFillBackground(False)
        self.pages.setStyleSheet(u"b")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_2 = QGridLayout(self.page_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pages.addTab(self.page_1, "")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pages.addTab(self.page_2, "")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_11 = QGridLayout(self.page_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.pages.addTab(self.page_3, "")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_10 = QGridLayout(self.page_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.pages.addTab(self.page_4, "")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_9 = QGridLayout(self.page_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pages.addTab(self.page_5, "")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_8 = QGridLayout(self.page_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pages.addTab(self.page_6, "")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_7 = QGridLayout(self.page_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pages.addTab(self.page_7, "")
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.gridLayout_6 = QGridLayout(self.page_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pages.addTab(self.page_8, "")
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.gridLayout_5 = QGridLayout(self.page_9)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pages.addTab(self.page_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_4 = QGridLayout(self.tab_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pages.addTab(self.tab_10, "")

        self.left_verticalLayout.addWidget(self.pages)

        self.left_verticalLayout.setStretch(1, 1)

        self.main_horizontalLayout.addLayout(self.left_verticalLayout)

        self.right_horizontalLayout = QHBoxLayout()
        self.right_horizontalLayout.setObjectName(u"right_horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(250, 0))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.imageButton = QPushButton(self.groupBox)
        self.imageButton.setObjectName(u"imageButton")

        self.horizontalLayout_2.addWidget(self.imageButton)

        self.removeButton = QPushButton(self.groupBox)
        self.removeButton.setObjectName(u"removeButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
        self.removeButton.setSizePolicy(sizePolicy3)
        self.removeButton.setMaximumSize(QSize(30, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.removeButton.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.removeButton)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.text = QTextEdit(self.groupBox)
        self.text.setObjectName(u"text")

        self.horizontalLayout_3.addWidget(self.text)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        
        self.text_v_align = QPushButton(self.groupBox)
        self.text_v_align.setObjectName(u"text_v_align")
        self.text_v_align.setMinimumSize(QSize(30, 0))
        self.text_v_align.setMaximumSize(QSize(30, 16777215))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/vertical-align.png", QSize(), QIcon.Normal, QIcon.Off)
        self.text_v_align.setIcon(icon2)

        self.verticalLayout_4.addWidget(self.text_v_align)

        self.text_h_align = QPushButton(self.groupBox)
        self.text_h_align.setObjectName(u"text_h_align")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/horizontal-align.png", QSize(), QIcon.Normal, QIcon.Off)
        self.text_h_align.setIcon(icon3)

        self.verticalLayout_4.addWidget(self.text_h_align)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.command = QLineEdit(self.groupBox)
        self.command.setObjectName(u"command")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.command)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_5)

        self.keys = QComboBox(self.groupBox)
        self.keys.addItem(u"")
        self.keys.addItem(u"F11")
        self.keys.addItem(u"alt+F4")
        self.keys.addItem(u"ctrl+w")
        self.keys.addItem(u"cmd+left")
        self.keys.addItem(u"alt+plus")
        self.keys.addItem(u"alt+delay+F3")
        self.keys.addItem(u"backspace")
        self.keys.addItem(u"right")
        self.keys.addItem(u"page_up")
        self.keys.addItem(u"media_volume_up")
        self.keys.addItem(u"media_volume_down")
        self.keys.addItem(u"media_volume_mute")
        self.keys.addItem(u"media_previous")
        self.keys.addItem(u"media_next")
        self.keys.addItem(u"media_play_pause")
        self.keys.setObjectName(u"keys")
        self.keys.setEditable(True)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.keys)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_8)

        self.switch_page = QSpinBox(self.groupBox)
        self.switch_page.setObjectName(u"switch_page")
        self.switch_page.setMinimum(0)
        self.switch_page.setMaximum(10)
        self.switch_page.setValue(0)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.switch_page)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_7)

        self.change_brightness = QSpinBox(self.groupBox)
        self.change_brightness.setObjectName(u"change_brightness")
        self.change_brightness.setMinimum(-99)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.change_brightness)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_6)

        self.write = QPlainTextEdit(self.groupBox)
        self.write.setObjectName(u"write")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.write)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.text_font = QComboBox(self.groupBox)
        self.text_font.setObjectName(u"text_font")

        self.horizontalLayout_4.addWidget(self.text_font)

        self.text_font_size = QSpinBox(self.groupBox)
        self.text_font_size.setObjectName(u"text_font_size")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.text_font_size.sizePolicy().hasHeightForWidth())
        self.text_font_size.setSizePolicy(sizePolicy4)
        self.text_font_size.setMinimum(12)
        self.text_font_size.setMaximum(72)

        self.horizontalLayout_4.addWidget(self.text_font_size)

        self.text_color = QPushButton(self.groupBox)
        self.text_color.setObjectName(u"text_color")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.text_color.sizePolicy().hasHeightForWidth())
        self.text_color.setSizePolicy(sizePolicy5)
        self.text_color.setMaximumSize(QSize(50, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.text_color.setPalette(palette)

        self.horizontalLayout_4.addWidget(self.text_color)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_4)


        self.verticalLayout_3.addLayout(self.formLayout)


        self.right_horizontalLayout.addWidget(self.groupBox)


        self.main_horizontalLayout.addLayout(self.right_horizontalLayout)


        self.verticalLayout_2.addLayout(self.main_horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 940, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.device_list, self.settingsButton)
        QWidget.setTabOrder(self.settingsButton, self.pages)
        QWidget.setTabOrder(self.pages, self.imageButton)
        QWidget.setTabOrder(self.imageButton, self.removeButton)
        QWidget.setTabOrder(self.removeButton, self.text)
        QWidget.setTabOrder(self.text, self.text_v_align)
        QWidget.setTabOrder(self.text_v_align, self.command)
        QWidget.setTabOrder(self.command, self.keys)
        QWidget.setTabOrder(self.keys, self.switch_page)
        QWidget.setTabOrder(self.switch_page, self.change_brightness)
        QWidget.setTabOrder(self.change_brightness, self.write)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionDocs)
        self.menuHelp.addAction(self.actionGithub)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Stream Deck UI", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionDocs.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionGithub.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About...", None))
        self.settingsButton.setText("")
        self.cpu_usage.setFormat("")
        self.pages.setTabText(self.pages.indexOf(self.page_1), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.pages.setTabText(self.pages.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"2", None))
        self.pages.setTabText(self.pages.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"3", None))
        self.pages.setTabText(self.pages.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"4", None))
        self.pages.setTabText(self.pages.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u"5", None))
        self.pages.setTabText(self.pages.indexOf(self.page_6), QCoreApplication.translate("MainWindow", u"6", None))
        self.pages.setTabText(self.pages.indexOf(self.page_7), QCoreApplication.translate("MainWindow", u"7", None))
        self.pages.setTabText(self.pages.indexOf(self.page_8), QCoreApplication.translate("MainWindow", u"8", None))
        self.pages.setTabText(self.pages.indexOf(self.page_9), QCoreApplication.translate("MainWindow", u"9", None))
        self.pages.setTabText(self.pages.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"10", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Configure Button", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Image:", None))
        self.imageButton.setText(QCoreApplication.translate("MainWindow", u"Image...", None))
#if QT_CONFIG(tooltip)
        self.removeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Remove the image from the button", None))
#endif // QT_CONFIG(tooltip)
        self.removeButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Label:", None))
#if QT_CONFIG(tooltip)
        self.text_v_align.setToolTip(QCoreApplication.translate("MainWindow", u"Text vertical alignment", None))
#endif // QT_CONFIG(tooltip)
        self.text_v_align.setText("")
#if QT_CONFIG(tooltip)
        self.text_h_align.setToolTip(QCoreApplication.translate("MainWindow", u"Text horizontal alignment", None))
#endif // QT_CONFIG(tooltip)
        self.text_h_align.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Font:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Command:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Press Keys:", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Switch Page:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Brightness +/-:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Write Text:", None))
#if QT_CONFIG(tooltip)
        self.text_color.setToolTip(QCoreApplication.translate("MainWindow", u"Text Color", None))
#endif // QT_CONFIG(tooltip)
        self.text_color.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

