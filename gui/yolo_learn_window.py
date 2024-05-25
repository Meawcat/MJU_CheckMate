# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/yolo_learn_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import tkinter as tk
from tkinter import filedialog, messagebox, Label
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import subprocess
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os

class Ui_YoloLearnWindow(object):
    def setupUi(self, YoloLearnWindow):

        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        os.chdir(script_dir)
        YoloLearnWindow.setObjectName("YoloLearnWindow")
        YoloLearnWindow.resize(553, 573)
        YoloLearnWindow.setStyleSheet("YoloLearnWindow{\n"
                                      "    font: 9pt \"맑은 고딕\";\n"
                                      "    background-color: #fff;\n"
                                      "}")
        self.centralwidget = QtWidgets.QWidget(YoloLearnWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.find_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.find_button.setFont(font)
        self.find_button.setStyleSheet("QPushButton:hover {\n"
                                       "    color: #fff;\n"
                                       "}\n"
                                       "QPushButton {\n"
                                       "    border: 4px solid#a6aaaf;\n"
                                       "    border-radius: 5px;\n"
                                       "    padding: 1px 5px;\n"
                                       "    background-color: #a6aaaf;\n"
                                       "}")
        self.find_button.setObjectName("find_button")
        self.gridLayout.addWidget(self.find_button, 1, 2, 1, 1)
        self.model_dir_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.model_dir_edit.setStyleSheet("border: 2px solid#a6aaaf;\n"
                                          "border-radius: 5px;\n"
                                          "padding: 1px 5px;\n"
                                          "\n"
                                          "")
        self.model_dir_edit.setObjectName("model_dir_edit")
        self.gridLayout.addWidget(self.model_dir_edit, 2, 1, 1, 1)
        self.yaml_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.yaml_edit.setStyleSheet("border: 2px solid#a6aaaf;\n"
                                     "border-radius: 5px;\n"
                                     "padding: 1px 5px;\n"
                                     "\n"
                                     "")
        self.yaml_edit.setObjectName("yaml_edit")
        self.gridLayout.addWidget(self.yaml_edit, 1, 1, 1, 1)
        self.load_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.load_button.setFont(font)
        self.load_button.setStyleSheet("QPushButton:hover {\n"
                                       "    color: #fff;\n"
                                       "}\n"
                                       "QPushButton {\n"
                                       "    border: 4px solid#a6aaaf;\n"
                                       "    border-radius: 5px;\n"
                                       "    padding: 1px 5px;\n"
                                       "    background-color: #a6aaaf;\n"
                                       "}")
        self.load_button.setObjectName("load_button")
        self.gridLayout.addWidget(self.load_button, 3, 2, 1, 1)
        self.model_dir = QtWidgets.QLabel(self.centralwidget)
        self.model_dir.setAlignment(QtCore.Qt.AlignCenter)
        self.model_dir.setObjectName("model_dir")
        self.gridLayout.addWidget(self.model_dir, 2, 0, 1, 1)
        self.model_save = QtWidgets.QLabel(self.centralwidget)
        self.model_save.setAlignment(QtCore.Qt.AlignCenter)
        self.model_save.setObjectName("model_save")
        self.gridLayout.addWidget(self.model_save, 3, 0, 1, 1)
        self.yaml_dir = QtWidgets.QLabel(self.centralwidget)
        self.yaml_dir.setAlignment(QtCore.Qt.AlignCenter)
        self.yaml_dir.setObjectName("yaml_dir")
        self.gridLayout.addWidget(self.yaml_dir, 1, 0, 1, 1)
        self.model_save_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.model_save_edit.setStyleSheet("border: 2px solid#a6aaaf;\n"
                                           "border-radius: 5px;\n"
                                           "padding: 1px 5px;\n"
                                           "\n"
                                           "")
        self.model_save_edit.setObjectName("model_save_edit")
        self.gridLayout.addWidget(self.model_save_edit, 3, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox.setStyleSheet("border: 2px solid #a6aaaf;\n"
                                    "border-radius: 5px;\n"
                                    "padding: 1px 5px;\n"
                                    "\n"
                                    "")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.item_name = QtWidgets.QLabel(self.centralwidget)
        self.item_name.setObjectName("item_name")
        self.gridLayout.addWidget(self.item_name, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.epoch_label = QtWidgets.QLabel(self.centralwidget)
        self.epoch_label.setObjectName("epoch_label")
        self.horizontalLayout_2.addWidget(self.epoch_label)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(300)
        self.horizontalSlider.setSingleStep(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(10)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.epoch_num = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.epoch_num.setFont(font)
        self.epoch_num.setObjectName("epoch_num")
        self.horizontalLayout_2.addWidget(self.epoch_num)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 527, 314))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.process = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.process.setText("")
        self.process.setObjectName("process")
        self.verticalLayout_3.addWidget(self.process)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.train_start = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.train_start.setFont(font)
        self.train_start.setStyleSheet("QPushButton:hover {\n"
                                       "    color: #fff;\n"
                                       "}\n"
                                       "QPushButton {\n"
                                       "    border: 4px solid#a6aaaf;\n"
                                       "    border-radius: 5px;\n"
                                       "    padding: 1px 5px;\n"
                                       "    background-color: #a6aaaf;\n"
                                       "}")
        self.train_start.setObjectName("train_start")
        self.horizontalLayout.addWidget(self.train_start, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        YoloLearnWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(YoloLearnWindow)
        QtCore.QMetaObject.connectSlotsByName(YoloLearnWindow)

        self.populate_directory_combo(self.comboBox)
        self.set_edit()
        self.find_button.clicked.connect(self.open_file_dialog)
        self.load_button.clicked.connect(self.open_directory_dialog)
        self.comboBox.currentIndexChanged.connect(self.set_edit)
        self.train_start.clicked.connect(self.start_training)
        self.model_dir_edit.textChanged.connect(self.model_dir_changed)
        self.horizontalSlider.valueChanged.connect(self.update_epoch_num)

    def update_epoch_num(self):
        value = self.horizontalSlider.value()
        self.epoch_num.setText(f"{value}")

    def retranslateUi(self, YoloLearnWindow):
        _translate = QtCore.QCoreApplication.translate
        YoloLearnWindow.setWindowTitle(_translate("YoloLearnWindow", "YOLOv5 학습"))
        self.find_button.setText(_translate("YoloLearnWindow", "찾아보기"))
        self.load_button.setText(_translate("YoloLearnWindow", "불러오기"))
        self.model_dir.setText(_translate("YoloLearnWindow", "학습 모델 폴더 이름"))
        self.model_save.setText(_translate("YoloLearnWindow", "학습 모델 저장 위치"))
        self.yaml_dir.setText(_translate("YoloLearnWindow", "data.yaml 파일 위치"))
        self.item_name.setText(_translate("YoloLearnWindow", "물품 이름"))
        self.epoch_label.setText(_translate("YoloLearnWindow", "에포크 수"))
        self.epoch_num.setText(_translate("YoloLearnWindow", "1"))
        self.train_start.setText(_translate("YoloLearnWindow", "학습 시작"))

    def model_dir_changed(self):
        combo_text = self.comboBox.currentText()  # combo_text는 현재 사용되지 않음
        model_dir_text = self.model_dir_edit.text()
        import os
        new_path = os.path.join("../yolov5/runs/train", model_dir_text, "weights")
        self.model_save_edit.setText(new_path)
    def show_loading_screen(self):
        self.loading_window = tk.Toplevel(self.root)
        self.loading_window.title("Loading")
        self.loading_window.geometry("300x200")
        self.loading_label = tk.Label(self.loading_window, text="학습 중입니다...\n잠시만 기다려주세요.", font=("Arial", 12))
        self.loading_label.pack(pady=20)
        gif_path = "icons/loading1.gif"
        self.loading_gif = [tk.PhotoImage(file=gif_path, format='gif -index %i' % i) for i in
                            range(30)]  # assuming 30 frames
        self.loading_gif_label = tk.Label(self.loading_window)
        self.loading_gif_label.pack()
        self.animate_gif(0)

    def start_training(self):
        data_yaml = self.yaml_edit.text()
        model_name = self.model_dir_edit.text()
        save_dir = self.model_save_edit.text()
        epoch = self.epoch_num.text()
        if not data_yaml or not model_name or not save_dir:
            QtWidgets.QMessageBox.warning(None, "경고", "모든 필드를 입력해 주세요")
            return
        try:
            command = f'python ../yolov5/train.py --img 640 --batch 16 --epochs {epoch} --data {data_yaml} --cfg ../yolov5/models/yolov5s.yaml --weights ../yolov5/yolov5s.pt --name {model_name} --project ../yolov5/runs/train'
            self.training_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8')
            self.read_process_output()
            self.thread = threading.Thread(target=self.run_command, args=(command,))
            self.thread.start()
        except subprocess.CalledProcessError as e:
            error_message = e.stderr.decode('utf-8')
            QtWidgets.QMessageBox.critical(None, "오류", f"명령 실행 중 오류가 발생했습니다:\n{error_message}")
        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "실패", f"알 수 없는 오류가 발생했습니다: {e}")


    def run_command(self, command):
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.show_message_box("성공", "명령이 성공적으로 실행되었습니다:\n" + result.stdout.decode('utf-8'), QMessageBox.Information)
        except subprocess.CalledProcessError as e:
            error_message = f"명령 실행 중 오류가 발생했습니다:\n{e.stderr.decode('utf-8')}"
            self.show_message_box("오류", error_message, QMessageBox.Critical)
        except Exception as e:
            self.show_message_box("오류", f"알 수 없는 오류가 발생했습니다: {e}", QMessageBox.Warning)

    def read_process_output(self):
        output_text = ""
        while True:
            line = self.training_process.stdout.readline()
            if not line:
                break
            output_text += line
            self.process.setText(output_text)
            QtWidgets.QApplication.processEvents()  # Immediate update of QLabel
            self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())

        self.training_process.stdout.close()
        self.training_process.wait()
        self.close_loading_screen()
        if self.training_process.returncode == 0:
            self.show_message_box("완료", "학습이 완료되었습니다.", QMessageBox.Information)
        else:
            self.show_message_box("오류", "학습 중 오류가 발생했습니다.", QMessageBox.Critical)
        self.training_process = None

    def show_message_box(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setIcon(icon)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()
    def stop_training(self):
        if hasattr(self, 'training_process') and self.training_process.poll() is None:
            self.training_process.terminate()
            QtWidgets.QMessageBox.information(None, "중지", "훈련 프로세스가 중지되었습니다.")


    def set_edit(self):
        selected_item = self.comboBox.currentText()
        import os
        selected_dir = os.path.join("../data", selected_item)
        selected_yaml = os.path.join(selected_dir, "data.yaml")
        selected_model_dir = os.path.join("../yolov5/runs/train")

        if not os.path.exists(selected_yaml):
            self.yaml_edit.setText("해당 파일이 존재하지 않습니다. 다시 확인해 주세요")
        else:
            self.yaml_edit.setText(selected_yaml)

        model_name = selected_item
        self.model_dir_edit.setText(model_name)

        selected_model_save_dir = os.path.join(selected_model_dir, self.model_dir_edit.text(), "weights")
        self.model_save_edit.setText(selected_model_save_dir)

    def animate_gif(self, ind):
        frame = self.loading_gif[ind]
        ind += 1
        if ind == len(self.loading_gif):
            ind = 0
        self.loading_gif_label.configure(image=frame)
        self.loading_window.after(50, self.animate_gif, ind)  # update every 50 ms

    def populate_directory_combo(self, combo):
        try:
            directory = "../data"
            directories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
            combo.addItems(directories)
        except Exception as e:
            QMessageBox.Warning(None, "경고", "data가 없습니다. 다시 확인해 주세요.")

    def close_loading_screen(self):
        if hasattr(self, 'loading_window'):
            self.loading_window.destroy()



    # 파일 열기 함수
    def open_file_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select data.yaml file", "", "YAML Files (*.yaml);;All Files (*)", options=options)
        if file_path:
                self.yaml_edit.setText(file_path)

    # 디렉토리 열기 함수
    def open_directory_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        directory_path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory", "", options=options)
        if directory_path:
            self.model_save_edit.setText(directory_path)

