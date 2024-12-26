# UI for label app
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image


class Ui_MainWindow(object):
    def setupUI(self, MainWindow):
        MainWindow.setObjectName(("MainWindow"))
        MainWindow.resize(1200, 600)
        # Central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # file name
        self.widget_file = QtWidgets.QWidget(self.centralwidget)
        # self.widget_file.setMinimumSize(QtCore.QSize(100, 10))
        self.widget_file.setGeometry(0, 0, 10, 10)
        self.widget_file.setObjectName("widget")
        # Layout
        self.gridLayout_file = QtWidgets.QGridLayout()
        self.gridLayout_file.setObjectName("gridLayout")

        # Greeness
        self.widget_Green = QtWidgets.QWidget(self.centralwidget)
        self.widget_Green.setObjectName("widget_Green")

        self.gridLayout_Green = QtWidgets.QGridLayout()
        self.gridLayout_Green.setObjectName("gridLayout_Green")

        # Coverry
        self.widget_Cover = QtWidgets.QWidget(self.centralwidget)
        self.widget_Cover.setObjectName("widget_Cover")

        self.gridLayout_Cover = QtWidgets.QGridLayout()
        self.gridLayout_Cover.setObjectName("gridLayout_Cover")

        # Coverry
        self.widget_Health = QtWidgets.QWidget(self.centralwidget)
        self.widget_Health.setObjectName("widget_Cover")

        self.gridLayout_Health = QtWidgets.QGridLayout()
        self.gridLayout_Health.setObjectName("gridLayout_Health")

        # Button
        self.widget_Proc = QtWidgets.QWidget(self.centralwidget)
        self.widget_Proc.setObjectName("widget_Proc")
        # Grid layout

        self.gridLayout_Proc = QtWidgets.QGridLayout()
        self.gridLayout_Proc.setObjectName("gridLayout_Proc")

        # Horizontal layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # horizontal layout for Radio button
        self.horizontalLayout_Button = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Button.setObjectName("horizontalLayout")
        # Vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalalLayout")
        # Image area
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.image_label = QtWidgets.QLabel(self.widget_2)

        self.image_label.setText("")
        self.image_label.setObjectName("image_label")

        img = Image.open('./resource/plan.jpg')
        img_arr = np.array(img)
        im = QtGui.QImage(
            img_arr, img_arr.shape[1], img_arr.shape[0], QtGui.QImage.Format_RGB888)
        self.pix = QtGui.QPixmap(im)
        self.pix = self.pix.scaled(QtCore.QSize(
            self.pix.height(), self.pix.width()))
        self.image_label.setPixmap(self.pix)

        # Label of current file name
        self.current_file_label = QtWidgets.QLabel(self.widget_file)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.current_file_label.setFont(font)
        self.current_file_label.setObjectName("current_file_label")
        self.gridLayout_file.addWidget(self.current_file_label, 0, 2, 1, 1)

        # Title of file name
        self.label_2 = QtWidgets.QLabel(self.widget_file)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_file.addWidget(self.label_2, 0, 0, 1, 1)

        # File number
        self.label_3 = QtWidgets.QLabel(self.widget_file)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_file.addWidget(self.label_3, 1, 0, 1, 1)

        # index of file
        self.label_4 = QtWidgets.QLabel(self.widget_file)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_file.addWidget(
            self.label_4, 1, 2, 1, 1, alignment=QtCore.Qt.AlignCenter)

        #  of
        self.label_5 = QtWidgets.QLabel(self.widget_file)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_file.addWidget(
            self.label_5, 1, 3, 1, 1, alignment=QtCore.Qt.AlignCenter)

        # total number of file
        self.label_6 = QtWidgets.QLabel(self.widget_file)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_file.addWidget(
            self.label_6, 1, 4, 1, 1, alignment=QtCore.Qt.AlignCenter)

        # Abnormal Label
        self.label_7 = QtWidgets.QLabel(self.widget_file)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_6")
        self.gridLayout_file.addWidget(
            self.label_7, 3, 0, 1, 1)

        # Load File
        self.LoadButton = QtWidgets.QPushButton(self.widget_file)
        self.LoadButton.setFont(font)
        self.gridLayout_file.addWidget(self.LoadButton, 2, 0, 1, 1)

        # Line
        self.line = QtWidgets.QFrame(self.widget_file)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_file.addWidget(self.line, 0, 1, 1, 1)
        # Line
        self.line2 = QtWidgets.QFrame(self.widget_file)
        self.line2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.gridLayout_file.addWidget(self.line2, 1, 1, 1, 1)

        # List of green
        # Label
        self.GreenLabel = QtWidgets.QLabel(self.widget_Green)
        self.GreenLabel.setFont(font)
        self.GreenLabel.setObjectName('GreenLabel')
        self.gridLayout_Green.addWidget(self.GreenLabel, 0, 0, 1, 1)

        self.Green_list0 = QtWidgets.QRadioButton('NA', self.widget_Green)
        self.Green_list0.setFont(font)
        self.gridLayout_Green.addWidget(self.Green_list0, 1, 0, 1, 1)

        self.Green_list1 = QtWidgets.QRadioButton('1', self.widget_Green)
        self.Green_list1.setFont(font)
        self.gridLayout_Green.addWidget(self.Green_list1, 2, 0, 1, 1)

        self.Green_list2 = QtWidgets.QRadioButton('2', self.widget_Green)
        self.Green_list2.setFont(font)
        self.gridLayout_Green.addWidget(self.Green_list2, 3, 0, 1, 1)

        self.Green_list3 = QtWidgets.QRadioButton('3', self.widget_Green)
        self.Green_list3.setFont(font)
        self.gridLayout_Green.addWidget(self.Green_list3, 4, 0, 1, 1)

        self.Green_list4 = QtWidgets.QRadioButton('4', self.widget_Green)
        self.Green_list4.setFont(font)
        self.gridLayout_Green.addWidget(self.Green_list4, 5, 0, 1, 1)

        self.Green_list5 = QtWidgets.QRadioButton('5', self.widget_Green)
        self.Green_list5.setFont(font)
        self.gridLayout_Green.addWidget(self.Green_list5, 6, 0, 1, 1)

       # Group all greeness
        self.GreenGroup = QtWidgets.QButtonGroup(self.widget_Green)
        self.GreenGroup.addButton(self.Green_list0, 0)
        self.GreenGroup.addButton(self.Green_list1, 1)
        self.GreenGroup.addButton(self.Green_list2, 2)
        self.GreenGroup.addButton(self.Green_list3, 3)
        self.GreenGroup.addButton(self.Green_list4, 4)
        self.GreenGroup.addButton(self.Green_list5, 5)
        self.Green_buttons = [self.Green_list0, self.Green_list1, self.Green_list2,
                              self.Green_list3, self.Green_list4, self.Green_list5]
        self.Green_buttons[0].setChecked(True)

        # List of cover
        # Label of cover
        self.CoverLabel = QtWidgets.QLabel(self.widget_Cover)
        self.CoverLabel.setObjectName('CoverLabel')
        self.CoverLabel.setFont(font)
        self.gridLayout_Cover.addWidget(self.CoverLabel, 0, 0, 1, 1)

        self.Cover_list0 = QtWidgets.QRadioButton('NA', self.widget_Cover)
        self.Cover_list0.setFont(font)
        self.gridLayout_Cover.addWidget(self.Cover_list0, 1, 0, 1, 1)

        self.Cover_list1 = QtWidgets.QRadioButton('1', self.widget_Cover)
        self.Cover_list1.setFont(font)
        self.gridLayout_Cover.addWidget(self.Cover_list1, 2, 0, 1, 1)

        self.Cover_list2 = QtWidgets.QRadioButton('2', self.widget_Cover)
        self.Cover_list2.setFont(font)
        self.gridLayout_Cover.addWidget(self.Cover_list2, 3, 0, 1, 1)

        self.Cover_list3 = QtWidgets.QRadioButton('3', self.widget_Cover)
        self.Cover_list3.setFont(font)
        self.gridLayout_Cover.addWidget(self.Cover_list3, 4, 0, 1, 1)

        self.Cover_list4 = QtWidgets.QRadioButton('4', self.widget_Cover)
        self.Cover_list4.setFont(font)
        self.gridLayout_Cover.addWidget(self.Cover_list4, 5, 0, 1, 1)

        self.Cover_list5 = QtWidgets.QRadioButton('5', self.widget_Cover)
        self.Cover_list5.setFont(font)
        self.gridLayout_Cover.addWidget(self.Cover_list5, 6, 0, 1, 1)

        # Group all Cover
        self.CoverGroup = QtWidgets.QButtonGroup(self.widget_Cover)
        self.CoverGroup.addButton(self.Cover_list0, 0)
        self.CoverGroup.addButton(self.Cover_list1, 1)
        self.CoverGroup.addButton(self.Cover_list2, 2)
        self.CoverGroup.addButton(self.Cover_list3, 3)
        self.CoverGroup.addButton(self.Cover_list4, 4)
        self.CoverGroup.addButton(self.Cover_list5, 5)
        self.Cover_buttons = [self.Cover_list0, self.Cover_list1, self.Cover_list2,
                              self.Cover_list3, self.Cover_list4, self.Cover_list5]
        self.Cover_buttons[0].setChecked(True)

        # Label of Health
        self.HealthLabel = QtWidgets.QLabel(self.widget_Health)
        self.HealthLabel.setObjectName('HealthLabel')
        self.HealthLabel.setFont(font)
        self.gridLayout_Health.addWidget(self.HealthLabel, 0, 0, 1, 1)

        self.Health_list0 = QtWidgets.QRadioButton('NA', self.widget_Health)
        self.Health_list0.setFont(font)
        self.gridLayout_Health.addWidget(self.Health_list0, 1, 0, 1, 1)

        self.Health_list1 = QtWidgets.QRadioButton('1', self.widget_Health)
        self.Health_list1.setFont(font)
        self.gridLayout_Health.addWidget(self.Health_list1, 2, 0, 1, 1)

        self.Health_list2 = QtWidgets.QRadioButton('2', self.widget_Health)
        self.Health_list2.setFont(font)
        self.gridLayout_Health.addWidget(self.Health_list2, 3, 0, 1, 1)

        self.Health_list3 = QtWidgets.QRadioButton('3', self.widget_Health)
        self.Health_list3.setFont(font)
        self.gridLayout_Health.addWidget(self.Health_list3, 4, 0, 1, 1)

        self.Health_list4 = QtWidgets.QRadioButton('4', self.widget_Health)
        self.Health_list4.setFont(font)
        self.gridLayout_Health.addWidget(self.Health_list4, 5, 0, 1, 1)

        self.Health_list5 = QtWidgets.QRadioButton('5', self.widget_Health)
        self.Health_list5.setFont(font)
        self.gridLayout_Health.addWidget(self.Health_list5, 6, 0, 1, 1)

        # Group all Health
        self.HealthGroup = QtWidgets.QButtonGroup(self.widget_Health)
        self.HealthGroup.addButton(self.Health_list0, 0)
        self.HealthGroup.addButton(self.Health_list1, 1)
        self.HealthGroup.addButton(self.Health_list2, 2)
        self.HealthGroup.addButton(self.Health_list3, 3)
        self.HealthGroup.addButton(self.Health_list4, 4)
        self.HealthGroup.addButton(self.Health_list5, 5)
        self.Health_buttons = [self.Health_list0, self.Health_list1, self.Health_list2,
                               self.Health_list3, self.Health_list4, self.Health_list5]
        self.Health_buttons[0].setChecked(True)

        # Confirm Button
        # self.ConfirmButton = QtWidgets.QPushButton(self.widget_Proc)
        # self.ConfirmButton.setFont(font)
        # self.gridLayout_Proc.addWidget(self.ConfirmButton, 0, 0, 1, 2)

        # Unknow
        self.unknowButton = QtWidgets.QPushButton(self.widget_Proc)
        self.unknowButton.setFont(font)
        self.gridLayout_Proc.addWidget(self.unknowButton, 1, 0, 1, 2)

        # Next
        self.NextButton = QtWidgets.QPushButton(self.widget_Proc)
        self.NextButton.setFont(font)
        self.gridLayout_Proc.addWidget(self.NextButton, 2, 1, 1, 1)

        # Prvious
        self.PreButton = QtWidgets.QPushButton(self.widget_Proc)
        self.PreButton.setFont(font)
        self.gridLayout_Proc.addWidget(self.PreButton, 2, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_file, stretch=100)
        self.horizontalLayout_Button.addLayout(
            self.gridLayout_Green, stretch=100)
        self.horizontalLayout_Button.addLayout(
            self.gridLayout_Cover, stretch=100)
        self.horizontalLayout_Button.addLayout(
            self.gridLayout_Health, stretch=100)

        self.verticalLayout.addLayout(
            self.horizontalLayout_Button, stretch=100)
        self.verticalLayout.addLayout(self.gridLayout_Proc, stretch=100)

        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalLayout.setStretchFactor(self.verticalLayout, 3)
        self.horizontalLayout.setStretchFactor(self.widget_2, 8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUI(MainWindow)

    def retranslateUI(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.current_file_label.setText(
            _translate("MainWindow", "current file"))
        # self.label_2.setText(_translate("MainWindow", (u'檔名').encode('utf-8')))
        # self.GreenLabel.setText(_translate('MainWindow', u'綠度'.encode('utf-8')))
        # self.HealthLabel.setText(_translate('MainWindow', u'健康度'.encode('utf-8')))
        # self.CoverLabel.setText(_translate('MainWindow', u'覆蓋度'.encode(('utf-8'))))
        # self.ConfirmButton.setText(_translate('MainWindow', u'確認'.encode('utf-8')))
        # self.unknowButton.setText(_translate('MainWindow', u'無法處理'.encode('utf-8')))
        # self.LoadButton.setText(_translate('MainWindow', 'Load File'))
        # self.NextButton.setText(_translate('MainWindow', u'下一個'.encode('utf-8')))
        # self.PreButton.setText(_translate('MainWindow', u'上一個'.encode('utf-8')))
        self.label_2.setText(_translate("MainWindow", 'File Name'))
        self.label_3.setText(_translate('MainWindow', 'Numbers of Image'))
        self.label_4.setText(_translate('MainWindow', '0'))
        self.label_5.setText(_translate('MainWindow', 'of'))
        self.label_6.setText(_translate('MainWindow', '0'))
        self.label_7.setText(_translate('MainWindow', '-'))

        self.GreenLabel.setText(_translate('MainWindow', 'Greeness'))
        self.HealthLabel.setText(_translate('MainWindow', 'Healthness'))
        self.CoverLabel.setText(_translate('MainWindow', 'Coverage'))
        # self.ConfirmButton.setText(_translate('MainWindow', 'Confirm'))
        self.unknowButton.setText(_translate('MainWindow', 'Abnormal'))
        self.LoadButton.setText(_translate('MainWindow', 'Load File'))
        self.NextButton.setText(_translate('MainWindow', 'Next'))
        self.PreButton.setText(_translate('MainWindow', 'Previous'))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
