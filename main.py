import time               
import colorama         # 색깔
colorama.init()
import msvcrt           # conio같은거
import threading        # 쓰레드 수행용
import sys              # 콘솔출력?
import os

def count_character(input_text):
    return len(input_text.replace(" ", ""))

def cpm_updater():
    global running, input_text, start_time
    while running:
        now = time.time()
        elapsed = now - start_time
        if elapsed > 0:
            cpm = count_character(input_text) / elapsed * 60
        else:
            cpm = 0
       
        print(f"\r현재 입력 : {input_text} | CPM: {cpm:.0f}        ", end="")
        sys.stdout.flush()
        time.sleep(0.01)



def typo(input_text, problem):
    result = ""
    for j in range(len(problem)):
        if j < len(input_text):
            if problem[j] == input_text[j]:
                result += "\033[32m" + input_text[j] + "\033[0m"
            else:
                result += "\033[41m" + problem[j] + "\033[0m"
        else:
            result += "\033[41m" + problem[j] + "\033[0m"
    return result

#메인함수 
import file
file.get_file()

print("타자연습을 시작합니다. (엔터로 각 문제 종료)")
input("엔터를 누르면 타자 시작!")
for i, problem in enumerate(file.global_problems):
    print(f"\n문제 {i+1}  : {problem}")
    
    input_text = ""
    start_time = time.time()
    running = True

    # CPM 쓰레드 시작
    thread_1 = threading.Thread(target=cpm_updater)
    thread_1.daemon = True
    thread_1.start()

    while True:
        if msvcrt.kbhit():        #입력받는거 
            ch = msvcrt.getwch()
            if ch == '\r':  # 엔터
                running = False
                break
            elif ch == '\b':
                input_text = input_text[:-1]
            else:
                input_text += ch
            
            os.system('cls')
            print(f"문제 {i+1}    : {problem}")
            print(f"현재 입력 : {input_text}")
            print(f"오타 표시 : {typo(input_text, problem)}")


    # 마지막 결과 한 번 더 출력
    print(f"최종 입력 : {input_text}")
    print(f"오타 표시 : {typo(input_text, problem)}")
    print(f"정답 일치 : {input_text == problem}")
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
        





        