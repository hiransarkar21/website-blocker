# imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
import os

# default application data location
WINDOWS_DEFAULT_LOCATION = os.path.join(os.environ.get("APPDATA"), "WebTrackerX")
LINUX_DEFAULT_LOCATION = ""


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # global variables
        self.master_font_x = QFont("Maven Pro", 13)
        self.master_font_x.setWordSpacing(1)
        self.master_font_x.setLetterSpacing(QFont.AbsoluteSpacing, 0.5)

        self.master_font = QFont("Maven Pro", 12)
        self.master_font.setWordSpacing(1)
        self.master_font.setLetterSpacing(QFont.AbsoluteSpacing, 0.5)

        self.available_window_width = QApplication.primaryScreen().availableGeometry().width()
        self.available_window_height = QApplication.primaryScreen().availableGeometry().height()

        # calling methods
        self.interface_configurations()
        self.user_interface()

    def interface_configurations(self):
        # setting a fixed size for the app
        self.setFixedSize(int(self.available_window_width / 2.2), int(self.available_window_height / 1.4))

    def user_interface(self):
        # layouts declaration
        self.master_layout = QVBoxLayout()
        self.header_layout = QHBoxLayout()
        self.header_layout.setAlignment(Qt.AlignTop)
        self.activate_webtracker_layout = QVBoxLayout()

        # widgets declaration
        self.application_name = QLabel()
        self.application_name.setText("WebTracker X")
        self.application_name.setFont(self.master_font_x)
        self.application_name.setStyleSheet("""QLabel{}""")

        self.master_interface_button = QPushButton()
        self.master_interface_button.setFont(self.master_font)
        self.master_interface_button.setText("interfaces")
        self.master_interface_button.setFlat(True)
        self.master_interface_button.setMaximumSize(int(self.master_interface_button.width() / 4),
                                                    int(self.master_interface_button.height() / 10))

        self.master_options_button = QPushButton()
        self.master_options_button.setFont(self.master_font)
        self.master_options_button.setText("options")
        self.master_options_button.setFlat(True)
        self.master_options_button.clicked.connect(self.master_options_button_clicked)
        self.master_options_button.setMaximumSize(int(self.master_options_button.width() / 4),
                                                  int(self.master_options_button.height() / 10))

        self.master_settings_button = QPushButton()
        self.master_settings_button.setFont(self.master_font)
        self.master_settings_button.setText("settings")
        self.master_settings_button.setFlat(True)
        self.master_settings_button.clicked.connect(self.master_settings_button_clicked)
        self.master_settings_button.setMaximumSize(int(self.master_settings_button.width() / 4),
                                                   int(self.master_settings_button.height() / 10))

        self.activate_webtracker_with_default_configs_label = QLabel()
        self.activate_webtracker_with_default_configs_label.setFont(self.master_font_x)
        self.activate_webtracker_with_default_configs_label.setText("Initialize Extension and start Track and Block Sequence")

        self.activate_webtracker_and_blocker_button = QPushButton()
        self.activate_webtracker_and_blocker_button.setFont(self.master_font_x)
        self.activate_webtracker_and_blocker_button.setText("Activate WebTracker")
        self.activate_webtracker_and_blocker_button.setFixedSize(int(self.width() / 3), int(self.width() / 3))
        self.activate_webtracker_and_blocker_button.setStyleSheet("""QPushButton{border: 2px solid ; border-radius: 145px;}""")

        self.load_default_session_button = QPushButton()
        self.load_default_session_button.setFont(self.master_font)
        self.load_default_session_button.setText("Load Default Session")
        self.load_default_session_button.setFlat(True)
        self.load_default_session_button.setMinimumSize(int(self.width() / 4), int(self.height() / 20))
        self.load_default_session_button.clicked.connect(self.load_default_session_button_clicked)
        self.load_default_session_button.setStyleSheet("""QPushButton{border-radius: 5px; background-color: #021c59; color: white;}""")

        self.load_custom_session_button = QPushButton()
        self.load_custom_session_button.setText("Load Custom Session")
        self.load_custom_session_button.setFont(self.master_font)
        self.load_custom_session_button.setFlat(True)
        self.load_custom_session_button.clicked.connect(self.load_custom_session_button_clicked)
        self.load_custom_session_button.setMinimumSize(int(self.width() / 4), int(self.height() / 20))
        self.load_custom_session_button.setStyleSheet("""QPushButton{border-radius: 5px; background-color: #021c59; color: white;}""")

        # adding widgets to layouts
        self.header_layout.addSpacing(40)
        self.header_layout.addWidget(self.application_name)
        self.header_layout.addWidget(self.master_interface_button)
        self.header_layout.addWidget(self.master_options_button)
        self.header_layout.addWidget(self.master_settings_button)
        self.header_layout.addSpacing(40)

        self.activate_webtracker_layout.addSpacing(40)
        self.activate_webtracker_layout.addWidget(self.activate_webtracker_with_default_configs_label, alignment=Qt.AlignHCenter | Qt.AlignTop)
        self.activate_webtracker_layout.addSpacing(40)
        self.activate_webtracker_layout.addWidget(self.activate_webtracker_and_blocker_button, alignment=Qt.AlignHCenter | Qt.AlignTop)
        self.activate_webtracker_layout.addSpacing(40)
        self.activate_webtracker_layout.addWidget(self.load_default_session_button, alignment=Qt.AlignHCenter | Qt.AlignTop)
        self.activate_webtracker_layout.addWidget(self.load_custom_session_button, alignment=Qt.AlignHCenter | Qt.AlignTop)

        # adding child layouts to parent layouts and setting the master layout as window layout
        self.master_layout.addLayout(self.header_layout)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.activate_webtracker_layout)
        self.master_layout.addStretch()
        self.setLayout(self.master_layout)

    def master_options_button_clicked(self):
        from interfaces import options_screen
        self.master_screen = options_screen.MainWindow()
        self.master_screen.show()
        self.close()

    def master_settings_button_clicked(self):
        from interfaces import settings_screen
        self.master_screen = settings_screen.MainWindow()
        self.master_screen.show()
        self.close()

    def load_default_session_button_clicked(self):
        pass

    def load_custom_session_button_clicked(self):
        from interfaces import options_screen
        self.master_screen = options_screen.MainWindow()
        self.master_screen.show()
        self.close()


def main():
    application = QApplication(sys.argv)
    interface = MainWindow()
    interface.show()
    application.exec_()
