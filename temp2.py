import time

# 예시 코드
example_code = [
    
    'def hello():',
    'print("hello world")'
]

print("아래 코드를 그대로 입력하세요. (엔터로 줄바꿈)")
for line in example_code:
    print(line)

input("준비되면 엔터를 누르세요...")  # 준비 신호

user_input = []
start = time.time()  # 시작 시간 기록
import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import Qt

EXAMPLE_CODE = [
    'def hello():',
    '    print("hello world")'
]

class TypingPractice(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("코드 타자연습 (PyQt5)")
        self.layout = QVBoxLayout()
        self.labels = []
        self.inputs = []
        self.result_labels = []
        self.current_line = 0
        self.start_time = None
        self.end_time = None
        self.user_inputs = []
        self.stats_label = QLabel("")  # 결과 통계 출력 라벨

        # 예시 코드 출력
        self.layout.addWidget(QLabel("아래 코드를 한 줄씩 입력하세요."))
        for idx, line in enumerate(EXAMPLE_CODE):
            label = QLabel(line)
            self.labels.append(label)
            self.layout.addWidget(label)
            # 입력란 및 결과 라벨 추가
            input_line = QLineEdit()
            input_line.returnPressed.connect(self.check_line)
            # 첫 입력란에 포커스되면 시작시간 기록
            if idx == 0:
                input_line.focusInEvent = self.make_focus_handler(input_line)
            self.inputs.append(input_line)
            self.layout.addWidget(input_line)
            result_label = QLabel("")
            self.result_labels.append(result_label)
            self.layout.addWidget(result_label)

        # 초기: 첫 줄만 활성화
        for i in range(1, len(self.inputs)):
            self.inputs[i].setDisabled(True)

        self.layout.addWidget(self.stats_label)  # 통계 라벨 추가
        self.setLayout(self.layout)

    def make_focus_handler(self, widget):
        # 첫 입력란에 포커스됐을 때 시간 기록
        def handler(event):
            if self.start_time is None:
                self.start_time = time.time()
            QLineEdit.focusInEvent(widget, event)
        return handler

    def check_line(self):
        idx = self.current_line
        typed = self.inputs[idx].text()
        self.user_inputs.append(typed)
        ref = EXAMPLE_CODE[idx]
        result = ""
        min_len = min(len(typed), len(ref))
        # 비교 및 색상 표시
        for i in range(min_len):
            if typed[i] == ref[i]:
                result += typed[i]
            else:
                result += f'<span style="color:red">{typed[i]}</span>'
        # 남은 부분 처리 (오타 or 미입력)
        if len(typed) > len(ref):
            result += f'<span style="color:red">{typed[min_len:]}</span>'
        elif len(typed) < len(ref):
            result += f'<span style="color:red">{ref[min_len:]}</span>'

        self.result_labels[idx].setText(result)
        self.result_labels[idx].setTextFormat(Qt.RichText)

        # 다음 줄 입력란 활성화
        if idx + 1 < len(self.inputs):
            self.inputs[idx + 1].setDisabled(False)
            self.inputs[idx + 1].setFocus()
            self.current_line += 1
        else:
            # 마지막 줄까지 다 입력한 경우
            self.end_time = time.time()
            self.show_stats()

    def show_stats(self):
        total_chars = sum(len(line) for line in self.user_inputs)
        elapsed = self.end_time - self.start_time if self.end_time and self.start_time else 0.001
        cpm = (total_chars / elapsed) * 60
        stats = (
            f"<b>=== 결과 통계 ===</b><br>"
            f"입력한 문자 수: {total_chars}<br>"
            f"경과 시간: {elapsed:.2f}초<br>"
            f"분당 타자수(CPM): {cpm:.2f}"
        )
        self.stats_label.setText(stats)
        self.stats_label.setTextFormat(Qt.RichText)

app = QApplication(sys.argv)
window = TypingPractice()
window.show()
sys.exit(app.exec_())



for i, line in enumerate(example_code):
    typed = input(f"{i+1}번째 줄: ")
    user_input.append(typed)

end = time.time()  # 종료 시간 기록

# 문자 수 집계
total_chars = sum(len(line) for line in user_input)

# 경과 시간 (초)
elapsed = end - start

# 분단위 환산
cpm = (total_chars / elapsed) * 60

print("\n=== 결과 ===")
print(f"입력한 문자 수: {total_chars}")
print(f"경과 시간: {elapsed:.2f}초")
print(f"분당 타자수(CPM): {cpm:.2f}")
