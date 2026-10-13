from PyQt6.QtWidgets import QMainWindow,QFrame , QScrollArea, QVBoxLayout,QHBoxLayout, QLabel
from PyQt6.QtCore import Qt
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

frame_0 = QFrame(parent= main_window)
frame_0.setStyleSheet("background-color: pink")
frame_0.setFixedSize(1024,800)
horizonal_layout = QHBoxLayout()
frame_0.setLayout(horizonal_layout)

main_scroll = QScrollArea(parent = frame_0)
main_scroll.setFixedWidth(400)
main_scroll.setFixedHeight(800)
main_scroll.setStyleSheet("background-color:purple")

main_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

main_scroll.setWidgetResizable(False)

frame_scroll = QFrame(parent=main_scroll) 
frame_scroll.setFixedWidth(390) 
frame_scroll.setStyleSheet("background-color:red;")



layout = QVBoxLayout()
frame_scroll.setLayout(layout)


list_1 = ["Oksana", "Liza", "Masha", "Lesha", "Sergey", "Maksim", "Arina", "Milana"] 

for name in list_1:
    frame = QFrame(parent= frame_scroll)
    frame.setStyleSheet("background-color:green; border-radius 10px")
    frame.setFixedSize(300,200)
    layout.addWidget(frame)
    lable = QLabel(text = name, parent = frame)
    


main_scroll.setWidget(frame_scroll)

frame_2 = QFrame(parent= frame_0)
frame_2.setFixedSize(550,700)
frame_2.setStyleSheet("background-color: white; border-radius: 10px")



horizonal_layout.addWidget(main_scroll)
horizonal_layout.addWidget(frame_2)


layout_1 = QVBoxLayout()
layout_1.setAlignment(Qt.AlignmentFlag.AlignTop)
frame_2.setLayout(layout_1)



frame_avatar = QFrame(parent= frame_2)
frame_avatar.setStyleSheet("background-color: pink")
frame_avatar.setFixedSize(100,100)
initials_label = QLabel("VK", parent=frame_avatar)
initials_label.setStyleSheet("color: purple; font-size: 24px")
layout_1.addWidget(frame_avatar)




name_surname = QLabel("Andrii Lovikov")
name_surname.setStyleSheet("font-size: 16px")
layout_1.addWidget(name_surname)