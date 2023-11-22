from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

import sys
import subprocess
import platform

system = platform.system()
if system == 'OpenBSD':
    fortune = '/usr/games/fortune'
else:
    fortune = 'fortune'

def get_fortune():
    process = subprocess.Popen([fortune] + sys.argv[1:], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    return output.decode()

def start_window():
    app = QApplication(sys.argv)

    mainwidget = QWidget()
    mainwidget.setWindowTitle("fortune")

    layout = QVBoxLayout()
    mainwidget.setLayout(layout)

    label = QLabel(get_fortune())
    label.setAlignment(Qt.AlignCenter)
    def set_fortune():
        label.setText(get_fortune())

    button = QPushButton("Get Fortune")
    button.clicked.connect(set_fortune)

    layout.addWidget(label)
    layout.addWidget(button)

    mainwidget.show()
    app.exec()

start_window()
