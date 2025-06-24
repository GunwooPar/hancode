import sys
import time
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                             QLabel, QLineEdit, QStackedWidget, QTextEdit)
from PyQt6.QtCore import Qt, QTimer, QEvent
from PyQt6.QtGui import QFont, QKeyEvent

import file
from main import TypingTest
import graph_plotter # 그래프 플로터 임포트

class TypingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.typing_test = None
        self.content_iterator = None
        self.grand_total_chars = 0
        self.line_start_time = 0.0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_text_changed)
        self.current_item = None # 현재 처리 중인 아이템 추적
        self.time_history = []  # 시간 기록
        self.cpm_history = []   # CPM 기록
        self.init_ui()
        self._apply_styles() # UI 설정 후 스타일 적용

    def init_ui(self):
        self.setWindowTitle('타자 연습')

        # [수정] 화면에 잘리지 않도록 창 크기와 위치 계산 로직을 변경합니다.
        main_width, main_height = 650, 750
        graph_width = 700  # graph_plotter.py와 맞출 그래프 너비
        MARGIN = 20

        # 두 창과 여백을 합친 전체 너비
        total_width = main_width + MARGIN + graph_width

        screen_geometry = QApplication.primaryScreen().geometry()

        # 전체 블록을 화면 중앙에 위치시키기 위한 시작 x좌표 계산
        start_x = (screen_geometry.width() - total_width) // 2
        
        # 메인 창 위치 설정 (화면 밖으로 나가지 않도록 보정)
        main_x = max(20, start_x)
        main_y = (screen_geometry.height() - main_height) // 2

        self.setGeometry(main_x, main_y, main_width, main_height)

        main_layout = QVBoxLayout()
        self.stacked_widget = QStackedWidget()
        self.setup_start_screen()
        self.setup_typing_screen()
        main_layout.addWidget(self.stacked_widget)
        self.setLayout(main_layout)

    def _apply_styles(self):
        """애플리케이션 전체에 다크 테마 스타일시트를 적용합니다."""
        self.setStyleSheet("""
            QWidget {
                background-color: #2E3440; /* 배경색 (Nord Polar Night) */
                color: #ECEFF4; /* 기본 글자색 (Nord Snow Storm) */
            }
            QPushButton {
                background-color: #5E81AC; /* 버튼색 (Nord Frost) */
                border: none;
                border-radius: 5px; /* 둥근 모서리 */
                padding: 10px;
                font-size: 16px;
                font-family: Arial;
            }
            QPushButton:hover {
                background-color: #81A1C1; /* 마우스 올렸을 때 색 */
            }
            QTextEdit, QLineEdit {
                background-color: #3B4252; /* 입력창 배경 */
                border-radius: 5px;
                border: 1px solid #4C566A; /* 입력창 테두리 */
                padding: 8px;
                font-family: 'Courier New';
                font-size: 16px;
            }
            QLabel {
                font-family: 'Courier New';
                font-size: 16px;
            }
        """)

    def setup_start_screen(self):
        start_widget = QWidget()
        layout = QVBoxLayout(start_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label = QLabel('타자 연습')
        title_label.setStyleSheet("font-size: 32px; font-family: Arial; font-weight: bold; color: #88C0D0;")
        layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignCenter)
        button_layout = QHBoxLayout()
        levels = {"상": "python_hard.txt", "중": "python_normal.txt", "하": "python_easy.txt"}
        for level, filename in levels.items():
            button = QPushButton(level)
            button.clicked.connect(lambda _, f=filename: self.start_typing_test(f))
            button_layout.addWidget(button)
        layout.addLayout(button_layout)
        self.stacked_widget.addWidget(start_widget)

    def setup_typing_screen(self):
        typing_widget = QWidget()
        layout = QVBoxLayout(typing_widget)
        self.history_view = QTextEdit()
        self.history_view.setReadOnly(True)
        layout.addWidget(self.history_view)
        self.correction_label = QLabel("여기에 문제가 표시됩니다.")
        layout.addWidget(self.correction_label)
        self.input_line = QLineEdit()
        self.input_line.installEventFilter(self)
        self.input_line.textChanged.connect(self.on_text_changed)
        layout.addWidget(self.input_line)
        self.info_label = QLabel("CPM: 0 | 진행도: 0 / 0")
        self.info_label.setStyleSheet("font-size: 12px; font-family: Arial; color: #81A1C1;")
        layout.addWidget(self.info_label)
        self.stacked_widget.addWidget(typing_widget)
    
    def start_typing_test(self, file_name):
        problems = file.ProblemParser.parse_problems_from_file(file_name)
        self.typing_test = TypingTest(problems)
        self.grand_total_chars = self.typing_test._calculate_grand_total_chars()
        
        all_content_items = []
        for i, p in enumerate(self.typing_test.problems):
            title = p.get('title', '제목없음')
            desc = p.get('desc', '설명 없음')
            all_content_items.append({'type': 'marker', 'text': f"========== 문제 {i + 1} =========="})
            all_content_items.append({'type': 'info', 'text': f"제목: {title}"})
            all_content_items.append({'type': 'info', 'text': f"설명: {desc}"})
            
            content_lines = [line for line in p.get('content', []) if line.strip()]
            num_lines = len(content_lines)
            for j, line in enumerate(content_lines):
                position = 'middle'
                if num_lines == 1:
                    position = 'single'
                elif j == 0:
                    position = 'first'
                elif j == num_lines - 1:
                    position = 'last'
                all_content_items.append({'type': 'code', 'text': line, 'position': position})

        self.content_iterator = iter(all_content_items)
        self.input_line.returnPressed.connect(self.advance_to_next_item)
        self.stacked_widget.setCurrentIndex(1)
        self.timer.start(100)
        self.time_history.clear()
        self.cpm_history.clear()
        self.advance_to_next_item()

    def advance_to_next_item(self):
        if self.typing_test.content_line:
            elapsed_this_line = time.time() - self.line_start_time
            self.typing_test.total_elapsed_time += elapsed_this_line
            correct_chars_this_line = 0
            for i, char in enumerate(self.typing_test.content_line):
                if char == ' ': continue
                if i < len(self.typing_test.input_text) and self.typing_test.input_text[i] == char:
                    correct_chars_this_line += 1
            self.typing_test.total_correct_chars += correct_chars_this_line
            
            position = 'middle'
            if self.current_item and self.current_item.get('type') == 'code':
                position = self.current_item.get('position', 'middle')
            
            completed_html = self.typing_test.is_correct(
                self.typing_test.input_text,
                self.typing_test.content_line,
                position
            )
            self.history_view.append(completed_html)

        self.current_item = next(self.content_iterator, None)
        item = self.current_item
        
        if item is None:
            self.show_results()
            return

        item_type = item.get('type')
        if item_type in ['marker', 'info']:
            if item_type == 'marker':
                self.history_view.append(f"<br><b>{item['text']}</b>")
            elif item_type == 'info':
                self.history_view.append(f"<i>{item['text']}</i>")
            
            self.typing_test.content_line = ""
            self.advance_to_next_item()
        elif item_type == 'code':
            self.typing_test.content_line = item['text']
            self.input_line.clear()
            self.input_line.setFocus()
            self.line_start_time = time.time()
            self.on_text_changed()

    def on_text_changed(self):
        if not self.typing_test or not self.typing_test.content_line: return
        self.typing_test.input_text = self.input_line.text()
        
        position = 'middle'
        if self.current_item and self.current_item.get('type') == 'code':
            position = self.current_item.get('position', 'middle')

        html_text = self.typing_test.is_correct(self.typing_test.input_text, self.typing_test.content_line, position)
        self.correction_label.setText(html_text)
        
        elapsed = time.time() - self.line_start_time
        current_cpm = 0
        if elapsed > 0:
            current_cpm = (self.typing_test.count_character(self.typing_test.input_text) / elapsed) * 60
        
        # [수정] 0.1초 간격의 시간과 CPM을 함께 기록
        current_time_point = len(self.time_history) * 0.1
        self.time_history.append(current_time_point)
        self.cpm_history.append(current_cpm)
        
        progress_text = f"진행도: {self.typing_test.total_correct_chars} / {self.grand_total_chars}"
        cpm_text = f"CPM: {current_cpm:.0f}"
        self.info_label.setText(f"{cpm_text} | {progress_text}")

    def show_results(self):
        self.timer.stop()
        self.input_line.setEnabled(False)
        self.correction_label.setText("")
        
        final_cpm = 0
        if self.typing_test.total_elapsed_time > 0:
            final_cpm = (self.typing_test.total_correct_chars / self.typing_test.total_elapsed_time) * 60
        
        self.history_view.append(f"<hr><h3>최종 평균 타수: {final_cpm:.0f}</h3>")
        self.info_label.setText("")

        if self.time_history and self.cpm_history:
            # getRect()로 현재 창의 최종 위치/크기 정보를 가져옵니다.
            main_window_geometry = self.geometry().getRect()
            graph_plotter.plot_cpm_history(
                self.time_history, self.cpm_history, main_window_geometry
            )

    def eventFilter(self, obj, event):
        """이벤트 필터: input_line에서 발생하는 이벤트를 가로챕니다."""
        if obj is self.input_line and event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Tab:
                self.input_line.insert('    ')
                return True  # True를 반환하여 이벤트가 다른 곳으로 전파되는 것을 막습니다.
        return super().eventFilter(obj, event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TypingApp()
    ex.show()
    sys.exit(app.exec()) 