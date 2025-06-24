class ProblemParser:
    @staticmethod
    def parse_problems_from_file(file_name: str) -> list:
        all_problems = []
        current_problem = {}
        with open(file_name, 'r', encoding='utf-8-sig') as f:
            for line in f:
                if '---' in line:
                    if current_problem:
                        all_problems.append(current_problem)
                    current_problem = {}
                    continue
                if '#title' in line:
                    current_problem['title'] = line.replace('#title','').replace(':','').strip()
                    continue
                if '#desc' in line:
                    current_problem['desc'] = line.replace('#desc','').replace(':','').strip()
                    continue
                if 'content' not in current_problem:
                    current_problem['content'] = []
                processed_line = line.rstrip().replace('\t', '    ')
                current_problem['content'].append(processed_line)
            if current_problem:
                all_problems.append(current_problem)
        return all_problems

if __name__ == "__main__":
    test = ProblemParser.parse_problems_from_file("python_easy.txt")
    print(test)