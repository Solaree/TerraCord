from Packets.Client.sraki import *; from Packets.Client.change_status import *; from Packets.Client.send_message import *; from Packets.Client.dm_message import *; from Packets.Client.file_upload import *; from Packets.Client.online import *; from Packets.Client.reactions import *;  
from Packets.Server.get_dm import *; from Packets.Server.send_message import *; from Packets.Server.get_channels import *; from Packets.Server.get_message import *; from Packets.Server.get_servers import *; from Packets.Server.join_server import *; from Packets.Server.leave_server import *;

from PyQt5 import QtGui, QtCore, QtWidgets; import sys
from PyQt5.QtWidgets import *; from PyQt5.QtCore import *; from PyQt5.QtGui import *


layout = QVBoxLayout()

FONT = "Helvetica [Cronyx]"
def generate_style(min_width):
    return """
        QPushButton {
        background-color: #FAFFC2;
        border-style: outset;
        border-width: 3px;
        border-radius: 10px;
        border-color: black;
        font: helvetica 0px;
        min-width: """ + min_width + """;
        padding: 6px;
        }
        QPushButton:pressed {
            background-color: #f7fae6;
            border-style: outset;
        }
        """

def buttons(self):
    button_1 = QPushButton("Info!") #help_page
    button_1.setFixedSize(QtCore.QSize(125, 70))
    button_1.setStyleSheet(generate_style("6em"))
    button_1.setFont(QFont(FONT, 15))
    button_1.clicked.connect(self.update_1)
    layout.addWidget(button_1)

    button_2 = QPushButton("Utils!") #client functions
    button_2.setFixedSize(QtCore.QSize(190, 70))
    button_2.setStyleSheet(generate_style("11em"))
    button_2.setFont(QFont(FONT, 15))
    button_2.clicked.connect(self.update_2)
    layout.addWidget(button_2)

    button_3 = QPushButton("Options!") #theme_changer
    button_3.setFixedSize(QtCore.QSize(250, 70))
    button_3.setStyleSheet(generate_style("16em"))
    button_3.setFont(QFont(FONT, 15))
    button_3.clicked.connect(self.update_3)
    layout.addWidget(button_3)

    button_1.clicked.connect(button_1.deleteLater)
    button_2.clicked.connect(button_1.deleteLater)
    button_3.clicked.connect(button_1.deleteLater)
    button_1.clicked.connect(button_2.deleteLater)
    button_2.clicked.connect(button_2.deleteLater)
    button_3.clicked.connect(button_2.deleteLater)
    button_1.clicked.connect(button_3.deleteLater)
    button_2.clicked.connect(button_3.deleteLater)
    button_3.clicked.connect(button_3.deleteLater)


class Window(QLabel):
    def __init__(self):
        super().__init__()
        global label
        self.label = QLabel(self)

        self.resize(1366, 768)
        self.setWindowTitle("Lemncord")
        self.setWindowIcon(QtGui.QIcon('GUI/Images/logo.png'))
        self.label.setStyleSheet('background-color: #FAFFC2;')
        self.label.resize(1980, 1080)
        self.pixmap = QPixmap('GUI/Images/image.png')
        self.label.setPixmap(self.pixmap)
        self.setLayout(layout)

        #widget
        self.widget = QLabel('Lemncord v0.9.0 [BETA]', self)
        self.widget.setStyleSheet("color: black;")
        self.widget.setFont(QFont(FONT, 15))
        self.widget.move(200, 75)
        layout.addWidget(self.widget)

        #buttons
        buttons(self)

    def update_1(self): #help page
        self.widget.setText("""Lemncord v0.9.0 made by notterra#9339, GUI by SolarSCRE#0156\n

Offical repo: https://github.com/terrawolf34/LemnCord""")

    def update_2(self): #client functions
        button_1 = QPushButton("Client login")
        button_1.setFixedSize(QtCore.QSize(300, 70))
        button_1.setStyleSheet(generate_style("16em"))
        button_1.setFont(QFont(FONT, 15))
        button_1.clicked.connect(self.token_input)
        layout.addWidget(button_1)

        button_2 = QPushButton("Send Message")
        button_2.setFixedSize(QtCore.QSize(350, 70))
        button_2.setStyleSheet(generate_style("16em"))
        button_2.setFont(QFont(FONT, 15))
        button_2.clicked.connect(self.update)
        layout.addWidget(button_2)

        button_3 = QPushButton("Upload File")
        button_3.setFixedSize(QtCore.QSize(400, 70))
        button_3.setStyleSheet(generate_style("16em"))
        button_3.setFont(QFont(FONT, 15))
        button_3.clicked.connect(self.update)
        layout.addWidget(button_3)

        button_1.clicked.connect(button_1.deleteLater)
        button_2.clicked.connect(button_1.deleteLater)
        button_3.clicked.connect(button_1.deleteLater)
        button_1.clicked.connect(button_2.deleteLater)
        button_2.clicked.connect(button_2.deleteLater)
        button_3.clicked.connect(button_2.deleteLater)
        button_1.clicked.connect(button_3.deleteLater)
        button_2.clicked.connect(button_3.deleteLater)
        button_3.clicked.connect(button_3.deleteLater)

    def token_input(self):
        self.widget.setText('Token:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.widget.move(20, 20)

        button = QPushButton('OK', self)
        button.clicked.connect(self.client_login)
        button.clicked.connect(button.deleteLater)
        button.resize(200,32)
        button.move(80, 60)
        layout.addWidget(button)
        layout.addWidget(self.line)

    def client_login(self):
        pass

    def update_3(self): #white theme call
        button = QPushButton("Change theme")
        button.setFixedSize(QtCore.QSize(250, 70))
        button.setStyleSheet(generate_style("16em"))
        button.setFont(QFont(FONT, 15))
        self.label.setStyleSheet('background-color: #FAFFC2;')
        self.label.resize(1980, 1080)
        self.widget.setStyleSheet("color: black;")
        button.clicked.connect(self.update_4) #black theme call
        button.clicked.connect(button.deleteLater)
        layout.addWidget(button)

    def update_4(self): #black_theme_call
        button = QPushButton("Change theme")
        button.setFixedSize(QtCore.QSize(250, 70))
        button.setStyleSheet(generate_style("16em"))
        button.setFont(QFont(FONT, 15))
        self.label.setStyleSheet('background-color: #36393F;')
        self.label.resize(1980, 1080)
        self.widget.setStyleSheet("color: white;")
        button.clicked.connect(self.update_3) #white theme call
        button.clicked.connect(button.deleteLater)
        layout.addWidget(button)