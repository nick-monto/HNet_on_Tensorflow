# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StructureSetup.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 566)
        self.config_GroupBox = QtWidgets.QGroupBox(Dialog)
        self.config_GroupBox.setGeometry(QtCore.QRect(10, 0, 461, 141))
        self.config_GroupBox.setObjectName("config_GroupBox")
        self.momentum_Label = QtWidgets.QLabel(self.config_GroupBox)
        self.momentum_Label.setGeometry(QtCore.QRect(10, 20, 90, 13))
        self.momentum_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.momentum_Label.setObjectName("momentum_Label")
        self.decayRate_label = QtWidgets.QLabel(self.config_GroupBox)
        self.decayRate_label.setGeometry(QtCore.QRect(10, 52, 90, 13))
        self.decayRate_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.decayRate_label.setObjectName("decayRate_label")
        self.initialWeightSD_Label = QtWidgets.QLabel(self.config_GroupBox)
        self.initialWeightSD_Label.setGeometry(QtCore.QRect(240, 52, 90, 13))
        self.initialWeightSD_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.initialWeightSD_Label.setObjectName("initialWeightSD_Label")
        self.momentum_LineEdit = QtWidgets.QLineEdit(self.config_GroupBox)
        self.momentum_LineEdit.setGeometry(QtCore.QRect(110, 18, 110, 20))
        self.momentum_LineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.momentum_LineEdit.setObjectName("momentum_LineEdit")
        self.decayRate_LineEdit = QtWidgets.QLineEdit(self.config_GroupBox)
        self.decayRate_LineEdit.setGeometry(QtCore.QRect(110, 50, 110, 20))
        self.decayRate_LineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.decayRate_LineEdit.setObjectName("decayRate_LineEdit")
        self.initalWeightSD_LineEdit = QtWidgets.QLineEdit(self.config_GroupBox)
        self.initalWeightSD_LineEdit.setGeometry(QtCore.QRect(340, 50, 110, 20))
        self.initalWeightSD_LineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.initalWeightSD_LineEdit.setObjectName("initalWeightSD_LineEdit")
        self.summit_Button = QtWidgets.QPushButton(self.config_GroupBox)
        self.summit_Button.setGeometry(QtCore.QRect(300, 100, 150, 31))
        self.summit_Button.setObjectName("summit_Button")
        self.deviceMode_Label = QtWidgets.QLabel(self.config_GroupBox)
        self.deviceMode_Label.setGeometry(QtCore.QRect(10, 80, 90, 13))
        self.deviceMode_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.deviceMode_Label.setObjectName("deviceMode_Label")
        self.deviceMode_Frame = QtWidgets.QFrame(self.config_GroupBox)
        self.deviceMode_Frame.setGeometry(QtCore.QRect(110, 80, 111, 21))
        self.deviceMode_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.deviceMode_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.deviceMode_Frame.setObjectName("deviceMode_Frame")
        self.deviceModeGPU_RadioButton = QtWidgets.QRadioButton(self.deviceMode_Frame)
        self.deviceModeGPU_RadioButton.setGeometry(QtCore.QRect(60, 0, 50, 17))
        self.deviceModeGPU_RadioButton.setObjectName("deviceModeGPU_RadioButton")
        self.deviceModeCPU_RadioButton = QtWidgets.QRadioButton(self.deviceMode_Frame)
        self.deviceModeCPU_RadioButton.setGeometry(QtCore.QRect(10, 0, 50, 17))
        self.deviceModeCPU_RadioButton.setChecked(True)
        self.deviceModeCPU_RadioButton.setObjectName("deviceModeCPU_RadioButton")
        self.learningRate_LineEdit = QtWidgets.QLineEdit(self.config_GroupBox)
        self.learningRate_LineEdit.setGeometry(QtCore.QRect(340, 20, 110, 20))
        self.learningRate_LineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.learningRate_LineEdit.setObjectName("learningRate_LineEdit")
        self.learningRate_Label = QtWidgets.QLabel(self.config_GroupBox)
        self.learningRate_Label.setGeometry(QtCore.QRect(240, 22, 90, 13))
        self.learningRate_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.learningRate_Label.setObjectName("learningRate_Label")
        self.structureSave_Button = QtWidgets.QPushButton(Dialog)
        self.structureSave_Button.setGeometry(QtCore.QRect(10, 530, 120, 30))
        self.structureSave_Button.setObjectName("structureSave_Button")
        self.structureLoad_Button = QtWidgets.QPushButton(Dialog)
        self.structureLoad_Button.setGeometry(QtCore.QRect(180, 530, 120, 30))
        self.structureLoad_Button.setObjectName("structureLoad_Button")
        self.exit_Button = QtWidgets.QPushButton(Dialog)
        self.exit_Button.setGeometry(QtCore.QRect(350, 530, 120, 30))
        self.exit_Button.setObjectName("exit_Button")
        self.structureWidget = QtWidgets.QTabWidget(Dialog)
        self.structureWidget.setGeometry(QtCore.QRect(10, 340, 461, 181))
        self.structureWidget.setObjectName("structureWidget")
        self.basicStructureBP_Tap = QtWidgets.QWidget()
        self.basicStructureBP_Tap.setObjectName("basicStructureBP_Tap")
        self.structureBPMake_Button = QtWidgets.QPushButton(self.basicStructureBP_Tap)
        self.structureBPMake_Button.setGeometry(QtCore.QRect(300, 120, 150, 31))
        self.structureBPMake_Button.setObjectName("structureBPMake_Button")
        self.structureBPHiddenLayerSize_LineEdit = QtWidgets.QLineEdit(self.basicStructureBP_Tap)
        self.structureBPHiddenLayerSize_LineEdit.setEnabled(True)
        self.structureBPHiddenLayerSize_LineEdit.setGeometry(QtCore.QRect(120, 40, 155, 20))
        self.structureBPHiddenLayerSize_LineEdit.setObjectName("structureBPHiddenLayerSize_LineEdit")
        self.structureBPHiddenLayerSize_Label = QtWidgets.QLabel(self.basicStructureBP_Tap)
        self.structureBPHiddenLayerSize_Label.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.structureBPHiddenLayerSize_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.structureBPHiddenLayerSize_Label.setObjectName("structureBPHiddenLayerSize_Label")
        self.structureBPInputLayerSize_LineEdit = QtWidgets.QLineEdit(self.basicStructureBP_Tap)
        self.structureBPInputLayerSize_LineEdit.setEnabled(True)
        self.structureBPInputLayerSize_LineEdit.setGeometry(QtCore.QRect(120, 10, 155, 20))
        self.structureBPInputLayerSize_LineEdit.setObjectName("structureBPInputLayerSize_LineEdit")
        self.structureBPOutputLayerSize_Label = QtWidgets.QLabel(self.basicStructureBP_Tap)
        self.structureBPOutputLayerSize_Label.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.structureBPOutputLayerSize_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.structureBPOutputLayerSize_Label.setObjectName("structureBPOutputLayerSize_Label")
        self.structureBPInputLayerSize_Label = QtWidgets.QLabel(self.basicStructureBP_Tap)
        self.structureBPInputLayerSize_Label.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.structureBPInputLayerSize_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.structureBPInputLayerSize_Label.setObjectName("structureBPInputLayerSize_Label")
        self.structureBPOutputLayerSize_LineEdit = QtWidgets.QLineEdit(self.basicStructureBP_Tap)
        self.structureBPOutputLayerSize_LineEdit.setEnabled(True)
        self.structureBPOutputLayerSize_LineEdit.setGeometry(QtCore.QRect(120, 70, 155, 20))
        self.structureBPOutputLayerSize_LineEdit.setObjectName("structureBPOutputLayerSize_LineEdit")
        self.structureWidget.addTab(self.basicStructureBP_Tap, "")
        self.basicStructureBPTT_Tap = QtWidgets.QWidget()
        self.basicStructureBPTT_Tap.setObjectName("basicStructureBPTT_Tap")
        self.structureBPTTMake_Button = QtWidgets.QPushButton(self.basicStructureBPTT_Tap)
        self.structureBPTTMake_Button.setGeometry(QtCore.QRect(300, 120, 150, 31))
        self.structureBPTTMake_Button.setObjectName("structureBPTTMake_Button")
        self.structureBPTTHiddenLayerSize_LineEdit = QtWidgets.QLineEdit(self.basicStructureBPTT_Tap)
        self.structureBPTTHiddenLayerSize_LineEdit.setEnabled(True)
        self.structureBPTTHiddenLayerSize_LineEdit.setGeometry(QtCore.QRect(120, 40, 155, 20))
        self.structureBPTTHiddenLayerSize_LineEdit.setObjectName("structureBPTTHiddenLayerSize_LineEdit")
        self.structureBPTTHiddenLayerSize_Label = QtWidgets.QLabel(self.basicStructureBPTT_Tap)
        self.structureBPTTHiddenLayerSize_Label.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.structureBPTTHiddenLayerSize_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.structureBPTTHiddenLayerSize_Label.setObjectName("structureBPTTHiddenLayerSize_Label")
        self.structureBPTTInputLayerSize_LineEdit = QtWidgets.QLineEdit(self.basicStructureBPTT_Tap)
        self.structureBPTTInputLayerSize_LineEdit.setEnabled(True)
        self.structureBPTTInputLayerSize_LineEdit.setGeometry(QtCore.QRect(120, 10, 155, 20))
        self.structureBPTTInputLayerSize_LineEdit.setObjectName("structureBPTTInputLayerSize_LineEdit")
        self.structureBPTTOutputLayerSize_Label = QtWidgets.QLabel(self.basicStructureBPTT_Tap)
        self.structureBPTTOutputLayerSize_Label.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.structureBPTTOutputLayerSize_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.structureBPTTOutputLayerSize_Label.setObjectName("structureBPTTOutputLayerSize_Label")
        self.structureBPTTInputLayerSize_Label = QtWidgets.QLabel(self.basicStructureBPTT_Tap)
        self.structureBPTTInputLayerSize_Label.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.structureBPTTInputLayerSize_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.structureBPTTInputLayerSize_Label.setObjectName("structureBPTTInputLayerSize_Label")
        self.structureBPTTOutputLayerSize_LineEdit = QtWidgets.QLineEdit(self.basicStructureBPTT_Tap)
        self.structureBPTTOutputLayerSize_LineEdit.setEnabled(True)
        self.structureBPTTOutputLayerSize_LineEdit.setGeometry(QtCore.QRect(120, 70, 155, 20))
        self.structureBPTTOutputLayerSize_LineEdit.setObjectName("structureBPTTOutputLayerSize_LineEdit")
        self.structureBPTTTick_LineEdit = QtWidgets.QLineEdit(self.basicStructureBPTT_Tap)
        self.structureBPTTTick_LineEdit.setEnabled(True)
        self.structureBPTTTick_LineEdit.setGeometry(QtCore.QRect(120, 100, 155, 20))
        self.structureBPTTTick_LineEdit.setObjectName("structureBPTTTick_LineEdit")
        self.structureBPTTTick_Label = QtWidgets.QLabel(self.basicStructureBPTT_Tap)
        self.structureBPTTTick_Label.setGeometry(QtCore.QRect(10, 100, 101, 16))
        self.structureBPTTTick_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.structureBPTTTick_Label.setObjectName("structureBPTTTick_Label")
        self.structureWidget.addTab(self.basicStructureBPTT_Tap, "")
        self.basicStructureSRN_Tap = QtWidgets.QWidget()
        self.basicStructureSRN_Tap.setObjectName("basicStructureSRN_Tap")
        self.structureSRNMake_Button = QtWidgets.QPushButton(self.basicStructureSRN_Tap)
        self.structureSRNMake_Button.setGeometry(QtCore.QRect(300, 120, 150, 31))
        self.structureSRNMake_Button.setObjectName("structureSRNMake_Button")
        self.structureSRNOutputLayerSize_LineEdit = QtWidgets.QLineEdit(self.basicStructureSRN_Tap)
        self.structureSRNOutputLayerSize_LineEdit.setEnabled(True)
        self.structureSRNOutputLayerSize_LineEdit.setGeometry(QtCore.QRect(120, 70, 155, 20))
        self.structureSRNOutputLayerSize_LineEdit.setObjectName("structureSRNOutputLayerSize_LineEdit")
        self.structureSRNOutputLayerSize_Label = QtWidgets.QLabel(self.basicStructureSRN_Tap)
        self.structureSRNOutputLayerSize_Label.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.structureSRNOutputLayerSize_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.structureSRNOutputLayerSize_Label.setObjectName("structureSRNOutputLayerSize_Label")
        self.structureSRNHiddenLayerSize_Label = QtWidgets.QLabel(self.basicStructureSRN_Tap)
        self.structureSRNHiddenLayerSize_Label.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.structureSRNHiddenLayerSize_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.structureSRNHiddenLayerSize_Label.setObjectName("structureSRNHiddenLayerSize_Label")
        self.structureSRNHiddenLayerSize_LineEdit = QtWidgets.QLineEdit(self.basicStructureSRN_Tap)
        self.structureSRNHiddenLayerSize_LineEdit.setEnabled(True)
        self.structureSRNHiddenLayerSize_LineEdit.setGeometry(QtCore.QRect(120, 40, 155, 20))
        self.structureSRNHiddenLayerSize_LineEdit.setObjectName("structureSRNHiddenLayerSize_LineEdit")
        self.structureSRNInputLayerSize_LineEdit = QtWidgets.QLineEdit(self.basicStructureSRN_Tap)
        self.structureSRNInputLayerSize_LineEdit.setEnabled(True)
        self.structureSRNInputLayerSize_LineEdit.setGeometry(QtCore.QRect(120, 10, 155, 20))
        self.structureSRNInputLayerSize_LineEdit.setObjectName("structureSRNInputLayerSize_LineEdit")
        self.structureSRNInputLayerSize_Label = QtWidgets.QLabel(self.basicStructureSRN_Tap)
        self.structureSRNInputLayerSize_Label.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.structureSRNInputLayerSize_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.structureSRNInputLayerSize_Label.setObjectName("structureSRNInputLayerSize_Label")
        self.structureWidget.addTab(self.basicStructureSRN_Tap, "")
        self.basicStructureCustom_Tap = QtWidgets.QWidget()
        self.basicStructureCustom_Tap.setObjectName("basicStructureCustom_Tap")
        self.customLayer_GroupBox = QtWidgets.QGroupBox(self.basicStructureCustom_Tap)
        self.customLayer_GroupBox.setGeometry(QtCore.QRect(0, 0, 221, 151))
        self.customLayer_GroupBox.setObjectName("customLayer_GroupBox")
        self.layerAdd_Button = QtWidgets.QPushButton(self.customLayer_GroupBox)
        self.layerAdd_Button.setGeometry(QtCore.QRect(10, 110, 201, 31))
        self.layerAdd_Button.setObjectName("layerAdd_Button")
        self.layerUnit_LineEdit = QtWidgets.QLineEdit(self.customLayer_GroupBox)
        self.layerUnit_LineEdit.setGeometry(QtCore.QRect(60, 50, 150, 20))
        self.layerUnit_LineEdit.setObjectName("layerUnit_LineEdit")
        self.layerName_LineEdit = QtWidgets.QLineEdit(self.customLayer_GroupBox)
        self.layerName_LineEdit.setGeometry(QtCore.QRect(60, 20, 150, 20))
        self.layerName_LineEdit.setObjectName("layerName_LineEdit")
        self.layerUnit_Label = QtWidgets.QLabel(self.customLayer_GroupBox)
        self.layerUnit_Label.setGeometry(QtCore.QRect(10, 50, 40, 16))
        self.layerUnit_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.layerUnit_Label.setObjectName("layerUnit_Label")
        self.layerName_Label = QtWidgets.QLabel(self.customLayer_GroupBox)
        self.layerName_Label.setGeometry(QtCore.QRect(10, 20, 40, 16))
        self.layerName_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.layerName_Label.setObjectName("layerName_Label")
        self.customConnection_GroupBox = QtWidgets.QGroupBox(self.basicStructureCustom_Tap)
        self.customConnection_GroupBox.setGeometry(QtCore.QRect(230, 0, 221, 151))
        self.customConnection_GroupBox.setObjectName("customConnection_GroupBox")
        self.connectionAdd_Button = QtWidgets.QPushButton(self.customConnection_GroupBox)
        self.connectionAdd_Button.setGeometry(QtCore.QRect(10, 110, 201, 30))
        self.connectionAdd_Button.setObjectName("connectionAdd_Button")
        self.connectionFrom_ComboBox = QtWidgets.QComboBox(self.customConnection_GroupBox)
        self.connectionFrom_ComboBox.setGeometry(QtCore.QRect(60, 50, 150, 22))
        self.connectionFrom_ComboBox.setObjectName("connectionFrom_ComboBox")
        self.connectionName_Label = QtWidgets.QLabel(self.customConnection_GroupBox)
        self.connectionName_Label.setGeometry(QtCore.QRect(10, 20, 40, 16))
        self.connectionName_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.connectionName_Label.setObjectName("connectionName_Label")
        self.connectionName_LineEdit = QtWidgets.QLineEdit(self.customConnection_GroupBox)
        self.connectionName_LineEdit.setGeometry(QtCore.QRect(60, 20, 150, 20))
        self.connectionName_LineEdit.setObjectName("connectionName_LineEdit")
        self.connectionFrom_Label = QtWidgets.QLabel(self.customConnection_GroupBox)
        self.connectionFrom_Label.setGeometry(QtCore.QRect(10, 50, 40, 16))
        self.connectionFrom_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.connectionFrom_Label.setObjectName("connectionFrom_Label")
        self.connectionTo_ComboBox = QtWidgets.QComboBox(self.customConnection_GroupBox)
        self.connectionTo_ComboBox.setGeometry(QtCore.QRect(60, 80, 150, 22))
        self.connectionTo_ComboBox.setObjectName("connectionTo_ComboBox")
        self.connectionTo_Label = QtWidgets.QLabel(self.customConnection_GroupBox)
        self.connectionTo_Label.setGeometry(QtCore.QRect(10, 80, 40, 16))
        self.connectionTo_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.connectionTo_Label.setObjectName("connectionTo_Label")
        self.structureWidget.addTab(self.basicStructureCustom_Tap, "")
        self.status_GroupBox = QtWidgets.QGroupBox(Dialog)
        self.status_GroupBox.setGeometry(QtCore.QRect(10, 150, 461, 191))
        self.status_GroupBox.setTitle("")
        self.status_GroupBox.setObjectName("status_GroupBox")
        self.basicHiddenLayer_Label_3 = QtWidgets.QLabel(self.status_GroupBox)
        self.basicHiddenLayer_Label_3.setGeometry(QtCore.QRect(240, 0, 111, 16))
        self.basicHiddenLayer_Label_3.setObjectName("basicHiddenLayer_Label_3")
        self.basicHiddenLayer_Label_2 = QtWidgets.QLabel(self.status_GroupBox)
        self.basicHiddenLayer_Label_2.setGeometry(QtCore.QRect(10, 0, 111, 16))
        self.basicHiddenLayer_Label_2.setObjectName("basicHiddenLayer_Label_2")
        self.connectionDelete_Button = QtWidgets.QPushButton(self.status_GroupBox)
        self.connectionDelete_Button.setGeometry(QtCore.QRect(240, 150, 211, 30))
        self.connectionDelete_Button.setObjectName("connectionDelete_Button")
        self.layer_ListWidget = QtWidgets.QListWidget(self.status_GroupBox)
        self.layer_ListWidget.setGeometry(QtCore.QRect(10, 20, 211, 121))
        self.layer_ListWidget.setObjectName("layer_ListWidget")
        self.connection_ListWidget = QtWidgets.QListWidget(self.status_GroupBox)
        self.connection_ListWidget.setGeometry(QtCore.QRect(240, 20, 211, 121))
        self.connection_ListWidget.setObjectName("connection_ListWidget")
        self.layerDelete_Button = QtWidgets.QPushButton(self.status_GroupBox)
        self.layerDelete_Button.setGeometry(QtCore.QRect(10, 150, 211, 30))
        self.layerDelete_Button.setObjectName("layerDelete_Button")

        self.retranslateUi(Dialog)
        self.structureWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Structure Setup"))
        self.config_GroupBox.setTitle(_translate("Dialog", "Simulator Config"))
        self.momentum_Label.setText(_translate("Dialog", "Momentum"))
        self.decayRate_label.setText(_translate("Dialog", "Decay Rate"))
        self.initialWeightSD_Label.setText(_translate("Dialog", "Initial Weight SD"))
        self.momentum_LineEdit.setText(_translate("Dialog", "0.9"))
        self.decayRate_LineEdit.setText(_translate("Dialog", "0"))
        self.initalWeightSD_LineEdit.setText(_translate("Dialog", "0.001"))
        self.summit_Button.setText(_translate("Dialog", "Summit"))
        self.deviceMode_Label.setText(_translate("Dialog", "Device Mode"))
        self.deviceModeGPU_RadioButton.setText(_translate("Dialog", "GPU"))
        self.deviceModeCPU_RadioButton.setText(_translate("Dialog", "CPU"))
        self.learningRate_LineEdit.setText(_translate("Dialog", "0.01"))
        self.learningRate_Label.setText(_translate("Dialog", "Learning Rate"))
        self.structureSave_Button.setText(_translate("Dialog", "Structure Save"))
        self.structureLoad_Button.setText(_translate("Dialog", "Structure Load"))
        self.exit_Button.setText(_translate("Dialog", "Exit"))
        self.structureBPMake_Button.setText(_translate("Dialog", "Make"))
        self.structureBPHiddenLayerSize_Label.setText(_translate("Dialog", "Hidden Layer Size"))
        self.structureBPOutputLayerSize_Label.setText(_translate("Dialog", "Output Layer Size"))
        self.structureBPInputLayerSize_Label.setText(_translate("Dialog", "Input Layer Size"))
        self.structureWidget.setTabText(self.structureWidget.indexOf(self.basicStructureBP_Tap), _translate("Dialog", "Back-Propagation"))
        self.structureBPTTMake_Button.setText(_translate("Dialog", "Make"))
        self.structureBPTTHiddenLayerSize_Label.setText(_translate("Dialog", "Hidden Layer Size"))
        self.structureBPTTOutputLayerSize_Label.setText(_translate("Dialog", "Output Layer Size"))
        self.structureBPTTInputLayerSize_Label.setText(_translate("Dialog", "Input Layer Size"))
        self.structureBPTTTick_Label.setText(_translate("Dialog", "Tick"))
        self.structureWidget.setTabText(self.structureWidget.indexOf(self.basicStructureBPTT_Tap), _translate("Dialog", "BP through Time"))
        self.structureSRNMake_Button.setText(_translate("Dialog", "Make"))
        self.structureSRNOutputLayerSize_Label.setText(_translate("Dialog", "Output Layer Size"))
        self.structureSRNHiddenLayerSize_Label.setText(_translate("Dialog", "Hidden Layer Size"))
        self.structureSRNInputLayerSize_Label.setText(_translate("Dialog", "Input Layer Size"))
        self.structureWidget.setTabText(self.structureWidget.indexOf(self.basicStructureSRN_Tap), _translate("Dialog", "SRN"))
        self.customLayer_GroupBox.setTitle(_translate("Dialog", "Layer"))
        self.layerAdd_Button.setText(_translate("Dialog", "Add"))
        self.layerUnit_Label.setText(_translate("Dialog", "Unit"))
        self.layerName_Label.setText(_translate("Dialog", "Name"))
        self.customConnection_GroupBox.setTitle(_translate("Dialog", "Connection"))
        self.connectionAdd_Button.setText(_translate("Dialog", "Add"))
        self.connectionName_Label.setText(_translate("Dialog", "Name"))
        self.connectionFrom_Label.setText(_translate("Dialog", "From"))
        self.connectionTo_Label.setText(_translate("Dialog", "To"))
        self.structureWidget.setTabText(self.structureWidget.indexOf(self.basicStructureCustom_Tap), _translate("Dialog", "Custom"))
        self.basicHiddenLayer_Label_3.setText(_translate("Dialog", "Connection Status"))
        self.basicHiddenLayer_Label_2.setText(_translate("Dialog", "Layer Status"))
        self.connectionDelete_Button.setText(_translate("Dialog", "Delete"))
        self.layerDelete_Button.setText(_translate("Dialog", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

