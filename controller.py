from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.submit_button.clicked.connect(lambda: self.submit())
        self.clear_button.clicked.connect(lambda: self.clear())

    def submit(self):
        for i in range(1):
            try:
                num1 = int(self.firtnumber_text())
                num2 = int(self.secondnumber_text())
                equation = str(self.equationtype_text())
                total = 0
                if equation == '+':
                    total = num1 + num2
                elif equation == '-':
                    total = num1 - num2
                elif equation == 'x':
                    total = num1 * num2
                elif equation == '/':
                    total = num1 / num2
                elif equation == '//':
                    total = num1 / num2
                elif equation == '^':
                    total = num1 ** num2
                elif equation == '%':
                    total = num1 % num2
                else:
                    break
            except ValueError:
                self.clear()
                break
            except ZeroDivisionError:
                self.answer_text.setText('Cannot divide by zero')
            self.answer_text.setText(total)

    def clear(self):
        self.firtnumber_text.setText('')
        self.secondnumber_text.setText('')
        self.answer_text.setText('')
        self.equationtype_text.setText('')







