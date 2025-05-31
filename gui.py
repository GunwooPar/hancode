# import sys
# from PyQt5.QtWidgets import *


# class Mainwindow(QMainWindow):  
#     def __init__(self):                           
#         super().__init__()

#         self.setWindowTitle("hancode")

#         self.resize(2000,1600)     

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mywindow = Mainwindow()
#     mywindow.show()
#     app.exec_()





# import sys
# from PyQt5.QtWidgets import *

# app = QApplication(sys.argv)

# window = QWidget()
# window.show()

# app.exec_()




# import sys
# from PyQt5.QtWidgets import *

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("hancode")
#         self.setGeometry(300,300,400,400)


# app = QApplication(sys.argv)

# window = MyWindow()   
# # 위의 기본 코드와 다른 점
# # QMainWindow 클래스를 상속받은 MyWindow 클래스를 선언
# # 그 후 부모클래스를 의미하는 super()메소드와 그 클래스의 속성을 불러오는 __init__ 초기화 메소드 사용
# # QMainWindow의 속성이 무엇인지는 모르겠음

# window.show()

# app.exec_()



import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):    
        btn = QPushButton("버튼", self)
        btn.clicked.connect(self.surprise)

    def surprise(self):
        print("으엌! 깜짝이야!!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
    
#해당 코드 실행 시 부터 이벤트 루프 발생 (즉, 이 코드 아래로는 이벤트 발생 전까지 안내려감)
app.exec_()

print("루프 밖")