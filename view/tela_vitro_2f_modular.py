# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_vitro_2f_modular.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_vitro_2f_modular(object):
    def setupUi(self, MainWindow_vitro_2f_modular):
        MainWindow_vitro_2f_modular.setObjectName("MainWindow_vitro_2f_modular")
        MainWindow_vitro_2f_modular.resize(920, 380)
        MainWindow_vitro_2f_modular.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow_vitro_2f_modular)
        self.centralwidget.setObjectName("centralwidget")
        self.label_vt_2f_modular = QtWidgets.QLabel(self.centralwidget)
        self.label_vt_2f_modular.setGeometry(QtCore.QRect(260, 10, 280, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_vt_2f_modular.setFont(font)
        self.label_vt_2f_modular.setObjectName("label_vt_2f_modular")
        self.label_modelo = QtWidgets.QLabel(self.centralwidget)
        self.label_modelo.setGeometry(QtCore.QRect(10, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_modelo.setFont(font)
        self.label_modelo.setObjectName("label_modelo")
        self.comboBox_vt_2f_modular = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_vt_2f_modular.setGeometry(QtCore.QRect(80, 70, 531, 22))
        self.comboBox_vt_2f_modular.setObjectName("comboBox_vt_2f_modular")
        self.label_quantidade = QtWidgets.QLabel(self.centralwidget)
        self.label_quantidade.setGeometry(QtCore.QRect(10, 125, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_quantidade.setFont(font)
        self.label_quantidade.setObjectName("label_quantidade")
        self.lineEdit_quantidade = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_quantidade.setGeometry(QtCore.QRect(110, 120, 50, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_quantidade.setFont(font)
        self.lineEdit_quantidade.setMaxLength(3)
        self.lineEdit_quantidade.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_quantidade.setObjectName("lineEdit_quantidade")
        self.label_custo_total = QtWidgets.QLabel(self.centralwidget)
        self.label_custo_total.setGeometry(QtCore.QRect(10, 180, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_custo_total.setFont(font)
        self.label_custo_total.setObjectName("label_custo_total")
        self.label_margem_de_lucro = QtWidgets.QLabel(self.centralwidget)
        self.label_margem_de_lucro.setGeometry(QtCore.QRect(10, 230, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_margem_de_lucro.setFont(font)
        self.label_margem_de_lucro.setObjectName("label_margem_de_lucro")
        self.label_total_geral = QtWidgets.QLabel(self.centralwidget)
        self.label_total_geral.setGeometry(QtCore.QRect(10, 280, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_total_geral.setFont(font)
        self.label_total_geral.setObjectName("label_total_geral")
        self.lineEdit_custo_total = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_custo_total.setEnabled(False)
        self.lineEdit_custo_total.setGeometry(QtCore.QRect(100, 175, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_custo_total.setFont(font)
        self.lineEdit_custo_total.setObjectName("lineEdit_custo_total")
        self.lineEdit_margem_de_lucro = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_margem_de_lucro.setEnabled(False)
        self.lineEdit_margem_de_lucro.setGeometry(QtCore.QRect(150, 225, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_margem_de_lucro.setFont(font)
        self.lineEdit_margem_de_lucro.setReadOnly(False)
        self.lineEdit_margem_de_lucro.setObjectName("lineEdit_margem_de_lucro")
        self.lineEdit_total_geral = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_total_geral.setEnabled(False)
        self.lineEdit_total_geral.setGeometry(QtCore.QRect(100, 275, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_total_geral.setFont(font)
        self.lineEdit_total_geral.setObjectName("lineEdit_total_geral")
        self.pushButton_calcular = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calcular.setGeometry(QtCore.QRect(20, 340, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_calcular.setFont(font)
        self.pushButton_calcular.setObjectName("pushButton_calcular")
        self.pushButton_inserir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_inserir.setGeometry(QtCore.QRect(180, 340, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_inserir.setFont(font)
        self.pushButton_inserir.setObjectName("pushButton_inserir")
        self.pushButton_plano_corte = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plano_corte.setGeometry(QtCore.QRect(340, 340, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_plano_corte.setFont(font)
        self.pushButton_plano_corte.setObjectName("pushButton_plano_corte")
        self.pushButton_fechar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_fechar.setGeometry(QtCore.QRect(760, 340, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_fechar.setFont(font)
        self.pushButton_fechar.setObjectName("pushButton_fechar")
        self.graphicsView_imagem_produto = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_imagem_produto.setGeometry(QtCore.QRect(640, 30, 256, 281))
        self.graphicsView_imagem_produto.setObjectName("graphicsView_imagem_produto")
        self.frame_cor_aluminio = QtWidgets.QFrame(self.centralwidget)
        self.frame_cor_aluminio.setGeometry(QtCore.QRect(300, 110, 161, 111))
        self.frame_cor_aluminio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cor_aluminio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cor_aluminio.setObjectName("frame_cor_aluminio")
        self.radioButton_al_preto = QtWidgets.QRadioButton(self.frame_cor_aluminio)
        self.radioButton_al_preto.setGeometry(QtCore.QRect(10, 80, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_al_preto.setFont(font)
        self.radioButton_al_preto.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.radioButton_al_preto.setObjectName("radioButton_al_preto")
        self.label_cor_aluminio = QtWidgets.QLabel(self.frame_cor_aluminio)
        self.label_cor_aluminio.setGeometry(QtCore.QRect(10, 10, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_cor_aluminio.setFont(font)
        self.label_cor_aluminio.setObjectName("label_cor_aluminio")
        self.radioButton_al_branco = QtWidgets.QRadioButton(self.frame_cor_aluminio)
        self.radioButton_al_branco.setGeometry(QtCore.QRect(10, 40, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_al_branco.setFont(font)
        self.radioButton_al_branco.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.radioButton_al_branco.setChecked(True)
        self.radioButton_al_branco.setObjectName("radioButton_al_branco")
        self.frame_grade = QtWidgets.QFrame(self.centralwidget)
        self.frame_grade.setGeometry(QtCore.QRect(480, 110, 131, 111))
        self.frame_grade.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_grade.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grade.setObjectName("frame_grade")
        self.radioButton_com_grade = QtWidgets.QRadioButton(self.frame_grade)
        self.radioButton_com_grade.setGeometry(QtCore.QRect(10, 80, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_com_grade.setFont(font)
        self.radioButton_com_grade.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.radioButton_com_grade.setObjectName("radioButton_com_grade")
        self.label_grade = QtWidgets.QLabel(self.frame_grade)
        self.label_grade.setGeometry(QtCore.QRect(10, 10, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_grade.setFont(font)
        self.label_grade.setObjectName("label_grade")
        self.radioButton_sem_grade = QtWidgets.QRadioButton(self.frame_grade)
        self.radioButton_sem_grade.setGeometry(QtCore.QRect(10, 40, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_sem_grade.setFont(font)
        self.radioButton_sem_grade.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.radioButton_sem_grade.setChecked(True)
        self.radioButton_sem_grade.setObjectName("radioButton_sem_grade")
        MainWindow_vitro_2f_modular.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_vitro_2f_modular)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_vitro_2f_modular)

    def retranslateUi(self, MainWindow_vitro_2f_modular):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_vitro_2f_modular.setWindowTitle(_translate("MainWindow_vitro_2f_modular", ".::PERFILARE::. - Vitro 2 folhas - Linha Modular"))
        self.label_vt_2f_modular.setText(_translate("MainWindow_vitro_2f_modular", "VITRO 2 FOLHAS - LINHA MODULAR"))
        self.label_modelo.setText(_translate("MainWindow_vitro_2f_modular", "Modelo:"))
        self.label_quantidade.setText(_translate("MainWindow_vitro_2f_modular", "Quantidade:"))
        self.label_custo_total.setText(_translate("MainWindow_vitro_2f_modular", "Custo total:"))
        self.label_margem_de_lucro.setText(_translate("MainWindow_vitro_2f_modular", "Margem de Lucro:"))
        self.label_total_geral.setText(_translate("MainWindow_vitro_2f_modular", "Total Geral:"))
        self.pushButton_calcular.setText(_translate("MainWindow_vitro_2f_modular", "Calcular"))
        self.pushButton_inserir.setText(_translate("MainWindow_vitro_2f_modular", "Inserir"))
        self.pushButton_plano_corte.setText(_translate("MainWindow_vitro_2f_modular", "Plano de Corte"))
        self.pushButton_fechar.setText(_translate("MainWindow_vitro_2f_modular", "Fechar"))
        self.radioButton_al_preto.setText(_translate("MainWindow_vitro_2f_modular", "Preto"))
        self.label_cor_aluminio.setText(_translate("MainWindow_vitro_2f_modular", "Cor do Alumínio:"))
        self.radioButton_al_branco.setText(_translate("MainWindow_vitro_2f_modular", "Branco"))
        self.radioButton_com_grade.setText(_translate("MainWindow_vitro_2f_modular", "Com Grade"))
        self.label_grade.setText(_translate("MainWindow_vitro_2f_modular", "Grade:"))
        self.radioButton_sem_grade.setText(_translate("MainWindow_vitro_2f_modular", "Sem Grade"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_vitro_2f_modular = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_vitro_2f_modular()
    ui.setupUi(MainWindow_vitro_2f_modular)
    MainWindow_vitro_2f_modular.show()
    sys.exit(app.exec_())
