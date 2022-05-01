import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import datetime
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

        self.custom_session_file = os.path.join(WINDOWS_DEFAULT_LOCATION, "custom_session_blacklisted_websites.txt")

        # triggering methods
        self.interface_configurations()
        self.user_interface()
        self.load_custom_session_entries()

    def interface_configurations(self):
        # the window configurations will be inherited by this window from the parent window ( master_interface )
        self.setFixedSize(int(self.available_window_width / 2.2), int(self.available_window_height / 1.4))

    def user_interface(self):
        # layouts declaration
        self.master_layout = QVBoxLayout()
        self.header_layout = QHBoxLayout()
        self.master_body_container_layout = QVBoxLayout()
        self.master_body_container_layout.setContentsMargins(20, 10, 20, 10)
        self.container_with_options_layout = QHBoxLayout()
        self.blacklisted_website_container_layout = QVBoxLayout()
        self.container_options_layout = QVBoxLayout()
        self.add_and_update_entry_options_layout = QHBoxLayout()
        self.schedule_session_layout = QVBoxLayout()
        self.session_start_time_layout = QHBoxLayout()
        self.session_end_time_layout = QHBoxLayout()

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
        self.master_options_button.setMaximumSize(int(self.master_options_button.width() / 4),
                                                  int(self.master_options_button.height() / 10))

        self.master_settings_button = QPushButton()
        self.master_settings_button.setFont(self.master_font)
        self.master_settings_button.setText("settings")
        self.master_settings_button.setFlat(True)
        self.master_settings_button.clicked.connect(self.master_settings_button_clicked)
        self.master_settings_button.setMaximumSize(int(self.master_settings_button.width() / 4),
                                                   int(self.master_settings_button.height() / 10))

        self.blacklisted_website_label = QLabel()
        self.blacklisted_website_label.setText("Blacklisted Websites to be Tracked and Stopped")
        self.blacklisted_website_label.setFont(self.master_font_x)

        self.blacklisted_website_container = QListWidget()
        self.blacklisted_website_container.setFont(self.master_font)
        self.blacklisted_website_container.setFixedSize(int(self.width() / 1.5), int(self.height() / 3.5))
        self.blacklisted_website_container.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.blacklisted_website_container.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.blacklisted_website_container.setStyleSheet("""QListWidget{padding-left: 5px; padding-right: 5px;}""")

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
        self.clear_entries_from_container.clicked.connect(lambda : self.blacklisted_website_container.clear())
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
        self.add_or_update_entry_label.setText("Add or Update Entries to Blacklisted container")

        self.get_new_entry = QLineEdit()
        self.get_new_entry.setFont(self.master_font)
        self.get_new_entry.setFixedSize(int(self.width() / 2.1), int(self.height() / 20))
        self.get_new_entry.setStyleSheet("""QLineEdit{border: 1px solid #828790; border-radius: 2px; padding-right: 10px;
        padding-left: 10px;}""")

        self.add_entry_button = QPushButton()
        self.add_entry_button.setFont(self.master_font)
        self.add_entry_button.setText("Add Website")
        self.add_entry_button.clicked.connect(self.add_entry_button_clicked)
        self.add_entry_button.setFixedSize(int(self.width() / 5), int(self.height() / 22))
        self.add_entry_button.setStyleSheet("""QPushButton{border-radius: 3px; background-color: #021c59; 
        color: white;}""")

        self.update_entry_button = QPushButton()
        self.update_entry_button.setText("Update")
        self.update_entry_button.setFont(self.master_font)
        self.update_entry_button.clicked.connect(self.update_entry_button_clicked)
        self.update_entry_button.setFixedSize(int(self.width() / 5), int(self.height() / 22))
        self.update_entry_button.setStyleSheet("""QPushButton{border-radius: 3px; background-color: #021c59; 
        color: white;}""")

        self.schedule_session_label = QLabel()
        self.schedule_session_label.setFont(self.master_font_x)
        self.schedule_session_label.setText("Schedule Custom Session")

        self.start_time_label = QLabel()
        self.start_time_label.setFont(self.master_font)
        self.start_time_label.setText("Start Time : ")

        self.get_custom_session_start_time = QLineEdit()
        self.get_custom_session_start_time.setFont(self.master_font)
        self.get_custom_session_start_time.setFixedSize(int(self.width() / 5), int(self.height() / 22))
        self.get_custom_session_start_time.setStyleSheet("""QLineEdit{border: 1px solid #828790; border-radius: 2px;
         padding-right: 10px; padding-left: 10px;}""")

        self.get_local_time_button = QPushButton()
        self.get_local_time_button.setFont(self.master_font)
        self.get_local_time_button.setText("Local Time")
        self.get_local_time_button.clicked.connect(self.fetch_local_time_and_modify_lineedit_field)
        self.get_local_time_button.setFixedSize(int(self.width() / 7), int(self.height() / 22))
        self.get_local_time_button.setStyleSheet("""QPushButton{border-radius: 3px; background-color: #021c59; 
        color: white;}""")

        self.end_time_label = QLabel()
        self.end_time_label.setFont(self.master_font)
        self.end_time_label.setText("  End Time : ")

        self.get_custom_session_end_time = QLineEdit()
        self.get_custom_session_end_time.setFont(self.master_font)
        self.get_custom_session_end_time.setFixedSize(int(self.width() / 5), int(self.height() / 22))
        self.get_custom_session_end_time.setStyleSheet("""QLineEdit{border: 1px solid #828790; border-radius: 2px;
         padding-right: 10px;padding-left: 10px;}""")

        self.next_thirty_minutes = QPushButton()
        self.next_thirty_minutes.setFont(self.master_font)
        self.next_thirty_minutes.setText("+30 mins")
        self.next_thirty_minutes.clicked.connect(self.next_thirty_minutes_clicked)
        self.next_thirty_minutes.setFixedSize(int(self.width() / 8), int(self.height() / 22))
        self.next_thirty_minutes.setStyleSheet("""QPushButton{border-radius: 3px; background-color: #021c59; 
        color: white;}""")

        self.next_forty_five_minutes = QPushButton()
        self.next_forty_five_minutes.setFont(self.master_font)
        self.next_forty_five_minutes.setText("+45 mins")
        self.next_forty_five_minutes.clicked.connect(self.next_forty_five_minutes_clicked)
        self.next_forty_five_minutes.setFixedSize(int(self.width() / 8), int(self.height() / 22))
        self.next_forty_five_minutes.setStyleSheet("""QPushButton{border-radius: 3px; background-color: #021c59; 
        color: white;}""")

        self.next_sixty_minutes = QPushButton()
        self.next_sixty_minutes.setFont(self.master_font)
        self.next_sixty_minutes.setText("+60 mins")
        self.next_sixty_minutes.clicked.connect(self.next_sixty_minutes_clicked)
        self.next_sixty_minutes.setFixedSize(int(self.width() / 8), int(self.height() / 22))
        self.next_sixty_minutes.setStyleSheet("""QPushButton{border-radius: 3px; background-color: #021c59; 
        color: white;}""")

        # adding widgets to layouts
        self.header_layout.addSpacing(40)
        self.header_layout.addWidget(self.application_name)
        self.header_layout.addWidget(self.master_interface_button)
        self.header_layout.addWidget(self.master_options_button)
        self.header_layout.addWidget(self.master_settings_button)
        self.header_layout.addSpacing(40)

        self.blacklisted_website_container_layout.addWidget(self.blacklisted_website_container)

        self.container_options_layout.addWidget(self.update_entry_from_container)
        self.container_options_layout.addWidget(self.delete_entry_from_container)
        self.container_options_layout.addWidget(self.clear_entries_from_container)
        self.container_options_layout.addWidget(self.save_entries_button)
        self.container_options_layout.addStretch()

        self.container_with_options_layout.addWidget(self.blacklisted_website_container)
        self.container_with_options_layout.addSpacing(5)
        self.container_with_options_layout.addLayout(self.container_options_layout)
        self.container_with_options_layout.addStretch()

        self.add_and_update_entry_options_layout.addWidget(self.add_entry_button)
        self.add_and_update_entry_options_layout.addWidget(self.update_entry_button)
        self.add_and_update_entry_options_layout.addStretch()

        self.session_start_time_layout.addWidget(self.start_time_label)
        self.session_start_time_layout.addWidget(self.get_custom_session_start_time)
        self.session_start_time_layout.addWidget(self.get_local_time_button)
        self.session_start_time_layout.addStretch()

        self.session_end_time_layout.addWidget(self.end_time_label)
        self.session_end_time_layout.addWidget(self.get_custom_session_end_time)
        self.session_end_time_layout.addWidget(self.next_thirty_minutes)
        self.session_end_time_layout.addWidget(self.next_forty_five_minutes)
        self.session_end_time_layout.addWidget(self.next_sixty_minutes)
        self.session_end_time_layout.addStretch()

        self.schedule_session_layout.addWidget(self.schedule_session_label)
        self.schedule_session_layout.addSpacing(15)
        self.schedule_session_layout.addLayout(self.session_start_time_layout)
        self.schedule_session_layout.addLayout(self.session_end_time_layout)

        self.master_body_container_layout.addWidget(self.blacklisted_website_label)
        self.master_body_container_layout.addSpacing(20)
        self.master_body_container_layout.addLayout(self.container_with_options_layout)
        self.master_body_container_layout.addSpacing(20)
        self.master_body_container_layout.addWidget(self.add_or_update_entry_label)
        self.master_body_container_layout.addSpacing(20)
        self.master_body_container_layout.addWidget(self.get_new_entry)
        self.master_body_container_layout.addSpacing(5)
        self.master_body_container_layout.addLayout(self.add_and_update_entry_options_layout)
        self.master_body_container_layout.addSpacing(25)
        self.master_body_container_layout.addLayout(self.schedule_session_layout)

        # adding child layouts to parent layouts and setting the master layout as window layout
        self.master_layout.addLayout(self.header_layout)
        self.master_layout.addSpacing(60)
        self.master_layout.addLayout(self.master_body_container_layout)
        self.master_layout.addStretch()
        self.setLayout(self.master_layout)

    def load_custom_session_entries(self):
        # loading custom session blacklisted websites from custom_session_blacklisted_websites.txt

        # with open(self.custom_session_file, "r") as custom_file:
        #     lines_from_file = custom_file.readlines()
        #     for entry in lines_from_file:
        #         self.blacklisted_website_container.addItem(entry.strip("\n"))

        pass

    def master_interface_button_clicked(self):
        from interfaces import master_interface
        self.master_screen = master_interface.MainWindow()
        self.master_screen.show()
        self.close()

    def master_settings_button_clicked(self):
        from interfaces import settings_screen
        self.master_screen = settings_screen.MainWindow()
        self.master_screen.show()
        self.close()

    def add_entry_button_clicked(self):
        self.new_entry = self.get_new_entry.text()

        if not self.new_entry.startswith(self.https_prefix):
            if not self.new_entry.startswith(self.http_prefix):
                # deny entry to container, invalid url or half url
                pass
            else:
                self.blacklisted_website_container.addItem(self.new_entry)
                self.get_new_entry.clear()
        else:
            self.blacklisted_website_container.addItem(self.new_entry)
            self.get_new_entry.clear()

    def update_entry_from_container_button_clicked(self):
        self.current_item_text = self.blacklisted_website_container.currentItem().text()
        self.get_new_entry.setText(self.current_item_text)

    def update_entry_button_clicked(self):
        # updating entry at fixed row
        self.new_entry = self.get_new_entry.text()
        self.current_item = self.blacklisted_website_container.currentRow()
        self.blacklisted_website_container.insertItem(self.current_item, self.new_entry)

        # deleting unwanted / duplicate entry and clearing get_new_entry after updating entry
        self.blacklisted_website_container.takeItem(self.current_item + 1)
        self.get_new_entry.clear()

    def fetch_local_time_and_modify_lineedit_field(self):
        # fetch current time in hh:mm:ss format and write it to get_current_session_start_time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        hours, minutes, seconds = current_time.split(":")
        self.current_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
        self.get_custom_session_start_time.setText(current_time)

    def next_thirty_minutes_clicked(self):
        # time after adding 30 minutes to the current time
        next_thirty_minutes = self.current_seconds + 30 * 60
        self.get_custom_session_end_time.setText(time.strftime("%H:%M:%S", time.gmtime(next_thirty_minutes)))

    def next_forty_five_minutes_clicked(self):
        # time after adding 45 minutes to the current time
        next_forty_five_minutes = self.current_seconds + 45 * 60
        self.get_custom_session_end_time.setText(time.strftime("%H:%M:%S", time.gmtime(next_forty_five_minutes)))

    def next_sixty_minutes_clicked(self):
        # time after adding 60 minutes to the current time
        next_sixty_minutes = self.current_seconds + 60 * 60
        self.get_custom_session_end_time.setText(time.strftime("%H:%M:%S", time.gmtime(next_sixty_minutes)))

    def delete_entry_from_container_button_clicked(self):
        # discard selected entry
        self.current_item = self.blacklisted_website_container.currentItem()
        self.blacklisted_website_container.takeItem(self.blacklisted_website_container.row(self.current_item))

    def save_entries_button_clicked(self):
        # storing all the active items to the variable all_entries_from_container
        # self.all_entries_from_container = []
        #
        # for i in range(self.blacklisted_website_container.count()):
        #     self.all_entries_from_container.append(self.blacklisted_website_container.item(i).text())
        #
        # # writing the entries into custom_session_file location in APPDATA/WebTrackerX/
        # with open(self.custom_session_file, "w+") as custom_session_file:
        #     for entry in self.all_entries_from_container:
        #         custom_session_file.write(entry.__add__("\n"))

        pass

