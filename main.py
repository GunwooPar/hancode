import time 
def jugment(i):
  enter=str(input(list[i])) 
  if list[i]== enter & i+1 <= len(list):
    
  else:
    typo(enter)#여기는 다시 출력되게 하던지 틀린곳을 지적하고 넘어가게 할것인지

def typo(enter):
  for i in range(0,len(enter)):
      for j in range(0,len(list[i])):
        if list[i][j]== enter[j]:
          print("\033[32",enter(j), end ="")
        else:
          print("\033[41m",list[i][j], end="")
  print("")


list=[]  #여기는 명령어(출력할 것, 입력받아야할 단어들을 넣는 공간)

print("\033[32",enter(j), end ="")
print("시작하시려면 터치하세요")                             #->터틀모듈을 이용해서 마우스를 따라다니는 것을 만들고 마우스를 클릭하면 시작되게 만들면 될듯
for i in range (0, len(list)):                                                #터틀에 글을 작성할 수 있으면 위부터 아래로 (한컴타자처럼 만들면 될거 같음)
   jugment(i)

                                                      #여기까지 기본적인 틀
                           


