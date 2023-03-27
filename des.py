# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'des.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,
                            QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QAction, QFont)
from PySide6.QtWidgets import (QCheckBox, QFrame, QGridLayout,
                               QGroupBox, QLabel, QLineEdit, QListView,
                               QListWidget, QMenu,
                               QMenuBar, QPushButton, QRadioButton, QSizePolicy,
                               QSpacerItem, QStatusBar, QTabWidget, QToolBox,
                               QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(450, 500)
        MainWindow.setMinimumSize(QSize(450, 500))
        MainWindow.setAcceptDrops(False)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setStyleSheet(u"QMainWindow::separator {\n"
                                 "    background: yellow;\n"
                                 "    width: 10px; /* when vertical */\n"
                                 "    height: 10px; /* when horizontal */\n"
                                 "}\n"
                                 "\n"
                                 "QMainWindow::separator:hover {\n"
                                 "    background: red;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu {\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "	background-color: rgb(61, 61, 61);\n"
                                 "    border: 1px solid black;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::item {\n"
                                 "   /* \u0443\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435"
                                 "\u0442 \u0444\u043e\u043d \u043f\u0443\u043d\u043a\u0442\u0430 "
                                 "\u043c\u0435\u043d\u044e. "
                                 "\u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0435 \u044d\u0442\u043e "
                                 "\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 "
                                 "\u043d\u0435\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u043c,\n"
                                 "	 \u0435\u0441\u043b\u0438 \u0432\u044b \u0445\u043e\u0442\u0438\u0442\u0435, "
                                 "\u0447\u0442\u043e\u0431\u044b \u0446\u0432\u0435\u0442 \u043c\u0435\u043d\u044e "
                                 "\u0438 \u0446\u0432\u0435\u0442 \u043f\u0443\u043d\u043a\u0442\u0430 "
                                 "\u043c\u0435\u043d\u044e \u043e\u0442\u043b\u0438\u0447"
                                 "\u0430\u043b\u0438\u0441\u044c */\n"
                                 "    background-color: transparent;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::item:selected { /* when user selects item using mouse or keyboard */\n"
                                 "    background-color: rgb(75, 75, 75);\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar {\n"
                                 "    \n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "	background-color: rgb(70, 70, 70);\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar::item {\n"
                                 "    background: transparent;\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
                                 "	background-color: rgb(80, 80, 80);\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar::item:pressed {\n"
                                 "    background: #888888;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "	color: rgb(255, 255, 255);\n"
                                 "    border: 1px solid rgb(85, 85, 127);\n"
                                 "	background-color: rgb(85, 85, 127);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: rgb(55, 55, 95);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:flat {\n"
                                 "    border: none; /* no border for a flat push button */\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:default {\n"
                                 "    border-color: navy; /* make the default button prominent */\n"
                                 "}\n"
                                 "\n"
                                 "QToolBox::t"
                                 "ab {\n"
                                 "	background-color: rgb(85, 170, 127);\n"
                                 "\n"
                                 "/*\n"
                                 "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
                                 "                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
                                 "*/\n"
                                 "	color: blek;\n"
                                 "}\n"
                                 "\n"
                                 "QToolBox::tab:selected { /* italicize selected tabs */\n"
                                 "    color: blek;\n"
                                 "}\n"
                                 "\n"
                                 "QStatusBar {\n"
                                 "    background: rgb(44, 44, 44);\n"
                                 "	color: rgb(255, 235, 254);\n"
                                 "}\n"
                                 "\n"
                                 "QStatusBar::item {\n"
                                 "    border: 1px solid red;\n"
                                 "    border-radius: 3px;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.tab_1.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.tab_1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_item_full = QLabel(self.tab_1)
        self.label_item_full.setObjectName(u"label_item_full")

        self.gridLayout_4.addWidget(self.label_item_full, 3, 0, 1, 2)

        self.lineEdit = QLineEdit(self.tab_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEdit, 0, 2, 1, 8)

        self.label_item_folders_num = QLabel(self.tab_1)
        self.label_item_folders_num.setObjectName(u"label_item_folders_num")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_item_folders_num.sizePolicy().hasHeightForWidth())
        self.label_item_folders_num.setSizePolicy(sizePolicy)
        self.label_item_folders_num.setStyleSheet(u"color: rgb(0, 150, 110);")

        self.gridLayout_4.addWidget(self.label_item_folders_num, 3, 5, 1, 1)

        self.label_item_sorted = QLabel(self.tab_1)
        self.label_item_sorted.setObjectName(u"label_item_sorted")

        self.gridLayout_4.addWidget(self.label_item_sorted, 3, 7, 1, 1)

        self.listWidget = QListWidget(self.tab_1)
        self.listWidget.setObjectName(u"listWidget")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setKerning(True)
        self.listWidget.setFont(font)
        self.listWidget.setLayoutDirection(Qt.LeftToRight)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setTabKeyNavigation(False)
        self.listWidget.setDragEnabled(False)
        self.listWidget.setDragDropOverwriteMode(False)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setIconSize(QSize(12, 12))
        self.listWidget.setMovement(QListView.Static)
        self.listWidget.setFlow(QListView.TopToBottom)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QListView.Fixed)
        self.listWidget.setLayoutMode(QListView.SinglePass)
        self.listWidget.setSpacing(0)
        self.listWidget.setViewMode(QListView.ListMode)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setWordWrap(False)
        self.listWidget.setSelectionRectVisible(False)

        self.gridLayout_4.addWidget(self.listWidget, 1, 0, 1, 10)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 3, 9, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 3, 3, 1, 1)

        self.label_item_sorted_num = QLabel(self.tab_1)
        self.label_item_sorted_num.setObjectName(u"label_item_sorted_num")
        sizePolicy.setHeightForWidth(self.label_item_sorted_num.sizePolicy().hasHeightForWidth())
        self.label_item_sorted_num.setSizePolicy(sizePolicy)
        self.label_item_sorted_num.setStyleSheet(u"color: rgb(170, 0, 0);")

        self.gridLayout_4.addWidget(self.label_item_sorted_num, 3, 8, 1, 1)

        self.label_item_files = QLabel(self.tab_1)
        self.label_item_files.setObjectName(u"label_item_files")

        self.gridLayout_4.addWidget(self.label_item_files, 4, 4, 1, 1)

        self.label_item_other_num = QLabel(self.tab_1)
        self.label_item_other_num.setObjectName(u"label_item_other_num")
        sizePolicy.setHeightForWidth(self.label_item_other_num.sizePolicy().hasHeightForWidth())
        self.label_item_other_num.setSizePolicy(sizePolicy)
        self.label_item_other_num.setStyleSheet(u"color: rgb(170, 0, 0);")

        self.gridLayout_4.addWidget(self.label_item_other_num, 4, 8, 1, 1)

        self.label_item_other = QLabel(self.tab_1)
        self.label_item_other.setObjectName(u"label_item_other")

        self.gridLayout_4.addWidget(self.label_item_other, 4, 7, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 3, 6, 1, 1)

        self.pushButton = QPushButton(self.tab_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 24))

        self.gridLayout_4.addWidget(self.pushButton, 2, 0, 1, 10)

        self.label_item_files_num = QLabel(self.tab_1)
        self.label_item_files_num.setObjectName(u"label_item_files_num")
        sizePolicy.setHeightForWidth(self.label_item_files_num.sizePolicy().hasHeightForWidth())
        self.label_item_files_num.setSizePolicy(sizePolicy)
        self.label_item_files_num.setStyleSheet(u"color: rgb(0, 150, 110);")

        self.gridLayout_4.addWidget(self.label_item_files_num, 4, 5, 1, 1)

        self.label_item_full_num = QLabel(self.tab_1)
        self.label_item_full_num.setObjectName(u"label_item_full_num")
        sizePolicy.setHeightForWidth(self.label_item_full_num.sizePolicy().hasHeightForWidth())
        self.label_item_full_num.setSizePolicy(sizePolicy)
        self.label_item_full_num.setStyleSheet(u"color: rgb(0, 150, 110);")

        self.gridLayout_4.addWidget(self.label_item_full_num, 3, 2, 1, 1)

        self.label_item_folders = QLabel(self.tab_1)
        self.label_item_folders.setObjectName(u"label_item_folders")

        self.gridLayout_4.addWidget(self.label_item_folders, 3, 4, 1, 1)

        self.pushButton_2 = QPushButton(self.tab_1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(65, 24))

        self.gridLayout_4.addWidget(self.pushButton_2, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_2 = QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.toolBox = QToolBox(self.tab_3)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setGeometry(QRect(0, 0, 408, 361))
        self.gridLayout_2 = QGridLayout(self.page_1)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.page_1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.groupBox.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_image_2 = QCheckBox(self.groupBox)
        self.checkBox_image_2.setObjectName(u"checkBox_image_2")
        self.checkBox_image_2.setChecked(True)
        self.checkBox_image_2.setTristate(False)

        self.gridLayout_3.addWidget(self.checkBox_image_2, 3, 0, 1, 1)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 2, 0, 1, 3)

        self.checkBox_video_2 = QCheckBox(self.groupBox)
        self.checkBox_video_2.setObjectName(u"checkBox_video_2")
        self.checkBox_video_2.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_video_2, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 130, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 12, 0, 1, 3)

        self.checkBox_document_2 = QCheckBox(self.groupBox)
        self.checkBox_document_2.setObjectName(u"checkBox_document_2")
        self.checkBox_document_2.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_document_2, 6, 0, 1, 1)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 11, 0, 1, 3)

        self.edit_folder_archive = QLineEdit(self.groupBox)
        self.edit_folder_archive.setObjectName(u"edit_folder_archive")
        self.edit_folder_archive.setMinimumSize(QSize(150, 0))
        self.edit_folder_archive.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.edit_folder_archive, 7, 2, 1, 1)

        self.checkBox_audio_2 = QCheckBox(self.groupBox)
        self.checkBox_audio_2.setObjectName(u"checkBox_audio_2")
        self.checkBox_audio_2.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_audio_2, 4, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_3.addWidget(self.radioButton_2, 1, 0, 1, 3)

        self.edit_folder_video = QLineEdit(self.groupBox)
        self.edit_folder_video.setObjectName(u"edit_folder_video")
        self.edit_folder_video.setMinimumSize(QSize(150, 0))
        self.edit_folder_video.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.edit_folder_video, 5, 2, 1, 1)

        self.edit_folder_other = QLineEdit(self.groupBox)
        self.edit_folder_other.setObjectName(u"edit_folder_other")
        self.edit_folder_other.setMinimumSize(QSize(150, 0))
        self.edit_folder_other.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.edit_folder_other, 10, 2, 1, 1)

        self.checkBox_program_2 = QCheckBox(self.groupBox)
        self.checkBox_program_2.setObjectName(u"checkBox_program_2")
        self.checkBox_program_2.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_program_2, 8, 0, 1, 1)

        self.edit_folder_image = QLineEdit(self.groupBox)
        self.edit_folder_image.setObjectName(u"edit_folder_image")
        self.edit_folder_image.setEnabled(True)
        self.edit_folder_image.setMinimumSize(QSize(150, 0))
        self.edit_folder_image.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.edit_folder_image.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.edit_folder_image, 3, 2, 1, 1)

        self.edit_folder_document = QLineEdit(self.groupBox)
        self.edit_folder_document.setObjectName(u"edit_folder_document")
        self.edit_folder_document.setMinimumSize(QSize(150, 0))
        self.edit_folder_document.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.edit_folder_document, 6, 2, 1, 1)

        self.edit_folder_program = QLineEdit(self.groupBox)
        self.edit_folder_program.setObjectName(u"edit_folder_program")
        self.edit_folder_program.setMinimumSize(QSize(150, 0))
        self.edit_folder_program.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.edit_folder_program, 8, 2, 1, 1)

        self.radioButton_1 = QRadioButton(self.groupBox)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setChecked(True)

        self.gridLayout_3.addWidget(self.radioButton_1, 0, 0, 1, 3)

        self.edit_folder_audio = QLineEdit(self.groupBox)
        self.edit_folder_audio.setObjectName(u"edit_folder_audio")
        self.edit_folder_audio.setMinimumSize(QSize(150, 0))
        self.edit_folder_audio.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.edit_folder_audio, 4, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 3, 1, 1, 1)

        self.checkBox_torrent_2 = QCheckBox(self.groupBox)
        self.checkBox_torrent_2.setObjectName(u"checkBox_torrent_2")
        self.checkBox_torrent_2.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_torrent_2, 9, 0, 1, 1)

        self.checkBox_other_2 = QCheckBox(self.groupBox)
        self.checkBox_other_2.setObjectName(u"checkBox_other_2")

        self.gridLayout_3.addWidget(self.checkBox_other_2, 10, 0, 1, 1)

        self.checkBox_archive_2 = QCheckBox(self.groupBox)
        self.checkBox_archive_2.setObjectName(u"checkBox_archive_2")
        self.checkBox_archive_2.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_archive_2, 7, 0, 1, 1)

        self.edit_folder_torrent = QLineEdit(self.groupBox)
        self.edit_folder_torrent.setObjectName(u"edit_folder_torrent")
        self.edit_folder_torrent.setMinimumSize(QSize(150, 0))
        self.edit_folder_torrent.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.edit_folder_torrent, 9, 2, 1, 1)

        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_1,
                             u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b "
                             u"\u043f\u043e\u0438\u0441\u043a\u0430 \u0438 "
                             u"\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438")

        self.verticalLayout_2.addWidget(self.toolBox)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 450, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy2)
        self.statusBar.setMinimumSize(QSize(0, 0))
        self.statusBar.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        self.statusBar.setFont(font1)
        self.statusBar.setInputMethodHints(Qt.ImhNone)
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_2)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.listWidget.clear)

        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        # if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.action.setText(QCoreApplication.translate("MainWindow",
                                                       u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c "
                                                       u"\u043f\u0430\u043f\u043a\u0443",
                                                       None))
        self.action_2.setText(
            QCoreApplication.translate("MainWindow", u"\u041e \u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435",
                                       None))
        self.label_item_full.setText(
            QCoreApplication.translate("MainWindow", u"\u042d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432:", None))
        # if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("MainWindow",
                                                            u"<html><head/><body><p> "
                                                            u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 "
                                                            u"\u043f\u0443\u0442\u044c</p></body></html>",
                                                            None))
        # endif // QT_CONFIG(tooltip)
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u" \u0421urrent path", None))
        self.label_item_folders_num.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_item_sorted.setText(QCoreApplication.translate("MainWindow",
                                                                  u"\u041e\u0442\u0441\u043e\u0440\u0442\u0438\u0440"
                                                                  u"\u043e\u0432\u0430\u043d\u043e:",
                                                                  None))
        self.label_item_sorted_num.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_item_files.setText(
            QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b\u043e\u0432:", None))
        self.label_item_other_num.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_item_other.setText(
            QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0443\u0433\u043e\u0435:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow",
                                                           u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430"
                                                           u"\u0442\u044c",
                                                           None))
        self.label_item_files_num.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_item_full_num.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_item_folders.setText(
            QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043f\u043e\u043a:", None))
        # if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow",
                                                                                                 u"\u0413\u043b\u0430"
                                                                                                 u"\u0432\u043d\u0430"
                                                                                                 u"\u044f",
                                                                                                 None))
        self.groupBox.setTitle("")
        self.checkBox_image_2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0442\u043e", None))
        self.checkBox_video_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0435\u043e", None))
        self.checkBox_document_2.setText(
            QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b", None))
        # if QT_CONFIG(tooltip)
        self.edit_folder_archive.setToolTip(QCoreApplication.translate("MainWindow",
                                                                       u"<html><head/><body><p>\u0418\u043c\u044f "
                                                                       u"\u043f\u0430\u043f\u043a\u0438 \u0432 "
                                                                       u"\u043a\u043e\u0442\u043e\u0440\u0443\u044e "
                                                                       u"\u0431\u0443\u0434\u0443\u0442 "
                                                                       u"\u043f\u043e\u043c\u0435\u0449\u0435\u043d"
                                                                       u"\u044b "
                                                                       u"\u0430\u0440\u0445\u0438\u0432\u044b</p"
                                                                       u"></body></html>",
                                                                       None))
        # endif // QT_CONFIG(tooltip)
        self.edit_folder_archive.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Archive", None))
        self.checkBox_audio_2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0443\u0434\u0438\u043e", None))
        # if QT_CONFIG(tooltip)
        self.radioButton_2.setToolTip(QCoreApplication.translate("MainWindow",
                                                                 u"<html><head/><body><p>\u0412\u044b\u0431\u043e"
                                                                 u"\u0440\u043a\u0430 \u0432\u0441\u0435\u0445 "
                                                                 u"\u0444\u0430\u0439\u043b\u043e\u0432 \u0432 "
                                                                 u"\u043f\u0430\u043f\u043a\u0430\u0445 \u0438 "
                                                                 u"\u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0430"
                                                                 u"\u0445 "
                                                                 u"\u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e"
                                                                 u"\u0433\u043e "
                                                                 u"\u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0430"
                                                                 u"</p></body></html>",
                                                                 None))
        # endif // QT_CONFIG(tooltip)
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u041f\u043e\u0438\u0441\u043a \u0432 "
                                                              u"\u043f\u0430\u043f\u043a\u0430\u0445 \u0438 "
                                                              u"\u043f\u043e\u0434\u043f\u0430\u043f\u043a\u0430"
                                                              u"\u0445 "
                                                              u"\u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0430",
                                                              None))
        # if QT_CONFIG(tooltip)
        self.edit_folder_video.setToolTip(QCoreApplication.translate("MainWindow",
                                                                     u"<html><head/><body><p>\u0418\u043c\u044f "
                                                                     u"\u043f\u0430\u043f\u043a\u0438 \u0432 "
                                                                     u"\u043a\u043e\u0442\u043e\u0440\u0443\u044e "
                                                                     u"\u0431\u0443\u0434\u0443\u0442 "
                                                                     u"\u043f\u043e\u043c\u0435\u0449\u0435\u043d"
                                                                     u"\u044b \u0432\u0438\u0434\u0435\u043e "
                                                                     u"\u0444\u0430\u0439\u043b\u044b</p></body></html>",
                                                                     None))
        # endif // QT_CONFIG(tooltip)
        self.edit_folder_video.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Video", None))
        # if QT_CONFIG(tooltip)
        self.edit_folder_other.setToolTip(QCoreApplication.translate("MainWindow",
                                                                     u"<html><head/><body><p>\u0418\u043c\u044f "
                                                                     u"\u043f\u0430\u043f\u043a\u0438 \u0432 "
                                                                     u"\u043a\u043e\u0442\u043e\u0440\u0443\u044e "
                                                                     u"\u0431\u0443\u0434\u0443\u0442 "
                                                                     u"\u043f\u043e\u043c\u0435\u0449\u0435\u043d"
                                                                     u"\u044b \u0444\u0430\u0439\u043b\u044b "
                                                                     u"\u043a\u043e\u0442\u043e\u0440\u044b\u0435 "
                                                                     u"\u043d\u0435 \u0432\u043e\u0448\u043b\u0438 "
                                                                     u"\u043d\u0435 \u0432 \u043e\u0434\u043d\u0443 "
                                                                     u"\u0438\u0437 "
                                                                     u"\u043a\u0430\u0442\u0435\u0433\u043e\u0433"
                                                                     u"\u0438\u0439</p></body></html>",
                                                                     None))
        # endif // QT_CONFIG(tooltip)
        self.edit_folder_other.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.checkBox_program_2.setText(
            QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
        # if QT_CONFIG(tooltip)
        self.edit_folder_image.setToolTip(QCoreApplication.translate("MainWindow",
                                                                     u"<html><head/><body><p>\u0418\u043c\u044f "
                                                                     u"\u043f\u0430\u043f\u043a\u0438 \u0432 "
                                                                     u"\u043a\u043e\u0442\u043e\u0440\u0443\u044e "
                                                                     u"\u0431\u0443\u0434\u0443\u0442 "
                                                                     u"\u043f\u043e\u043c\u0435\u0449\u0435\u043d"
                                                                     u"\u044b "
                                                                     u"\u0444\u043e\u0442\u043e</p></body></html>",
                                                                     None))
        # endif // QT_CONFIG(tooltip)
        self.edit_folder_image.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Images", None))
        # if QT_CONFIG(tooltip)
        self.edit_folder_document.setToolTip(QCoreApplication.translate("MainWindow",
                                                                        u"<html><head/><body><p>\u0418\u043c\u044f "
                                                                        u"\u043f\u0430\u043f\u043a\u0438 \u0432 "
                                                                        u"\u043a\u043e\u0442\u043e\u0440\u0443\u044e "
                                                                        u"\u0431\u0443\u0434\u0443\u0442 "
                                                                        u"\u043f\u043e\u043c\u0435\u0449\u0435\u043d"
                                                                        u"\u044b "
                                                                        u"\u0434\u043e\u043a\u0443\u043c\u0435\u043d"
                                                                        u"\u0442\u044b</p></body></html>",
                                                                        None))
        # endif // QT_CONFIG(tooltip)
        self.edit_folder_document.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Document", None))
        # if QT_CONFIG(tooltip)
        self.edit_folder_program.setToolTip(QCoreApplication.translate("MainWindow",
                                                                       u"<html><head/><body><p>\u0418\u043c\u044f "
                                                                       u"\u043f\u0430\u043f\u043a\u0438 \u0432 "
                                                                       u"\u043a\u043e\u0442\u043e\u0440\u0443\u044e "
                                                                       u"\u0431\u0443\u0434\u0443\u0442 "
                                                                       u"\u043f\u043e\u043c\u0435\u0449\u0435\u043d"
                                                                       u"\u044b "
                                                                       u"\u043f\u0440\u043e\u0433\u0440\u0430\u043c"
                                                                       u"\u043c\u044b</p></body></html>",
                                                                       None))
        # endif // QT_CONFIG(tooltip)
        self.edit_folder_program.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Program", None))
        # if QT_CONFIG(tooltip)
        self.radioButton_1.setToolTip(QCoreApplication.translate("MainWindow",
                                                                 u"<html><head/><body><p>\u0412\u044b\u0431\u043e"
                                                                 u"\u0440\u043a\u0430 "
                                                                 u"\u0444\u0430\u0439\u043b\u043e\u0432 "
                                                                 u"\u0442\u043e\u043b\u044c\u043a\u043e \u0432 "
                                                                 u"\u043a\u043e\u0440\u043d\u0435 "
                                                                 u"\u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e"
                                                                 u"\u0433\u043e "
                                                                 u"\u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0430"
                                                                 u"</p></body></html>",
                                                                 None))
        # endif // QT_CONFIG(tooltip)
        self.radioButton_1.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u041f\u043e\u0438\u0441\u043a \u0432 "
                                                              u"\u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0435",
                                                              None))
        # if QT_CONFIG(tooltip)
        self.edit_folder_audio.setToolTip(QCoreApplication.translate("MainWindow",
                                                                     u"<html><head/><body><p>\u0418\u043c\u044f "
                                                                     u"\u043f\u0430\u043f\u043a\u0438 \u0432 "
                                                                     u"\u043a\u043e\u0442\u043e\u0440\u0443\u044e "
                                                                     u"\u0431\u0443\u0434\u0443\u0442 "
                                                                     u"\u043f\u043e\u043c\u0435\u0449\u0435\u043d"
                                                                     u"\u044b \u0430\u0443\u0434\u0438\u043e "
                                                                     u"\u0444\u0430\u0439\u043b\u044b</p></body></html>",
                                                                     None))
        # endif // QT_CONFIG(tooltip)
        self.edit_folder_audio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.checkBox_torrent_2.setText(
            QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0440\u0440\u0435\u043d\u0442\u044b", None))
        self.checkBox_other_2.setText(
            QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0447\u0438\u0435", None))
        self.checkBox_archive_2.setText(
            QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0445\u0438\u0432\u044b", None))
        # if QT_CONFIG(tooltip)
        self.edit_folder_torrent.setToolTip(QCoreApplication.translate("MainWindow",
                                                                       u"<html><head/><body><p>\u0418\u043c\u044f "
                                                                       u"\u043f\u0430\u043f\u043a\u0438 \u0432 "
                                                                       u"\u043a\u043e\u0442\u043e\u0440\u0443\u044e "
                                                                       u"\u0431\u0443\u0434\u0443\u0442 "
                                                                       u"\u043f\u043e\u043c\u0435\u0449\u0435\u043d"
                                                                       u"\u044b "
                                                                       u"\u0442\u043e\u0440\u0440\u0435\u043d\u0442 "
                                                                       u"\u0444\u0430\u0439\u043b\u044b</p></body"
                                                                       u"></html>",
                                                                       None))
        # endif // QT_CONFIG(tooltip)
        self.edit_folder_torrent.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Torrent", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_1), QCoreApplication.translate("MainWindow",
                                                                                               u"\u041f\u0430\u0440"
                                                                                               u"\u0430\u043c\u0435"
                                                                                               u"\u0442\u0440\u044b "
                                                                                               u"\u043f\u043e\u0438"
                                                                                               u"\u0441\u043a\u0430 "
                                                                                               u"\u0438 "
                                                                                               u"\u0441\u043e\u0440"
                                                                                               u"\u0442\u0438\u0440"
                                                                                               u"\u043e\u0432\u043a"
                                                                                               u"\u0438",
                                                                                               None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow",
                                                                                                 u"\u041f\u0430\u0440"
                                                                                                 u"\u0430\u043c\u0435"
                                                                                                 u"\u0442\u0440\u044b",
                                                                                                 None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi
