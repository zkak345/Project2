from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    Num = ''
    Num2 = ''
    Sign = ''
    Total = 0
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.clear_button.clicked.connect(lambda: self.clear())
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
        self.plus_button.clicked.connect(lambda: self.plus())
        self.minus_button.clicked.connect(lambda: self.minus())
        self.multiply_button.clicked.connect(lambda: self.multiply())
        self.divide_button.clicked.connect(lambda: self.divide())
        self.floored_button.clicked.connect(lambda: self.floored())
        self.modulo_button.clicked.connect(lambda: self.modulo())

    def one(self):
        if len(Controller.Num) >= 1 and Controller.Sign == '':
            Controller.Num += '1'
            self.answer_text.setText(f'{Controller.Num}')
        elif Controller.Num == '':
            Controller.Num = '1'
            self.answer_text.setText(f'{Controller.Num}')
        else:
            if len(Controller.Num2) >= 1:
                Controller.Num2 += '1'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')
            else:
                Controller.Num2 = '1'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def two(self):
        if len(Controller.Num) >= 1 and Controller.Sign == '':
            Controller.Num += '2'
            self.answer_text.setText(f'{Controller.Num}')
        elif Controller.Num == '':
            Controller.Num = '2'
            self.answer_text.setText(f'{Controller.Num}')
        else:
            if len(Controller.Num2) >= 1:
                Controller.Num2 += '2'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')
            else:
                Controller.Num2 = '2'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')


    def three(self):
        if len(Controller.Num) >= 1 and Controller.Sign == '':
            Controller.Num += '3'
            self.answer_text.setText(f'{Controller.Num}')
        elif Controller.Num == '':
            Controller.Num = '3'
            self.answer_text.setText(f'{Controller.Num}')
        else:
            if len(Controller.Num2) >= 1:
                Controller.Num2 += '3'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')
            else:
                Controller.Num2 = '3'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def four(self):
        if len(Controller.Num) >= 1 and Controller.Sign == '':
            Controller.Num += '4'
            self.answer_text.setText(f'{Controller.Num}')
        elif Controller.Num == '':
            Controller.Num = '4'
            self.answer_text.setText(f'{Controller.Num}')
        else:
            if len(Controller.Num2) >= 1:
                Controller.Num2 += '4'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')
            else:
                Controller.Num2 = '4'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def five(self):
        if len(Controller.Num) >= 1 and Controller.Sign == '':
            Controller.Num += '5'
            self.answer_text.setText(f'{Controller.Num}')
        elif Controller.Num == '':
            Controller.Num = '5'
            self.answer_text.setText(f'{Controller.Num}')
        else:
            if len(Controller.Num2) >= 1:
                Controller.Num2 += '5'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')
            else:
                Controller.Num2 = '5'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def six(self):
        if len(Controller.Num) >= 1 and Controller.Sign == '':
            Controller.Num += '6'
            self.answer_text.setText(f'{Controller.Num}')
        elif Controller.Num == '':
            Controller.Num = '6'
            self.answer_text.setText(f'{Controller.Num}')
        else:
            if len(Controller.Num2) >= 1:
                Controller.Num2 += '6'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')
            else:
                Controller.Num2 = '6'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def seven(self):
        if len(Controller.Num) >= 1 and Controller.Sign == '':
            Controller.Num += '7'
            self.answer_text.setText(f'{Controller.Num}')
        elif Controller.Num == '':
            Controller.Num = '7'
            self.answer_text.setText(f'{Controller.Num}')
        else:
            if len(Controller.Num2) >= 1:
                Controller.Num2 += '7'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')
            else:
                Controller.Num2 = '7'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def eight(self):
        if len(Controller.Num) >= 1 and Controller.Sign == '':
            Controller.Num += '8'
            self.answer_text.setText(f'{Controller.Num}')
        elif Controller.Num == '':
            Controller.Num = '8'
            self.answer_text.setText(f'{Controller.Num}')
        else:
            if len(Controller.Num2) >= 1:
                Controller.Num2 += '8'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')
            else:
                Controller.Num2 = '8'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def nine(self):
        if len(Controller.Num) >= 1 and Controller.Sign == '':
            Controller.Num += '9'
            self.answer_text.setText(f'{Controller.Num}')
        elif Controller.Num == '':
            Controller.Num = '9'
            self.answer_text.setText(f'{Controller.Num}')
        else:
            if len(Controller.Num2) >= 1:
                Controller.Num2 += '9'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')
            else:
                Controller.Num2 = '9'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def zero(self):
        if Controller.Num == 0:
            Controller.Num = 0
            self.answer_text.setText(f'{Controller.Num}')
        else:
            Controller.Num2 = 0
            self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')





    def plus(self):
        if Controller.Total == 0:
            Controller.Sign = '+'
            self.answer_text.setText(f'{Controller.Num} +')
        else:
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'{Controller.Num} +')

    def minus(self):
        if Controller.Total == 0:
            Controller.Sign = '-'
            self.answer_text.setText(f'{Controller.Num} -')
        else:
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'{Controller.Num} -')


    def multiply(self):
        if Controller.Total == 0:
            Controller.Sign = 'x'
            self.answer_text.setText(f'{Controller.Num} x')
        else:
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'{Controller.Num} x')

    def divide(self):
        if Controller.Total == 0:
            Controller.Sign = '/'
            self.answer_text.setText(f'{Controller.Num} /')
        else:
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'{Controller.Num} /')

    def floored(self):
        if Controller.Total == 0:
            Controller.Sign = '//'
            self.answer_text.setText(f'{Controller.Num} //')
        else:
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'{Controller.Num} //')

    def modulo(self):
        if Controller.Total == 0:
            Controller.Sign = '%'
            self.answer_text.setText(f'{Controller.Num} %')
        else:
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'{Controller.Num} %')






    def total(self):
        if Controller.Sign == '+':
            Controller.Total = int(Controller.Num) + int(Controller.Num2)
        elif Controller.Sign == '-':
            Controller.Total = int(Controller.Num) - int(Controller.Num2)
        elif Controller.Sign == 'x':
            Controller.Total = int(Controller.Num) * int(Controller.Num2)
        elif Controller.Sign == '/':
            Controller.Total = int(Controller.Num) / int(Controller.Num2)
        elif Controller.Sign == '//':
            Controller.Total = int(Controller.Num) // int(Controller.Num2)
        elif Controller.Sign == '%':
            Controller.Total = int(Controller.Num) % int(Controller.Num2)
        self.answer_text.setText(f'{Controller.Total}')
        Controller.Num2 = ''

    def clear(self):
        self.answer_text.setText('')
        Controller.Num = ''
        Controller.Num2 = ''
        Controller.Sign = ''
        Controller.Total = 0






