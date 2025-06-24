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

    def cpm_updater(self):                  # 실시간 속도 출력
        while self.running:
            now = time.time()
            elapsed = now - self.start_time
            if elapsed > 0:
                self.current_cpm = self.count_character(self.input_text) / elapsed * 60
            else:
                self.current_cpm = 0
            time.sleep(0.01)

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
        for i, problem in enumerate(self.problems):
            self.i = i
            content_lines = problem.get('content', [])
            print(f"\n========== 문제 {i + 1} ==========")
            title = problem.get('title', '제목없음')            # 딕셔너리에서 해당하는 키가 없으면 '제목없음' 반환 
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

                # CPM 쓰레드 시작
                thread_1 = threading.Thread(target=self.cpm_updater)
                thread_1.daemon = True
                thread_1.start()

               
                self.get_live_input()

                


              
            
            




   # 마지막 결과 한 번 더 출력
    
    # print(f"오타 표시 : {typo(input_text, problem)}")
# print(f"정답 일치 : {input_text == problem}")
# print(f"\r최종 입력 : {input_text}")
        print(f"최종 타/분: {self.count_character(self.input_text) / (time.time()-self.start_time) * 60:.0f}")

        time.sleep(0.3)





# def jugment():
#   for i in range(len(problems)):      #행 수만큼 반복
#     print()
#     enter=input(problems[i]+"\n")              # 한줄씩 입력받음 
#     typo(enter,i)
#     if i+1< len(problems):     
#       pass                  
#     else:
        





        
if __name__ == "__main__":
    file_name = TypingTest.file_list()
    all_problems = file.ProblemParser.parse_problems_from_file(file_name)
    test = TypingTest(all_problems)
    test.run()
        