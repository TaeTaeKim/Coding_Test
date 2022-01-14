from collections import deque
import numpy as np
import math
def solution(jobs):
    jobs = deque(sorted(jobs,key=lambda x:(x[0],x[1])))
    process_time = []
    requested = deque()
    time =jobs[0][0]
    while True:
        if len(jobs)==0 and len(requested)==0:
            break
        if not requested:
            process_time.append(jobs[0][1])
            time += jobs.popleft()[1]
            while jobs:
                if jobs[0][0]<=time:
                    requested.append(jobs.popleft())
                else:
                    break
            requested = deque(sorted(requested,key=lambda x:x[1]))
        else:
            processing = requested.popleft()
            process_time.append(time-processing[0]+processing[1])
            time +=processing[1]
            while jobs:
                if jobs[0][0]<=time:
                    requested.append(jobs.popleft())
                else:
                    break
            requested = deque(sorted(requested,key=lambda x:x[1]))

    answer = math.floor(np.mean(process_time))
    return answer

jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
print(solution(jobs))