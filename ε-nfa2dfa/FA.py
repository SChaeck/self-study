import re
import os

# Finite Automa 클래스
class FA:
    def __init__(self, state, terminal, mapping_function, start_state, final_state):
        self.state = state
        self.terminal = terminal
        self.mapping_function = mapping_function
        self.start_state = start_state
        self.final_state = final_state

    # 입력받은 state list의 state에 대해 'ε'로 유도되는 state를 찾은 뒤, 기존 리스트에 추가하여 반환하는 함수
    def ε_closure(self, state_list):

        # state 중복을 제거하기 위해 set() 사용
        ε_set = set(state_list)        
        
        # state에서 'ε'으로 유도되는 state를 찾아 ε_set에 추가
        for state in state_list:
            if 'ε' in self.mapping_function[state]:
                ε_set.update(self.mapping_function[state]['ε'])
        
        # ε_set에 추가된 state가 없는 경우
        if len(state_list) == len(ε_set): 
            # list로 변환하여 정렬을 진행한 뒤 반환
            ε_list = sorted(list(ε_set))    
            return ε_list

        # 추가된 state가 있는 경우 재귀적으로 ε_closure을 호출해 'ε'으로 유도되는 state를 다시 찾음
        return self.ε_closure(ε_set) 

    # FA의 현재 상태를 .txt 파일로 출력하는 함수 
    def export_text(self, dir_name, file_name):

        create_directory(dir_name) # 디렉토리 생성

        # 파라미터로 받은 주소에 .txt 파일을 생성한 뒤 FA의 현재 상태 작성
        with open(f'{dir_name}/{file_name}.txt', 'w', encoding="utf-8") as f:
            f.writelines(f"StateSet = {{{', '.join(self.state)}}}\n")
            f.writelines(f"TerminalSet = {{{', '.join(self.terminal)}}}\n")
            f.writelines('DeltaFunctions = {\n')
            for state in self.mapping_function:
                for ter in self.mapping_function[state]:
                    f.writelines(f"\t({state}, {ter}) = {{{', '.join(list(self.mapping_function[state][ter]))}}}\n")
            f.writelines('}\n')
            f.writelines(f"StartState = {''.join(self.start_state)}\n")
            f.writelines(f"FinalStateSet = {{{', '.join(self.final_state)}}}")
        
        print(f'{dir_name}/{file_name}.txt 파일을 생성했습니다.')

# 디렉토리를 생성하는 함수
def create_directory(directory):

    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

# FA 정보를 입력받아 FA를 생성하는 함수 
def make_FA(info):

    # 정규표현식을 사용하기 위한 준비
    brace_p = re.compile('\{([^}]+)\}')         # 중괄호 안의 내용 
    parenthesis_p = re.compile('\(([^}]+)\)')   # 소괄호 안의 내용
    end_p = re.compile('([^ ]+)$')              # 마지막 단어

    # data의 각 줄을 나눠서 리스트로 저장(이때 \t, \n 제거)
    info = [line.replace('\t', '').replace('\n', '') for line in info]

    # re를 사용해 state, terminal, start_state, final_state를 추출
    state = brace_p.findall(info[0])[0].split(', ')
    terminal = brace_p.findall(info[1])[0].split(', ')
    start_state = end_p.findall(info[-2]) 
    final_state = brace_p.findall(info[-1])[0].split(', ')

    # mapping_function을 dictionary로 만든 뒤 DeltaFunctions 부분만 추출해 저장
    mapping_function = {st: {} for st in state}
    for line in info[3:-3]: 
        cur_state, cur_terminal = parenthesis_p.findall(line)[0].split(', ')
        next_state = brace_p.findall(line)[0].split(', ')
        mapping_function[cur_state][cur_terminal] = next_state # next_state: list
        
    # 추출한 정보로 FA 클래스 생성 후 반환
    fa = FA(state, terminal, mapping_function, start_state, final_state)
    return fa