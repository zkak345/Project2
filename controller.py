from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.calculate_button.clicked.connect(lambda: self.submit())
        self.clear_button.clicked.connect(lambda: self.clear())

    def submit(self):
        for i in range(1):
            try:
                num1 = int(self.firtnumber_text.text())
                num2 = int(self.secondnumber_text.text())
                equation = str(self.equationtype_text.text())
                total = 0
                if equation == '+':
                    total = num1 + num2
                    self.answer_text.setText(str(total))
                elif equation == '-':
                    total = num1 - num2
                    self.answer_text.setText(str(total))
                elif equation == 'x':
                    total = num1 * num2
                    self.answer_text.setText(str(total))
                elif equation == '/':
                    total = num1 / num2
                    self.answer_text.setText(f'{total:.2f}')
                elif equation == '//':
                    total = num1 / num2
                    self.answer_text.setText(f'{total:.2f}')
                elif equation == '^':
                    total = num1 ** num2
                    self.answer_text.setText(str(total))
                elif equation == '%':
                    total = num1 % num2
                    self.answer_text.setText(str(total))
                else:
                    self.textBrowser.setText('Please use a proper equation')
                    break
            except ValueError:
                self.textBrowser.setText('Please use a proper input')
                break
            except ZeroDivisionError:
                self.textBrowser.setText('Cannot divide by zero')

    def clear(self):
        self.firtnumber_text.setText('')
        self.secondnumber_text.setText('')
        self.answer_text.setText('')
        self.equationtype_text.setText('')
        self.textBrowser.setText('Equation Type must use a symbol: Addition (+), Subtraction (-), Multiplication (x), Division (/), Floored Division (//), Modulo Division (%), exponential (^)')







