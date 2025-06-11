def parse_problems_from_file():
    
    all_problems = []
    current_problem = {}
    with open('python_easy.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if '---' in line:
                
                if current_problem:

                    all_problems.append(current_problem)
                
                current_problem = {}        # 현재 문제 비우기 
                continue
            
            if '#title' in line:
                current_problem['title'] = line.replace('#title','').replace(':','').strip()
                continue

            if '#desc' in line:
                current_problem['desc'] = line.replace('#desc','').replace(':','').strip()
                continue
            
            if 'content' not in current_problem:
                current_problem['content'] = []
            
            current_problem['content'].append(line.strip())

        if current_problem:
            all_problems.append(current_problem)
    
    return all_problems 



test= parse_problems_from_file()

print(test)