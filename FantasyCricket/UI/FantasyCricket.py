# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FantasyCricket.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from UI.EvaluateTeam import Ui_Dialog


class Ui_FantasyCricket(object):
    def setupUi(self, FantasyCricket):
        FantasyCricket.setObjectName("FantasyCricket")
        #FantasyCricket.resize(800, 600)
        FantasyCricket.setFixedSize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FantasyCricket.sizePolicy().hasHeightForWidth())
        FantasyCricket.setSizePolicy(sizePolicy)
        FantasyCricket.setBaseSize(QtCore.QSize(600, 400))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        FantasyCricket.setFont(font)
        FantasyCricket.setAutoFillBackground(False)
        FantasyCricket.setStyleSheet("background-color: rgb(252, 252, 252);")
        FantasyCricket.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(FantasyCricket)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(110, 140, 290, 340))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rbat = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbat.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbat.sizePolicy().hasHeightForWidth())
        self.rbat.setSizePolicy(sizePolicy)
        self.rbat.setBaseSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.rbat.setFont(font)
        self.rbat.setStyleSheet("color: rgb(16, 16, 16);")
        self.rbat.setIconSize(QtCore.QSize(15, 12))
        self.rbat.setObjectName("rbat")
        self.horizontalLayout_4.addWidget(self.rbat)
        spacerItem = QtWidgets.QSpacerItem(5, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.rbow = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbow.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbow.sizePolicy().hasHeightForWidth())
        self.rbow.setSizePolicy(sizePolicy)
        self.rbow.setBaseSize(QtCore.QSize(10, 5))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.rbow.setFont(font)
        self.rbow.setStyleSheet("color: rgb(16, 16, 16);")
        self.rbow.setObjectName("rbow")
        self.horizontalLayout_4.addWidget(self.rbow)
        spacerItem1 = QtWidgets.QSpacerItem(5, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.rar = QtWidgets.QRadioButton(self.groupBox_2)
        self.rar.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rar.sizePolicy().hasHeightForWidth())
        self.rar.setSizePolicy(sizePolicy)
        self.rar.setBaseSize(QtCore.QSize(10, 5))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.rar.setFont(font)
        self.rar.setStyleSheet("color: rgb(16, 16, 16);")
        self.rar.setObjectName("rar")
        self.horizontalLayout_4.addWidget(self.rar)
        spacerItem2 = QtWidgets.QSpacerItem(5, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.rwk = QtWidgets.QRadioButton(self.groupBox_2)
        self.rwk.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rwk.sizePolicy().hasHeightForWidth())
        self.rwk.setSizePolicy(sizePolicy)
        self.rwk.setBaseSize(QtCore.QSize(10, 5))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(6)
        self.rwk.setFont(font)
        self.rwk.setStyleSheet("color: rgb(16, 16, 16);")
        self.rwk.setObjectName("rwk")
        self.horizontalLayout_4.addWidget(self.rwk)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.avlist = QtWidgets.QListWidget(self.groupBox_2)
        self.avlist.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.avlist.setObjectName("avlist")
        self.verticalLayout.addWidget(self.avlist)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(470, 140, 290, 340))
        self.groupBox_3.setStyleSheet("border-color: rgb(107, 107, 107);")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.teamname = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        self.teamname.setFont(font)
        self.teamname.setAutoFillBackground(False)
        self.teamname.setStyleSheet("color: rgb(52, 208, 255);")
        self.teamname.setFrame(False)
        self.teamname.setObjectName("teamname")
        self.horizontalLayout_5.addWidget(self.teamname)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.selectlist = QtWidgets.QListWidget(self.groupBox_3)
        self.selectlist.setStyleSheet("border-color: rgb(15, 15, 15);")
        self.selectlist.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.selectlist.setObjectName("selectlist")
        self.verticalLayout_2.addWidget(self.selectlist)
