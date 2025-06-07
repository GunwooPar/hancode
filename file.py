def get_file():
    global problems 
    problems = []
    with open('python_easy.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if '#title' in line:
                print(line)
                continue
            if '#desc' in line:
                print(line)
                continue
            if '---' in line:
                continue    
            problems.append(line.strip())
     
    return problems  
       
problems = get_file()
print(problems)

