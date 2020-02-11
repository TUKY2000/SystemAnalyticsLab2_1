from PyQt5 import QtCore, QtGui, QtWidgets

class InputLabelWidget(QtWidgets.QWidget):
    def __init__(self):
        super(InputLabelWidget, self).__init__()

        # create Labels : as items in list
        self.labelList = []
        # create PushButtons : as items in list
        self.buttonsList = []

    def cusomizeWidget(self, filePath, widgets : list):
        '''
        set stylesheet for qt widgets 
        '''
        with open(filePath, 'r') as file:
            style = file.read()
            for item in widgets:
                item.setStyleSheet(style)


class LssInputLabel(InputLabelWidget):
    def __init__(self):
        super(LssInputLabel, self).__init__()

        # set label list
        self.labelList.append(QtWidgets.QLabel('x\'(t) = '))
        self.labelList.append(QtWidgets.QLabel('(t)*x(t) + '))
        self.labelList.append(QtWidgets.QLabel('(t)*u(t)'))

        # set button list
        self.buttonsList.append(QtWidgets.QPushButton('A'))
        self.buttonsList.append(QtWidgets.QPushButton('B'))
        self.cusomizeWidget('src\View\StyleSheets\InputButtons.css', self.buttonsList)

        # layout combining
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.labelList[0])
        layout.addWidget(self.buttonsList[0])
        layout.addWidget(self.labelList[1])
        layout.addWidget(self.buttonsList[1])
        layout.addWidget(self.labelList[2])
        layout.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.setLayout(layout)