# 내가 작성한 코

def solution(bridge_length, weight, truck_weights):
    truck_nums = len(truck_weights)
    finish_truck = 0
    bridge = [0]*bridge_length
    sum_bridge  = 0
    time_ = 0
    while finish_truck != truck_nums:
        #print(truck_weights, bridge)
        time_ += 1
        if sum_bridge > 0:  #다리에 트럭이 있음
            # 한 단계씩 옮기기
            out = bridge.pop(0)
            bridge.append(0)
            if out > 0:
                sum_bridge -= out
                finish_truck += 1
            # 맨 뒤칸에 트럭 추가가 가능하다면
            if len(truck_weights) > 0: 
                if sum_bridge + truck_weights[0] <= weight:
                    bridge[-1] = truck_weights.pop(0)
                    sum_bridge += bridge[-1]
        elif sum_bridge == 0:  #다리위에 아무것도 없을 때
            bridge[-1] = truck_weights.pop(0)
            sum_bridge += bridge[-1]
    return time_
