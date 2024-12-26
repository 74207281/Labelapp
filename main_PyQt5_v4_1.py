

# Labeling app for grass
# By PyQt5

import sys
import os
import cv2
import json
import pandas as pd
import numpy as np
from PyQt5 import QtWidgets
from PIL import Image
from mainUI import Ui_MainWindow
from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QLabel,
    QMainWindow,
    QFileDialog,
    QMessageBox,
    QHBoxLayout,
    QVBoxLayout,
    QMenu
)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # information of file
        self.image_info = {}
        self.setObjectName("MainWindow")
        self.setWindowTitle('Grass Label')
        self.resize(300, 200)

        # Check is image loaded
        self.data_load_flag = False
        # number of file in this respotory
        self.image_index = 0
        # Check if the image  is loaded
        self.isimageload = False
        # Check if the image is modified
        self.modified_falg = False
        # Check if the save button is pressed
        self.save_flag = False
        # Check if is other image processed
        self.other_flag = False
        # Call UI
        self.setupUI(self)
        # Button of Load File
        self.LoadButton.clicked.connect(self.loadfile)
        # Abnormal
        self.Abnormal_flag = False
        # Button of confirm
        # self.ConfirmButton.clicked.connect(self.Confirm)
        # Button of Previous image
        self.PreButton.clicked.connect(self.Pre)
        # Button of Next image
        self.NextButton.clicked.connect(self.Next)
        # Can't Handel
        self.unknowButton.clicked.connect(self.canthandel)

    # Load file

    def loadfile(self):
        # Get respotory of image storge
        path = QFileDialog.getExistingDirectory(self, '選擇資料夾')
        print(path)
        self.source = path
        root, group = os.path.split(self.source)
        if path:  # path exist
            # old json file exist
            if f'{group}_output.json' in os.listdir(path):
                with open(os.path.join(path, f'{group}_output.json')) as f:
                    self.image_info = json.load(f)
                # print(self.image_info)
                try:
                    # From last image had been done
                    for last in range(len(self.image_info)):
                        if self.image_info[str(last)]['Greeness'] == '':
                            self.image_index = int(last)
                            # break
                            self.other_flag = True
                            self.label_6.setText(str(len(self.image_info)))
                            # self.isimageload = True
                            self.data_load_flag = True
                            self.loadinfo()
                            self.__load_image()
                            # if last == (len(self.image_info)-1):
                            #     QMessageBox.information(
                            #         self, 'All Done', 'All Image In This Folder Had Been Labeled', QMessageBox.Ok)
                            #     break
                            # print(last)
                            break
                        elif ((last == (len(self.image_info)-1)) & (self.image_info[str(last)]['Greeness'] != '')):
                            QMessageBox.information(
                                self, 'All Done', 'All Image In This Folder Had Been Labeled', QMessageBox.Ok)
                            self.image_index = int(0)
                            # break
                            self.other_flag = True
                            self.label_6.setText(str(len(self.image_info)))
                            # self.isimageload = True
                            self.data_load_flag = True
                            self.loadinfo()
                            self.__load_image()
                            # self.close()
                            break
                except:
                    return
            # pass
            else:
                try:
                    # Make a dictionary of each file
                    i = 0  # Counter
                    for f in os.listdir(path):
                        if (f.endswith('.JPG') or f.endswith('.jpg') or f.endswith('.PNG') or f.endswith('.png')):
                            # Dictionary of each file
                            self.image_info[str(i)] = {'Source': path,
                                                       #    'filename': os.path.join(os.path.normpath(path), f),
                                                       'Filename': f,
                                                       'Greeness': '',
                                                       'Coverage': '',
                                                       'Healthness': ''}
                            i += 1
                    self.label_6.setText(str(i))
                    # self.isimageload = True
                    self.data_load_flag = True
                    self.__load_image()
                except:
                    QMessageBox.critical(
                        self, 'No image', 'No image', QMessageBox.Ok)

    def Confirm(self):
        try:
            if self.isimageload:  # Chech if image is loaded
                if self.Abnormal_flag:
                    self.Abnormal_flag = False
                    pass
                else:
                    # Greeness
                    green = self.GreenGroup.checkedId()
                    # Covery
                    cover = self.CoverGroup.checkedId()
                    # Healthyness
                    health = self.HealthGroup.checkedId()
                    # print(green)

                    # NA Condition
                    if (green == 0 | cover == 0 | health == 0):
                        self.image_info[str(self.image_index)
                                        ]['Greeness'] = "NA"
                        self.image_info[str(self.image_index)
                                        ]['Healthness'] = "NA"
                        self.image_info[str(self.image_index)
                                        ]['Coverage'] = "NA"
                    else:
                        self.image_info[str(self.image_index)
                                        ]['Greeness'] = str(green)
                        self.image_info[str(self.image_index)
                                        ]['Healthness'] = str(health)
                        self.image_info[str(self.image_index)
                                        ]['Coverage'] = str(cover)
                    # file is confirmed
                    self.modified_falg = True
                    self.saveinfo()
            else:
                QMessageBox.critical(
                    self, 'No Image Loaded', 'No Image Loaded', QMessageBox.Ok)
        except:
            print("error (Confirm)")
            return
    # Next button

    def Next(self):
        if self.image_info == {}:
            pass
        else:

            self.Confirm()
            if (self.image_index < (len(self.image_info)-1) and (self.image_index >= 0)):
                cv2.destroyAllWindows()
                self.image_index += 1
                self.loadinfo()
                self.__load_image()
            elif (self.image_index == (len(self.image_info)-1)):
                QMessageBox.information(
                    self, 'No Next', 'Last Image of The Folder', QMessageBox.Ok)

    # Previous button
    def Pre(self):
        try:
            if self.isimageload:  # is image
                self.Confirm()
                if ((self.image_index <= (len(self.image_info)-1)) and (self.image_index > 0)):
                    cv2.destroyAllWindows()
                    self.image_index -= 1
                    self.loadinfo()
                    self.__load_image()
            # First Image
                elif (self.image_index == 0):
                    QMessageBox.information(
                        self, 'No Previous', 'First Image of The Folder', QMessageBox.Ok)
                else:
                    raise SystemError
        except SystemError:
            QMessageBox.critical(
                self, 'Error', 'Error of PreButton', QMessageBox.Ok)
        except:
            QMessageBox.critical(self, 'Error', 'Error in Pre', QMessageBox.Ok)
            return

    # Save file
    def saveinfo(self):
        if self.image_info == {}:
            QMessageBox.critical(self, 'Please Load Data',
                                 'Please Load data', QMessageBox.Ok)
        else:
            # Turn into json file
            json_info = json.dumps(
                self.image_info, indent=4, ensure_ascii=False)

            root, group = os.path.split(self.source)

            with open(os.path.join(self.source, f'{group}_output.json'), 'w') as json_f:
                json_f.write(json_info)

            # Write into csv
            df = pd.DataFrame(self.image_info).transpose()
            df.to_csv(os.path.join(
                self.source, f'{group}_output.csv'), index=False)
            self.save_flag = True

    # Unknown Data
    def canthandel(self):
        if self.image_info == {}:
            QMessageBox.critical(
                self, 'No Data', 'Please Load Image', QMessageBox.Ok)
        else:
            # Write Na as can't handled data
            self.image_info[str(self.image_index)]["Greeness"] = str('Ab')
            self.image_info[str(self.image_index)]["Coverage"] = str('Ab')
            self.image_info[str(self.image_index)]["Healthness"] = str('Ab')
            self.Abnormal_flag = True
            self.label_7.setText('Abnormal')

            # Save image info
            self.saveinfo()

    # Load info

    def loadinfo(self):
        if self.image_info != {}:
            try:
                # Get greeness of file
                green = self.image_info[str(self.image_index)]['Greeness']
                # Get covery of file
                cover = self.image_info[str(self.image_index)]['Coverage']
                health = self.image_info[str(self.image_index)]['Healthness']
                self.Green_buttons[int(green)].setChecked(True)
                # print(green)
                self.Cover_buttons[int(cover)].setChecked(True)
                self.Health_buttons[int(health)].setChecked(True)
            except:
                self.Green_buttons[0].setChecked(True)
                self.Cover_buttons[0].setChecked(True)
                self.Health_buttons[0].setChecked(True)
                return

    # Load image

    def __load_image(self):
        # Get image path
        self.isimageload = True
        self.imgpath = os.path.join(self.image_info[str(
            self.image_index)]['Source'], self.image_info[str(self.image_index)]['Filename'])
        # img_arr = Image.open(self.imgpath)

        # RGB = np.array(img_arr)
        # RGBImg = np.zeros((RGB.shape[0], RGB.shape[1], 3))

        # Get all channel
        # for ch in range(RGBImg.shape[2]):
        # RGBImg[..., ch] = RGB[..., ch]
        # RGBImg = np.array(img_arr)
        # RGBImg = np.delete(arr=np.array(img_arr), obj=3, axis=2)
        # print(RGBImg)
        RGBImg = cv2.imdecode(np.fromfile(
            self.imgpath, dtype='uint8'), cv2.IMREAD_COLOR)
        cv2.imshow(f'{self.imgpath}', RGBImg)
        # print(RGBImg.shape)
        # Check if is file exist
        if os.path.isfile(self.imgpath):
            # Pixmap
            # if (img_arr.mode == "RGBA"):
            # self.pix_image = QtGui.QImage(
            # RGBImg, RGBImg.shape[1], RGBImg.shape[0], QtGui.QImage.Format_RGBA8888)
            # elif (img_arr.mode == "RGB"):
            # self.pix_image = QtGui.QImage(
            # RGBImg, RGBImg.shape[1], RGBImg.shape[0], QtGui.QImage.Format_RGB888)
            # self.pix_image = QtGui.QPixmap(self.pix_image)
            self.__show_img()
            # Abnormal occur
            if self.image_info[str(self.image_index)]['Greeness'] == 'Ab':
                self.Abnormal_flag = True
                self.label_7.setText('Abnormal')
            else:
                self.Abnormal_flag = False
                self.label_7.setText('-')

        # No file
        else:
            QMessageBox.critical(self, 'No such file',
                                 'No such file', QMessageBox.OK)

    # Show image
    def __show_img(self):
        # if the image is loaded
        if self.isimageload:

            # Change name
            self.current_file_label.setText(
                os.path.basename(self.image_info[str(self.image_index)]["Filename"]))

            self.label_4.setText(str(self.image_index+1))
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            pass

    def resizeEvent(self, event) -> None:
        self.__show_img()

    def closeEvent(self, event) -> None:
        if self.modified_falg:
            if self.image_info != {}:
                if self.save_flag:
                    pass
                else:
                    # Haven't save
                    choice = QMessageBox.question(
                        self, 'Save', 'Do you want to save info?', QMessageBox.Yes | QMessageBox.No)
                    if choice == QMessageBox.Yes:
                        self.saveinfo()
                    else:
                        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
