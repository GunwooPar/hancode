problems = [ 'def hello():',
    'print("hello world")']
with open('python_easy.txt', 'r', encoding='utf-8') as f:
    block = []
    meta = {}
    for line in f:
        if line.strip() == '---':
            if block:
                problems.append({'meta': meta, 'code': block})
                block = []
                meta = {}
        elif line.startswith('#title:'):
            meta['title'] = line[len('#title:'):].strip()
        elif line.startswith('#desc:'):
            meta['desc'] = line[len('#desc:'):].strip()
        else:
            block.append(line.rstrip('\n'))
    # 마지막 문제 추가
    if block:
        problems.append({'meta': meta, 'code': block})

# 예시 출력
for p in problems:
    print(p['meta'].get('title', ''), p['code'])





# 실질적 개발 순서(프로그램/로컬 버전 기준)
# 예시코드 데이터 파일화 (json/csv/txt)

# UI 프레임워크 선정 및 기본 화면

# 코드 출제/입력/실시간 채점 모듈 구현

# 속도/정확도/오타 분석

# 로컬 기록 저장(파일, sqlite 등)

# (선택) 랭킹/통계 집계, 커스텀 문제 등
