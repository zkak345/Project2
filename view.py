# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 527)
        MainWindow.setMaximumSize(QtCore.QSize(550, 527))
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calculator_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.calculator_label.setGeometry(QtCore.QRect(210, 10, 151, 51))
        self.calculator_label.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.calculator_label.setFont(font)
        self.calculator_label.setObjectName("calculator_label")
        self.answer_text = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.answer_text.setGeometry(QtCore.QRect(70, 70, 421, 41))
        self.answer_text.setObjectName("answer_text")
        self.floored_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.floored_button.setGeometry(QtCore.QRect(400, 210, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.floored_button.setFont(font)
        self.floored_button.setObjectName("floored_button")
        self.divide_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.divide_button.setGeometry(QtCore.QRect(400, 260, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.divide_button.setFont(font)
        self.divide_button.setObjectName("divide_button")
        self.multiply_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.multiply_button.setGeometry(QtCore.QRect(400, 310, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.multiply_button.setFont(font)
        self.multiply_button.setObjectName("multiply_button")
        self.minus_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.minus_button.setGeometry(QtCore.QRect(400, 360, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.minus_button.setFont(font)
        self.minus_button.setObjectName("minus_button")
        self.plus_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.plus_button.setGeometry(QtCore.QRect(400, 410, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plus_button.setFont(font)
        self.plus_button.setObjectName("plus_button")
        self.equal_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.equal_button.setGeometry(QtCore.QRect(400, 460, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.equal_button.setFont(font)
        self.equal_button.setObjectName("equal_button")
        self.decimal_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.decimal_button.setGeometry(QtCore.QRect(290, 460, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.decimal_button.setFont(font)
        self.decimal_button.setObjectName("decimal_button")
        self.zero_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.zero_button.setGeometry(QtCore.QRect(180, 460, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.zero_button.setFont(font)
        self.zero_button.setObjectName("zero_button")
        self.negative_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.negative_button.setGeometry(QtCore.QRect(70, 460, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.negative_button.setFont(font)
        self.negative_button.setObjectName("negative_button")
        self.three_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.three_button.setGeometry(QtCore.QRect(290, 410, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.three_button.setFont(font)
        self.three_button.setObjectName("three_button")
        self.two_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.two_button.setGeometry(QtCore.QRect(180, 410, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.two_button.setFont(font)
        self.two_button.setObjectName("two_button")
        self.one_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.one_button.setGeometry(QtCore.QRect(70, 410, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.one_button.setFont(font)
        self.one_button.setObjectName("one_button")
        self.six_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.six_button.setGeometry(QtCore.QRect(290, 360, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.six_button.setFont(font)
        self.six_button.setObjectName("six_button")
        self.five_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.five_button.setGeometry(QtCore.QRect(180, 360, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.five_button.setFont(font)
        self.five_button.setObjectName("five_button")
        self.four_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.four_button.setGeometry(QtCore.QRect(70, 360, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.four_button.setFont(font)
        self.four_button.setObjectName("four_button")
        self.nine_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.nine_button.setGeometry(QtCore.QRect(290, 310, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nine_button.setFont(font)
        self.nine_button.setObjectName("nine_button")
        self.eight_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.eight_button.setGeometry(QtCore.QRect(180, 310, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.eight_button.setFont(font)
        self.eight_button.setObjectName("eight_button")
        self.seven_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.seven_button.setGeometry(QtCore.QRect(70, 310, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.seven_button.setFont(font)
        self.seven_button.setObjectName("seven_button")
        self.square_root_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.square_root_button.setGeometry(QtCore.QRect(290, 260, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.square_root_button.setFont(font)
        self.square_root_button.setObjectName("square_root_button")
        self.x_squared_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.x_squared_button.setGeometry(QtCore.QRect(180, 260, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.x_squared_button.setFont(font)
        self.x_squared_button.setObjectName("x_squared_button")
        self.one_over_x_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.one_over_x_button.setGeometry(QtCore.QRect(70, 260, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.one_over_x_button.setFont(font)
        self.one_over_x_button.setObjectName("one_over_x_button")
        self.modulo_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.modulo_button.setGeometry(QtCore.QRect(290, 210, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.modulo_button.setFont(font)
        self.modulo_button.setObjectName("modulo_button")
        self.cube_root_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cube_root_button.setGeometry(QtCore.QRect(180, 210, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cube_root_button.setFont(font)
        self.cube_root_button.setObjectName("cube_root_button")
        self.x_cubed_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.x_cubed_button.setGeometry(QtCore.QRect(70, 210, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.x_cubed_button.setFont(font)
        self.x_cubed_button.setObjectName("x_cubed_button")
        self.backspace_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.backspace_button.setGeometry(QtCore.QRect(400, 160, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.backspace_button.setFont(font)
        self.backspace_button.setObjectName("backspace_button")
        self.clear_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(290, 160, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        self.cos_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cos_button.setGeometry(QtCore.QRect(180, 160, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cos_button.setFont(font)
        self.cos_button.setObjectName("cos_button")
        self.sin_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sin_button.setGeometry(QtCore.QRect(70, 160, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sin_button.setFont(font)
        self.sin_button.setObjectName("sin_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calculator_label.setText(_translate("MainWindow", "Calculator"))
        self.answer_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.floored_button.setText(_translate("MainWindow", "//"))
        self.divide_button.setText(_translate("MainWindow", "÷"))
        self.multiply_button.setText(_translate("MainWindow", "×"))
        self.minus_button.setText(_translate("MainWindow", "−"))
        self.plus_button.setText(_translate("MainWindow", "+"))
        self.equal_button.setText(_translate("MainWindow", "="))
        self.decimal_button.setText(_translate("MainWindow", "."))
        self.zero_button.setText(_translate("MainWindow", "0"))
        self.negative_button.setText(_translate("MainWindow", "±"))
        self.three_button.setText(_translate("MainWindow", "3"))
        self.two_button.setText(_translate("MainWindow", "2"))
        self.one_button.setText(_translate("MainWindow", "1"))
        self.six_button.setText(_translate("MainWindow", "6"))
        self.five_button.setText(_translate("MainWindow", "5"))
        self.four_button.setText(_translate("MainWindow", "4"))
        self.nine_button.setText(_translate("MainWindow", "9"))
        self.eight_button.setText(_translate("MainWindow", "8"))
        self.seven_button.setText(_translate("MainWindow", "7"))
        self.square_root_button.setText(_translate("MainWindow", "√"))
        self.x_squared_button.setText(_translate("MainWindow", "x²"))
        self.one_over_x_button.setText(_translate("MainWindow", "1 / x"))
        self.modulo_button.setText(_translate("MainWindow", "mod"))
        self.cube_root_button.setText(_translate("MainWindow", "∛"))
        self.x_cubed_button.setText(_translate("MainWindow", "x³"))
        self.backspace_button.setText(_translate("MainWindow", "⌫"))
        self.clear_button.setText(_translate("MainWindow", "C"))
        self.cos_button.setText(_translate("MainWindow", "cos"))
        self.sin_button.setText(_translate("MainWindow", "sin"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
