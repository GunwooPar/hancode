import html
import file

class TypingTest:
    def __init__(self, problems):
        self.problems = problems
        # GUI에서 상태를 관리하므로, 필요한 최소한의 속성만 남깁니다.
        self.input_text = ""
        self.content_line = ""
        self.total_correct_chars = 0
        self.total_elapsed_time = 0.0

    @staticmethod
    def count_character(input_text):
        return len(input_text.replace(" ", ""))

    @staticmethod
    def is_correct(input_text, problem_text, position='middle'):
        """
        입력 텍스트와 문제 텍스트를 비교하여,
        PyQt의 QLabel에서 표시할 수 있는 HTML 문자열을 반환합니다.
        position: 'first', 'last', 'middle', 'single' 중 하나로, 줄의 위치에 따라 다른 테두리를 적용합니다.
        """
        result = ""
        escaped_problem_text = html.escape(problem_text)
        for j, char_to_display in enumerate(escaped_problem_text):
            if j < len(input_text):
                if input_text[j] == problem_text[j]:
                    result += f'<span style="color: #00FF00;">{char_to_display}</span>'
                else:
                    result += f'<span style="background-color: #FF4444;">{char_to_display}</span>'
            else:
                result += f'<span>{char_to_display}</span>'
        
        # [수정] 줄의 위치(position)에 따라 다른 테두리 스타일을 적용합니다.
        style = 'white-space: pre; margin: 0; padding: 2px;'
        border_color = '#AAAAAA'

        if position == 'first':
            style += f' border-top: 1px solid {border_color};'
        elif position == 'last':
            style += f' border-bottom: 1px solid {border_color};'
        elif position == 'single':
            style += f' border-top: 1px solid {border_color}; border-bottom: 1px solid {border_color};'
        
        return f'<p style="{style}">{result}</p>'

    def _calculate_grand_total_chars(self):
        """모든 문제의 공백 제외 전체 글자 수를 계산합니다."""
        total_chars = 0
        for p in self.problems:
            total_chars += sum(self.count_character(line) for line in p.get('content', []))
        return total_chars
        