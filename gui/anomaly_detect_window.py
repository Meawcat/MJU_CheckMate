# -*- coding: utf-8 -*-
import shutil

# Form implementation generated from reading ui file 'gui/anomaly_detect_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QDialog, QHBoxLayout, QLabel, QVBoxLayout, QScrollArea, QWidget
import subprocess
import os

# # 현재 스크립트 파일의 절대 경로를 가져옵니다.
# script_path = os.path.abspath(__file__)

# # 스크립트 파일이 있는 디렉토리 경로를 가져옵니다.
# script_dir = os.path.dirname(script_path)

# # 작업 디렉토리를 스크립트 파일이 있는 디렉토리로 변경합니다.
# os.chdir(script_dir)

class Ui_anomaly_detection_window(object):
    def setupUi(self, anomaly_detection_window):
        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        os.chdir(script_dir)
        anomaly_detection_window.setObjectName("anomaly_detection_window")
        anomaly_detection_window.resize(587, 547)
        anomaly_detection_window.setStyleSheet("background-color: #fff;font-family: 'Noto Sans Kr'; font-size: 9pt;")
        self.verticalLayout = QtWidgets.QVBoxLayout(anomaly_detection_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.detect_image_upload_button = QtWidgets.QPushButton(anomaly_detection_window)
        font = QtGui.QFont()
        font.setFamily("Noto Sans KR")
        font.setPointSize(9)
        font.setItalic(False)
        self.detect_image_upload_button.setFont(font)
        self.detect_image_upload_button.setStyleSheet("QPushButton:hover {\n"
"    color: #fff;\n"
"}\n"
"QPushButton {\n"
"    border: 4px solid#DBE2EF;\n"
"    border-radius: 5px;\n"
"    padding: 1px 5px;\n"
"    background-color: #DBE2EF;\n"
"    color: #112D4E"  
"}")
        self.detect_image_upload_button.setObjectName("detect_image_upload_button")
        self.gridLayout.addWidget(self.detect_image_upload_button, 1, 2, 1, 1)
        self.model_dir_label = QtWidgets.QLabel(anomaly_detection_window)
        self.model_dir_label.setObjectName("model_dir_label")
        self.gridLayout.addWidget(self.model_dir_label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.threshold_label = QtWidgets.QLabel(anomaly_detection_window)
        self.threshold_label.setAlignment(QtCore.Qt.AlignCenter)
        self.threshold_label.setObjectName("threshold_label")
        self.gridLayout.addWidget(self.threshold_label, 2, 0, 1, 1)
        self.detect_image_edit = QtWidgets.QLineEdit(anomaly_detection_window)
        self.detect_image_edit.setStyleSheet("border: 2px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"\n"
"")
        self.detect_image_edit.setObjectName("detect_image_edit")
        self.gridLayout.addWidget(self.detect_image_edit, 1, 1, 1, 1)
        self.detect_image_label = QtWidgets.QLabel(anomaly_detection_window)
        self.detect_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detect_image_label.setObjectName("detect_image_label")
        self.gridLayout.addWidget(self.detect_image_label, 1, 0, 1, 1)
        self.model_dir_combo = QtWidgets.QComboBox(anomaly_detection_window)
        self.model_dir_combo.setStyleSheet("""
            QComboBox {
                background-color: #fff;
                padding: 3px;
                border: 1px solid #a6aaaf;
                border-radius: 5px;
            }
            QComboBox:hover {
                background-color: #F9F9F9;
            }
            QComboBox:disabled {
                background-color: #F1F1F1;
                color: #A0A0A0;
            }
            QComboBox QAbstractItemView {
                background-color: #FFFFFF;
                border: 1px solid #112D4E;
                selection-background-color: #3F72AF;
                selection-color: #fff;
            }
            """)
        self.model_dir_combo.setObjectName("model_dir_edit")
        self.gridLayout.addWidget(self.model_dir_combo, 0, 1, 1, 1)
        self.threshold_edit = QtWidgets.QLineEdit(anomaly_detection_window)
        self.threshold_edit.setStyleSheet("border: 2px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"\n"
"")
        self.threshold_edit.setObjectName("threshold_edit")
        self.gridLayout.addWidget(self.threshold_edit, 2, 1, 1, 1)
        self.model_dir_button = QtWidgets.QPushButton(anomaly_detection_window)
        font = QtGui.QFont()
        font.setFamily("Noto Sans KR")
        font.setPointSize(9)
        font.setItalic(False)
        self.model_dir_button.setFont(font)
        self.model_dir_button.setStyleSheet("QPushButton:hover {\n"
"    color: #fff;\n"
"}\n"
"QPushButton {\n"
"    border: 4px solid#DBE2EF;\n"
"    border-radius: 5px;\n"
"    padding: 1px 5px;\n"
"    background-color: #DBE2EF;\n"
"    color: #112D4E;\n"
"}")
        self.model_dir_button.setObjectName("model_dir_button")
        self.gridLayout.addWidget(self.model_dir_button, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.scrollArea = QtWidgets.QScrollArea(anomaly_detection_window)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 563, 365))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.log = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.log.setText("")
        self.log.setObjectName("log")
        self.verticalLayout_3.addWidget(self.log)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setStyleSheet("border: none; background-color: #F9F7F7;")
        self.log.verticalScrollBar().setStyleSheet(
            "QScrollBar:vertical { border: none; background-color: #3F72AF; }"
        )
        self.verticalLayout.addWidget(self.scrollArea)
        self.anomaly_detection_button = QtWidgets.QPushButton(anomaly_detection_window)
        font = QtGui.QFont()
        font.setFamily("Noto Sans KR")
        font.setPointSize(9)
        font.setItalic(False)
        self.anomaly_detection_button.setFont(font)
        self.anomaly_detection_button.setStyleSheet("QPushButton:hover {\n"
"    color: #fff;\n"
"}\n"
"QPushButton {\n"
"    border: 4px solid#DBE2EF;\n"
"    border-radius: 5px;\n"
"    padding: 1px 5px;\n"
"    background-color: #DBE2EF;\n"
"    color: #112D4E;\n"
"}")
        self.anomaly_detection_button.setObjectName("anomaly_detection_button")
        self.verticalLayout.addWidget(self.anomaly_detection_button)

        self.retranslateUi(anomaly_detection_window)
        QtCore.QMetaObject.connectSlotsByName(anomaly_detection_window)
        self.model_dir_button.clicked.connect(self.upload_model_dir)
        self.detect_image_upload_button.clicked.connect(self.upload_detect_image_dir)
        self.anomaly_detection_button.clicked.connect(self.start_detecting)
    def retranslateUi(self, anomaly_detection_window):
        _translate = QtCore.QCoreApplication.translate
        anomaly_detection_window.setWindowTitle(_translate("anomaly_detection_window", "이상 탐지"))
        self.detect_image_upload_button.setText(_translate("anomaly_detection_window", "찾아보기"))
        self.model_dir_label.setText(_translate("anomaly_detection_window", "모델 이름"))
        self.threshold_label.setText(_translate("anomaly_detection_window", "임곗값"))
        self.detect_image_label.setText(_translate("anomaly_detection_window", "탐지 이미지"))
        self.model_dir_button.setText(_translate("anomaly_detection_window", "찾아보기"))
        self.anomaly_detection_button.setText(_translate("anomaly_detection_window", "이상 탐지"))

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("에러")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    def show_warning_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("경고")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def start_detecting(self):
        # Check if image paths and weights file exist
        if not self.model_dir_combo.currentText():
            self.show_warning_message("모델을 선택하세요.")
            return
        elif not self.detect_image_edit.text():
            self.show_warning_message("이미지를 선택하세요.")
            return

        self.image_paths = self.detect_image_edit.text()
        print(self.detect_image_edit.text())
        item = self.model_dir_combo.currentText()
        mvtec_ad = os.path.join("../EfficientAD-main/output/", item, "trainings/mvtec_ad")
        item_path = os.listdir(mvtec_ad)[0]
        self.model_path = os.path.join(mvtec_ad, item_path)
        try:
            self.threshold = float(self.threshold_edit.text())  # 문자열을 실수로 변환
        except ValueError:
            self.show_warning_message("잘못된 임계값입니다. 숫자를 입력하세요.")
            return

        # Run detection for each image path
        for image_path in self.image_paths.split(", "):  # 다중 파일 선택시 경로 분리
            try:
                command = f'python ..\EfficientAD-main\AnomalyMapNoM.py -d {self.model_path} -i {image_path} -t {self.threshold} -o ../EfficientAD-main/map'
                print(f"Running command: {command}")
                result = subprocess.run(command, shell=True, capture_output=True, text=True, check=False, encoding='utf-8')
                if result.returncode == 0:
                    self.log.setText(result.stdout)
                    self.get_result(self.log.toPlainText())
                else:
                    self.show_error_message(f"Command failed with error:\n{result.stderr}")
            except subprocess.CalledProcessError as e:
                self.show_error_message(str(e))

    def display_result(self):
        dialog = QDialog()
        dialog.setWindowTitle("이상 탐지 결과")
        dialog.setMinimumSize(800, 600)  # Optional: Set a minimum size for the dialog
        dialog.setStyleSheet("background-color: #fff;")

        # Create a scroll area
        scroll_area = QScrollArea(dialog)
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("border: none; background-color: #F9F7F7;")
        scroll_area.verticalScrollBar().setStyleSheet(
            "QScrollBar:vertical { border: none; background-color: #3F72AF; }"
        )

        # Create a container widget
        container = QWidget()
        img_layout = QVBoxLayout(container)  # Set layout for the container

        # Create a dictionary to map file names to their map paths
        map_dir = "../EfficientAD-main/map"
        map_paths = {os.path.splitext(file)[0]: os.path.join(map_dir, file) for file in os.listdir(map_dir)}

        for result in self.extracted_results:
            vlayout = QVBoxLayout()
            hlayout = QHBoxLayout()
            img_label = QLabel()
            name_label = QLabel()
            status_label = QLabel()

            # 이미지 경로 설정
            img_path = result[0]
            img_label.setPixmap(QPixmap(img_path).scaled(300, 300, Qt.KeepAspectRatio))

            vlayout.addWidget(img_label)

            if not img_path:
                break

            # 파일 이름 추출
            file_name = os.path.basename(img_path)
            name_label.setText(file_name)

            vlayout.addWidget(name_label)

            hlayout.addLayout(vlayout)

            # 상태에 따라 아이콘 설정
            if result[1] == "정상":
                status_icon = "icons/right.png"
            else:
                status_icon = "icons/wrong.png"
                # Construct the expected anomaly map file name
                base_name, ext = os.path.splitext(file_name)
                anomaly_file_name = f"{base_name}_anomaly{ext}"
                if base_name in map_paths:
                    map_label = QLabel()
                    anomaly_file_path = os.path.join(map_dir, anomaly_file_name)
                    if os.path.exists(anomaly_file_path):
                        map_label.setPixmap(QPixmap(anomaly_file_path).scaled(300, 300, Qt.KeepAspectRatio))
                        hlayout.addWidget(map_label)

            status_label.setPixmap(QPixmap(status_icon))

            hlayout.addWidget(status_label)
            # 레이아웃에 위젯 추가
            img_layout.addLayout(hlayout)

        # Set the container widget as the scroll area's widget
        scroll_area.setWidget(container)

        # Create a main layout and add the scroll area to it
        main_layout = QVBoxLayout(dialog)
        main_layout.addWidget(scroll_area)

        dialog.setLayout(main_layout)
        dialog.exec_()

    def get_result(self, input_str):
        lines = input_str.splitlines()
        self.extracted_results = []

        for line in lines:
            # 각 줄을 "||"로 나누어 results 리스트에 저장
            results = line.split("||")

            # 각 요소의 존재 여부를 확인하고 안전하게 처리
            image_info = results[0].split("Image:")[1].strip(" []") if len(results) > 0 and "Image:" in results[
                0] else ""
            anomaly_detect_info = results[1].split("Anomaly Detected:")[1].strip(" []") if len(
                results) > 1 and "Anomaly Detected:" in results[1] else ""
            mean_value_info = results[2].split("Mean Value:")[1].strip(" []") if len(results) > 2 and "Mean Value:" in \
                                                                                 results[2] else ""

            self.extracted_results.append((image_info, anomaly_detect_info, mean_value_info))

        self.display_result()
    def set_model_dir(self):
        model_dir_path = "../EfficientAD-main/output"

        if not os.path.exists(model_dir_path):
            QMessageBox.warning(None, "경고", "학습된 모델이 없습니다. 다시 확인해 주세요.")
            return False
        self.model_dir_combo.clear()
        for dir_name in os.listdir(model_dir_path):
            dir_path = os.path.join(model_dir_path, dir_name)
            if os.path.isdir(dir_path):
                self.model_dir_combo.addItem(dir_name)
        return True

    def open_file_or_directory_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setOptions(options)
        file_dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        file_dialog.setViewMode(QtWidgets.QFileDialog.Detail)

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                selected_path = selected_files[0]
                self.model_dir_combo.setText()

    def upload_detect_image_dir(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("이미지 선택")
        msg_box.setText("원하는 이미지의 형태를 선택하세요.")
        image_button = msg_box.addButton("하나의 이미지", QMessageBox.YesRole)
        directory_button = msg_box.addButton("하나의 디렉터리", QMessageBox.NoRole)
        # 디폴트 버튼을 제거함
        msg_box.setDefaultButton(None)
        msg_box.exec_()

        button_clicked = msg_box.clickedButton()

        if button_clicked == image_button:
            options = QtWidgets.QFileDialog.Options()
            file_dialog = QtWidgets.QFileDialog()
            file_dialog.setOptions(options)
            file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)  # 이미지 파일 하나 선택
            file_dialog.setViewMode(QtWidgets.QFileDialog.Detail)

            if file_dialog.exec_():
                selected_files = file_dialog.selectedFiles()
                if selected_files:
                    selected_path = selected_files[0]
                    self.detect_image_edit.setText(selected_path)
        elif button_clicked == directory_button:
            options = QtWidgets.QFileDialog.Options()
            file_dialog = QtWidgets.QFileDialog()
            file_dialog.setOptions(options)
            file_dialog.setFileMode(QtWidgets.QFileDialog.Directory)  # 디렉토리 선택
            file_dialog.setViewMode(QtWidgets.QFileDialog.Detail)
            if file_dialog.exec_():
                selected_directory = file_dialog.selectedFiles()
                if selected_directory:
                    selected_path = selected_directory[0]
                    self.detect_image_edit.setText(selected_path)

    def set_images(self, image_paths):
        # 현재 작업 디렉토리의 상위 디렉토리 가져오기
        current_directory = os.getcwd()
        parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
        tempdata_directory = os.path.join(parent_directory, "tempdata")

        # tempdata 디렉토리가 존재하면 삭제
        if os.path.exists(tempdata_directory):
            shutil.rmtree(tempdata_directory)

        # tempdata 디렉토리 생성
        os.mkdir(tempdata_directory)

        # image_paths의 모든 파일을 tempdata 디렉토리로 복사
        for image_path in image_paths:
            if os.path.isfile(image_path):
                shutil.copy(image_path, tempdata_directory)

        # self.detect_image_edit에 tempdata 디렉토리 경로 설정
        self.detect_image_edit.setText(tempdata_directory)

    def upload_model_dir(self):
        options = QFileDialog.Options()
        file_dialog = QFileDialog()
        file_dialog.setOptions(options)
        file_dialog.setFileMode(QFileDialog.Directory)  # 디렉터리 선택 모드로 설정
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.setDirectory("../EfficientAD-main/output")  # 여기서 기본 경로 설정

        if file_dialog.exec_():
            selected_directory = file_dialog.selectedFiles()

            if selected_directory:
                dirs = selected_directory[0].split("/")
                for i, dir in enumerate(dirs):
                    if dir == 'output':
                        if i + 1 < len(dirs):
                            self.model_dir_combo.setCurrentText(dirs[i + 1])
                        break

                self.model_dir_combo.setCurrentText(dirs[i + 1])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    anomaly_detection_window = QtWidgets.QWidget()
    ui = Ui_anomaly_detection_window()
    ui.setupUi(anomaly_detection_window)
    anomaly_detection_window.show()
    sys.exit(app.exec_())
