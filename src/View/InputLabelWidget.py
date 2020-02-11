from PyQt5 import QtCore, QtGui, QtWidgets

class InputLabelWidget(QtWidgets.QWidget):
    def __init__(self):
        # create Labels : as items in list
        self.labelList = []
        # create PushButtons : as items in list
        self.buttonsList = []
        # create layout
        self.layout = QtWidgets.QHBoxLayout()
        # customize labels
        # customize buttons

class LssInputLabel(InputLabelWidget):
    def __init__(self):
        # set label list
        self.labelList.append(QtWidgets.QLabel('x\'(t) = '))
        self.labelList.append(QtWidgets.QLabel('(t)*x(t) + '))
        self.labelList.append(QtWidgets.QLabel('(t)*u(t)'))

        # set button list
        self.buttonsList.append(QtWidgets.QPushButton('A'))
        self.buttonsList.append(QtWidgets.QPushButton('B'))

        # layout combining
        self.layout.addWidget(self.labelList[1])
        self.layout.addWidget(self.buttonList[1])
        self.layout.addWidget(self.labelList[2])
        self.layout.addWidget(self.buttonList[2])
        self.layout.addWidget(self.labelList[3])
        self.layout.addWidget(QtWidgets.QLayoutItem.QSpacerItem())
