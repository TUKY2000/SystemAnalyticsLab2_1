# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\View\Main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(350, 200))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.InputTab = QtWidgets.QWidget()
        self.InputTab.setObjectName("InputTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.InputTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.toolBox = QtWidgets.QToolBox(self.InputTab)
        self.toolBox.setObjectName("toolBox")
        self.lssInBox = QtWidgets.QWidget()
        self.lssInBox.setGeometry(QtCore.QRect(0, 0, 306, 476))
        self.lssInBox.setObjectName("lssInBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.lssInBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Property1 = QtWidgets.QWidget(self.lssInBox)
        self.Property1.setObjectName("Property1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Property1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.Property1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.matrApushButton = QtWidgets.QPushButton(self.Property1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matrApushButton.sizePolicy().hasHeightForWidth())
        self.matrApushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.matrApushButton.setFont(font)
        self.matrApushButton.setStyleSheet("QPushButton{\n"
"    color: balck;\n"
"    background: transparent;\n"
"    max-height: 30px;\n"
"    max-width: 30px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    font: 24px \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:pressed{\n"
"    color: red;\n"
"    background: transparent;\n"
"    max-height: 30px;\n"
"    max-width: 30px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    font: 24px \"MS Shell Dlg 2\";\n"
"}")
        self.matrApushButton.setChecked(False)
        self.matrApushButton.setFlat(False)
        self.matrApushButton.setObjectName("matrApushButton")
        self.horizontalLayout_3.addWidget(self.matrApushButton)
        self.label_2 = QtWidgets.QLabel(self.Property1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.Property1)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: balck;\n"
"    background: transparent;\n"
"    max-height: 30px;\n"
"    max-width: 30px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    font: 24px \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:pressed{\n"
"    color: red;\n"
"    background: transparent;\n"
"    max-height: 30px;\n"
"    max-width: 30px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    font: 24px \"MS Shell Dlg 2\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(self.Property1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.Property1)
        self.Property1_2 = QtWidgets.QWidget(self.lssInBox)
        self.Property1_2.setObjectName("Property1_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Property1_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.Property1_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.matrApushButton_2 = QtWidgets.QPushButton(self.Property1_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matrApushButton_2.sizePolicy().hasHeightForWidth())
        self.matrApushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.matrApushButton_2.setFont(font)
        self.matrApushButton_2.setStyleSheet("QPushButton{\n"
"    color: balck;\n"
"    background: transparent;\n"
"    max-height: 30px;\n"
"    max-width: 30px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    font: 24px \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:pressed{\n"
"    color: red;\n"
"    background: transparent;\n"
"    max-height: 30px;\n"
"    max-width: 30px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    font: 24px \"MS Shell Dlg 2\";\n"
"}")
        self.matrApushButton_2.setChecked(False)
        self.matrApushButton_2.setFlat(False)
        self.matrApushButton_2.setObjectName("matrApushButton_2")
        self.horizontalLayout_4.addWidget(self.matrApushButton_2)
        self.label_5 = QtWidgets.QLabel(self.Property1_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.pushButton_2 = QtWidgets.QPushButton(self.Property1_2)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    color: balck;\n"
"    background: transparent;\n"
"    max-height: 30px;\n"
"    max-width: 30px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    font: 24px \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:pressed{\n"
"    color: red;\n"
"    background: transparent;\n"
"    max-height: 30px;\n"
"    max-width: 30px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    font: 24px \"MS Shell Dlg 2\";\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.label_6 = QtWidgets.QLabel(self.Property1_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.Property1_2)
        self.Property1_3 = QtWidgets.QWidget(self.lssInBox)
        self.Property1_3.setObjectName("Property1_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Property1_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.Property1_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.matrApushButton_3 = QtWidgets.QPushButton(self.Property1_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matrApushButton_3.sizePolicy().hasHeightForWidth())
        self.matrApushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.matrApushButton_3.setFont(font)
        self.matrApushButton_3.setStyleSheet("QPushButton{\n"
"    color: balck;\n"
"    background: transparent;\n"
"    max-height: 30px;\n"
"    max-width: 30px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    font: 24px \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:pressed{\n"
"    color: red;\n"
"    background: transparent;\n"
"    max-height: 30px;\n"
"    max-width: 30px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    font: 24px \"MS Shell Dlg 2\";\n"
"}")
        self.matrApushButton_3.setChecked(False)
        self.matrApushButton_3.setFlat(False)
        self.matrApushButton_3.setObjectName("matrApushButton_3")
        self.horizontalLayout_5.addWidget(self.matrApushButton_3)
        self.label_8 = QtWidgets.QLabel(self.Property1_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.pushButton_3 = QtWidgets.QPushButton(self.Property1_3)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    color: balck;\n"
"    background: transparent;\n"
"    max-height: 30px;\n"
"    max-width: 30px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    font: 24px \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:pressed{\n"
"    color: red;\n"
"    background: transparent;\n"
"    max-height: 30px;\n"
"    max-width: 30px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    font: 24px \"MS Shell Dlg 2\";\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.label_9 = QtWidgets.QLabel(self.Property1_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.Property1_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.toolBox.addItem(self.lssInBox, "")
        self.funcInBox = QtWidgets.QWidget()
        self.funcInBox.setGeometry(QtCore.QRect(0, 0, 306, 476))
        self.funcInBox.setObjectName("funcInBox")
        self.toolBox.addItem(self.funcInBox, "")
        self.verticalLayout_2.addWidget(self.toolBox)
        self.tabWidget.addTab(self.InputTab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.SeparatorLine = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SeparatorLine.sizePolicy().hasHeightForWidth())
        self.SeparatorLine.setSizePolicy(sizePolicy)
        self.SeparatorLine.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SeparatorLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SeparatorLine.setLineWidth(2)
        self.SeparatorLine.setMidLineWidth(2)
        self.SeparatorLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.SeparatorLine.setObjectName("SeparatorLine")
        self.horizontalLayout.addWidget(self.SeparatorLine)
        self.PlotWidgetMain = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlotWidgetMain.sizePolicy().hasHeightForWidth())
        self.PlotWidgetMain.setSizePolicy(sizePolicy)
        self.PlotWidgetMain.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.PlotWidgetMain.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PlotWidgetMain.setAutoFillBackground(True)
        self.PlotWidgetMain.setObjectName("PlotWidgetMain")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.PlotWidgetMain)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PlotWidgetButtons = QtWidgets.QWidget(self.PlotWidgetMain)
        self.PlotWidgetButtons.setMinimumSize(QtCore.QSize(462, 38))
        self.PlotWidgetButtons.setObjectName("PlotWidgetButtons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.PlotWidgetButtons)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addWidget(self.PlotWidgetButtons, 0, QtCore.Qt.AlignTop)
        self.PlotWidgetGraph = QtWidgets.QWidget(self.PlotWidgetMain)
        self.PlotWidgetGraph.setMinimumSize(QtCore.QSize(250, 400))
        self.PlotWidgetGraph.setMaximumSize(QtCore.QSize(16777215, 9999999))
        self.PlotWidgetGraph.setObjectName("PlotWidgetGraph")
        self.verticalLayout.addWidget(self.PlotWidgetGraph)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)
        self.horizontalLayout.addWidget(self.PlotWidgetMain)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "x\'(t) ="))
        self.matrApushButton.setText(_translate("MainWindow", "A"))
        self.label_2.setText(_translate("MainWindow", "(t)*x(t) + "))
        self.pushButton.setText(_translate("MainWindow", "B"))
        self.label_3.setText(_translate("MainWindow", "(t)*u(t)"))
        self.label_4.setText(_translate("MainWindow", "x\'(t) ="))
        self.matrApushButton_2.setText(_translate("MainWindow", "A"))
        self.label_5.setText(_translate("MainWindow", "(t)*x(t) + "))
        self.pushButton_2.setText(_translate("MainWindow", "B"))
        self.label_6.setText(_translate("MainWindow", "(t)*u(t)"))
        self.label_7.setText(_translate("MainWindow", "x\'(t) ="))
        self.matrApushButton_3.setText(_translate("MainWindow", "A"))
        self.label_8.setText(_translate("MainWindow", "(t)*x(t) + "))
        self.pushButton_3.setText(_translate("MainWindow", "B"))
        self.label_9.setText(_translate("MainWindow", "(t)*u(t)"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.lssInBox), _translate("MainWindow", "Linear Stationary System"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.funcInBox), _translate("MainWindow", "Functional"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.InputTab), _translate("MainWindow", "Input"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
