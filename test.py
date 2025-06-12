# 학생 정보를 담은 딕셔너리
student = {
    'name': '홍길동',
    'grade': 2,
    'subjects': ['수학', '영어',] 
}

# 'grade'라는 '키'가 있는지 확인 -> True
if 'grade' in student:
    print("student 딕셔너리에는 'grade'라는 키가 있습니다.")

# '홍길동'이라는 '값'이 있는지 확인 -> False
# in 연산자는 기본적으로 값(value)을 검색하지 않습니다.
if '홍길동' in student:
    print("student 딕셔너리에는 '홍길동'이라는 키가 있습니다.") # 이 코드는 실행되지 않음

# '영어'라는 문자열이 있는지 확인 -> False
# 'subjects'라는 키의 값(리스트) 안에 있지만, 딕셔너리 자체를 검색하지는 않습니다.
if '영어' in student:
    print("student 딕셔너리에는 '영어'라는 키가 있습니다.") # 이 코드는 실행되지 않음