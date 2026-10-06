from PyQt6.QtWidgets import QMainWindow, QFrame
from modules.app import app 
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QScrollArea

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

main_frame = QFrame(parent = main_window)
main_frame.setFixedSize(1024, 800)
main_frame.setStyleSheet("background-color:pink; border-radius: 15px")

scroll_area = QScrollArea(parent= main_frame)
scroll_area.setFixedSize(400,800)

scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

# запрещает scroll_area автоматически изменять размеры виджета
scroll_area.setWidgetResizable(False)
scroll_area.setStyleSheet("background-color:red")

scroll_content = QFrame(parent = scroll_area)
scroll_content.setFixedWidth(390)
scroll_content.setStyleSheet("background-color:green")

scroll_content_layout = QVBoxLayout()
scroll_content_layout.setSpacing(20)
scroll_content_layout.setContentsMargins(0, 0, 0, 0)
scroll_content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)


scroll_content.setLayout(scroll_content_layout)

for frame in range(50):
    frame_4 = QFrame( parent = scroll_area)
    frame_4.setStyleSheet("background-color:yellow")
    frame_4.setFixedSize(200,200)
    scroll_content_layout.addWidget(frame_4)

scroll_area.setWidget(scroll_content)



# 1. Создаем пространство в котором будет скролл
# 2. задать размеры этому пространству и выключить ненужный скролл (либо вправо. либо лево)
# 3. запрещает scroll_area автоматически изменять размеры виджета
# 4. создаем фрейм в котором будет размещен контент скролла
# 5. задаем схему размещения виджетов внутри скрола
# 6. устанавливаем схему размещения для фрейма
# 7.  добавляем фреймы внутрь скрола
# 8. устанавливаем виджет с контентом скролла в пространство сролла


























# frame_layout= QVBoxLayout()
# main_frame.setLayout(frame_layout)



# frame_4 = QFrame( parent = main_frame)
# frame_4.setStyleSheet("background-color:red")
# frame_4.setFixedSize(200,200)



# frame_2 = QFrame(parent=main_frame) 
# frame_2.setStyleSheet("background-color:blue")
# frame_2.setFixedSize(200,200)


# frame_3 = QFrame(parent= main_frame)
# frame_3.setStyleSheet("background-color: red")
# frame_3.setFixedSize(200,200)


# frame_layout.addWidget(frame_2)
# frame_layout.addWidget(frame_3)
# frame_layout.addWidget(frame_4)

# # .setSpacing() - метод, что бы задать растоние между фреймами внутри леяута(применяем к леяуту)
# frame_layout.setSpacing(100)
# # .setContentsMargins() - метод, что бы задать отсупы от окна слева, 
# # сверху, справа, снизн(применяем к леяуту)
# frame_layout.setContentsMargins(100, 50, 100, 50)
# # .setAlignment(Qt.AlignmentFlag.AlignCenter) - метод для выравнивания элементов(по центру, прибить к верху и тд)
# # AlignCenter - можно заменить на любой вид выравнивания
# frame_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)




