import math
def solution(w,h):
    total = w*h

    # 함수의 선이 지나가는 값들 W
    y_val = [(-h/w)*i+h for i in range(w+1)]
    # 각 구간 함수가 지나는 y값의 크기
    y_delta = [y_val[i]-y_val[i+1] for i in range(len(y_val)-1)]

    lined_square =sum(list(map(math.ceil,y_delta)))
    #x값 기준 사각형의 개수  = h개

    answer = total -lined_square
    return answer


## 정확성 33.3 시간초과도 발생했다. w,h가 1억개이므로 1억번의 iter가 발생할 수 있다.