from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
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

        self.https_prefix = "https://www."
        self.http_prefix = "http://www."

        self.default_session_file = os.path.join(WINDOWS_DEFAULT_LOCATION, "default_session_blacklisted_websites.txt")

        # triggering methods
        self.interface_configurations()
        self.user_interface()
        self.load_default_blacklisted_websites()

    def interface_configurations(self):
        # the window configurations will be inherited by this window from the parent window ( master_interface )
        self.setFixedSize(int(self.available_window_width / 2.2), int(self.available_window_height / 1.4))

    def user_interface(self):
        # layouts declaration
        self.master_layout = QVBoxLayout()
        self.header_layout = QHBoxLayout()
        self.master_body_layout = QVBoxLayout()
        self.master_body_layout.setContentsMargins(20, 10, 20, 10)
        self.container_with_options_layout = QHBoxLayout()
        self.container_options_layout = QVBoxLayout()
        self.add_and_update_entry_options_layout = QHBoxLayout()

        # widgets declaration
        self.application_name = QLabel()
        self.application_name.setText("WebTracker X")
        self.application_name.setFont(self.master_font_x)
        self.application_name.setStyleSheet("""QLabel{}""")

        self.master_interface_button = QPushButton()
        self.master_interface_button.setFont(self.master_font)
        self.master_interface_button.setText("interfaces")
        self.master_interface_button.setFlat(True)
        self.master_interface_button.clicked.connect(self.master_interface_button_clicked)
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
        self.master_settings_button.setMaximumSize(int(self.master_settings_button.width() / 4),
                                                   int(self.master_settings_button.height() / 10))

        self.default_blacklisted_websites_label = QLabel()
        self.default_blacklisted_websites_label.setFont(self.master_font_x)
        self.default_blacklisted_websites_label.setText(" Default Blacklisted Websites and Webpages")

        self.default_blacklisted_websites_container = QListWidget()
        self.default_blacklisted_websites_container.setFont(self.master_font)
        self.default_blacklisted_websites_container.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.default_blacklisted_websites_container.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.default_blacklisted_websites_container.setMinimumSize(int(self.width() / 1.5), int(self.height() / 3.5))
        self.default_blacklisted_websites_container.setStyleSheet("""QListWidget{padding-left: 5px; padding-right: 5px;}""")

        self.delete_entry_from_container = QPushButton()
        self.delete_entry_from_container.setFont(self.master_font)
        self.delete_entry_from_container.setText("Discard")
        self.delete_entry_from_container.clicked.connect(self.delete_entry_from_container_button_clicked)
        self.delete_entry_from_container.setFixedSize(int(self.width() / 5.5), int(self.height() / 22))
        self.delete_entry_from_container.setStyleSheet("""QPushButton{border-radius: 3px; background-color: #021c59;
                color: white;}""")

        self.update_entry_from_container = QPushButton()
        self.update_entry_from_container.setFont(self.master_font)
        self.update_entry_from_container.setText("Update")
        self.update_entry_from_container.clicked.connect(self.update_entry_from_container_button_clicked)
        self.update_entry_from_container.setFixedSize(int(self.width() / 5.5), int(self.height() / 22))
        self.update_entry_from_container.setStyleSheet("""QPushButton{border-radius: 3px; background-color: #021c59;
                color: white;}""")

        self.clear_entries_from_container = QPushButton()
        self.clear_entries_from_container.setFont(self.master_font)
        self.clear_entries_from_container.setText("Clear All")
        self.clear_entries_from_container.clicked.connect(lambda : self.default_blacklisted_websites_container.clear())
        self.clear_entries_from_container.setFixedSize(int(self.width() / 5.5), int(self.height() / 22))
        self.clear_entries_from_container.setStyleSheet("""QPushButton{border-radius: 3px; background-color: #021c59; 
                color: white;}""")

        self.save_entries_button = QPushButton()
        self.save_entries_button.setFont(self.master_font)
        self.save_entries_button.setText("Save Entries")
        self.save_entries_button.clicked.connect(self.save_entries_button_clicked)
        self.save_entries_button.setFixedSize(int(self.width() / 5.5), int(self.height() / 22))
        self.save_entries_button.setStyleSheet("""QPushButton{border-radius: 3px; background-color: #021c59;
                color: white;}""")

        self.add_or_update_entry_label = QLabel()
        self.add_or_update_entry_label.setFont(self.master_font_x)
        self.add_or_update_entry_label.setText("Add or Update Entries to container")

        self.get_new_entry = QLineEdit()
        self.get_new_entry.setFont(self.master_font)
        self.get_new_entry.setFixedSize(int(self.width() / 2.5), int(self.height() / 22))
        self.get_new_entry.setStyleSheet("""QLineEdit{border: 1px solid #828790; border-radius: 2px; padding-right: 10px;
                padding-left: 10px;}""")

        self.add_entry_button = QPushButton()
        self.add_entry_button.setFont(self.master_font)
        self.add_entry_button.setText("Add Website")
        self.add_entry_button.clicked.connect(self.add_entry_button_clicked)
        self.add_entry_button.setFixedSize(int(self.width() / 6), int(self.height() / 22))
        self.add_entry_button.setStyleSheet("""QPushButton{border-radius: 3px; background-color: #021c59; 
                color: white;}""")

        self.update_entry_button = QPushButton()
        self.update_entry_button.setText("Update")
        self.update_entry_button.setFont(self.master_font)
        self.update_entry_button.clicked.connect(self.update_entry_button_clicked)
        self.update_entry_button.setFixedSize(int(self.width() / 6), int(self.height() / 22))
        self.update_entry_button.setStyleSheet("""QPushButton{border-radius: 3px; background-color: #021c59; 
                color: white;}""")

        self.additional_settings_label = QLabel()
        self.additional_settings_label.setFont(self.master_font)
        self.additional_settings_label.setText("Additional Configurations and Documentations")

        self.advanced_configurations_button = QPushButton()
        self.advanced_configurations_button.setFont(self.master_font)
        self.advanced_configurations_button.setText("Advanced Configurations")
        self.advanced_configurations_button.setFixedSize(int(self.width() / 3.2), int(self.height() / 18))
        self.advanced_configurations_button.setStyleSheet("""QPushButton{border-radius: 5px; background-color: #021c59;
         color: white;}""")

        self.documentation_button = QPushButton()
        self.documentation_button.setFont(self.master_font)
        self.documentation_button.setText("Developers Notes")
        self.documentation_button.setFixedSize(int(self.width() / 3.2), int(self.height() / 18))
        self.documentation_button.setStyleSheet("""QPushButton{border-radius: 5px; background-color: #021c59;
        color: white;}""")

        # adding widgets to layouts
        self.header_layout.addSpacing(40)
        self.header_layout.addWidget(self.application_name)
        self.header_layout.addWidget(self.master_interface_button)
        self.header_layout.addWidget(self.master_options_button)
        self.header_layout.addWidget(self.master_settings_button)
        self.header_layout.addSpacing(40)

        self.container_options_layout.addWidget(self.update_entry_from_container)
        self.container_options_layout.addWidget(self.delete_entry_from_container)
        self.container_options_layout.addWidget(self.clear_entries_from_container)
        self.container_options_layout.addWidget(self.save_entries_button)
        self.container_options_layout.addStretch()

        self.container_with_options_layout.addWidget(self.default_blacklisted_websites_container)
        self.container_with_options_layout.addSpacing(5)
        self.container_with_options_layout.addLayout(self.container_options_layout)
        self.container_with_options_layout.addStretch()

        self.add_and_update_entry_options_layout.addWidget(self.get_new_entry)
        self.add_and_update_entry_options_layout.addWidget(self.add_entry_button)
        self.add_and_update_entry_options_layout.addWidget(self.update_entry_button)
        self.add_and_update_entry_options_layout.addStretch()

        self.master_body_layout.addWidget(self.default_blacklisted_websites_label)
        self.master_body_layout.addSpacing(30)
        self.master_body_layout.addLayout(self.container_with_options_layout)
        self.master_body_layout.addSpacing(30)
        self.master_body_layout.addWidget(self.add_or_update_entry_label)
        self.master_body_layout.addSpacing(20)
        self.master_body_layout.addLayout(self.add_and_update_entry_options_layout)
        self.master_body_layout.addSpacing(30)
        self.master_body_layout.addWidget(self.additional_settings_label)
        self.master_body_layout.addSpacing(20)
        self.master_body_layout.addWidget(self.documentation_button)
        self.master_body_layout.addWidget(self.advanced_configurations_button)

        # adding child layouts to parent layouts and setting the master layout as window layout
        self.master_layout.addLayout(self.header_layout)
        self.master_layout.addSpacing(60)
        self.master_layout.addLayout(self.master_body_layout)
        self.master_layout.addStretch()
        self.setLayout(self.master_layout)

    def load_default_blacklisted_websites(self):
        # loading custom session blacklisted websites from custom_session_blacklisted_websites.txt

        try:
            with open(self.default_session_file, "r") as custom_file:
                lines_from_file = custom_file.readlines()
                for entry in lines_from_file:
                    self.default_blacklisted_websites_container.addItem(entry.strip("\n"))

        except FileNotFoundError:
            pass

    def master_interface_button_clicked(self):
        from interfaces import master_interface
        self.master_screen = master_interface.MainWindow()
        self.master_screen.show()
        self.close()

    def master_options_button_clicked(self):
        from interfaces import options_screen
        self.master_screen = options_screen.MainWindow()
        self.master_screen.show()
        self.close()

    def delete_entry_from_container_button_clicked(self):
        self.current_item = self.default_blacklisted_websites_container.currentItem()
        self.default_blacklisted_websites_container.takeItem(self.default_blacklisted_websites_container.row(self.current_item))

    def add_entry_button_clicked(self):
        self.new_entry = self.get_new_entry.text()

        if not self.new_entry.startswith(self.https_prefix):
            if not self.new_entry.startswith(self.http_prefix):
                # deny entry to container, invalid url or half url
                pass
            else:
                self.default_blacklisted_websites_container.addItem(self.new_entry)
                self.get_new_entry.clear()
        else:
            self.default_blacklisted_websites_container.addItem(self.new_entry)
            self.get_new_entry.clear()

    def update_entry_from_container_button_clicked(self):
        self.current_item_text = self.default_blacklisted_websites_container.currentItem().text()
        self.get_new_entry.setText(self.current_item_text)

    def update_entry_button_clicked(self):
        # updating entry at fixed row
        self.new_entry = self.get_new_entry.text()
        self.current_item = self.default_blacklisted_websites_container.currentRow()
        self.default_blacklisted_websites_container.insertItem(self.current_item, self.new_entry)

        # deleting unwanted / duplicate entry and clearing get_new_entry after updating entry
        self.default_blacklisted_websites_container.takeItem(self.current_item + 1)
        self.get_new_entry.clear()

    def save_entries_button_clicked(self):
        # storing all the active items to the variable all_entries_from_container
        self.all_entries_from_container = []

        for i in range(self.default_blacklisted_websites_container.count()):
            self.all_entries_from_container.append(self.default_blacklisted_websites_container.item(i).text())

        # writing the entries into custom_session_file location in APPDATA/WebTrackerX/
        with open(self.default_session_file, "w+") as default_session_file:
            for entry in self.all_entries_from_container:
                default_session_file.write(entry.__add__("\n"))

