from collections import deque
def cal_weight(que):
    weight = 0
    for i in que:
        weight +=i[0]
    return weight

def add_time(que):
    for i in que:
        i[1] +=1
    return

def solution(bridge_length, weight, truck_weights):
    trucks= deque([[i,0] for i in truck_weights])
    
    bridge = deque()
    passed = 0
    time =0
    while not(passed ==len(truck_weights)):
        time +=1
        if bridge:
            i=0
            while bridge:
                if bridge[0][1] ==bridge_length+1:
                    bridge.popleft()
                    passed +=1
                    i+=1
                else:
                    break
        if not bridge and trucks:
            bridge.append(trucks.popleft())
            bridge[-1][1] +=1            
        elif trucks and cal_weight(bridge)+trucks[0][0]<=weight:
            bridge.append(trucks.popleft())
            bridge[-1][1] +=1
        if bridge:
            add_time(bridge)
        
        
        
        
    return time