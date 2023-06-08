# 내가 작성한 코드
def solution(arr):
    answer = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

# 베스트 코드
def no_continuous(s):
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))
