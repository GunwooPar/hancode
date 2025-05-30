import sys
print("hello", end="")   # flush 안 하면 바로 안 보일 수 있음
# sys.stdout.flush()       # 강제로 출력!















# import threading
# import time

# # 쓰레드가 할 일 정의 (작업개수, 작업속도, 직원이름)
# def doingJob(_jobs, _delay, _name):

#     print(f"{_name} 님에게 {_jobs}개의 일이 주어졌습니다.\n")

#     for i in range(_jobs):
#         print(f"{_name}님이 {i+1}번 째 일을 완료하였습니다.")
#         time.sleep(_delay)

#     print(f"{_name}님이 일을 마치고 퇴근합니다.\n")

# # 쓰레드 생성
# thread_1 = threading.Thread(target = doingJob, args = (5, 0.1, '일반직원'))
# thread_1.start()


# thread_2 = threading.Thread(target = doingJob, args = (10, 0.1, '관리직원'))
# thread_2.daemon = True          # 데몬 쓰레드 생성
# thread_2.start()

# # 메인 쓰레드
# doingJob(3, 0.1, '사장')