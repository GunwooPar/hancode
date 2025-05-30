import time             # 시간측정용
import msvcrt           # conio같은거
import threading        # 쓰레드 수행용
import sys              # 콘솔출력?

def count_character(input_text):          # 글자수 계산(공백빼고)
    return len(text.replace(" ", ""))   

def cpm_updater():          # 분당 입력 속도 실시간 갱신 함수 
    global running, input_text, start_time      # 전역변수 선언 
    while running:
        now = time.time()               # 현재시간(초 형태로)
        elapsed = now - start_time
        # 실시간 cpm(공백 제외 글자수/시간*60)  타수(타/분) CPM(Characters Per Minute) 
        if elapsed > 0:
            cpm = count_character(input_text) / elapsed * 60
        else:
            cpm = 0
        # 실시간 표출
        print(f"\r현재 입력: {input_text} | CPM: {cpm:.0f}        ", end="")  # end=""의 의미:줄바꿈안할려고 원래는 print할때마다 줄바꿈(\r)이 자동으로 들어감
        sys.stdout.flush()                                                   # 버퍼에 쌓은 내용을 바로 내보내려고(일반적인 환경에서는 안써도되는데 호환성을 위해)
        time.sleep(0.001)


# 메인함수
input("아무 글자나 입력하세요(끝내려면 Enter): ")
print("입력 시작(Enter로 종료): ")
input_text = ''
start_time = time.time()                    # 현재시간(초 형태로)
running = True

# 쓰레드로 CPM 업데이트 실행
thread_1 = threading.Thread(target=cpm_updater)
thread_1.daemon = True              # 데몬쓰레드(메인 함수 끝나면 얘도 그냥 종료됨)
thread_1.start()

while True:  
    if msvcrt.kbhit():                  # 입력하는지 안하는지 검사 (버퍼없이)
        ch = msvcrt.getwch()
        if ch == '\r':  # 엔터면 종료
            running = False  # 데몬 쓰레드라서 메인함수가 끝나면 자동으로 함수가 종료되지만 실시간으로 while문 종료시키기위해   
            break
        elif ch == '\b':                        # 백스페이스 처리
            input_text = input_text[:-1]
        else:
            input_text += ch
    # 사용자가 입력 안 하고 있으면 자연스럽게 cpm 내려감 (글자수 증가가 없으니)

time.sleep(0.5)  # 마지막 출력 반영 시간
print(f"\n입력 종료. 총 입력: {input_text} | 최종 타/분: {count_character(input_text) / (time.time()-start_time) * 60:.0f}")




































































