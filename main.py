import time               
import colorama         # 색깔
colorama.init()
import msvcrt           # conio같은거
import threading        # 쓰레드 수행용
import sys              # 콘솔출력?
import os




def count_character(input_text):        #글자수 세는거 
    return len(input_text.replace(" ", ""))

def cpm_updater():                  # 실시간 속도 출력
    global running, input_text, start_time, current_cpm
    while running:
        now = time.time()
        elapsed = now - start_time
        if elapsed > 0:
            current_cpm = count_character(input_text) / elapsed * 60
        else:
            current_cpm = 0
       
       
    
        time.sleep(0.01)



def is_correct(input_text, problem_text):
    result = ""
    for j in range(len(problem_text)):
        if j < len(input_text):     # 현재확인 중인 글자위치번호가 사용자가 입력중인 위치보다 작은가 
            if problem_text[j] == input_text[j]:
                result += "\033[32m" + input_text[j] + "\033[0m"        # 맞으면 녹색
            else:
                result += "\033[41m" + problem_text[j] + "\033[0m"           # 틀리면 빨간색
        else:
            result += "\033[41m" + problem_text[j] + "\033[0m"               # 틀리면 빨간색
    return result

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


def get_live_input():
    while running:
      
      if msvcrt.kbhit():        # 입력받는거 
                ch = msvcrt.getwch()
                if ch == '\r':  # 엔터
                    running = False
                    continue
                elif ch == '\b':  # 백스페이스
                    input_text = input_text[:-1]
                else:
                    input_text += ch        # 입력 받는거 바로바로 반영 
                
                print(f"문제 {i+1}    : {content_line}")
                print(f"\r현재 입력 : {input_text}                 | CPM: {current_cpm:.0f}        ", end="")
                print(f"오타 표시 : {is_correct(input_text, content_line)}",end="")

        

        

# 메인함수 
import file


file_name = file_list()
print("타자연습을 시작합니다. (엔터로 각 문제 종료)")
input("엔터를 누르면 타자 시작!")

all_problems = file.parse_problems_from_file(file_name)  # file.py에서 파일 불러오기 (딕셔너리(title,desc,content)가 들어있는 리스트형식)
for i, problem in enumerate(all_problems):
    content_lines = problem.get('content', [])

   
    

    print(f"\n========== 문제 {i + 1} ==========")
    
    title = problem.get('title', '제목없음')            # 딕셔너리에서 해당하는 키가 없으면 '제목없음' 반환 
    desc = problem.get('desc','설명 없음')

    print(f"제목: {title}")
    print(f"설명: {desc}")
    print("----------------------------")

    input_text = ""
    start_time = time.time()
    running = True

    # CPM 쓰레드 시작
    thread_1 = threading.Thread(target=cpm_updater)
    thread_1.daemon = True
    thread_1.start()

    get_live_input()


        






   # 마지막 결과 한 번 더 출력
    
    # print(f"오타 표시 : {typo(input_text, problem)}")
# print(f"정답 일치 : {input_text == problem}")
# print(f"\r최종 입력 : {input_text}")
print(f"최종 타/분: {count_character(input_text) / (time.time()-start_time) * 60:.0f}")

time.sleep(0.3)





# def jugment():
#   for i in range(len(problems)):      #행 수만큼 반복
#     print()
#     enter=input(problems[i]+"\n")              # 한줄씩 입력받음 
#     typo(enter,i)
#     if i+1< len(problems):     
#       pass                  
#     else:
        





        