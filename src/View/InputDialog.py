from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class InputDialog(QtWidgets.QDialog):
    def __init__(self):
        super(InputDialog, self).__init__()


        # combine layouts
        layoutUpper = self.__initLayoutUpper()
        layoutMain = self.__initLayoutMain()
        layoutLower = self.__initLayoutLower()

        Layout = QtWidgets.QVBoxLayout()
        Layout.addItem(layoutUpper)
        Layout.addItem(layoutMain)
        Layout.addItem(layoutLower)

        self.setLayout(Layout)


    def __initLayoutUpper(self):
        _rankLabel = QtWidgets.QLabel('Rank')
        _separatorLabel = QtWidgets.QLabel('X')
        
        _inLine1 = QtWidgets.QLineEdit()
        _inLine1.setStyleSheet('max-width: 30px')
        _inLine2 = QtWidgets.QLineEdit()
        _inLine2.setStyleSheet('max-width: 30px')
        
        layout = QtWidgets.QHBoxLayout()
        layout.addItem(QtWidgets.QSpacerItem(20, 40
        , QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        layout.addWidget(_rankLabel)
        layout.addWidget(_inLine1)
        layout.addWidget(_separatorLabel)
        layout.addWidget(_inLine2)

        return layout
    
    def __initLayoutMain(self):
        equationLabel = QtWidgets.QLabel('A = ')
        inputMatrixTable = QtWidgets.QTableWidget()

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(equationLabel)
        layout.addWidget(inputMatrixTable)

        return layout

    def __initLayoutLower(self):
        dialogButtonAccept = QtWidgets.QPushButton('Accept')
        dialogButtonCancel = QtWidgets.QPushButton('Cancel')

        layout = QtWidgets.QHBoxLayout()
        layout.addItem(QtWidgets.QSpacerItem(20, 40
        , QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        layout.addWidget(dialogButtonAccept)
        layout.addWidget(dialogButtonCancel)

        return layout


app = QtWidgets.QApplication([])

w = InputDialog()
w.show()

sys.exit(app.exec_())
