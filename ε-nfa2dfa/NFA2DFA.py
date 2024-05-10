from collections import deque
from FA import FA, make_FA

# 두 state list 간에 겹치는 원소가 존재하는지 확인하는 함수
def check_intersection(state_list1, state_list2):

    set_s1 = set(state_list1)
    set_s2 = set(state_list2)
    
    # 겹치는 원소가 하나라도 있다면 True 반환
    return True if set_s1.intersection(set_s2) else False 

# nfa에서 dfa로 변환해주는 함수
def nfa2dfa(nfa: FA):

    # dfa 정보로 사용될 state, terminal, mapping_function, start_state, final_state 초기화
    dfa_state = []
    dfa_terminal = nfa.terminal
    dfa_mapping_function = {}
    dfa_start_state = str(nfa.ε_closure(nfa.start_state))
    # 시작 state와 final_state가 겹친다면 dfa_final_state에 추가하면서 초기화
    if check_intersection(nfa.final_state, nfa.ε_closure(nfa.start_state)):
        dfa_final_state = [str(nfa.ε_closure(nfa.start_state))]
    else:     
        dfa_final_state = []

    # nfa -> dfa로 변환할 때 매핑할 상태들을 저장할 mapping_list와 이미 매핑한 상태를 저장할 already_mapping 초기화 
    mapping_list = deque([nfa.ε_closure(nfa.start_state)])
    already_mapping = []

    # mapping_list에 원소가 있으면 매핑 진행
    while(mapping_list):
        mapping_states = mapping_list.popleft() # mapping_states: list
        str_mapping_states = str(mapping_states) # str_mapping_states: str

        # 매핑되지 않은 경우에만 매핑 진행
        if str_mapping_states not in already_mapping: 
            # 매핑을 진행하므로 already_mapping에 추가
            already_mapping.append(str_mapping_states) 

            # dfa_state와 dfa_mapping_function에 매핑하려는 state 추가
            dfa_state.append(str_mapping_states)
            dfa_mapping_function[str_mapping_states] = {}

            # 각 terminal에 대해 매핑
            for terminal in nfa.terminal:
                # state_mapping_rule: 매핑하려는 state들의 매핑규칙 저장 (중복 제거)
                state_mapping_rule = set()

                # 각 state가 terminal에 따라 매핑되는 상태를 state_mapping_rule에 저장
                for st in mapping_states:
                    if terminal in nfa.mapping_function[st]:
                        state_mapping_rule.update(nfa.mapping_function[st][terminal]) 

                # ε-closure 확인
                state_mapping_rule = nfa.ε_closure(state_mapping_rule) # set -> list
                
                # 매핑 규칙이 없다면 다음 terminal에 대해 매핑 수행
                if not state_mapping_rule: 
                    continue
                
                # 매핑 규칙으로 얻은 상태에 final_state가 존재한다면 dfa_final_state에 추가 
                if check_intersection(nfa.final_state, state_mapping_rule) and str(state_mapping_rule) not in dfa_final_state:
                    dfa_final_state.append(str(state_mapping_rule))

                # 매핑 함수에 매핑 규칙을 추가하고, mapping_list에 추가
                dfa_mapping_function[str_mapping_states][terminal] = [str(state_mapping_rule)] 
                mapping_list.append(state_mapping_rule) 

    # 구해진 정보로 FA 클래스 생성 후 반환
    dfa = FA(dfa_state, dfa_terminal, dfa_mapping_function, dfa_start_state, dfa_final_state)
    return dfa

