import time               
import colorama         # 색깔
colorama.init()
import msvcrt           # conio같은거
import threading        # 쓰레드 수행용
import sys              # 콘솔출력?
import os
import file


class TypingTest:
    def __init__(self, problems):
        self.problems = problems
        self.input_text = ""
        self.start_time = 0
        self.running = False
        self.current_cpm = 0
        self.i = 0
        self.content_line = ""
        self.total_correct_chars = 0
        self.total_elapsed_time = 0.0

    @staticmethod
    def count_character(input_text):        #글자수 세는거 
        return len(input_text.replace(" ", ""))

    @staticmethod
    def is_correct(input_text, problem_text):
        result = ""
        for j in range(len(problem_text)):
            if j < len(input_text):
                if problem_text[j] == input_text[j]:
                    result += "\033[32m" + input_text[j] + "\033[0m"        # 맞으면 녹색
                else:
                    result += "\033[41m" + problem_text[j] + "\033[0m"           # 틀리면 빨간색
            else:
                # 입력하지 않은 부분은 색칠 없이 원래 글자만 표시
                result += problem_text[j]
        return result

    def get_live_input(self):
        while self.running:
            if msvcrt.kbhit():
                ch = msvcrt.getwch()
                if ch == '\r':
                    self.running = False
                    continue
                elif ch == '\b':
                    self.input_text = self.input_text[:-1]
                elif ch == '\t':
                    self.input_text += '    '  # Tab을 공백 4칸으로 변환
                else:
                    self.input_text += ch
            
            # cpm_updater 로직을 이곳으로 통합합니다.
            now = time.time()
            elapsed = now - self.start_time
            if elapsed > 0:
                self.current_cpm = self.count_character(self.input_text) / elapsed * 60
            else:
                self.current_cpm = 0

            os.system('cls')
            print(f"문제 {self.i+1}    : {self.content_line}")
            print(f"현재 입력 : {self.input_text}                 | CPM: {self.current_cpm:.0f}")
            print(f"오타 표시 : {self.is_correct(self.input_text, self.content_line)}")
            time.sleep(0.05)

    @staticmethod
    def file_list():
        while True:
            level = input("난이도 입력하시오(상중하): ")

            if level == "상":
                
                return "python_hard.txt"
            elif level == "중":

                return "python_normal.txt"
            elif level == "하":
                
                return "python_easy.txt"
            elif level == "0":

                return "python_test.txt"
            else:
                print("상중하중에서만 입력해주세요")
                continue

    def run(self):
        print("타자연습을 시작합니다. (엔터로 각 문제 종료)")
        input("엔터를 누르면 타자 시작!")

        # [수정] 모든 문제의 전체 글자수를 미리 계산합니다.
        grand_total_chars = 0
        for p in self.problems:
            grand_total_chars += sum(self.count_character(line) for line in p.get('content', []))

        self.total_correct_chars = 0
        self.total_elapsed_time = 0.0

        for i, problem in enumerate(self.problems):
            self.i = i
            content_lines = problem.get('content', [])
            print(f"\n========== 문제 {i + 1} ==========")
            title = problem.get('title', '제목없음')
            desc = problem.get('desc','설명 없음')

            print(f"제목: {title}")
            print(f"설명: {desc}")
            print("----------------------------")

            for content_line in content_lines:
                if not content_line: # 내용이 없는 빈 줄은 건너뜁니다.
                    continue
                self.content_line = content_line.rstrip()       # \r\n 등 모든 줄바꿈 문자 제거
                self.input_text = ""
                self.start_time = time.time()
                self.running = True

                self.get_live_input()

                elapsed_this_line = time.time() - self.start_time
                self.total_elapsed_time += elapsed_this_line

                # [가독성 개선] 입력이 끝난 후, 맞춘 글자 수 계산
                
                # 공백 제외, 정확히 입력된 글자수 계산
                correct_chars_this_line = 0
                for i_char, char_in_problem in enumerate(self.content_line):
                    # 공백은 계산에서 제외
                    if char_in_problem == ' ':
                        continue
                    
                    # 사용자가 입력한 길이 내에 있고, 글자가 일치하는 경우
                    if i_char < len(self.input_text) and self.input_text[i_char] == char_in_problem:
                        correct_chars_this_line += 1
                
                self.total_correct_chars += correct_chars_this_line

                print(f"맞은 갯수: {self.total_correct_chars} / {grand_total_chars}")

                


              
        final_cpm = 0
        if self.total_elapsed_time > 0:
            final_cpm = (self.total_correct_chars / self.total_elapsed_time) * 60
        
        print(f"최종 타/분: {final_cpm:.0f}")

        time.sleep(0.3)





if __name__ == "__main__":
    file_name = TypingTest.file_list()
    all_problems = file.ProblemParser.parse_problems_from_file(file_name)
    test = TypingTest(all_problems)
    test.run()
        