import sys
from random import choice
from datetime import datetime
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QHBoxLayout, QGridLayout, QGroupBox,
    QPushButton, QLabel, QCheckBox,
    QSpinBox, QTextEdit
)

__version__ = 'version: 1.0'


class PWDGenerator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.bn_generate.clicked.connect(self.all_pwds_generate)
        self.bn_clear.clicked.connect(self.te_clear)
        self.bn_save.clicked.connect(self.pwds_save)

    def initUI(self):
        # Settings for main window
        self.setWindowTitle(f'PWDGen {str(__version__)}')
        self.setWindowIcon(QIcon('icon.ico'))
        self.setGeometry(100, 100, 420, 600)
        self.setMinimumSize(420, 600)
        self.setMaximumSize(420, 600)

        # Main Layout is vertical
        main_vbox = QVBoxLayout()
        self.setLayout(main_vbox)

        # GroupBox
        gb_layout = QGridLayout()
        self.gb_settings = QGroupBox('Настройки генерации пароля: ')
        self.gb_settings.setLayout(gb_layout)
        gb_layout.setSpacing(10)

        self.lb_pwd_len = QLabel('Длина пароля: ')
        self.sb_pwd_len = QSpinBox()
        self.sb_pwd_len.setRange(5, 25)

        # check boxes
        self.cb_lower_letters = QCheckBox('Использовать строчные буквы')
        self.cb_lower_letters.setChecked(True)
        self.cb_upper_letters = QCheckBox('Использовать прописные буквы')
        self.cb_digits = QCheckBox('Использовать цифры')
        self.cb_syms = QCheckBox('Использовать доп. символы')
        self.cb_dict = {
            self.cb_lower_letters: ascii_lowercase,
            self.cb_upper_letters: ascii_uppercase,
            self.cb_digits: digits,
            self.cb_syms: punctuation
        }

        self.lb_pwd_count = QLabel('Количество паролей')
        self.sb_pwd_count = QSpinBox()
        self.sb_pwd_count.setRange(1, 100)

        gb_layout.addWidget(self.lb_pwd_len, 0, 1)
        gb_layout.addWidget(self.sb_pwd_len, 0, 2)
        gb_layout.addWidget(self.cb_lower_letters, 1, 1)
        gb_layout.addWidget(self.cb_upper_letters, 1, 2)
        gb_layout.addWidget(self.cb_digits, 2, 1)
        gb_layout.addWidget(self.cb_syms, 2, 2)
        gb_layout.addWidget(self.lb_pwd_count, 3, 1)
        gb_layout.addWidget(self.sb_pwd_count, 3, 2)
        main_vbox.addWidget(self.gb_settings)

        # Text editor for passwords
        self.te_pwds = QTextEdit()
        self.te_pwds.setReadOnly(True)

        main_vbox.addWidget(self.te_pwds)

        # Status lbl
        self.lb_status = QLabel('')
        main_vbox.addWidget(self.lb_status)

        # Layout for buttons
        bn_layout = QHBoxLayout()
        main_vbox.addLayout(bn_layout)
        self.bn_generate = QPushButton('Генерировать')
        self.bn_clear = QPushButton('Очистить')
        self.bn_save = QPushButton('Сохранить')
        bn_layout.addWidget(self.bn_generate)
        bn_layout.addWidget(self.bn_clear)
        bn_layout.addWidget(self.bn_save)

    def get_syms(self):
        symbols = ''
        for k, v in self.cb_dict.items():
            if k.isChecked():
                symbols += v
        return symbols

    def pwd_generate(self):
        symbols = self.get_syms()
        password = ''
        if symbols:
            for i in range(self.sb_pwd_len.value()):
                sym = choice(symbols)
                password += sym
            self.lb_status.setStyleSheet("QLabel { color : black; }")
            self.lb_status.setText(f'Сгенерировано {self.sb_pwd_count.value()} парол(ь, я, ей)')
        else:
            self.lb_status.setStyleSheet("QLabel { color : red; }")
            self.lb_status.setText('Нет символов для генерации...')
        return password

    def all_pwds_generate(self):
        self.te_pwds.clear()
        count = self.sb_pwd_count.value()
        if count == 1:
            result = self.pwd_generate()
            self.te_pwds.append(result)
            return

        for i in range(1, count + 1):
            result = self.pwd_generate()
            self.te_pwds.append(result)

    def te_clear(self):
        self.te_pwds.clear()

    def pwds_save(self):
        if self.te_pwds.toPlainText():
            filename = datetime.now().strftime('%m_%d_%Y-%H_%M_%S')
            with open(f'{filename}.pwd', 'w', encoding='utf-8') as f:
                f.write(self.te_pwds.toPlainText())
        self.te_pwds.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = PWDGenerator()
    wnd.show()
    sys.exit(app.exec_())