##        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_3)
##        self.listWidget_2.setFrameShape(QtWidgets.QFrame.NoFrame)
##        self.listWidget_2.setObjectName("listWidget_2")
##        self.verticalLayout_2.addWidget(self.listWidget_2)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 100, 231, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.avpoints = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        self.avpoints.setFont(font)
        self.avpoints.setAutoFillBackground(False)
        self.avpoints.setStyleSheet("color: rgb(52, 208, 255);")
        self.avpoints.setFrame(False)
        self.avpoints.setObjectName("avpoints")
        self.horizontalLayout.addWidget(self.avpoints)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(470, 100, 221, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.usedpoints = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        self.usedpoints.setFont(font)
        self.usedpoints.setAutoFillBackground(False)
        self.usedpoints.setStyleSheet("color: rgb(52, 208, 255);")
        self.usedpoints.setFrame(False)
        self.usedpoints.setObjectName("usedpoints")
        self.horizontalLayout_2.addWidget(self.usedpoints)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(60, 10, 700, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(134, 134, 134);\n"
"color: rgb(78, 78, 78);")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))#changed
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(33, 33, 33);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.bat = QtWidgets.QLineEdit(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        self.bat.setFont(font)
        self.bat.setStyleSheet("\n"
"color: rgb(52, 208, 255);")
        self.bat.setFrame(False)
        self.bat.setObjectName("bat")
        self.horizontalLayout_6.addWidget(self.bat)
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.bowl = QtWidgets.QLineEdit(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        self.bowl.setFont(font)
        self.bowl.setStyleSheet("color: rgb(52, 208, 255);")
        self.bowl.setFrame(False)
        self.bowl.setObjectName("bowl")
        self.horizontalLayout_6.addWidget(self.bowl)
        spacerItem10 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.ar = QtWidgets.QLineEdit(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        self.ar.setFont(font)
        self.ar.setStyleSheet("color: rgb(52, 208, 255);")
        self.ar.setFrame(False)
        self.ar.setObjectName("ar")
        self.horizontalLayout_6.addWidget(self.ar)
        spacerItem11 = QtWidgets.QSpacerItem(10, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        spacerItem12 = QtWidgets.QSpacerItem(10, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.wk = QtWidgets.QLineEdit(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(7)
        self.wk.setFont(font)
        self.wk.setStyleSheet("color: rgb(52, 208, 255);")
        self.wk.setFrame(False)
        self.wk.setObjectName("wk")
        self.horizontalLayout_6.addWidget(self.wk)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(420, 300, 35, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        FantasyCricket.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FantasyCricket)
        #addedd stylesheet
        self.menubar.setStyleSheet("""
                                   
                                    QMenuBar::item {
                                    background-color: rgb(174, 174, 174);
                                    border: 1px solid ;
                                         
                                    }

   
                                        """)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.menuManage_Teams.setFont(font)
        #self.menuManage_Teams.setStyleSheet("background-color: rgb(175, 175, 175);")
        #added styleshheet to menu items
        self.menuManage_Teams.setStyleSheet("""
                                    QMenu{
                                    
                                    border: 1px solid ;
                                         
                                    }
                                   
                                    QMenu::item {
                                    background-color: rgb(174, 174, 174);
                                   
                                         
                                    }

   
                                        """)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        FantasyCricket.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FantasyCricket)
        self.statusbar.setObjectName("statusbar")
        FantasyCricket.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(FantasyCricket)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.actionNEW_Team.setFont(font)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(FantasyCricket)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.actionOPEN_Team.setFont(font)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(FantasyCricket)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.actionSAVE_Team.setFont(font)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_TEAM = QtWidgets.QAction(FantasyCricket)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.actionEVALUATE_TEAM.setFont(font)
        self.actionEVALUATE_TEAM.setObjectName("actionEVALUATE_TEAM")        
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_TEAM)
        #self.actionEVALUATE_TEAM.triggered.connect(self.help_window)#adding trigger
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(FantasyCricket)
        QtCore.QMetaObject.connectSlotsByName(FantasyCricket)
        
##    def help_window(self):        
##          dialog=QtWidgets.QDialog()
##          dialog.ui=Ui_Dialog()
##          dialog.ui.setupUi(dialog)
##          dialog.exec_()
##          dialog.show()
          
    def retranslateUi(self, FantasyCricket):
        _translate = QtCore.QCoreApplication.translate
        FantasyCricket.setWindowTitle(_translate("FantasyCricket", "Fantasy Cricket"))
        self.rbat.setText(_translate("FantasyCricket", "BAT"))
        self.rbow.setText(_translate("FantasyCricket", "BOW"))
        self.rar.setText(_translate("FantasyCricket", "AR"))
        self.rwk.setText(_translate("FantasyCricket", " WK"))
        self.label_8.setText(_translate("FantasyCricket", "Team Name"))
        self.teamname.setText(_translate("FantasyCricket", "####"))
        self.label_6.setText(_translate("FantasyCricket", "Points Available"))
        self.avpoints.setText(_translate("FantasyCricket", "####"))
        self.label_7.setText(_translate("FantasyCricket", "Points Used"))
        self.usedpoints.setText(_translate("FantasyCricket", "####"))
        self.label.setText(_translate("FantasyCricket", "Your Selections"))
        self.label_2.setText(_translate("FantasyCricket", "Batsmen(BAT)"))
        self.bat.setText(_translate("FantasyCricket", "##"))
        self.label_3.setText(_translate("FantasyCricket", "Bowlers(BOW)"))
        self.bowl.setText(_translate("FantasyCricket", "##"))
        self.label_4.setText(_translate("FantasyCricket", "All-rounders(AR)"))
        self.ar.setText(_translate("FantasyCricket", " ##"))
        self.label_5.setText(_translate("FantasyCricket", "Wicket-keeper(WK)"))
        self.wk.setText(_translate("FantasyCricket", "##"))
        self.label_9.setText(_translate("FantasyCricket", ">"))
        self.menuManage_Teams.setTitle(_translate("FantasyCricket", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("FantasyCricket", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("FantasyCricket", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("FantasyCricket", "SAVE Team"))
        self.actionEVALUATE_TEAM.setText(_translate("FantasyCricket", "EVALUATE Team"))


##if __name__ == "__main__":
##    import sys
##    app = QtWidgets.QApplication(sys.argv)
##    FantasyCricket = QtWidgets.QMainWindow()
##    ui = Ui_FantasyCricket()
##    ui.setupUi(FantasyCricket)
##    FantasyCricket.show()
##    sys.exit(app.exec_())
