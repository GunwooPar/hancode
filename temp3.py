import time

# 색상 코드 정의
RED = "\033[31m"
RESET = "\033[0m"

# 예시 코드 (각 줄)
example_code = [
    'def hello():',
    '    print("hello world")'
]

print("아래 코드를 한 줄씩 입력하세요.")
for line in example_code:
    print(line)
input("준비되면 엔터...")

user_input = []
start = time.time()

for i, ref_line in enumerate(example_code):
    typed = input(f"{i+1}번째 줄: ")
    user_input.append(typed)
    # 채점 및 색상 표시
    result = ""
    for t_char, r_char in zip(typed, ref_line):
        if t_char == r_char:
            result += t_char
        else:
            result += f"{RED}{t_char}{RESET}"
    # 남은 문자 처리 (입력이 짧거나 길 경우)
    if len(typed) > len(ref_line):
        result += f"{RED}{typed[len(ref_line):]}{RESET}"
    elif len(typed) < len(ref_line):
        result += f"{RED}{ref_line[len(typed):]}{RESET}"
    print("채점결과:", result)

end = time.time()

total_chars = sum(len(line) for line in user_input)
elapsed = end - start
cpm = (total_chars / elapsed) * 60

print("\n=== 최종 결과 ===")
print(f"입력한 문자 수: {total_chars}")
print(f"경과 시간: {elapsed:.2f}초")
print(f"분당 타자수(CPM): {cpm:.2f}")
