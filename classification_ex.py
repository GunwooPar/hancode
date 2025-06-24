import time
import msvcrt
import os

# ------------------------------------------------------------------
# 1. 핵심 로직을 담은 '엔진' 클래스
# ------------------------------------------------------------------
class TypingGame:
    def __init__(self, problem_text: str):
        """타자 연습 한 판에 대한 모든 상태와 로직을 관리합니다."""
        self.problem_text = problem_text
        self.input_text = ""
        self.start_time = None  
        self.is_running = True

    def start_if_not_running(self):
        """첫 키 입력 시 게임을 시작하고 시작 시간을 기록합니다."""
        if self.start_time is None:
            self.start_time = time.time()

    def process_keypress(self, key: str):
        """키 입력을 받아 내부 상태를 업데이트합니다."""
        self.start_if_not_running() # 첫 키가 눌리면 시간 측정 시작
        
        if key == '\b':  # 백스페이스
            self.input_text = self.input_text[:-1]
        # 엔터, 탭 등 제어 문자는 입력되지 않도록 처리
        elif not key.isprintable() or key == '\r':
            pass
        else:
            self.input_text += key
    
    def get_stats(self) -> dict:
        """현재 타속(CPM)과 정확도를 계산하여 딕셔너리로 반환합니다."""
        if self.start_time is None:
            return {'cpm': 0, 'accuracy': 0.0}

        elapsed = time.time() - self.start_time
        if elapsed == 0:
            return {'cpm': 0, 'accuracy': 0.0}

        # 공백 포함 글자 수 기준 CPM
        cpm = (len(self.input_text) / elapsed) * 60

        # 정확도
        correct_chars = 0
        typed_len = len(self.input_text)
        for i in range(typed_len):
            if i < len(self.problem_text) and self.input_text[i] == self.problem_text[i]:
                correct_chars += 1
        accuracy = (correct_chars / typed_len * 100) if typed_len > 0 else 0.0
        
        return {'cpm': cpm, 'accuracy': accuracy}

# ------------------------------------------------------------------
# 2. 화면 표시를 도와주는 유틸리티 함수
# ------------------------------------------------------------------
def format_text_for_display(input_text: str, problem_text: str) -> str:
    """사용자 입력과 정답을 비교하여 색깔있는 문자열로 만듭니다."""
    result = ""
    for i in range(len(problem_text)):
        if i < len(input_text):
            if input_text[i] == problem_text[i]:
                result += f"\033[32m{input_text[i]}\033[0m"  # 초록색
            else:
                result += f"\033[41m{problem_text[i]}\033[0m"  # 빨간 배경
        else:
            result += f"\033[90m{problem_text[i]}\033[0m"  # 회색 (아직 입력 안 함)
    return result

# ------------------------------------------------------------------
# 3. 프로그램의 전체 흐름을 제어하는 메인 실행부
# ------------------------------------------------------------------
if __name__ == "__main__":
    # 이 부분은 파일 처리, 난이도 선택 등 기존 로직을 그대로 사용 가능합니다.
    # 예시를 위해 문제 텍스트를 직접 지정합니다.
    # problems = parse_problems_from_file('python_easy.txt')
    problems = [{'content': ["이것은 새로운 구조의 예시 문장입니다.", "로직과 화면이 완벽하게 분리되었습니다."]}]

    print("타자 연습을 시작합니다. (엔터로 각 줄 종료)")
    input("엔터를 누르면 타자 시작!")

    for i, problem_data in enumerate(problems):
        content_lines = problem_data.get('content', [])
        
        print(f"\n========== 문제 {i + 1} ==========")
        # ... (제목, 설명 출력) ...

        for line_text in content_lines:
            
            # 1. 한 줄짜리 타자 게임 '엔진'을 생성합니다.
            game = TypingGame(line_text)

            # 2. 이 한 줄에 대한 메인 루프를 실행합니다.
            while game.is_running:
                
                # --- 입력 처리 ---
                if msvcrt.kbhit():
                    key = msvcrt.getwch()
                    if key == '\r':
                        game.stop() # 엔진에게 종료 신호를 보냄
                        continue
                    game.process_keypress(key) # 키 입력을 엔진에게 전달

                # --- 화면 그리기 ---
                os.system('cls' if os.name == 'nt' else 'clear')
                stats = game.get_stats() # 엔진에게 현재 상태를 물어봄

                # 엔진이 보내준 데이터를 화면에 예쁘게 표시
                print(f"문제: {game.problem_text}")
                print("-" * 40)
                print(f"입력: {format_text_for_display(game.input_text, game.problem_text)}")
                print("-" * 40)
                print(f"타속: {stats['cpm']:.0f} CPM | 정확도: {stats['accuracy']:.2f}%")
                
                time.sleep(0.03)

    print("\n모든 문제를 완료했습니다!")