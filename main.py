from PyQt6 import QtCore, QtGui, QtWidgets
from pathlib import Path
import requests

class AboutDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.resize(400, 300)
        self.setFixedSize(self.size())
        layout = QtWidgets.QVBoxLayout()
        title_label = QtWidgets.QLabel("Movie Info Finder (GUI)")
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        version_label = QtWidgets.QLabel("Version: 1.0")
        version_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(version_label)

        creator_label = QtWidgets.QLabel("Creator: Danial Rashidi")
        creator_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(creator_label)

        email_label = QtWidgets.QLabel('<a href="mailto:danialrashidi0456@outlook.com">Email: danialrashidi0456@outlook.com</a>')
        email_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        email_label.setOpenExternalLinks(True)
        layout.addWidget(email_label)

        website_label = QtWidgets.QLabel('<a href="https://danialrashidi.ir">Website: danialrashidi.ir</a>')
        website_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        website_label.setOpenExternalLinks(True)
        layout.addWidget(website_label)

        github_label = QtWidgets.QLabel('<a href="https://github.com/danialrashidi0456/movie-info-finder-GUI">Github: https://github.com/danialrashidi0456</a>')
        github_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        github_label.setOpenExternalLinks(True)
        layout.addWidget(github_label)

        ok_button = QtWidgets.QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        ok_button.setMaximumWidth(100)
        ok_button.setStyleSheet("padding: 5px; margin-top: 10px")
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(ok_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.setLayout(layout)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(970, 610)
        MainWindow.setFixedSize(MainWindow.size())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.mainBody = QtWidgets.QFrame(parent=self.centralwidget)
        self.mainBody.setGeometry(QtCore.QRect(0, 0, 481, 601))
        self.mainBody.setObjectName("mainBody")
        self.titleSection = QtWidgets.QWidget(parent=self.mainBody)
        self.titleSection.setGeometry(QtCore.QRect(0, 40, 491, 111))
        self.titleSection.setObjectName("titleSection")
        self.title = QtWidgets.QLabel(parent=self.titleSection)
        self.title.setGeometry(QtCore.QRect(0, -40, 491, 151))
        self.title.setObjectName("title")
        self.searchInpSeection = QtWidgets.QWidget(parent=self.mainBody)
        self.searchInpSeection.setGeometry(QtCore.QRect(0, 150, 491, 91))
        self.searchInpSeection.setObjectName("searchInpSection")
        self.searchInp = QtWidgets.QLineEdit(parent=self.searchInpSeection)
        self.searchInp.setGeometry(QtCore.QRect(100, 20, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setStrikeOut(False)
        self.searchInp.setFont(font)
        self.searchInp.setAcceptDrops(True)
        self.searchInp.setAutoFillBackground(False)
        self.searchInp.setObjectName("searchInp")
        self.buttonSection = QtWidgets.QWidget(parent=self.mainBody)
        self.buttonSection.setGeometry(QtCore.QRect(0, 240, 491, 91))
        self.buttonSection.setObjectName("buttonSection")
        self.searchButton = QtWidgets.QPushButton(parent=self.buttonSection)
        self.searchButton.setGeometry(QtCore.QRect(167, 50, 161, 41))
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(lambda: self.movie_info(self.searchInp.text()))
        self.InfoSection = QtWidgets.QFrame(parent=self.centralwidget)
        self.InfoSection.setGeometry(QtCore.QRect(490, 0, 491, 601))
        self.InfoSection.setObjectName("InfoSection")
        self.showInfo = QtWidgets.QTextBrowser(parent=self.InfoSection)
        self.showInfo.setGeometry(QtCore.QRect(0, 0, 481, 590))
        self.showInfo.setObjectName("showInfo")
        self.showInfo.document().setDefaultFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 970, 22))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtWidgets.QMenu(parent=self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.show_about_dialog)
        self.actionCopy = QtGui.QAction(parent=MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtGui.QAction(parent=MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.actionPaste.triggered.connect(self.searchInp.paste) # type: ignore
        self.actionCopy.triggered.connect(lambda: self.showInfo.selectAll())
        self.actionCopy.triggered.connect(lambda: self.showInfo.copy())
        self.searchInp.returnPressed.connect(self.searchButton.click)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def show_about_dialog(self):
        dialog = AboutDialog()
        dialog.exec()
    
    def movie_info(self, name):
        api_key = "26b4c440"
        url = f"http://www.omdbapi.com/?apikey={api_key}&t={name}"
        response = requests.get(url)
        movie_info_json = response.json()

        if movie_info_json["Response"] == "True":
            info_text = f"Title: {movie_info_json.get('Title')}\n" \
                        f"Year: {movie_info_json.get('Year')}\n" \
                        f"Time: {movie_info_json.get('Runtime')}\n" \
                        f"Genre: {movie_info_json.get('Genre')}\n" \
                        f"Director: {movie_info_json.get('Director')}\n" \
                        f"Writer: {movie_info_json.get('Writer')}\n" \
                        f"Actors: {movie_info_json.get('Actors')}\n" \
                        f"Awards: {movie_info_json.get('Awards')}\n" \
                        f"BoxOffice: {movie_info_json.get('BoxOffice')}\n" \
                        f"Metascore: {movie_info_json.get('Metascore')}\n" \
                        f"IMDB: {movie_info_json.get('imdbRating')}\n"
            self.showInfo.setText(info_text)
        else:
            self.showInfo.setText("Movie not found!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Movie Info Finder"))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:700;\">Movie Info Finder</span></p><p align=\"center\"><br/></p></body></html>"))
        self.searchInp.setPlaceholderText(_translate("MainWindow", "Enter Movie Name"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.showInfo.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("/icon.png"))
    app.setStyleSheet(Path('style.qss').read_text())
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
