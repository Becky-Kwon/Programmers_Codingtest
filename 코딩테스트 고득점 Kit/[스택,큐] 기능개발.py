# 내가 작성한 코드
def solution(progresses, speeds):
    day = 0
    answer = []
    check = [False] *len(progresses)
    while len(check) > 0:
        day += 1
        print(day)
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            if progresses[i] >= 100:
                check[i] = True
        print('progresses : ',progresses)
        if check[0] == True:
            cnt = 1
            if len(check) > 1:
                while len(check) > 1 and check[0] and check[1]:
                    cnt +=1
                    del check[0]
                    del progresses[0]
                    del speeds[0]
                answer.append(cnt)
                del check[0]
                del progresses[0]
                del speeds[0] 
            else: 
                check = []
                answer.append(1)
            
    return answer
  
  
# 베스트 코드
def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

