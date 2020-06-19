# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Tue Sep  3 16:33:22 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_DeepMedic2(object):
    def setupUi(self, DeepMedic2):
        DeepMedic2.setObjectName("DeepMedic2")
        DeepMedic2.resize(533, 541)
        DeepMedic2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralWidget = QtWidgets.QWidget(DeepMedic2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.session_combobox = QtWidgets.QComboBox(self.centralWidget)
        self.session_combobox.setObjectName("session_combobox")
        self.session_combobox.addItem("")
        self.session_combobox.addItem("")
        self.gridLayout.addWidget(self.session_combobox, 3, 1, 1, 1)
        self.load_path = QtWidgets.QLineEdit(self.centralWidget)
        self.load_path.setObjectName("load_path")
        self.gridLayout.addWidget(self.load_path, 7, 1, 1, 1)
        self.model_config_search_button = QtWidgets.QPushButton(self.centralWidget)
        self.model_config_search_button.setObjectName("model_config_search_button")
        self.gridLayout.addWidget(self.model_config_search_button, 1, 2, 1, 1)
        self.device_label = QtWidgets.QLabel(self.centralWidget)
        self.device_label.setObjectName("device_label")
        self.gridLayout.addWidget(self.device_label, 9, 0, 1, 1)
        self.train_config_path = QtWidgets.QLineEdit(self.centralWidget)
        self.train_config_path.setObjectName("train_config_path")
        self.gridLayout.addWidget(self.train_config_path, 5, 1, 1, 1)
        self.train_config_search_button = QtWidgets.QPushButton(self.centralWidget)
        self.train_config_search_button.setObjectName("train_config_search_button")
        self.gridLayout.addWidget(self.train_config_search_button, 5, 2, 1, 1)
        self.load_path_label = QtWidgets.QLabel(self.centralWidget)
        self.load_path_label.setObjectName("load_path_label")
        self.gridLayout.addWidget(self.load_path_label, 7, 0, 1, 1)
        self.device_combobox = QtWidgets.QComboBox(self.centralWidget)
        self.device_combobox.setObjectName("device_combobox")
        self.device_combobox.addItem("")
        self.device_combobox.addItem("")
        self.gridLayout.addWidget(self.device_combobox, 9, 1, 1, 1)
        self.train_config_label = QtWidgets.QLabel(self.centralWidget)
        self.train_config_label.setObjectName("train_config_label")
        self.gridLayout.addWidget(self.train_config_label, 5, 0, 1, 1)
        self.load_path_search_button = QtWidgets.QPushButton(self.centralWidget)
        self.load_path_search_button.setObjectName("load_path_search_button")
        self.gridLayout.addWidget(self.load_path_search_button, 7, 2, 1, 1)
        self.model_config_path = QtWidgets.QLineEdit(self.centralWidget)
        self.model_config_path.setObjectName("model_config_path")
        self.gridLayout.addWidget(self.model_config_path, 1, 1, 1, 1)
        self.resetopt_label = QtWidgets.QLabel(self.centralWidget)
        self.resetopt_label.setObjectName("resetopt_label")
        self.gridLayout.addWidget(self.resetopt_label, 8, 0, 1, 1)
        self.device_num_text = QtWidgets.QLineEdit(self.centralWidget)
        self.device_num_text.setEnabled(False)
        self.device_num_text.setObjectName("device_num_text")
        self.gridLayout.addWidget(self.device_num_text, 10, 1, 1, 1)
        self.model_config_label = QtWidgets.QLabel(self.centralWidget)
        self.model_config_label.setObjectName("model_config_label")
        self.gridLayout.addWidget(self.model_config_label, 1, 0, 1, 1)
        self.session_label = QtWidgets.QLabel(self.centralWidget)
        self.session_label.setObjectName("session_label")
        self.gridLayout.addWidget(self.session_label, 3, 0, 1, 1)
        self.resetopt_checkbox = QtWidgets.QCheckBox(self.centralWidget)
        self.resetopt_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.resetopt_checkbox.setText("")
        self.resetopt_checkbox.setObjectName("resetopt_checkbox")
        self.gridLayout.addWidget(self.resetopt_checkbox, 8, 1, 1, 1)
        self.device_num_label = QtWidgets.QLabel(self.centralWidget)
        self.device_num_label.setEnabled(False)
        self.device_num_label.setObjectName("device_num_label")
        self.gridLayout.addWidget(self.device_num_label, 10, 0, 1, 1)
        self.model_config_create_button = QtWidgets.QPushButton(self.centralWidget)
        self.model_config_create_button.setObjectName("model_config_create_button")
        self.gridLayout.addWidget(self.model_config_create_button, 1, 3, 1, 1)
        self.run_button = QtWidgets.QPushButton(self.centralWidget)
        self.run_button.setObjectName("run_button")
        self.gridLayout.addWidget(self.run_button, 14, 1, 1, 1)
        self.stop_button = QtWidgets.QPushButton(self.centralWidget)

        self.stop_button.setObjectName("stop_button")
        self.gridLayout.addWidget(self.stop_button, 14, 2, 1, 2)
        self.output_log = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.output_log.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.output_log.setObjectName("output_log")
        self.output_log.setMaximumBlockCount(10000)
        self.output_log.setReadOnly(True)
        self.gridLayout.addWidget(self.output_log, 16, 0, 1, 4)
        self.train_config_create_button = QtWidgets.QPushButton(self.centralWidget)
        self.train_config_create_button.setObjectName("train_config_create_button")
        self.gridLayout.addWidget(self.train_config_create_button, 5, 3, 1, 1)
        self.test_config_label = QtWidgets.QLabel(self.centralWidget)
        self.test_config_label.setObjectName("test_config_label")
        self.gridLayout.addWidget(self.test_config_label, 6, 0, 1, 1)
        self.test_config_path = QtWidgets.QLineEdit(self.centralWidget)
        self.test_config_path.setObjectName("test_config_path")
        self.gridLayout.addWidget(self.test_config_path, 6, 1, 1, 1)
        self.test_config_search_button = QtWidgets.QPushButton(self.centralWidget)
        self.test_config_search_button.setObjectName("test_config_search_button")
        self.gridLayout.addWidget(self.test_config_search_button, 6, 2, 1, 1)
        self.test_config_create_button = QtWidgets.QPushButton(self.centralWidget)
        self.test_config_create_button.setObjectName("test_config_create_button")
        self.gridLayout.addWidget(self.test_config_create_button, 6, 3, 1, 1)
        DeepMedic2.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(DeepMedic2)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 533, 22))
        self.menuBar.setObjectName("menuBar")
        DeepMedic2.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(DeepMedic2)
        self.mainToolBar.setObjectName("mainToolBar")
        DeepMedic2.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(DeepMedic2)
        self.statusBar.setObjectName("statusBar")
        DeepMedic2.setStatusBar(self.statusBar)

        self.retranslateUi(DeepMedic2)
        QtCore.QMetaObject.connectSlotsByName(DeepMedic2)

    def retranslateUi(self, DeepMedic2):
        DeepMedic2.setWindowTitle(QtWidgets.QApplication.translate("DeepMedic2", "DeepMedic2", None, -1))
        self.session_combobox.setItemText(0, QtWidgets.QApplication.translate("DeepMedic2", "Train", None, -1))
        self.session_combobox.setItemText(1, QtWidgets.QApplication.translate("DeepMedic2", "Test", None, -1))
        self.model_config_search_button.setText(QtWidgets.QApplication.translate("DeepMedic2", "Search", None, -1))
        self.device_label.setText(QtWidgets.QApplication.translate("DeepMedic2", "Device Type", None, -1))
        self.train_config_search_button.setText(QtWidgets.QApplication.translate("DeepMedic2", "Search", None, -1))
        self.load_path_label.setText(QtWidgets.QApplication.translate("DeepMedic2", "Saved Model Checkpoint Path", None, -1))
        self.device_combobox.setItemText(0, QtWidgets.QApplication.translate("DeepMedic2", "CPU", None, -1))
        self.device_combobox.setItemText(1, QtWidgets.QApplication.translate("DeepMedic2", "GPU", None, -1))
        self.train_config_label.setText(QtWidgets.QApplication.translate("DeepMedic2", "Train Configuration File", None, -1))
        self.load_path_search_button.setText(QtWidgets.QApplication.translate("DeepMedic2", "Search", None, -1))
        self.resetopt_label.setText(QtWidgets.QApplication.translate("DeepMedic2", "Reset Trainer Parameters", None, -1))
        self.model_config_label.setText(QtWidgets.QApplication.translate("DeepMedic2", "Model Configuration File", None, -1))
        self.session_label.setText(QtWidgets.QApplication.translate("DeepMedic2", "Session Type", None, -1))
        self.device_num_label.setText(QtWidgets.QApplication.translate("DeepMedic2", "Device Number(s)", None, -1))
        self.model_config_create_button.setText(QtWidgets.QApplication.translate("DeepMedic2", "Create", None, -1))
        self.run_button.setText(QtWidgets.QApplication.translate("DeepMedic2", "Run", None, -1))
        self.stop_button.setText(QtWidgets.QApplication.translate("DeepMedic2", "Stop", None, -1))
        self.train_config_create_button.setText(QtWidgets.QApplication.translate("DeepMedic2", "Create", None, -1))
        self.test_config_label.setText(QtWidgets.QApplication.translate("DeepMedic2", "Test Configuration File", None, -1))
        self.test_config_search_button.setText(QtWidgets.QApplication.translate("DeepMedic2", "Search", None, -1))
        self.test_config_create_button.setText(QtWidgets.QApplication.translate("DeepMedic2", "Create", None, -1))
