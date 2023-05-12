from PyQt5.QtWidgets import *
from view import *
from math import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    """

    A Class representing the whole functionality of the code

    """

    Num = ''
    Num2 = ''
    Sign = ''
    Total = 0

    def __init__(self, *args, **kwargs):
        """
        A constructor to create the initial state of the buttons on the calculator and when they are clicked

        """
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
        self.x_squared_button.clicked.connect(lambda: self.square())
        self.x_cubed_button.clicked.connect(lambda: self.cube())
        self.square_root_button.clicked.connect(lambda: self.root())
        self.cube_root_button.clicked.connect(lambda: self.cuberoot())
        self.sin_button.clicked.connect(lambda: self.sine())
        self.cos_button.clicked.connect(lambda: self.cosine())
        self.backspace_button.clicked.connect(lambda: self.backspace())
        self.decimal_button.clicked.connect(lambda: self.decimal())
        self.negative_button.clicked.connect(lambda: self.negative())
        self.one_over_x_button.clicked.connect(lambda: self.one_over())

    def one(self):
        """
        Functionality for number 1
        :return: returns the number one on the calculator and accounts if 1 was used as two or three digits

        """
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
        """
        Functionality for number 2
        :return: returns the number 2 on the calculator and accounts if 2 was used as two or three digits

        """
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
        """
        Functionality for Number 3
        :return: returns the number 3 on the calculator and accounts if 3 was used as two or three digits
        """
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
        """
        Functionality for Number 4
        :return: returns the number 4 on the calculator and accounts if 4 was used as two or three digits
        """
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
        """
        Functionality for Number 5
        :return: returns the number 5 on the calculator and accounts if 5 was used as two or three digits
        """
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
        """
        Functionality for Number 6
        :return: returns the number 6 on the calculator and accounts if 6 was used as two or three digits
        """
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
        """
        Functionality for Number 7
        :return: returns the number 7 on the calculator and accounts if 7 was used as two or three digits
        """
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
        """
        Functionality for Number 8
        :return: returns the number 8 on the calculator and accounts if 8 was used as two or three digits
        """
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
        """
        Functionality for Number 9
        :return: returns the number 9 on the calculator and accounts if 9 was used as two or three digits
        """
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
        """
        Functionality for 0
        :return: returns the number 0 on the calculator and accounts if 0 was used as two or three digits
        """
        if len(Controller.Num) >= 1 and Controller.Sign == '':
            Controller.Num += '0'
            self.answer_text.setText(f'{Controller.Num}')
        elif Controller.Num == '':
            Controller.Num = '0'
            self.answer_text.setText(f'{Controller.Num}')
        else:
            if len(Controller.Num2) >= 1:
                Controller.Num2 += '0'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')
            else:
                Controller.Num2 = '0'
                self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def plus(self):
        """
        Functionality for + sign
        :return: Specifies to use a plus sign and account for addition after finding a total
        """
        if Controller.Total == 0:
            Controller.Sign = '+'
            self.answer_text.setText(f'{Controller.Num} +')
        else:
            Controller.Sign = '+'
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'{Controller.Num} +')

    def minus(self):
        """
        Functionality for - sign
        :return: Specifies to use a minus sign and account for subtraction after finding a total
        """
        if Controller.Total == 0:
            Controller.Sign = '-'
            self.answer_text.setText(f'{Controller.Num} -')
        else:
            Controller.Sign = '-'
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'{Controller.Num} -')

    def multiply(self):
        """
        Functionality for x sign
        :return: Specifies to use a multiplication sign and account for multiplication after finding a total
        """
        if Controller.Total == 0:
            Controller.Sign = 'x'
            self.answer_text.setText(f'{Controller.Num} x')
        else:
            Controller.Sign = 'x'
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'{Controller.Num} x')

    def divide(self):
        """
        Functionality for / sign
        :return: Specifies to use a division sign and account for division after finding a total
        """
        if Controller.Total == 0:
            Controller.Sign = '/'
            self.answer_text.setText(f'{Controller.Num} /')
        else:
            Controller.Sign = '/'
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'{Controller.Num} /')

    def floored(self):
        """
        Functionality for //
        :return: Specifies to use a floored division sign and account for division after finding a total
        """
        if Controller.Total == 0:
            Controller.Sign = '//'
            self.answer_text.setText(f'{Controller.Num} //')
        else:
            Controller.Sign = '//'
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'{Controller.Num} //')

    def modulo(self):
        """
        Functionality for %
        """
        if Controller.Total == 0:
            Controller.Sign = '%'
            self.answer_text.setText(f'{Controller.Num} %')
        else:
            Controller.Sign = '%'
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'{Controller.Num} %')

    def square(self):
        """
        Functionaltiy for square function
        :return: squared number
        """
        if Controller.Total == 0:
            Controller.Sign = '^2'
            self.answer_text.setText(f'{Controller.Num} ^2')
        else:
            Controller.Sign = '^2'
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'{Controller.Num} ^2')

    def cube(self):
        """
        functionality for cube function
        """
        if Controller.Total == 0:
            Controller.Sign = '^3'
            self.answer_text.setText(f'{Controller.Num} ^3')
        else:
            Controller.Sign = '^3'
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'{Controller.Num} ^3')

    def root(self):
        """
        Functionality for root
        """
        if Controller.Total == 0:
            Controller.Sign = 'r'
            self.answer_text.setText(f'{Controller.Num} r')
        else:
            Controller.Sign = 'r'
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'{Controller.Num} r')

    def cuberoot(self):
        """
        Functionality for cube root
        """
        if Controller.Total == 0:
            Controller.Sign = 'c'
            self.answer_text.setText(f'{Controller.Num} c')
        else:
            Controller.Sign = 'c'
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'{Controller.Num} c')

    def sine(self):
        """

        :return: sin functionality
        """
        if Controller.Total == 0:
            Controller.Sign = 'sin'
            self.answer_text.setText(f'sin({Controller.Num})')
        else:
            Controller.Sign = 'sin'
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'sin({Controller.Num})')

    def cosine(self):
        """

        :return: cosine functionality
        """
        if Controller.Total == 0:
            Controller.Sign = 'cosine'
            self.answer_text.setText(f'cos({Controller.Num})')
        else:
            Controller.Sign = 'cosine'
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'cos({Controller.Num})')

    def backspace(self):
        """

        :return: Backspace functionality
        """
        if Controller.Sign == '':
            Controller.Num = Controller.Num[:-1]
            self.answer_text.setText(f'{Controller.Num}')
        else:
            Controller.Num2 = Controller.Num2[:-1]
            self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def one_over(self):
        """

        :return: 1/ function
        """
        if Controller.Total == 0:
            Controller.Sign = '1/'
            self.answer_text.setText(f'1/{Controller.Num}')
        else:
            Controller.Sign = '1/'
            Controller.Num = str(Controller.Total)
            self.answer_text.setText(f'1/{Controller.Num}')

    def decimal(self):
        """

        :return: Accounting for decimal
        """
        if Controller.Sign == '':
            Controller.Num += '.'
            self.answer_text.setText(f'{Controller.Num}')
        else:
            Controller.Num2 += '.'
            self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def negative(self):
        """

        :return: Accounting for negative numbers
        """
        if Controller.Sign == '':
            Controller.Num += '-'
            self.answer_text.setText(f'{Controller.Num}')
        else:
            Controller.Num2 += '-'
            self.answer_text.setText(f'{Controller.Num} {Controller.Sign} {Controller.Num2}')

    def total(self):
        """
        Functionality to determine what sign is being used and compute the total
        :return: The Total
        """
        try:
            if Controller.Sign == '+':
                Controller.Total = float(Controller.Num) + float(Controller.Num2)
            elif Controller.Sign == '-':
                Controller.Total = float(Controller.Num) - float(Controller.Num2)
            elif Controller.Sign == 'x':
                Controller.Total = float(Controller.Num) * float(Controller.Num2)
            elif Controller.Sign == '/':
                Controller.Total = float(Controller.Num) / float(Controller.Num2)
            elif Controller.Sign == '//':
                Controller.Total = float(Controller.Num) // float(Controller.Num2)
            elif Controller.Sign == '%':
                Controller.Total = float(Controller.Num) % float(Controller.Num2)
            elif Controller.Sign == '^2':
                Controller.Total = float(Controller.Num) ** 2
            elif Controller.Sign == '^3':
                Controller.Total = float(Controller.Num) ** 3
            elif Controller.Sign == 'r':
                Controller.Total = sqrt(float(Controller.Num))
            elif Controller.Sign == 'c':
                Controller.Total = float(Controller.Num) ** (1/3)
            elif Controller.Sign == 'sin':
                Controller.Total = sin(float(Controller.Num))
            elif Controller.Sign == 'cosine':
                Controller.Total = cos(float(Controller.Num))
            elif Controller.Sign == '1/':
                Controller.Total = 1 / float(Controller.Num)
            self.answer_text.setText(f'{Controller.Total}')
            Controller.Num2 = ''
            Controller.Sign = 'new'
        except ZeroDivisionError:
            self.answer_text.setText(f'Error cannot divide by zero')

    def clear(self):
        self.answer_text.setText('')
        Controller.Num = ''
        Controller.Num2 = ''
        Controller.Sign = ''
        Controller.Total = 0
