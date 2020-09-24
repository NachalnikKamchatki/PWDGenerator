import sys

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

    def initUI(self):
        # Settings for main window
        self.setWindowTitle(f'PWDGen {str(__version__)}')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(100, 100, 420, 480)
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
        self.cb_lower_letters = QCheckBox('Использовать строчные буквы')
        self.cb_upper_letters = QCheckBox('Использовать прописные буквы')
        self.cb_digits = QCheckBox('Использовать цифры')
        self.cb_syms = QCheckBox('Использовать доп. символы')
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
        main_vbox.addWidget(self.te_pwds)

        # Layout for buttons
        bn_layout = QHBoxLayout()
        main_vbox.addLayout(bn_layout)
        self.bn_generate = QPushButton('Генерировать')
        self.bn_clear = QPushButton('Очистить')
        self.bn_save = QPushButton('Сохранить')
        bn_layout.addWidget(self.bn_generate)
        bn_layout.addWidget(self.bn_clear)
        bn_layout.addWidget(self.bn_save)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = PWDGenerator()
    wnd.show()
    sys.exit(app.exec_())
