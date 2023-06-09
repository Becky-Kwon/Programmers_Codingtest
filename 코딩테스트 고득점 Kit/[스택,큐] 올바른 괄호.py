# 내가 작성한 코드
def solution(s):
    stack_list = []
    answer = True
    for a in s:
        if a == '(':
            stack_list.append('(')
        else :  #')'인 경우
            if len(stack_list) == 0:
                answer = False
                break
            if stack_list[-1] == '(':
                del stack_list[-1]
            else : 
                answer = False
                break
    if len(stack_list) != 0:
        answer = False

    return answer





# 베스트 코드
def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0
