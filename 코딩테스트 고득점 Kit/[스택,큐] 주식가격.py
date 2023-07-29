# 참고해서 작성한 것

def solution(prices):
    answer = [0]*len(prices)
    for i, target in enumerate(prices):
        #print(i, target)
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if target > prices[j] :
                break

    return answer
