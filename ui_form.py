# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QThread,Signal,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLCDNumber, QLabel, QPushButton,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)
import cv2

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1400, 700)
        Widget.setMinimumSize(QSize(1400, 700))
        Widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.giaodien = QGroupBox(Widget)
        self.giaodien.setObjectName(u"giaodien")
        self.giaodien.setEnabled(True)
        self.giaodien.setMinimumSize(QSize(500, 800))
        self.giaodien.setMaximumSize(QSize(2000, 2800))
        self.label = QLabel(self.giaodien)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 41, 981, 741))
        self.label.setStyleSheet(u" QPushButton {\n"
"        border: none;  \n"
"        background-color: transparent;  \n"
"        padding: 10px; \n"
"    }\n"
"QPushButton:pressed {\n"
"        background-color: rgba(0, 0, 0, 100);  \n"
"    }")
        self.label.setPixmap(QPixmap(u"../../../../UI/giao_dien/User/ADMIN/img/3d.png"))
        self.label.setScaledContents(True)

        # Label cho living_room_l1
        self.label_living_l1 = QLabel(self.giaodien)
        self.label_living_l1.setObjectName(u"label_living_l1")
        self.label_living_l1.setGeometry(QRect(10, 41, 981, 741))
        self.label_living_l1.setPixmap(QPixmap(u"../../../../UI/giao_dien/User/ADMIN/img/3d_living1.png"))  # Thay đường dẫn
        self.label_living_l1.setScaledContents(True)
        #self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_living_l1.hide()

        # Label cho living_room_l2
        self.label_living_l2 = QLabel(self.giaodien)
        self.label_living_l1.setObjectName(u"label_living_l2")
        self.label_living_l2.setGeometry(QRect(10, 41, 981, 741))
        self.label_living_l2.setPixmap(QPixmap(u"../../../../UI/giao_dien/User/ADMIN/img/3d_living2.png"))  # Thay đường dẫn
        self.label_living_l2.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_living_l2.hide()

        # Label cho bed_room_l1
        self.label_bed_l1 = QLabel(self.giaodien)
        self.label_bed_l1.setObjectName(u"label_bed_l1")
        self.label_bed_l1.setGeometry(QRect(10, 41, 981, 741))
        self.label_bed_l1.setPixmap(QPixmap(u"../../../../UI/giao_dien/User/ADMIN/img/3d_bed1.png"))  # Thay đường dẫn
        self.label_bed_l1.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_bed_l1.hide()

        # Label cho bed_room_l2
        self.label_bed_l2 = QLabel(self.giaodien)
        self.label_bed_l2.setObjectName(u"label_bed_l2")
        self.label_bed_l2.setGeometry(QRect(10, 41, 981, 741))
        self.label_bed_l2.setPixmap(QPixmap(u"../../../../UI/giao_dien/User/ADMIN/img/3d_bed2.png"))  # Thay đường dẫn
        self.label_bed_l2.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_bed_l2.hide()


        # Label cho kitchen_l1
        self.label_kitchen_l1 = QLabel(self.giaodien)
        self.label_kitchen_l1.setObjectName(u"label_kitchen_l1")
        self.label_kitchen_l1.setGeometry(QRect(10, 41, 981, 741))
        self.label_kitchen_l1.setPixmap(QPixmap(u"../../../../UI/giao_dien/User/ADMIN/img/3d_kitchen1.png"))  # Thay đường dẫn
        self.label_kitchen_l1.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_kitchen_l1.hide()

        # Label cho kitchen_l2
        self.label_kitchen_l2 = QLabel(self.giaodien)
        self.label_kitchen_l2.setObjectName(u"label_kitchen_l2")
        self.label_kitchen_l2.setGeometry(QRect(10, 41, 981, 741))
        self.label_kitchen_l2.setPixmap(QPixmap(u"../../../../UI/giao_dien/User/ADMIN/img/3d_kitchen2.png"))  # Thay đường dẫn
        self.label_kitchen_l2.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_kitchen_l2.hide()

        # Label cho wc
        self.label_wc = QLabel(self.giaodien)
        self.label_wc.setObjectName(u"label_wc")
        self.label_wc.setGeometry(QRect(10, 41, 981, 741))
        self.label_wc.setPixmap(QPixmap(u"../../../../UI/giao_dien/User/ADMIN/img/3d_WC.png"))  # Thay đường dẫn
        self.label_wc.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_wc.hide()

        # Label cho study_room_l1
        self.label_study_room_l1 = QLabel(self.giaodien)
        self.label_study_room_l1.setObjectName(u"label_study_room_l1")
        self.label_study_room_l1.setGeometry(QRect(10, 41, 981, 741))
        self.label_study_room_l1.setPixmap(QPixmap(u"../../../../UI/giao_dien/User/ADMIN/img/3d_bed2_1.png"))  # Thay đường dẫn
        self.label_study_room_l1.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_study_room_l1.hide()

        # Label cho study_room_l2
        self.label_study_room_l2 = QLabel(self.giaodien)
        self.label_study_room_l2.setObjectName(u"label_study_room_l2")
        self.label_study_room_l2.setGeometry(QRect(10, 41, 981, 741))
        self.label_study_room_l2.setPixmap(QPixmap(u"../../../../UI/giao_dien/User/ADMIN/img/3d_bed2_2.png"))  # Thay đường dẫn
        self.label_study_room_l2.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_study_room_l2.hide()

        # Label cho led_living1
        self.label_led_living1 = QLabel(self.giaodien)
        self.label_led_living1.setObjectName(u"label_led_living1")
        self.label_led_living1.setGeometry(QRect(10, 41, 981, 741))
        self.label_led_living1.setPixmap(QPixmap(u"D:/Intern/fileanhsua/3d_led_living1.png"))  # Thay đường dẫn
        self.label_led_living1.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_led_living1.hide()

        # Label cho led_living2
        self.label_led_living2 = QLabel(self.giaodien)
        self.label_led_living2.setObjectName(u"label_led_living2")
        self.label_led_living2.setGeometry(QRect(10, 41, 981, 741))
        self.label_led_living2.setPixmap(QPixmap(u"D:/Intern/fileanhsua/3d_led_living2.png"))  # Thay đường dẫn
        self.label_led_living2.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_led_living2.hide()

        # Label cho led_led_living3
        self.label_led_living3 = QLabel(self.giaodien)
        self.label_led_living3.setObjectName(u"label_led_living3")
        self.label_led_living3.setGeometry(QRect(10, 41, 981, 741))
        self.label_led_living3.setPixmap(QPixmap(u"D:/Intern/fileanhsua/3d_led_living3.png"))  # Thay đường dẫn
        self.label_led_living3.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_led_living3.hide()

        # Label cho led_kitchen1
        self.label_led_kitchen1 = QLabel(self.giaodien)
        self.label_led_kitchen1.setObjectName(u"label_led_kitchen1")
        self.label_led_kitchen1.setGeometry(QRect(10, 41, 981, 741))
        self.label_led_kitchen1.setPixmap(QPixmap(u"D:/Intern/fileanhsua/3d_led_kitchen1.png"))  # Thay đường dẫn
        self.label_led_kitchen1.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_led_kitchen1.hide()

        # Label cho led_kitchen2
        self.label_led_kitchen2 = QLabel(self.giaodien)
        self.label_led_kitchen2.setObjectName(u"label_led_kitchen2")
        self.label_led_kitchen2.setGeometry(QRect(10, 41, 981, 741))
        self.label_led_kitchen2.setPixmap(QPixmap(u"D:/Intern/fileanhsua/3d_led_kitchen2.png"))  # Thay đường dẫn
        self.label_led_kitchen2.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_led_kitchen2.hide()

        # Label cho led_kitchen3
        self.label_led_kitchen3 = QLabel(self.giaodien)
        self.label_led_kitchen3.setObjectName(u"label_led_kitchen3")
        self.label_led_kitchen3.setGeometry(QRect(10, 41, 981, 741))
        self.label_led_kitchen3.setPixmap(QPixmap(u"D:/Intern/fileanhsua/3d_led_kitchen3.png"))  # Thay đường dẫn
        self.label_led_kitchen3.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_led_kitchen3.hide()

        # Label cho led_bed1_1
        self.label_led_bed1_1= QLabel(self.giaodien)
        self.label_led_bed1_1.setObjectName(u"label_led_bed1_1")
        self.label_led_bed1_1.setGeometry(QRect(10, 41, 981, 741))
        self.label_led_bed1_1.setPixmap(QPixmap(u"D:/Intern/fileanhsua/3d_led_bed1.1.png"))  # Thay đường dẫn
        self.label_led_bed1_1.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_led_bed1_1.hide()

        # Label cho led_bed1_2
        self.label_led_bed1_2= QLabel(self.giaodien)
        self.label_led_bed1_2.setObjectName(u"label_led_bed1_2")
        self.label_led_bed1_2.setGeometry(QRect(10, 41, 981, 741))
        self.label_led_bed1_2.setPixmap(QPixmap(u"D:/Intern/fileanhsua/3d_led_bed1.2.png"))  # Thay đường dẫn
        self.label_led_bed1_2.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_led_bed1_2.hide()

        # Label cho led_bed1_3
        self.label_led_bed1_3= QLabel(self.giaodien)
        self.label_led_bed1_3.setObjectName(u"label_led_bed1_3")
        self.label_led_bed1_3.setGeometry(QRect(10, 41, 981, 741))
        self.label_led_bed1_3.setPixmap(QPixmap(u"D:/Intern/fileanhsua/3d_led_bed1.3.png"))  # Thay đường dẫn
        self.label_led_bed1_3.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_led_bed1_3.hide()

        # Label cho led_bed2_1
        self.label_led_bed2_1= QLabel(self.giaodien)
        self.label_led_bed2_1.setObjectName(u"label_led_bed2_1")
        self.label_led_bed2_1.setGeometry(QRect(10, 41, 981, 741))
        self.label_led_bed2_1.setPixmap(QPixmap(u"D:/Intern/fileanhsua/3d_led_bed2.1.png"))  # Thay đường dẫn
        self.label_led_bed2_1.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_led_bed2_1.hide()

        # Label cho led_bed2_2
        self.label_led_bed2_2= QLabel(self.giaodien)
        self.label_led_bed2_2.setObjectName(u"label_led_bed2_2")
        self.label_led_bed2_2.setGeometry(QRect(10, 41, 981, 741))
        self.label_led_bed2_2.setPixmap(QPixmap(u"D:/Intern/fileanhsua/3d_led_bed2.2.png"))  # Thay đường dẫn
        self.label_led_bed2_2.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_led_bed2_2.hide()

        # Label cho led_bed2_3
        self.label_led_bed2_3= QLabel(self.giaodien)
        self.label_led_bed2_3.setObjectName(u"label_led_bed2_3")
        self.label_led_bed2_3.setGeometry(QRect(10, 41, 981, 741))
        self.label_led_bed2_3.setPixmap(QPixmap(u"D:/Intern/fileanhsua/3d_led_bed2.3.png"))  # Thay đường dẫn
        self.label_led_bed2_3.setScaledContents(True)
        # self.label_living.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_led_bed2_3.hide()

        self.living_room = QPushButton(self.giaodien)
        self.living_room.setObjectName(u"living_room")
        self.living_room.setGeometry(QRect(280, 480, 251, 201))
        self.living_room.setStyleSheet(u" QPushButton {\n"
"        border: none;  \n"
"        background-color: transparent;  \n"
"        border-radius: 50px;            \n"
        
"        padding: 10px; \n"
"    }\n"
)
        self.kitchen = QPushButton(self.giaodien)
        self.kitchen.setObjectName(u"kitchen")
        self.kitchen.setGeometry(QRect(532, 320, 281, 151))
        self.kitchen.setStyleSheet(u" QPushButton {\n"
"        border: none;  \n"
"        background-color: transparent;  \n"
"        border-radius: 50px;            \n"
                                   
"        padding: 10px; \n"
"    }\n"
)
        self.bed_room = QPushButton(self.giaodien)
        self.bed_room.setObjectName(u"bed_room")
        self.bed_room.setGeometry(QRect(200, 360, 150, 100))
        self.bed_room.setStyleSheet(u" QPushButton {\n"
"        border: none;  \n"
"        background-color: transparent;  \n"
"        border-radius: 50px;            \n"
                                   
"        padding: 10px; \n"
"    }\n"
"QPushButton:pressed {\n"
)
        self.wc = QPushButton(self.giaodien)
        self.wc.setObjectName(u"wc")
        self.wc.setGeometry(QRect(345, 320, 100, 100))
        self.wc.setStyleSheet(u" QPushButton {\n"
"        border: none;  \n"
"        background-color: transparent;  \n"
"        border-radius: 50px;            \n"
                
"        padding: 10px; \n"
"    }\n"
)
        self.study_room = QPushButton(self.giaodien)
        self.study_room.setObjectName(u"study_room")
        self.study_room.setGeometry(QRect(430, 260, 110, 110))
        self.study_room.setStyleSheet(u" QPushButton {\n"
"        border: none;  \n"
"        background-color: transparent;  \n"
"        border-radius: 50px;            \n"

                              "        padding: 10px; \n"
                              "    }\n"
                              )

        self.horizontalLayout.addWidget(self.giaodien)

        self.control = QGroupBox(Widget)
        self.control.setObjectName(u"control")
        self.control.setEnabled(True)
        self.control.setMinimumSize(QSize(200, 600))
        self.control.setMaximumSize(QSize(500, 1500))
        self.verticalLayout = QVBoxLayout(self.control)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.control_led = QGroupBox(self.control)
        self.control_led.setObjectName(u"control_led")
        self.verticalLayout_2 = QVBoxLayout(self.control_led)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_8 = QGroupBox(self.control_led)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sw_0 = QPushButton(self.groupBox_8)
        self.sw_0.setObjectName(u"sw_0")
        self.sw_0.setMinimumSize(QSize(100, 100))
        self.sw_0.setMaximumSize(QSize(100, 100))
        self.sw_0.setTabletTracking(False)
        self.sw_0.setStyleSheet("""
            QPushButton {
                border: none;
                border-radius: 50px;  /* Bán kính = 1/2 kích thước */
                background-color: #32CD32;
                color: white;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #28A428;
            }
            QPushButton:pressed {
                background-color: #1E7B1E;
            }
        """)
        # icon = QIcon()
        # icon.addFile(u"../../../../tt_nghiencuu/UI/power-on.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        # self.sw_0.setIcon(icon)
        # self.sw_0.setIconSize(QSize(100, 50))

        self.horizontalLayout_2.addWidget(self.sw_0)

        self.lcd_0 = QLCDNumber(self.groupBox_8)
        self.lcd_0.setObjectName(u"lcd_0")
        self.lcd_0.setMaximumSize(QSize(200, 150))
        self.lcd_0.setFrameShape(QFrame.Shape.Box)

        self.horizontalLayout_2.addWidget(self.lcd_0)


        self.verticalLayout_2.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.control_led)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.sw_1 = QPushButton(self.groupBox_9)
        self.sw_1.setObjectName(u"sw_1")
        self.sw_1.setMinimumSize(QSize(100, 100))
        self.sw_1.setMaximumSize(QSize(100, 100))
        self.sw_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.sw_1.setStyleSheet("""
            QPushButton {
                border: none;
                border-radius: 50px;  /* Bán kính = 1/2 kích thước */
                background-color: #32CD32;
                color: white;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #28A428;
            }
            QPushButton:pressed {
                background-color: #1E7B1E;
            }
        """)
        # self.sw_1.setIcon(icon)
        # self.sw_1.setIconSize(QSize(100, 50))

        self.horizontalLayout_3.addWidget(self.sw_1)

        self.lcd_1 = QLCDNumber(self.groupBox_9)
        self.lcd_1.setObjectName(u"lcd_1")
        self.lcd_1.setMaximumSize(QSize(200, 150))

        self.horizontalLayout_3.addWidget(self.lcd_1)


        self.verticalLayout_2.addWidget(self.groupBox_9)

        self.groupBox_3 = QGroupBox(self.control_led)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")


        self.Dimmer = QSlider(Qt.Horizontal)
        self.Dimmer.setRange(0, 4)
        self.Dimmer.setTickPosition(QSlider.TicksBelow)
        self.Dimmer.setTickInterval(1)
        self.Dimmer.setStyleSheet("""
                    QSlider::groove:horizontal {
                        border: 1px solid #bbb;
                        background: #f0f0f0;
                        height: 15px;
                        border-radius: 7px;
                    }

                    /* Phần đã trượt (sáng lên) */
                    QSlider::sub-page:horizontal {
                        background: #007bff;  /* Màu sáng cho phần đã trượt */
                        border-radius: 7px;
                    }

                    /* Phần chưa trượt (xám và chia theo các nấc rõ ràng) */
                    QSlider::add-page:horizontal {
                        background: #ccc;    /* Màu xám cho phần chưa trượt */
                        border-radius: 7px;
                        background: linear-gradient(to right,
                            #ccc 0%,        /* Vị trí chưa trượt */
                            #ccc 25%,       /* 25% chưa trượt */
                            #bbb 25%,       /* 50% chưa trượt */
                            #bbb 50%,       /* 75% chưa trượt */
                            #ccc 75%,       /* 100% chưa trượt */
                            #ccc 100%);     /* Kết thúc */
                    }

                    /* Nút kéo */
                    QSlider::handle:horizontal {
                        background: #007bff;
                        border: 2px solid #0056b3;
                        width: 20px;
                        height: 20px;
                        margin: -8px 0;
                        border-radius: 10px;
                    }

                    QSlider::handle:horizontal:hover {
                        background: #0056b3;
                    }

                    /* Nấc và vạch chia */
                    QSlider::tick-mark:horizontal {
                        background: #000;
                        width: 2px;
                        height: 10px;
                    }
                """)

        self.horizontalLayout_5.addWidget(self.Dimmer)

        self.lcd_2 = QLCDNumber(self.groupBox_3)
        self.lcd_2.setObjectName(u"lcd_2")

        self.horizontalLayout_5.addWidget(self.lcd_2)
        self.lcd_2.setStyleSheet("""
                    QLCDNumber {
                        background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                                    stop: 0 #222, stop: 1 #555);
                        color: #00FF00;
                        border: 2px solid #00FF00;
                        border-radius: 10px;
                        padding: 5px;
                    }
                """)
        self.lcd_2.setMinimumSize(80, 80)
        self.lcd_2.setMaximumSize(1800, 800)

        self.verticalLayout_2.addWidget(self.groupBox_3)


        self.verticalLayout.addWidget(self.control_led)

        self.camera = QGroupBox(self.control)
        self.camera.setObjectName(u"camera")
        self.camera.setMaximumSize(QSize(16777215, 250))
        self.horizontalLayout_4 = QHBoxLayout(self.camera)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_6 = QGroupBox(self.camera)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMaximumSize(QSize(100, 16777215))
        self.groupBox_6.setStyleSheet(u"QGroupBox { border: 0px; }")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_12 = QGroupBox(self.groupBox_6)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_2 = QGridLayout(self.groupBox_12)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cam_0 = QPushButton(self.groupBox_12)
        self.cam_0.setObjectName(u"cam_0")
        icon1 = QIcon()
        icon1.addFile(u"../../../../UI/giao_dien/User/ADMIN/img/cctv-camera.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cam_0.setIcon(icon1)
        self.cam_0.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.cam_0, 0, 1, 1, 1)

        self.cam_1 = QPushButton(self.groupBox_12)
        self.cam_1.setObjectName(u"cam_1")
        self.cam_1.setIcon(icon1)
        self.cam_1.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.cam_1, 1, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_12)


        self.horizontalLayout_4.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.camera)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMaximumSize(QSize(100, 16777215))
        self.groupBox_7.setStyleSheet(u"QGroupBox { border: 0px; }")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_14 = QGroupBox(self.groupBox_7)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_5 = QGridLayout(self.groupBox_14)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.cam_2 = QPushButton(self.groupBox_14)
        self.cam_2.setObjectName(u"cam_2")
        self.cam_2.setIcon(icon1)
        self.cam_2.setIconSize(QSize(50, 50))

        self.gridLayout_5.addWidget(self.cam_2, 0, 0, 1, 1)

        self.cam_3 = QPushButton(self.groupBox_14)
        self.cam_3.setObjectName(u"cam_3")
        self.cam_3.setIcon(icon1)
        self.cam_3.setIconSize(QSize(50, 50))

        self.gridLayout_5.addWidget(self.cam_3, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_14)


        self.horizontalLayout_4.addWidget(self.groupBox_7)

        self.groupBox_10 = QGroupBox(self.camera)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMaximumSize(QSize(100, 16777215))
        self.groupBox_10.setStyleSheet(u"QGroupBox { border: 0px; }")
        self.groupBox_10.setFlat(False)
        self.groupBox_10.setCheckable(False)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_16 = QGroupBox(self.groupBox_10)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.gridLayout_6 = QGridLayout(self.groupBox_16)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.cam_4 = QPushButton(self.groupBox_16)
        self.cam_4.setObjectName(u"cam_4")
        self.cam_4.setIcon(icon1)
        self.cam_4.setIconSize(QSize(50, 50))

        self.gridLayout_6.addWidget(self.cam_4, 0, 0, 1, 1)

        self.cam_5 = QPushButton(self.groupBox_16)
        self.cam_5.setObjectName(u"cam_5")
        self.cam_5.setIcon(icon1)
        self.cam_5.setIconSize(QSize(50, 50))

        self.gridLayout_6.addWidget(self.cam_5, 1, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.groupBox_16)


        self.horizontalLayout_4.addWidget(self.groupBox_10)


        self.verticalLayout.addWidget(self.camera)

        self.groupBox_5 = QGroupBox(self.control)
        self.groupBox_5.setObjectName(u"groupBox_5")

        self.verticalLayout.addWidget(self.groupBox_5)


        self.horizontalLayout.addWidget(self.control)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)


        self.living_visible_l1 = False
        self.living_visible_l2 = False


        self.bed_visible_l1 = False
        self.bed_visible_l2 = False


        self.kitchen_visible_l1 = False
        self.kitchen_visible_l2 = False

        self.study_room_visible_l1 = False
        self.study_room_visible_l2 = False


        self.wc_visible = False
        self.flag = 0
        self.sw_0.clicked.connect(self.check_bt_0)
        self.sw_1.clicked.connect(self.check_bt_1)
        self.living_room.clicked.connect(lambda: setattr(self, 'flag', 1))
        self.bed_room.clicked.connect(lambda: setattr(self, 'flag', 2))
        self.kitchen.clicked.connect(lambda: setattr(self, 'flag', 3))
        self.wc.clicked.connect(lambda: setattr(self, 'flag', 4))
        self.study_room.clicked.connect(lambda: setattr(self, 'flag', 5))
        self.Dimmer.valueChanged.connect(self.update_lcd)
        #self.Dimmer.valueChanged.connect(self.updateSliderColor)
        self.update_lcd(0)
        self.stream_thread = None
        self.Dimmer.setMinimum(0)
        self.Dimmer.setMaximum(100)
        self.Dimmer.valueChanged.connect(self.check_dimmer)
        # Kết nối sự kiện nút nhấn để bắt đầu phát video
        #self.cam_0.clicked.connect(self.start_stream)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.giaodien.setTitle(QCoreApplication.translate("Widget", u"Interface", None))
        self.living_room.setText("")
        self.kitchen.setText("")
        self.bed_room.setText("")
        self.wc.setText("")
        self.control.setTitle(QCoreApplication.translate("Widget", u"Control", None))
        self.control_led.setTitle(QCoreApplication.translate("Widget", u"LED", None))
        self.groupBox_8.setTitle("")
        self.sw_0.setText("")
        self.groupBox_9.setTitle("")
        self.sw_1.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"Dim", None))
        self.camera.setTitle(QCoreApplication.translate("Widget", u"Camera", None))
        self.groupBox_6.setTitle("")
        self.groupBox_12.setTitle("")
        self.cam_0.setText("")
        self.cam_1.setText("")
        self.groupBox_7.setTitle("")
        self.groupBox_14.setTitle("")
        self.cam_2.setText("")
        self.cam_3.setText("")
        self.groupBox_10.setTitle("")
        self.groupBox_16.setTitle("")
        self.cam_4.setText("")
        self.cam_5.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("Widget", u"GroupBox", None))
    # retranslateUi

    def toggle_living_room_l1 (self):
        self.living_visible_l1 = not self.living_visible_l1
        if self.living_visible_l1:
            self.label_living_l1.show()
            self.set_red_style_l1()
        else:
            self.label_living_l1.hide()
            self.set_green_style_l1()
    def toggle_living_room_l2 (self):
        self.living_visible_l2 = not self.living_visible_l2
        if self.living_visible_l2:
            self.label_living_l2.show()
            self.set_red_style_l2()
        else:
            self.label_living_l2.hide()
            self.set_green_style_l2()
    def toggle_bed_room_l1 (self):
        self.bed_visible_l1 = not self.bed_visible_l1
        if self.bed_visible_l1:
            self.label_bed_l1.show()
            self.set_red_style_l1()
        else:
            self.label_bed_l1.hide()
            self.set_green_style_l1()
    def toggle_bed_room_l2 (self):
        self.bed_visible_l2 = not self.bed_visible_l2
        if self.bed_visible_l2:
            self.label_bed_l2.show()
            self.set_red_style_l2()
        else:
            self.label_bed_l2.hide()
            self.set_green_style_l2()
    def toggle_kitchen_l1 (self):
        self.kitchen_visible_l1 = not self.kitchen_visible_l1
        if self.kitchen_visible_l1:
            self.label_kitchen_l1.show()
            self.set_red_style_l1()
        else:
            self.label_kitchen_l1.hide()
            self.set_green_style_l1()
    def toggle_kitchen_l2 (self):
        self.kitchen_visible_l2 = not self.kitchen_visible_l2
        if self.kitchen_visible_l2:
            self.label_kitchen_l2.show()
            self.set_red_style_l2()
        else:
            self.label_kitchen_l2.hide()
            self.set_green_style_l2()
    def toggle_study_room_l1 (self):
        self.study_room_visible_l1 = not self.study_room_visible_l1
        if self.study_room_visible_l1:
            self.label_study_room_l1.show()
            self.set_red_style_l1()
        else:
            self.label_study_room_l1.hide()
            self.set_green_style_l1()
    def toggle_study_room_l2 (self):
        self.study_room_visible_l2 = not self.study_room_visible_l2
        if self.study_room_visible_l2:
            self.label_study_room_l2.show()
            self.set_red_style_l2()
        else:
            self.label_study_room_l2.hide()
            self.set_green_style_l2()
    def toggle_wc (self):
        self.wc_visible = not self.wc_visible
        if self.wc_visible:
            self.label_wc.show()
            self.set_red_style_l1()
        else:
            self.label_wc.hide()
            self.set_green_style_l1()
    def led_living(self):
        if (self.Dimmer.value() ==0):
            self.label_led_living1.hide()
            self.label_led_living2.hide()
            self.label_led_living3.hide()
        if (1<=self.Dimmer.value() <=50):
            self.label_led_living1.show()
            self.label_led_living2.hide()
            self.label_led_living3.hide()
        if (70>=self.Dimmer.value() >50):
            self.label_led_living1.hide()
            self.label_led_living2.show()
            self.label_led_living3.hide()
        if (100>=self.Dimmer.value() >70):
            self.label_led_living1.hide()
            self.label_led_living2.hide()
            self.label_led_living3.show()
        
    def led_kitchen(self):
        if (self.Dimmer.value() ==0):
            self.label_led_kitchen1.hide()
            self.label_led_kitchen2.hide()
            self.label_led_kitchen3.hide()
        if (1<=self.Dimmer.value() <=50):
            self.label_led_kitchen1.show()
            self.label_led_kitchen2.hide()
            self.label_led_kitchen3.hide()
        if (70>=self.Dimmer.value() >50):
            self.label_led_kitchen1.hide()
            self.label_led_kitchen2.show()
            self.label_led_kitchen3.hide()
        if (100>=self.Dimmer.value() >70):
            self.label_led_kitchen1.hide()
            self.label_led_kitchen2.hide()
            self.label_led_kitchen3.show()
    def led_bed1(self):
        if (self.Dimmer.value() ==0):
            self.label_led_bed1_1.hide()
            self.label_led_bed1_2.hide()
            self.label_led_bed1_3.hide()
        if (1<=self.Dimmer.value() <=50):
            self.label_led_bed1_1.show()
            self.label_led_bed1_2.hide()
            self.label_led_bed1_3.hide()
        if (70>=self.Dimmer.value() >50):
            self.label_led_bed1_1.hide()
            self.label_led_bed1_2.show()
            self.label_led_bed1_3.hide()
        if (100>=self.Dimmer.value() >70):
            self.label_led_bed1_1.hide()
            self.label_led_bed1_2.hide()
            self.label_led_bed1_3.show()
    def led_bed2(self):
        if (self.Dimmer.value() ==0):
            self.label_led_bed2_1.hide()
            self.label_led_bed2_2.hide()
            self.label_led_bed2_3.hide()
        if (1<=self.Dimmer.value() <=50):
            self.label_led_bed2_1.show()
            self.label_led_bed2_2.hide()
            self.label_led_bed2_3.hide()
        if (70>=self.Dimmer.value() >50):
            self.label_led_bed2_1.hide()
            self.label_led_bed2_2.show()
            self.label_led_bed2_3.hide()
        if (100>=self.Dimmer.value() >70):
            self.label_led_bed2_1.hide()
            self.label_led_bed2_2.hide()
            self.label_led_bed2_3.show()
    # def flag_livingroom (self):
    #     self.flag = 1
    def check_bt_0(self):
        if(self.flag == 1):
            self.toggle_living_room_l1()
        if(self.flag == 2):
            self.toggle_bed_room_l1()
        if(self.flag == 3):
            self.toggle_kitchen_l1()
        if(self.flag == 4):
            self.toggle_wc()
        if (self.flag == 5):
            self.toggle_study_room_l1()

    def check_bt_1(self):
        if(self.flag == 1):
            self.toggle_living_room_l2()
        if(self.flag == 2):
            self.toggle_bed_room_l2()
        if(self.flag == 3):
            self.toggle_kitchen_l2()
        if(self.flag == 4):
            self.toggle_wc()
        if(self.flag == 5):
            self.toggle_study_room_l2()
            
    def check_dimmer(self):
        if(self.flag==1):
            self.led_living()
        if(self.flag==2):
            self.led_bed1()
        if(self.flag==3):
            self.led_kitchen()
        if(self.flag==5):
            self.led_bed2()
            
    def update_lcd(self, value):
        brightness_levels = [0,25,50,75,100]
        percentage = brightness_levels[value]
        self.lcd_2.display(percentage)

    def updateSliderColor(self, value):
        # Tính toán màu sắc cho phần đã trượt
        # Tạo hiệu ứng sáng tối cho các vùng
        color = f"rgb({value * 85}, {255 - value * 85}, 255)"  # Dựa trên mức trượt
        self.Dimmer.setStyleSheet(f"""
            QSlider::groove:horizontal {{
                border: 1px solid #bbb;
                background: #f0f0f0;
                height: 15px;
                border-radius: 7px;
            }}
            QSlider::sub-page:horizontal {{
                background: {color};  /* Màu thay đổi theo giá trị */
                border-radius: 7px;
            }}
            QSlider::add-page:horizontal {{
                background: #ccc;
                border-radius: 7px;
            }}
            QSlider::handle:horizontal {{
                background: #007bff;
                border: 2px solid #0056b3;
                width: 20px;
                height: 20px;
                margin: -8px 0;
                border-radius: 10px;
            }}
            QSlider::handle:horizontal:hover {{
                background: #0056b3;
            }}
            QSlider::tick-mark:horizontal {{
                background: #000;
                width: 2px;
                height: 10px;
            }}
        """)

    def set_green_style_l1(self):
        """Thiết lập stylesheet cho màu xanh lục"""
        self.sw_0.setStyleSheet("""
            QPushButton {
                border: none;
                border-radius: 50px;
                background-color: #32CD32;  /* Xanh lục trung */
                color: white;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #28A428;  /* Đậm hơn khi hover */
            }
            QPushButton:pressed {
                background-color: #1E7B1E;  /* Rất đậm khi nhấn */
            }
        """)

    def set_red_style_l1(self):
        """Thiết lập stylesheet cho màu đỏ"""
        self.sw_0.setStyleSheet("""
            QPushButton {
                border: none;
                border-radius: 50px;
                background-color: #FF0000;  /* Đỏ cơ bản */
                color: white;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #CC0000;  /* Đậm hơn khi hover */
            }
            QPushButton:pressed {
                background-color: #990000;  /* Rất đậm khi nhấn */
            }
        """)

    def set_green_style_l2(self):
            """Thiết lập stylesheet cho màu xanh lục"""
            self.sw_1.setStyleSheet("""
                QPushButton {
                    border: none;
                    border-radius: 50px;
                    background-color: #32CD32;  /* Xanh lục trung */
                    color: white;
                    font-size: 16px;
                }
                QPushButton:hover {
                    background-color: #28A428;  /* Đậm hơn khi hover */
                }
                QPushButton:pressed {
                    background-color: #1E7B1E;  /* Rất đậm khi nhấn */
                }
            """)

    def set_red_style_l2(self):
            """Thiết lập stylesheet cho màu đỏ"""
            self.sw_1.setStyleSheet("""
                QPushButton {
                    border: none;
                    border-radius: 50px;
                    background-color: #FF0000;  /* Đỏ cơ bản */
                    color: white;
                    font-size: 16px;
                }
                QPushButton:hover {
                    background-color: #CC0000;  /* Đậm hơn khi hover */
                }
                QPushButton:pressed {
                    background-color: #990000;  /* Rất đậm khi nhấn */
                }
            """)


