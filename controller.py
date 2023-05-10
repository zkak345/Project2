from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    Num = 0
    Num2 = 0
    Sign = ''
    Total = 0
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.clear_button.clicked.connect(lambda: self.clear())
        self.plus_button.clicked.connect(lambda: self.plus())
        self.one_button.clicked.connect(lambda: self.one())
        self.two_button.clicked.connect(lambda: self.two())
        self.three_button.clicked.connect(lambda: self.three())
        self.four_button.clicked.connect(lambda: self.four())
        self.five_button.clicked.connect(lambda: self.five())
        self.six_button.clicked.connect(lambda: self.six())
        self.seven_button.clicked.connect(lambda: self.seven())
        self.eight_button.clicked.connect(lambda: self.eight())
        self.nine_button.clicked.connect(lambda: self.nine())
        self.zero_button.clicked.connect(lambda: self.zero())
        self.equal_button.clicked.connect(lambda: self.total())

    def one(self):
        if Controller.Num == 0:
            Controller.Num = 1
            self.answer_text.setText(f'{Controller.Num}')
        else:
            Controller.Num2 = 1
            self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def two(self):
        if Controller.Num == 0:
            Controller.Num = 2
            self.answer_text.setText(f'{Controller.Num}')
        else:
            Controller.Num2 = 2
            self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')


    def three(self):
        if Controller.Num == 0:
            Controller.Num = 3
            self.answer_text.setText(f'{Controller.Num}')
        else:
            Controller.Num2 = 3
            self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def four(self):
        if Controller.Num == 0:
            Controller.Num = 4
            self.answer_text.setText(f'{Controller.Num}')
        else:
            Controller.Num2 = 4
            self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def five(self):
        if Controller.Num == 0:
            Controller.Num = 5
            self.answer_text.setText(f'{Controller.Num}')
        else:
            Controller.Num2 = 5
            self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def six(self):
        if Controller.Num == 0:
            Controller.Num = 6
            self.answer_text.setText(f'{Controller.Num}')
        else:
            Controller.Num2 = 6
            self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def seven(self):
        if Controller.Num == 0:
            Controller.Num = 7
            self.answer_text.setText(f'{Controller.Num}')
        else:
            Controller.Num2 = 7
            self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def eight(self):
        if Controller.Num == 0:
            Controller.Num = 8
            self.answer_text.setText(f'{Controller.Num}')
        else:
            Controller.Num2 = 8
            self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def nine(self):
        if Controller.Num == 0:
            Controller.Num = 9
            self.answer_text.setText(f'{Controller.Num}')
        else:
            Controller.Num2 = 9
            self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def zero(self):
        if Controller.Num == 0:
            Controller.Num = 0
            self.answer_text.setText(f'{Controller.Num}')
        else:
            Controller.Num2 = 0
            self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')





    def plus(self):
        Controller.Sign = '+'
        self.answer_text.setText(f'{Controller.Num} +')

    def total(self):
        if Controller.Sign == '+':
            Controller.Total = Controller.Num + Controller.Num2
            total = Controller.Total
            self.answer_text.setText(f'{Controller.Total}')




    def equal(self):
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
        self.answer_text.setText('')
        Controller.Num = 0
        Controller.Num2 = 0
        Controller.Sign = ''
        Controller.Total = 0






