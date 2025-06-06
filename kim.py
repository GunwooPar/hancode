import time 
from tkinter import *
def jugment(i):
  wind = Tk()     # 새로운 창 생성
  wind.geometry("1000x800")           # 화면크기 

  # ()
  enter=str(input(words[i])) 
  typo(enter,i)
  if i+1 <= len(words):
    jugment(i+1)
  else:
    print("")                 #여기는 다시 출력되게 하던지 틀린곳을 지적하고 넘어가게 할것인지

def typo(enter,i):
  for j in range(0,len(words[i])):
      if words[i][j]== enter[j]:
        print("\033[32",enter(j), end ="")
      else:
        print("\033[41m",words[i][j], end="")
  print("")



# 메인 함수

words=["#include"]              #여기는 명령어(출력할 것, 입력받아야할 단어들을 넣는 공간)
win = Tk()
win.geometry("1000x800")

btn=Button(win)
btn.config(text = "시작하려면 버튼을 누르세요")
btn.pack()
win.mainloop     
                     # ->터틀모듈을 이용해서 마우스를 따라다니는 것을 만들고 마우스를 클릭하면 시작되게 만들면 될듯                                          #터틀에 글을 작성할 수 있으면 위부터 아래로 (한컴타자처럼 만들면 될거 같음)
   #시작
jugment(0)

                                                      #여기까지 기본적인 틀
                           




def typo(enter,i):
 for j in range(len(problems[i])):
    if j < len(enter):
        # 정상 비교
        if problems[i][j] == enter[j]:
            print("\033[32m"+enter[j]+"\33[0m",end="")
            
        else:
            print("\033[41m"+problems[i][j]+"\033[0m", end="")
            
    else:
        # 입력이 부족한 부분은 오타로 처리
        print("\033[41m"+problems[i][j]+"\033[0m",end="")
print()


def jugment():
  for i in range(len(problems)):      #행 수만큼 반복
    print()
    enter=input(problems[i]+"\n")              # 한줄씩 입력받음 
    typo(enter,i)
    if i+1< len(problems):     
      pass                  
    else: