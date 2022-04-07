from PyQt5 import QtCore, QtGui, QtWidgets

from Course import Course

import webbrowser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.listWidget.itemClicked.connect(self.listWidgetClicked)
        self.pushButton.clicked.connect(self.addCourse)
        self.urls = []

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Add New Course"))
        self.setListWidget()

    def setListWidget(self):
        courses = self.readCourses()
        for course in courses:

            self.urls.append(course.get_course_link())

            item = QtWidgets.QListWidgetItem()

            widget = QtWidgets.QWidget()
            widget_name = QtWidgets.QLabel(course.get_course_name())
            widget_progress = QtWidgets.QProgressBar()
            widget_progress.setValue(int(course.get_progress()))

            widget_layout = QtWidgets.QHBoxLayout()
            widget_layout.addWidget(widget_name)
            widget_layout.addWidget(widget_progress)
            widget_layout.addStretch()

            widget_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
            widget.setLayout(widget_layout)
            item.setSizeHint(widget.sizeHint())

            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)
            
    def listWidgetClicked(self, item):
        webbrowser.open(self.urls[self.listWidget.row(item)], new=0, autoraise=True)
        
    def addCourse(self):
        course_name = self.lineEdit.text()
        course_link = self.lineEdit_2.text()
        course = Course(course_name, course_link, "0")
        file = open("courses.txt", "a")
        file.write(course.get_course_name() + "0;0" + course.get_course_link() + "0;0" + course.get_progress() + "\n")
        file.close()
        self.setListWidget()

    def readCourses(self):
        self.listWidget.clear()
        file = open("courses.txt", "r")
        courses = []
        for line in file.readlines():
            if line != '\n':
                line_course = line.split("0;0")
                course = Course(line_course[0], line_course[1], line_course[2].strip())
                courses.append(course)
        file.close()
        return courses

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
