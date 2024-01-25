import sys
from PyQt6 import QtWidgets, uic
from splash import *
from PyQt6.QtWidgets import QMainWindow, QApplication
from dbconnection import adaptor
from PyQt6.QtCore import Qt,QObject,QSize
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QLineEdit, QSizeGrip,QFrame
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import sip


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("watersystem.ui", self)
        self.show()

        ####shadow effect
        #self.shadow=QGraphicsDropShadowEffect(self)
        #self.shadow.setBlurRadius(50)
        #self.shadow.setXOffset(0)
        #self.shadow.setYOffset(0)
        #self.shadow.setColor(QColor(0,92,157,550))
        #self.centralWidget.setGrapicsEffect(self.shadow)
        
        
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setWindowTitle("Water Monitoring System")
        self.setWindowIcon(QtGui.QIcon("icons/activity.svg"))

        QSizeGrip(self.size_grip)

        self.minimize_button.clicked.connect(lambda: self.showMinimized())
        self.close.clicked.connect(lambda: self.close())
        self.max.clicked.connect(lambda: self.Rest_or_max())
        self.open_close.clicked.connect(lambda: self.SideMenu())
        self.pushButton_6.clicked.connect(lambda: self.close())
        self.pushButton.clicked.connect(lambda: self.submit_complaint())

        self.pushButton_10.clicked.connect(
            lambda: self.callmain()
        )
        self.pushButton_11.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_4)
        )
        self.pushButton_14.clicked.connect(
            lambda: self.callsub()
        )
        self.pushButton_16.clicked.connect(
            lambda: self.callcom()
        )
        self.pushButton_7.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_7)
        )
        self.pushButton_8.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_3)
        )
        
        self.pushButton.clicked.connect(lambda: self.submit_complaint())
        self.pushButton_15.clicked.connect(lambda: self.submit_Subm())
        self.pushButton_12.clicked.connect(lambda: self.login())
        self.pushButton_13.clicked.connect(lambda: self.register())
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5))
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5))
        self.pushButton_9.clicked.connect(lambda: self.callGchat())
        self.pushButton_17.clicked.connect(lambda: self.callAchat())
        self.pushButton_18.clicked.connect(lambda: self.sendA())
        self.pushButton_19.clicked.connect(lambda: self.sendG())
        self.pushButton_2.clicked.connect(lambda: self.logout())

        # Image relaod
        self.open_close.setIcon(QtGui.QIcon("icons/align-left.svg"))
        self.pushButton_7.setIcon(QtGui.QIcon("icons/anchor.svg"))
        self.pushButton_8.setIcon(QtGui.QIcon("icons/user.svg"))
        #self.pushButton_9.setIcon(QtGui.QIcon("icons/settings.svg"))
        self.pushButton_6.setIcon(QtGui.QIcon("icons/external-link.svg"))
        self.pushButton_4.setIcon(QtGui.QIcon("icons/box.svg"))
        self.pushButton_10.setIcon(QtGui.QIcon("icons/home.svg"))
        self.pushButton_11.setIcon(QtGui.QIcon("icons/alert-triangle.svg"))
        self.pushButton_16.setIcon(QtGui.QIcon("icons/alert-octagon.svg"))
        self.pushButton_14.setIcon(QtGui.QIcon("icons/clipboard.svg"))
        self.pushButton.setIcon(QtGui.QIcon("icons/send.svg"))
        self.pushButton_18.setIcon(QtGui.QIcon("icons/send.svg"))
        self.pushButton_19.setIcon(QtGui.QIcon("icons/send.svg"))
        self.pushButton_17.setIcon(QtGui.QIcon("icons/gitlab.svg"))
        self.pushButton_9.setIcon(QtGui.QIcon("icons/feather.svg"))
        
        self.close.setIcon(QtGui.QIcon("icons/x.svg"))
        self.max.setIcon(QtGui.QIcon("icons/maximize-2.svg"))
        self.minimize_button.setIcon(QtGui.QIcon("icons/arrow-down.svg"))

        self.label_3.setPixmap(QPixmap("icons/droplet.svg"))
        
        myFont=QtGui.QFont()
        myFont.setBold(True)
        self.label.setFont(myFont)

        # set start page******************************************************
        self.stackedWidget.setCurrentWidget(self.page_1)

        # get water source info
        information = []
        information = adaptor.retrive_all()
        userinfo=[]
        #hide a button
        if not userinfo:  
            pass
            self.hide()
        else:
            pass

        # load  mainframes###############################################################################################################################33
        self.loadmain()
           
            
        zones=["Urban","Semi_Urban","Rural"]
        AccType=["MOD","User"]
        
            
        # load QcomboBox
        for i in range((len(information)-1)):
            self.comboBox_2.addItem(information[i][1])
        for i in range(11):
            self.comboBox_3.addItem(str(i))
        for i in range(11):
            self.comboBox_6.addItem(str(i))
            
        for i in range((len(zones))):
            self.comboBox_5.addItem(str(zones[i]))
            
        for i in range((len(AccType))):
            self.comboBox_4.addItem(str(AccType[i]))
            
        
            

    # Slots
    
    
    def hide(self):
        self.pushButton_11.hide()
        self.pushButton_14.hide()
        self.pushButton_7.hide()
        self.pushButton_2.hide()
        self.pushButton_17.hide()
        self.pushButton_9.hide()
        self.pushButton_2.hide()
        
        
    def logout(self):
        userinfo.clear()
        self.hide()
        self.pushButton_3.show()
        self.pushButton_5.show()
        self.label_10.setText("")
        self.label_14.setText("")
        self.label_16.setText("")
    
    def callsub(self):
            for i in range(2,len(self.frame_22.children())):
                self.frame_22.children()[i].deleteLater()
            self.loadsub()
            self.stackedWidget.setCurrentWidget(self.page_6)
    
    def callmain(self):
            for i in range(2,len(self.frame_12.children())):
                self.frame_12.children()[i].deleteLater()
            self.loadmain()
            self.stackedWidget.setCurrentWidget(self.page_1)
    
    def callcom(self):
            for i in range(2,len(self.frame_33.children())):
                self.frame_33.children()[i].deleteLater()
                
            self.loadcom()
            self.stackedWidget.setCurrentWidget(self.page_8)
    
    
        
        
        
    def loadsub(self):
        information = []
        information.clear()
        information = adaptor.retrive_submi()
        for i in range((len(information)-1)):
            self.fframe_24 = QFrame(self.frame_22)
            self.fframe_24.setObjectName(u"fframe_24")
            self.fframe_24.setStyleSheet(u"background-color: rgb(84, 126, 126);")
            self.fframe_24.setFrameShape(QFrame.Shape.StyledPanel)
            self.fframe_24.setFrameShadow(QFrame.Shadow.Raised)
            self.horizontalLayout_24 = QHBoxLayout(self.fframe_24)
            self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
            self.fframe_26 = QFrame(self.fframe_24)
            self.fframe_26.setObjectName(u"fframe_26")
            self.fframe_26.setFrameShape(QFrame.Shape.StyledPanel)
            self.fframe_26.setFrameShadow(QFrame.Shadow.Raised)
            self.verticalLayout_17 = QVBoxLayout(self.fframe_26)
            self.verticalLayout_17.setSpacing(1)
            self.verticalLayout_17.setObjectName(u"verticalLayout_17")
            self.verticalLayout_17.setContentsMargins(10, 10, 10, 10)
            self.formLayout_5 = QFormLayout()
            self.formLayout_5.setObjectName(u"formLayout_5")
            self.formLayout_5.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
            self.label_26 = QLabel(self.fframe_26)
            self.label_26.setObjectName(u"label_26")

            self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_26)

            self.label_27 = QLabel(self.fframe_26)
            self.label_27.setObjectName(u"label_27")

            self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_27)

            self.label_28 = QLabel(self.fframe_26)
            self.label_28.setObjectName(u"label_28")

            self.formLayout_5.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_28)

            self.label_29 = QLabel(self.fframe_26)
            self.label_29.setObjectName(u"label_29")

            self.formLayout_5.setWidget(1, QFormLayout.ItemRole.FieldRole, self.label_29)

            self.label_30 = QLabel(self.fframe_26)
            self.label_30.setObjectName(u"label_30")

            self.formLayout_5.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_30)

            self.label_31 = QLabel(self.fframe_26)
            self.label_31.setObjectName(u"label_31")

            self.formLayout_5.setWidget(2, QFormLayout.ItemRole.FieldRole, self.label_31)

            self.label_32 = QLabel(self.fframe_26)
            self.label_32.setObjectName(u"label_32")

            self.formLayout_5.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_32)

            self.label_33 = QLabel(self.fframe_26)
            self.label_33.setObjectName(u"label_33")

            self.formLayout_5.setWidget(3, QFormLayout.ItemRole.FieldRole, self.label_33)


            self.verticalLayout_17.addLayout(self.formLayout_5)

            self.buttons = QFrame(self.fframe_26)
            self.buttons.setObjectName(u"buttons")
            self.buttons.setFrameShape(QFrame.Shape.StyledPanel)
            self.buttons.setFrameShadow(QFrame.Shadow.Raised)
            self.horizontalLayout_25 = QHBoxLayout(self.buttons)
            self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
            self.pushButton_16 = QPushButton(self.buttons)
            self.pushButton_16.setObjectName(u"pushButton_16")
            self.pushButton_16.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "background-color: rgb(0, 0, 127);")
            self.pushButton_16.setIcon(QtGui.QIcon("icons/x.svg"))

            self.horizontalLayout_25.addWidget(self.pushButton_16)

            self.pushButton_17 = QPushButton(self.buttons)
            self.pushButton_17.setObjectName(u"pushButton_17")
            self.pushButton_17.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "background-color: rgb(0, 0, 127);")
            self.pushButton_16.setIcon(QtGui.QIcon("icons/check.svg"))
            self.pushButton_10.setIcon(QtGui.QIcon("icons/x.svg"))

            self.horizontalLayout_25.addWidget(self.pushButton_17)


            self.verticalLayout_17.addWidget(self.buttons)


            self.horizontalLayout_24.addWidget(self.fframe_26)

            self.fframe_27 = QFrame(self.fframe_24)
            self.fframe_27.setObjectName(u"fframe_27")
            self.fframe_27.setFrameShape(QFrame.Shape.StyledPanel)
            self.fframe_27.setFrameShadow(QFrame.Shadow.Raised)
            self.verticalLayout_14 = QVBoxLayout(self.fframe_27)
            self.verticalLayout_14.setObjectName(u"verticalLayout_14")
            self.fframe_28 = QFrame(self.fframe_27)
            self.fframe_28.setObjectName(u"fframe_28")
            self.fframe_28.setFrameShape(QFrame.Shape.StyledPanel)
            self.fframe_28.setFrameShadow(QFrame.Shadow.Raised)
            self.horizontalLayout_26 = QHBoxLayout(self.fframe_28)
            self.horizontalLayout_26.setSpacing(0)
            self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
            self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
            self.formLayout_6 = QFormLayout()
            self.formLayout_6.setObjectName(u"formLayout_6")
            self.label_34 = QLabel(self.fframe_28)
            self.label_34.setObjectName(u"label_34")

            self.formLayout_6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_34)

            self.label_35 = QLabel(self.fframe_28)
            self.label_35.setObjectName(u"label_35")
            font2 = QFont()
            font2.setPointSize(12)
            self.label_35.setFont(font2)

            self.formLayout_6.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_35)


            self.horizontalLayout_26.addLayout(self.formLayout_6)


            self.verticalLayout_14.addWidget(self.fframe_28)

            self.fframe_29 = QFrame(self.fframe_27)
            self.fframe_29.setObjectName(u"fframe_29")
            self.fframe_29.setFrameShape(QFrame.Shape.StyledPanel)
            self.fframe_29.setFrameShadow(QFrame.Shadow.Raised)
            self.horizontalLayout_27 = QHBoxLayout(self.fframe_29)
            self.horizontalLayout_27.setSpacing(0)
            self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
            self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
            self.formLayout_7 = QFormLayout()
            self.formLayout_7.setObjectName(u"formLayout_7")
            self.label_36 = QLabel(self.fframe_29)
            self.label_36.setObjectName(u"label_36")

            self.formLayout_7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_36)

            self.label_37 = QLabel(self.fframe_29)
            self.label_37.setObjectName(u"label_37")

            self.formLayout_7.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_37)


            self.horizontalLayout_27.addLayout(self.formLayout_7)


            self.verticalLayout_14.addWidget(self.fframe_29)


            self.horizontalLayout_24.addWidget(self.fframe_27)


            self.verticalLayout_13.addWidget(self.fframe_24)
            
            myFont=QtGui.QFont()
            myFont.setBold(True)
            myFont.setUnderline(True)
            self.label_26.setFont(myFont)
            self.label_28.setFont(myFont)
            self.label_30.setFont(myFont)
            self.label_32.setFont(myFont)
            self.label_34.setFont(myFont)
            self.label_36.setFont(myFont)
            
            self.label_26.setText("Water Source Name")
            self.label_27.setText(str(information[i][6]))
            self.label_28.setText("Water Source Location")
            self.label_29.setText(str(information[i][8]))
            self.label_30.setText("Water Source Type")
            self.label_31.setText(str(information[i][7]))
            self.label_32.setText("Water Source Condition")
            self.label_33.setText(str(information[i][3]))
            self.pushButton_16.setText("Discard")
            self.pushButton_17.setText("Validated")
            self.label_34.setText("Approximate Danger")
            self.label_35.setText(str(information[i][4]))
            self.label_36.setText("Water Source Zone")
            self.label_37.setText(str(information[i][5]))
            self.label_35.setFont(QFont('Arial', 20))
            if(int(information[i][4])>5):
                self.label_35.setStyleSheet("color: red")
            else:
                self.label_35.setStyleSheet("color: green")
            self.pushButton_16.clicked.connect(
            lambda: self.Sdel(information,i)
            )
            self.pushButton_17.clicked.connect(
            lambda: self.select(information,i)
            )
            ###################################################################################################################3
    def Sdel(self,info,i):
        adaptor.deletesub(str(info[i][6]))
        self.callsub()
            
    def select(self,inform,i):
        stuff=adaptor.select(str(inform[i][6]))
        if stuff is None or not stuff or []:
            adaptor.storewater(str(inform[i][6]),str(inform[i][8]),str(inform[i][7]),str(inform[i][3]),str(inform[i][4]),str(inform[i][5]))
            adaptor.deletesub(str(inform[i][6]))
            self.callsub()
        else:
            adaptor.updatewater(str(inform[i][6]),str(inform[i][8]),str(inform[i][7]),str(inform[i][3]),str(inform[i][4]),str(inform[i][5])) 
            adaptor.deletesub(str(inform[i][6]))
            self.callsub()
        
    def loadcom(self):
        data1=[]
        data1.clear()
        data1=adaptor.retrive_com()
        for i in range(len(data1)-1):
            self.eframe_34 = QFrame(self.frame_33)
            self.eframe_34.setObjectName(u"eframe_34")
            self.eframe_34.setStyleSheet(u"background-color: rgb(124, 41, 0);")
            self.eframe_34.setFrameShape(QFrame.Shape.StyledPanel)
            self.eframe_34.setFrameShadow(QFrame.Shadow.Raised)
            self.horizontalLayout_30 = QHBoxLayout(self.eframe_34)
            self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
            self.eframe_37 = QFrame(self.eframe_34)
            self.eframe_37.setObjectName(u"eframe_37")
            self.eframe_37.setFrameShape(QFrame.Shape.StyledPanel)
            self.eframe_37.setFrameShadow(QFrame.Shadow.Raised)
            self.horizontalLayout_32 = QHBoxLayout(self.eframe_37)
            self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
            self.eframe_38 = QFrame(self.eframe_37)
            self.eframe_38.setObjectName(u"eframe_38")
            self.eframe_38.setFrameShape(QFrame.Shape.StyledPanel)
            self.eframe_38.setFrameShadow(QFrame.Shadow.Raised)
            self.verticalLayout_23 = QVBoxLayout(self.eframe_38)
            self.verticalLayout_23.setObjectName(u"verticalLayout_23")
            self.label_45 = QLabel(self.eframe_38)
            self.label_45.setObjectName(u"label_45")

            self.verticalLayout_23.addWidget(self.label_45)

            self.label_47 = QLabel(self.eframe_38)
            self.label_47.setObjectName(u"label_47")

            self.verticalLayout_23.addWidget(self.label_47)

            self.label_48 = QLabel(self.eframe_38)
            self.label_48.setObjectName(u"label_48")

            self.verticalLayout_23.addWidget(self.label_48)


            self.horizontalLayout_32.addWidget(self.eframe_38)

            self.eframe_39 = QFrame(self.eframe_37)
            self.eframe_39.setObjectName(u"eframe_39")
            self.eframe_39.setFrameShape(QFrame.Shape.StyledPanel)
            self.eframe_39.setFrameShadow(QFrame.Shadow.Raised)
            self.verticalLayout_24 = QVBoxLayout(self.eframe_39)
            self.verticalLayout_24.setObjectName(u"verticalLayout_24")
            self.label_49 = QLabel(self.eframe_39)
            self.label_49.setObjectName(u"label_49")

            self.verticalLayout_24.addWidget(self.label_49)

            self.label_51 = QLabel(self.eframe_39)
            self.label_51.setObjectName(u"label_51")

            self.verticalLayout_24.addWidget(self.label_51)

            self.label_52 = QLabel(self.eframe_39)
            self.label_52.setObjectName(u"label_52")

            self.verticalLayout_24.addWidget(self.label_52)


            self.horizontalLayout_32.addWidget(self.eframe_39)


            self.horizontalLayout_30.addWidget(self.eframe_37)

            self.eframe_36 = QFrame(self.eframe_34)
            self.eframe_36.setObjectName(u"eframe_36")
            self.eframe_36.setFrameShape(QFrame.Shape.StyledPanel)
            self.eframe_36.setFrameShadow(QFrame.Shadow.Raised)
            self.horizontalLayout_31 = QHBoxLayout(self.eframe_36)
            self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
            self.eframe_40 = QFrame(self.eframe_36)
            self.eframe_40.setObjectName(u"eframe_40")
            self.eframe_40.setFrameShape(QFrame.Shape.StyledPanel)
            self.eframe_40.setFrameShadow(QFrame.Shadow.Raised)
            self.verticalLayout_22 = QVBoxLayout(self.eframe_40)
            self.verticalLayout_22.setObjectName(u"verticalLayout_22")
            self.eframe_43 = QFrame(self.eframe_40)
            self.eframe_43.setObjectName(u"eframe_43")
            self.eframe_43.setFrameShape(QFrame.Shape.StyledPanel)
            self.eframe_43.setFrameShadow(QFrame.Shadow.Raised)
            self.verticalLayout_25 = QVBoxLayout(self.eframe_43)
            self.verticalLayout_25.setObjectName(u"verticalLayout_25")
            self.label_53 = QLabel(self.eframe_43)
            self.label_53.setObjectName(u"label_53")

            self.verticalLayout_25.addWidget(self.label_53)


            self.verticalLayout_22.addWidget(self.eframe_43)

            self.eframe_44 = QFrame(self.eframe_40)
            self.eframe_44.setObjectName(u"eframe_44")
            self.eframe_44.setFrameShape(QFrame.Shape.StyledPanel)
            self.eframe_44.setFrameShadow(QFrame.Shadow.Raised)

            self.verticalLayout_22.addWidget(self.eframe_44)


            self.horizontalLayout_31.addWidget(self.eframe_40)

            self.eframe_41 = QFrame(self.eframe_36)
            self.eframe_41.setObjectName(u"eframe_41")
            self.eframe_41.setFrameShape(QFrame.Shape.StyledPanel)
            self.eframe_41.setFrameShadow(QFrame.Shadow.Raised)
            self.verticalLayout_21 = QVBoxLayout(self.eframe_41)
            self.verticalLayout_21.setObjectName(u"verticalLayout_21")
            self.eframe_35 = QFrame(self.eframe_41)
            self.eframe_35.setObjectName(u"eframe_35")
            self.eframe_35.setFrameShape(QFrame.Shape.StyledPanel)
            self.eframe_35.setFrameShadow(QFrame.Shadow.Raised)
            self.verticalLayout_26 = QVBoxLayout(self.eframe_35)
            self.verticalLayout_26.setObjectName(u"verticalLayout_26")
            self.label_54 = QLabel(self.eframe_35)
            self.label_54.setObjectName(u"label_54")

            self.verticalLayout_26.addWidget(self.label_54)


            self.verticalLayout_21.addWidget(self.eframe_35)

            self.eframe_42 = QFrame(self.eframe_41)
            self.eframe_42.setObjectName(u"eframe_42")
            self.eframe_42.setFrameShape(QFrame.Shape.StyledPanel)
            self.eframe_42.setFrameShadow(QFrame.Shadow.Raised)
            self.horizontalLayout_33 = QHBoxLayout(self.eframe_42)
            self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
            self.pushButton_9 = QPushButton(self.eframe_42)
            self.pushButton_9.setObjectName(u"pushButton_9")
            self.pushButton_9.setStyleSheet(u"background-color: rgb(0, 0, 127);\n"
    "color: rgb(255, 255, 255);")
            self.pushButton_9.setIcon(QtGui.QIcon("icons/check.svg"))

            self.horizontalLayout_33.addWidget(self.pushButton_9)


            self.verticalLayout_21.addWidget(self.eframe_42)


            self.horizontalLayout_31.addWidget(self.eframe_41)


            self.horizontalLayout_30.addWidget(self.eframe_36)


            self.verticalLayout_20.addWidget(self.eframe_34)
            
            
            myFont=QtGui.QFont()
            myFont.setBold(True)
            myFont.setUnderline(True)
            self.label_45.setFont(myFont)
            self.label_47.setFont(myFont)
            self.label_48.setFont(myFont)
            self.label_53.setFont(myFont)
            
            self.label_45.setText("Water Source Name")
            self.label_47.setText("Water Source Type")
            self.label_48.setText("Complaint")
            self.label_49.setText(str(data1[i][5]))
            self.label_51.setText(str(data1[i][6]))
            self.label_52.setText(str(data1[i][3]))
            self.label_53.setText("Approximate Danger")
            self.label_54.setText(str(data1[i][4]))
            self.pushButton_9.setText("Checked")
            self.label_54.setFont(QFont('Arial', 20))
            if(int(data1[i][4])>5):
                self.label_54.setStyleSheet("color: red")
            else:
                self.label_54.setStyleSheet("color: green")
                
            self.pushButton_9.clicked.connect(
            lambda: self.Sdelcom(data1,i)
            )
            
    def Sdelcom(self,info,i):
        adaptor.deletecom(str(info[i][5]))
        self.callcom()
     
     
    def loadGchat(self):
        information1 = []
        information1.clear()
        information1 = adaptor.retrive_Gchat()
        for i in range((len(information1)-1)):
            if(str(information1[i][1])!=str(userinfo[0][0])):
                self.GRframe_28 = QFrame(self.frame_27)
                self.GRframe_28.setObjectName(u"GRframe_28")
                self.GRframe_28.setStyleSheet(u"background-color: rgb(147, 98, 0);")
                self.GRframe_28.setFrameShape(QFrame.Shape.StyledPanel)
                self.GRframe_28.setFrameShadow(QFrame.Shadow.Raised)
                self.verticalLayout_27 = QVBoxLayout(self.GRframe_28)
                self.verticalLayout_27.setObjectName(u"verticalLayout_27")
                self.GRframe_34 = QFrame(self.GRframe_28)
                self.GRframe_34.setObjectName(u"GRframe_34")
                self.GRframe_34.setFrameShape(QFrame.Shape.StyledPanel)
                self.GRframe_34.setFrameShadow(QFrame.Shadow.Raised)
                self.horizontalLayout_31 = QHBoxLayout(self.GRframe_34)
                self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
                self.label_26 = QLabel(self.GRframe_34)
                self.label_26.setObjectName(u"label_26")
                #self.label_26.setFont(font3)

                self.horizontalLayout_31.addWidget(self.label_26)


                self.verticalLayout_27.addWidget(self.GRframe_34)

                self.GRframe_42 = QFrame(self.GRframe_28)
                self.GRframe_42.setObjectName(u"GRframe_42")
                self.GRframe_42.setFrameShape(QFrame.Shape.StyledPanel)
                self.GRframe_42.setFrameShadow(QFrame.Shadow.Raised)
                self.horizontalLayout_30 = QHBoxLayout(self.GRframe_42)
                self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
                self.label_27 = QLabel(self.GRframe_42)
                self.label_27.setObjectName(u"label_27")
                
                self.label_26.setText(str(information1[i][2]))
                self.label_27.setText(str(information1[i][3]))

                self.horizontalLayout_30.addWidget(self.label_27)


                self.verticalLayout_27.addWidget(self.GRframe_42)


                self.verticalLayout_26.addWidget(self.GRframe_28, 0, Qt.AlignmentFlag.AlignLeft)
            else:

                self.GSframe_29 = QFrame(self.frame_27)
                self.GSframe_29.setObjectName(u"GSframe_29")
                self.GSframe_29.setStyleSheet(u"background-color: rgb(89, 89, 134);")
                self.GSframe_29.setFrameShape(QFrame.Shape.StyledPanel)
                self.GSframe_29.setFrameShadow(QFrame.Shadow.Raised)
                self.verticalLayout_28 = QVBoxLayout(self.GSframe_29)
                self.verticalLayout_28.setObjectName(u"verticalLayout_28")
                self.GSframe_44 = QFrame(self.GSframe_29)
                self.GSframe_44.setObjectName(u"GSframe_44")
                #self.GSframe_44.setFont(font3)
                self.GSframe_44.setFrameShape(QFrame.Shape.StyledPanel)
                self.GSframe_44.setFrameShadow(QFrame.Shadow.Raised)
                self.horizontalLayout_26 = QHBoxLayout(self.GSframe_44)
                self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
                self.label_28 = QLabel(self.GSframe_44)
                self.label_28.setObjectName(u"label_28")
                #self.label_28.setFont(font3)

                self.horizontalLayout_26.addWidget(self.label_28)


                self.verticalLayout_28.addWidget(self.GSframe_44)

                self.GSframe_45 = QFrame(self.GSframe_29)
                self.GSframe_45.setObjectName(u"GSframe_45")
                self.GSframe_45.setFrameShape(QFrame.Shape.StyledPanel)
                self.GSframe_45.setFrameShadow(QFrame.Shadow.Raised)
                self.horizontalLayout_32 = QHBoxLayout(self.GSframe_45)
                self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
                self.label_29 = QLabel(self.GSframe_45)
                self.label_29.setObjectName(u"label_29")
                
                self.label_28.setText(str(information1[i][2]))
                self.label_29.setText(str(information1[i][3]))

                self.horizontalLayout_32.addWidget(self.label_29)


                self.verticalLayout_28.addWidget(self.GSframe_45)


                self.verticalLayout_26.addWidget(self.GSframe_29, 0, Qt.AlignmentFlag.AlignRight)


            self.verticalLayout_21.addWidget(self.frame_27, 0, Qt.AlignmentFlag.AlignTop)
        
    def callGchat(self):
        for i in range(2,len(self.frame_27.children())):
                self.frame_27.children()[i].deleteLater()
                
        self.loadGchat()
        self.stackedWidget.setCurrentWidget(self.page_10)
            
            
    def loadAchat(self):
        information1 = []
        information1.clear()
        information1 = adaptor.retrive_Achat()
        for i in range((len(information1)-1)):
            print(information1[i][1])
            if(str(information1[i][1])!=str(userinfo[0][0])):
                self.ARframe_36 = QFrame(self.frame_35)
                self.ARframe_36.setObjectName(u"ARframe_36")
                self.ARframe_36.setStyleSheet(u"background-color: rgb(92, 92, 138);")
                self.ARframe_36.setFrameShape(QFrame.Shape.StyledPanel)
                self.ARframe_36.setFrameShadow(QFrame.Shadow.Raised)
                self.verticalLayout_24 = QVBoxLayout(self.ARframe_36)
                self.verticalLayout_24.setObjectName(u"verticalLayout_24")
                self.ARframe_38 = QFrame(self.ARframe_36)
                self.ARframe_38.setObjectName(u"ARframe_38")
                self.ARframe_38.setFrameShape(QFrame.Shape.StyledPanel)
                self.ARframe_38.setFrameShadow(QFrame.Shadow.Raised)
                self.horizontalLayout_35 = QHBoxLayout(self.ARframe_38)
                self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
                self.label_31 = QLabel(self.ARframe_38)
                self.label_31.setObjectName(u"label_31")
                #self.label_31.setFont(font3)

                self.horizontalLayout_35.addWidget(self.label_31)


                self.verticalLayout_24.addWidget(self.ARframe_38)

                self.ARframe_39 = QFrame(self.ARframe_36)
                self.ARframe_39.setObjectName(u"ARframe_39")
                self.ARframe_39.setFrameShape(QFrame.Shape.StyledPanel)
                self.ARframe_39.setFrameShadow(QFrame.Shadow.Raised)
                self.horizontalLayout_36 = QHBoxLayout(self.ARframe_39)
                self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
                self.label_32 = QLabel(self.ARframe_39)
                self.label_32.setObjectName(u"label_32")
                
                self.label_31.setText(str(information1[i][2]))
                self.label_32.setText(str(information1[i][3]))

                self.horizontalLayout_36.addWidget(self.label_32)


                self.verticalLayout_24.addWidget(self.ARframe_39)


                self.verticalLayout_22.addWidget(self.ARframe_36, 0, Qt.AlignmentFlag.AlignLeft)
            else:

                self.ASframe_37 = QFrame(self.frame_35)
                self.ASframe_37.setObjectName(u"ASframe_37")
                self.ASframe_37.setStyleSheet(u"background-color: rgb(136, 90, 68);")
                self.ASframe_37.setFrameShape(QFrame.Shape.StyledPanel)
                self.ASframe_37.setFrameShadow(QFrame.Shadow.Raised)
                self.verticalLayout_23 = QVBoxLayout(self.ASframe_37)
                self.verticalLayout_23.setObjectName(u"verticalLayout_23")
                self.ASframe_41 = QFrame(self.ASframe_37)
                self.ASframe_41.setObjectName(u"ASframe_41")
                self.ASframe_41.setFrameShape(QFrame.Shape.StyledPanel)
                self.ASframe_41.setFrameShadow(QFrame.Shadow.Raised)
                self.horizontalLayout_37 = QHBoxLayout(self.ASframe_41)
                self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
                self.label_33 = QLabel(self.ASframe_41)
                self.label_33.setObjectName(u"label_33")
                #self.label_33.setFont(font3)

                self.horizontalLayout_37.addWidget(self.label_33)


                self.verticalLayout_23.addWidget(self.ASframe_41)

                self.ASframe_40 = QFrame(self.ASframe_37)
                self.ASframe_40.setObjectName(u"ASframe_40")
                self.ASframe_40.setFrameShape(QFrame.Shape.StyledPanel)
                self.ASframe_40.setFrameShadow(QFrame.Shadow.Raised)
                self.horizontalLayout_38 = QHBoxLayout(self.ASframe_40)
                self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
                self.label_34 = QLabel(self.ASframe_40)
                self.label_34.setObjectName(u"label_34")
                
                self.label_33.setText(str(information1[i][2]))
                self.label_34.setText(str(information1[i][3]))

                self.horizontalLayout_38.addWidget(self.label_34)


                self.verticalLayout_23.addWidget(self.ASframe_40)


                self.verticalLayout_22.addWidget(self.ASframe_37, 0, Qt.AlignmentFlag.AlignRight)


            self.horizontalLayout_34.addWidget(self.frame_35, 0, Qt.AlignmentFlag.AlignTop)
            
            
    def callAchat(self):
        for i in range(2,len(self.frame_35.children())):
                self.frame_35.children()[i].deleteLater()
                
        self.loadAchat()
        self.stackedWidget.setCurrentWidget(self.page_11)
        
        
    def loadmain(self):
        information1 = []
        information1.clear()
        information1 = adaptor.retrive_all()
        for i in range((len(information1)-1)):
            self.wframe_24 = QFrame(self.frame_12)
            self.wframe_24.setObjectName(u"wframe_24")
            self.wframe_24.setStyleSheet(u"background-color: rgb(84, 126, 126);")
            self.wframe_24.setFrameShape(QFrame.Shape.StyledPanel)
            self.wframe_24.setFrameShadow(QFrame.Shadow.Raised)
            self.horizontalLayout_24 = QHBoxLayout(self.wframe_24)
            self.horizontalLayout_24.setSpacing(0)
            self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
            self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
            self.wframe_25 = QFrame(self.wframe_24)
            self.wframe_25.setObjectName(u"wframe_25")
            self.wframe_25.setFrameShape(QFrame.Shape.StyledPanel)
            self.wframe_25.setFrameShadow(QFrame.Shadow.Raised)
            self.horizontalLayout_25 = QHBoxLayout(self.wframe_25)
            self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
            self.wframe_13 = QFrame(self.wframe_25)
            self.wframe_13.setObjectName(u"wframe_13")
            self.wframe_13.setFrameShape(QFrame.Shape.StyledPanel)
            self.wframe_13.setFrameShadow(QFrame.Shadow.Raised)
            self.verticalLayout_14 = QVBoxLayout(self.wframe_13)
            self.verticalLayout_14.setObjectName(u"verticalLayout_14")
            self.label_25 = QLabel(self.wframe_13)
            self.label_25.setObjectName(u"label_25")

            self.verticalLayout_14.addWidget(self.label_25)

            self.label_26 = QLabel(self.wframe_13)
            self.label_26.setObjectName(u"label_26")

            self.verticalLayout_14.addWidget(self.label_26)

            self.label_27 = QLabel(self.wframe_13)
            self.label_27.setObjectName(u"label_27")

            self.verticalLayout_14.addWidget(self.label_27)

            self.label_28 = QLabel(self.wframe_13)
            self.label_28.setObjectName(u"label_28")

            self.verticalLayout_14.addWidget(self.label_28)


            self.horizontalLayout_25.addWidget(self.wframe_13)

            self.wframe_27 = QFrame(self.wframe_25)
            self.wframe_27.setObjectName(u"wframe_27")
            self.wframe_27.setFrameShape(QFrame.Shape.StyledPanel)
            self.wframe_27.setFrameShadow(QFrame.Shadow.Raised)
            self.verticalLayout_17 = QVBoxLayout(self.wframe_27)
            self.verticalLayout_17.setObjectName(u"verticalLayout_17")
            self.label_29 = QLabel(self.wframe_27)
            self.label_29.setObjectName(u"label_29")

            self.verticalLayout_17.addWidget(self.label_29)

            self.label_30 = QLabel(self.wframe_27)
            self.label_30.setObjectName(u"label_30")

            self.verticalLayout_17.addWidget(self.label_30)

            self.label_31 = QLabel(self.wframe_27)
            self.label_31.setObjectName(u"label_31")

            self.verticalLayout_17.addWidget(self.label_31)

            self.label_32 = QLabel(self.wframe_27)
            self.label_32.setObjectName(u"label_32")

            self.verticalLayout_17.addWidget(self.label_32)


            self.horizontalLayout_25.addWidget(self.wframe_27)


            self.horizontalLayout_24.addWidget(self.wframe_25)

            self.wframe_26 = QFrame(self.wframe_24)
            self.wframe_26.setObjectName(u"wframe_26")
            self.wframe_26.setStyleSheet(u"")
            self.wframe_26.setFrameShape(QFrame.Shape.StyledPanel)
            self.wframe_26.setFrameShadow(QFrame.Shadow.Raised)
            self.horizontalLayout_26 = QHBoxLayout(self.wframe_26)
            self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
            self.wframe_28 = QFrame(self.wframe_26)
            self.wframe_28.setObjectName(u"wframe_28")
            self.wframe_28.setFrameShape(QFrame.Shape.StyledPanel)
            self.wframe_28.setFrameShadow(QFrame.Shadow.Raised)
            self.verticalLayout_18 = QVBoxLayout(self.wframe_28)
            self.verticalLayout_18.setObjectName(u"verticalLayout_18")
            self.label_33 = QLabel(self.wframe_28)
            self.label_33.setObjectName(u"label_33")

            self.verticalLayout_18.addWidget(self.label_33)

            self.label_36 = QLabel(self.wframe_28)
            self.label_36.setObjectName(u"label_36")

            self.verticalLayout_18.addWidget(self.label_36)


            self.horizontalLayout_26.addWidget(self.wframe_28)

            self.wframe_29 = QFrame(self.wframe_26)
            self.wframe_29.setObjectName(u"wframe_29")
            self.wframe_29.setFrameShape(QFrame.Shape.StyledPanel)
            self.wframe_29.setFrameShadow(QFrame.Shadow.Raised)
            self.verticalLayout_19 = QVBoxLayout(self.wframe_29)
            self.verticalLayout_19.setObjectName(u"verticalLayout_19")
            self.label_34 = QLabel(self.wframe_29)
            self.label_34.setObjectName(u"label_34")

            self.verticalLayout_19.addWidget(self.label_34)

            self.label_35 = QLabel(self.wframe_29)
            self.label_35.setObjectName(u"label_35")

            self.verticalLayout_19.addWidget(self.label_35)


            self.horizontalLayout_26.addWidget(self.wframe_29)


            self.horizontalLayout_24.addWidget(self.wframe_26)


            self.verticalLayout_11.addWidget(self.wframe_24)
            
            myFont=QtGui.QFont()
            myFont.setBold(True)
            myFont.setUnderline(True)
            self.label_25.setFont(myFont)
            self.label_26.setFont(myFont)
            self.label_27.setFont(myFont)
            self.label_28.setFont(myFont)
            self.label_33.setFont(myFont)
            self.label_36.setFont(myFont)
            
            self.label_25.setText("Water Source Name")
            self.label_26.setText("Water Source Location")
            self.label_27.setText("Water Source Type")
            self.label_28.setText("Water Source Condition")
            self.label_29.setText(str(information1[i][1]))
            self.label_30.setText(str(information1[i][2]))
            self.label_31.setText(str(information1[i][3]))
            self.label_32.setText(str(information1[i][4]))
            self.label_33.setText("Approximate Danger")
            self.label_36.setText("Water Source Zone")
            self.label_34.setText(str(information1[i][5]))
            self.label_35.setText(str(information1[i][6]))
            self.label_34.setFont(QFont('Arial', 20))
            if(int(information1[i][5])>5):
                self.label_34.setStyleSheet("color: red")
            else:
                self.label_34.setStyleSheet("color: green")
        
        
    def register(self):
        name=self.lineEdit_4.text()
        location=self.lineEdit_6.text()
        passw=self.lineEdit_7.text()
        Cpassw=self.lineEdit_8.text()
        typeu=self.comboBox_4.currentText()
        
        self.lineEdit_4.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        
        if(passw==Cpassw):
            adaptor.storeuser(name,location,typeu,passw)
        else:
            self.response("ERROR","Password Doesn't Match")
           
    def login(self):
        print("test")
        name=self.lineEdit_2.text()
        password=self.lineEdit_3.text()
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        global userinfo
        userinfo=adaptor.search(name,password)
        if not userinfo:       
            # Stores the return value for the button pressed
            self.hide()
            self.label_10.setText("")
            self.label_14.setText("")
            self.label_16.setText("")
            self.stackedWidget.setCurrentWidget(self.page_1)
        else:
            
              
            if (str(userinfo[0][2])=="ADMIN"):
                self.pushButton_9.show()
                self.pushButton_11.show()
                self.pushButton_17.show()
                self.pushButton_14.show()
                self.pushButton_7.show()
                self.pushButton_2.show()
                self.pushButton_3.hide()
                self.pushButton_5.hide()
            elif (str(userinfo[0][2])=="MOD"):
                self.pushButton_9.show()
                self.pushButton_11.show()
                self.pushButton_17.show()
                self.pushButton_14.show()
                self.pushButton_7.show()
                self.pushButton_2.show()
                self.pushButton_3.hide()
                self.pushButton_5.hide()
            else:
                self.pushButton_9.show()
                self.pushButton_11.show()
                self.pushButton_2.show()
                self.pushButton_3.hide()
                self.pushButton_5.hide()
            
            
            
            
            
            self.label_10.setText(userinfo[0][1])
            self.label_14.setText(userinfo[0][3])
            self.label_16.setText(userinfo[0][2])
            self.stackedWidget.setCurrentWidget(self.page_1)
    
    def store(self):
        a4=self.lineEdit_10.text()
        a5=self.textEdit.toPlainText()

    def submit_complaint(self):
        userid = userinfo[0][0]
        wName = self.comboBox_2.currentText()
        dd=[]
        dd = adaptor.select(wName)
        wID=dd[0][0]
        wtype=self.lineEdit_10.text()
        DComp = self.textEdit.toPlainText()
        approx = self.comboBox_3.currentText()
        self.lineEdit_10.setText("")
        adaptor.storecomplaint(userid, wID, wName, wtype,DComp, approx)
        
        
    def submit_Subm(self):
        userid = userinfo[0][0]
        wname = self.lineEdit.text()
        wloca = self.lineEdit_5.text()
        wtype = self.lineEdit_9.text()
        DComd = self.textEdit_2.toPlainText()
        waprox = self.comboBox_6.currentText()
        Wzone = self.comboBox_5.currentText()
        self.lineEdit_5.setText("")
        self.lineEdit_9.setText("")
        adaptor.storeSubmission(userid,wname,wloca,wtype,DComd,waprox,Wzone)

    def Rest_or_max(self):
        
        if self.isMaximized():
            self.showNormal()
            self.max.setIcon(QtGui.QIcon("icons/maximize-2.svg"))

        else:
            self.showMaximized()
            self.max.setIcon(QtGui.QIcon("icons/minimize-2.svg"))
            self.max
            
    def response(self,title,message):
        dlg = QMessageBox(self)
        dlg.setWindowTitle(title)
        dlg.setText(message)
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
        dlg.setIcon(QMessageBox.Icon.Information)
        button = dlg.exec()

        #if button == QMessageBox.Yes:
        #    print("Yes!")
        #else:
        #    print("No!")
        
    def sendG(self):
        Uid=userinfo[0][0]
        Uname=userinfo[0][1]
        msg=self.lineEdit_12.text()
        self.lineEdit_12.setText("")
        adaptor.storemessageG(Uid,Uname,msg)
        self.callGchat()
    
    def sendA(self):
        Uid=userinfo[0][0]
        Uname=userinfo[0][1]
        msg=self.lineEdit_11.text()
        self.lineEdit_11.setText("")
        adaptor.storemessageA(Uid,Uname,msg)
        self.callAchat()


counter = 0


class SplashScreen(QtWidgets.QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui_ = Ui_self()
        self.ui_.setupUi_(self)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        self.show()
        self.center()

    def center(self):
        geo_frame = self.frameGeometry()
        # cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        # geo_frame.moveCenter(cp)
        self.move(geo_frame.topLeft())

    def progress(self):
        global counter
        if counter > 20:
            self.timer.stop()
            self.main = Ui()
            self.main.show()
            self.close()
        counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    window = SplashScreen()
    window.show()
    sys.exit(app.exec())
