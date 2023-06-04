# https://jyj98020.tistory.com/47 참고함.

# Hash를 활용한 풀이
def solution(participant, completion):
    hashDict={}
    sumHash=0
    
    for name in participant:
        hashDict[hash(name)] = name
        sumHash += hash(name)
    for name in completion:
        sumHash -= hash(name)
    answer = hashDict[sumHash]
    

# Counter 클래스를 활용한 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