# dfa를 최소화 해주는 함수
def minimization_fa(dfa: FA):

    # non_final_state가 존재하면, final state와 non final state로 나눈다. non_final_state가 존재하지 않으면 하나의 그룹에 모두 넣는다. 
    non_final_state = [st for st in dfa.state if st not in dfa.final_state]
    if non_final_state: 
        # group_dict: 각 group에 어떤 state가 있는지 저장하는 dictionary (여기서 group은 교재의 동치류(equivalence class)를 의미한다.)
        group_dict = {0:dfa.final_state, 1:non_final_state}
    else: 
        group_dict = {0:dfa.final_state}
    
    # state_dict: 각 state에 대한 정보를 저장하는 dictionary
    state_dict = {st: {'group': 0} if st in dfa.final_state else {'group': 1} for st in dfa.state} 
    
    # min_dfa 정보로 사용될 state, terminal, mapping_function, final_state 초기화 (start_state는 아직 초기화 불가)
    min_state = []
    min_terminal = dfa.terminal
    min_mapping_function = {}
    min_final_state = []

    # distinguish 플래그를 사용해 구별 가능한 상태가 되면 반복문 탈출
    distinguish = False
    while not distinguish:
        # state_dict에 각 state가 매핑되는 group 정보를 저장함
        for state in dfa.state:
            # 각 terminal에 대해 state가 매핑되는 그룹을 찾음
            mapping_group = []
            for terminal in dfa.terminal:
                # mapping_function에 해당 terminal로 매핑되는 state가 존재한다면 가져온 뒤 group 번호를 얻음
                if terminal in dfa.mapping_function[state]:
                    mapped_state = dfa.mapping_function[state][terminal][0] # dfa.mapping_function[state][terminal]: [ mapped_state ]
                    mapping_group.append(state_dict[mapped_state]["group"]) 
                else:
                    mapping_group.append(None)

            # state가 각 terminal에 대해 어떤 그룹으로 매핑되는지 tuple()로 변환해 저장
            state_dict[state]['mapping_group'] = tuple(mapping_group)

        # 기존 그룹을 분할하기 위한 partition_group_idx, partition_group_dict 초기화
        partition_group_idx = 0            
        partition_group_dict = {}
        
        # group 내에서 각 state의 mapping_group을 확인해 partition 
        for _, states in group_dict.items():
            # distinguish_mapping: mapping_group이 다른 state를 저장하기 위한 dictionary
            distinguish_mapping = {}
            for state in states:
                # 1. group의 state를 반복하며 mapping_group 값을 가져옴
                # 2. mapping_group을 기준으로 state를 distinguish_mapping에 저장  
                if state_dict[state]['mapping_group'] not in distinguish_mapping:
                    distinguish_mapping[state_dict[state]['mapping_group']] = [state]  
                else: 
                    distinguish_mapping[state_dict[state]['mapping_group']].append(state)

            # 그룹 내에서 나뉜 distinguish_mapping에 따라 partition_group을 생성
            for mapping_group in distinguish_mapping:
                # mapping_group이 같은 상태들을 하나의 그룹으로 만들어 partition_group_dict에 추가함 
                partition_group_dict[partition_group_idx] = distinguish_mapping[mapping_group]
                partition_group_idx += 1

        # 분할된 group 수와 기존의 group 수가 같다면 distinguish한 것이므로 반복문 탈출 
        if len(group_dict) == len(partition_group_dict):
            distinguish = True
        else:
            # 분할된 그룹 정보로 group_dict를 업데잍트
            group_dict = partition_group_dict
            
            # 새로운 group_dict를 기반으로 state_dict의 그룹 정보를 업데이트
            new_group_mapping = {} # 역매핑 딕셔너리 생성
            for group_idx, states in partition_group_dict.items():
                for state in states:
                    new_group_mapping[state] = group_idx
            for state in dfa.state: 
                # state_dict의 그룹 정보 업데이트
                state_dict[state]['group'] = new_group_mapping[state]

    # 모든 그룹이 distinguish 함으로 min_dfa를 생성하기 위한 정보를 구함
    for _, group in group_dict.items():
        # 각 그룹을 하나의 문자열로 변경하여 min_state에 저장
        str_group = '[' + ', '.join(group) + ']'
        min_state.append(str_group)

        # group 내에 기존 start_state가 존재한다면 해당 그룹이 min_start_state가 됨 
        if dfa.start_state in group:
            min_start_state = str_group

        # group 내에 기존 final_state가 존재한다면 min_final_state에 추가됨
        if check_intersection(dfa.final_state, group): 
            min_final_state.append(str_group)

        # min_mapping_function에 mapping_rule 추가
        min_mapping_function[str_group] = {}
        for idx, terminal in enumerate(dfa.terminal):            
            # 현재 그룹이 해당 terminal에서 매핑되는 그룹 번호를 가져와 mapping_group_num에 저장한다.
            mapping_group_num = state_dict[group[0]]['mapping_group'][idx]
            
            # mapping_group_num이 존재하면 min_mapping_function에 매핑 규칙 추가
            if mapping_group_num != None: 
                min_mapping_function[str_group][terminal] = ['[' + ', '.join(group_dict[mapping_group_num]) + ']']

    # 길이순, 오름차순으로 정렬
    min_state.sort(key=lambda x: (len(x), x))
    min_mapping_function = dict(sorted(min_mapping_function.items(), key=lambda item: (len(str(item[0])), str(item[0]))))

    # 구해진 정보로 FA 클래스 생성 후 반환
    min_dfa = FA(min_state, min_terminal, min_mapping_function, min_start_state, min_final_state)
    return min_dfa

if __name__ == "__main__":
    # 10개의 예제에 대한 검증
    example_num_list = ['3.18', '3.22', '3.23', '3.25', '3.26', 'Ex2(www.javatpoint.com)', 'P3.7', 'P3.8(1)', 'P3.8(2)', 'P3.8(3)']
    for example_num in example_num_list:

        # 예제 번호에 맞는 파일을 open하여 FA 정보를 읽어들임
        with open(f'examples/{example_num}.txt', 'r', encoding="utf-8") as f:
            info = f.readlines()

        # 읽어들인 파일로 nfa 생성
        nfa = make_FA(info)

        # nfa를 파일로 내보냄
        nfa.export_text(f'examples/{example_num}', '(ε-)NFA')
        
        # nfa를 dfa로 바꿈
        dfa = nfa2dfa(nfa)

        # dfa를 파일로 내보냄
        dfa.export_text(f'examples/{example_num}', 'DFA')

        # dfa를 최소화 함
        reduced_dfa = minimization_fa(dfa)

        # 최소화된 dfa를 파일로 내보냄
        reduced_dfa.export_text(f'examples/{example_num}', 'reduced DFA')