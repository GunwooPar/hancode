problems = []
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

