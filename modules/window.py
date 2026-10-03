from PyQt6.QtWidgets import QMainWindow , QFrame, QHBoxLayout, QVBoxLayout,QGridLayout, QLabel
from modules.app import app



main_window = QMainWindow()

WIDTH_WINDOW = 1024
HEIGHT_WINDOW  = 800

# получаем обьект экрана
primary_screen = app.primaryScreen()
# получаем размеры экрана
screen_size = primary_screen.size()
# получаем ширину экрана
width_screen = screen_size.width()
# получаем высоту экрана
height_screen = screen_size.height()


main_window.setGeometry(
    (width_screen // 2) - (WIDTH_WINDOW // 2), 
    (height_screen // 2) - (HEIGHT_WINDOW // 2), 
    WIDTH_WINDOW, 
    HEIGHT_WINDOW
)

frame_1 = QFrame(parent=main_window)
frame_1.setStyleSheet("background-color:magenta; border-radius: 10px")
frame_1.setFixedSize(100 ,200)


# frame_1_layout = QVBoxLayout()
# frame_1.setLayout(frame_1_layout)



# frame_2 = QFrame(parent = frame_1)
# frame_2.setStyleSheet("background-color: green")
# frame_2.setFixedSize(50, 80)

# frame_3 = QFrame(parent= frame_1)
# frame_3.setStyleSheet("background-color: grey; border-radius: 10px")
# frame_3.setFixedSize(90 ,140)


# frame_4 = QFrame(parent=frame_1)
# frame_4.setStyleSheet("background-color: blue")
# frame_4.setFixedSize(60, 67)


# frame_1_layout.addWidget(frame_2)
# frame_1_layout.addWidget(frame_3)
# frame_1_layout.addWidget(frame_4)



# главный фрейм
frame_1_1 = QFrame(parent= main_window)
frame_1_1.setStyleSheet("background-color: black")
frame_1_1.setFixedSize(WIDTH_WINDOW, HEIGHT_WINDOW)

frame_1_2_layout = QGridLayout()
frame_1_1.setLayout(frame_1_2_layout)

# фреймы внутри
frame_1_2 = QFrame(parent= frame_1_1)
frame_1_2.setStyleSheet("background-color: red")
frame_1_2.setFixedSize(100, 100)

frame_1_3 = QFrame(parent= frame_1_1)
frame_1_3.setStyleSheet("background-color: white")
frame_1_3.setFixedSize(100, 100)

frame_1_4 = QFrame(parent= frame_1_1)
frame_1_4.setStyleSheet("background-color: yellow")
frame_1_4.setFixedSize(100, 100)

frame_1_5 = QFrame(parent= frame_1_1)
frame_1_5.setStyleSheet("background-color: green")
frame_1_5.setFixedSize(100, 100)

frame_1_6 = QFrame(parent= frame_1_1)
frame_1_6.setStyleSheet("background-color: purple")
frame_1_6.setFixedSize(100, 100)

frame_1_7 = QFrame(parent= frame_1_1)
frame_1_7.setStyleSheet("background-color: orange")
frame_1_7.setFixedSize(100, 100)





frame_1_2_layout.addWidget(frame_1_2, 1, 5)
frame_1_2_layout.addWidget(frame_1_3, 4, 6)
frame_1_2_layout.addWidget(frame_1_4, 2, 6)
frame_1_2_layout.addWidget(frame_1_5, 4, 5)
frame_1_2_layout.addWidget(frame_1_6, 2, 7)
frame_1_2_layout.addWidget(frame_1_7, 9, 7)


label1 = QLabel(
    text= "Hello world",
    parent= frame_1_1
)
label1.setStyleSheet("font-size: 104px; font-weight: 200; color: white")
