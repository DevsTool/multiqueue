# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiqueueapp.ui',
# licensing of 'multiqueueapp.ui' applies.
#
# Created: Tue Oct  1 11:55:20 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1009, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setLineWidth(-1)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.urgent = QtWidgets.QListWidget(self.centralwidget)
        self.urgent.setAcceptDrops(False)
        self.urgent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.urgent.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.urgent.setTabKeyNavigation(True)
        self.urgent.setDragEnabled(True)
        self.urgent.setDragDropOverwriteMode(True)
        self.urgent.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.urgent.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.urgent.setAlternatingRowColors(True)
        self.urgent.setWordWrap(True)
        self.urgent.setObjectName("urgent")
        self.verticalLayout_5.addWidget(self.urgent)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.priority = QtWidgets.QListWidget(self.centralwidget)
        self.priority.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.priority.setTabKeyNavigation(True)
        self.priority.setDragEnabled(True)
        self.priority.setDragDropOverwriteMode(True)
        self.priority.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.priority.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.priority.setWordWrap(True)
        self.priority.setObjectName("priority")
        self.verticalLayout_6.addWidget(self.priority)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.dueDate = QtWidgets.QListWidget(self.centralwidget)
        self.dueDate.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.dueDate.setTabKeyNavigation(True)
        self.dueDate.setDragEnabled(True)
        self.dueDate.setDragDropOverwriteMode(True)
        self.dueDate.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.dueDate.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.dueDate.setWordWrap(True)
        self.dueDate.setObjectName("dueDate")
        self.verticalLayout_7.addWidget(self.dueDate)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(100, 27))
        self.label_2.setMaximumSize(QtCore.QSize(150, 150))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(100, 27))
        self.comboBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMinimumDate(QtCore.QDate(1753, 10, 18))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_3.addWidget(self.dateEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.AddBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AddBtn.setObjectName("AddBtn")
        self.verticalLayout_4.addWidget(self.AddBtn)
        self.closeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeBtn.setObjectName("closeBtn")
        self.verticalLayout_4.addWidget(self.closeBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionAbout_Program = QtWidgets.QAction(MainWindow)
        self.actionAbout_Program.setCheckable(False)
        self.actionAbout_Program.setObjectName("actionAbout_Program")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuHelp.addAction(self.actionAbout_Program)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.closeBtn, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("editingFinished()"), self.lineEdit.copy)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Urgent", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Priority", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "Due Date", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Add task", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Priority List", None, -1))
        self.comboBox.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "HighPriority", None, -1))
        self.comboBox.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Priority", None, -1))
        self.comboBox.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "ByDate", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Due date", None, -1))
        self.dateEdit.setDisplayFormat(QtWidgets.QApplication.translate("MainWindow", "M/d/yyyy", None, -1))
        self.AddBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Add", None, -1))
        self.closeBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Close", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.menuEdit.setTitle(QtWidgets.QApplication.translate("MainWindow", "Edit", None, -1))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.actionOpen.setText(QtWidgets.QApplication.translate("MainWindow", "Open", None, -1))
        self.actionSave.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))
        self.actionCopy.setText(QtWidgets.QApplication.translate("MainWindow", "Copy", None, -1))
        self.actionCut.setText(QtWidgets.QApplication.translate("MainWindow", "Cut", None, -1))
        self.actionPaste.setText(QtWidgets.QApplication.translate("MainWindow", "Paste", None, -1))
        self.actionAbout_Program.setText(QtWidgets.QApplication.translate("MainWindow", "About Program", None, -1))

