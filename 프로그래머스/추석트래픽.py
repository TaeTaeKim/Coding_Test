import datetime as dt

def solution(lines):
    # 날짜 자료형의 처리 참고
    # https://www.delftstack.com/howto/python/how-to-convert-string-to-datetime/
    # https://docs.python.org/ko/3/library/datetime.html
    timestamp = []
    for line in lines:
        log = line.split(" ")
        endday = log[0]
        endtime = log[1]
        dsec = log[2].split("s")[0]
        end_dt = dt.datetime.strptime(endday+" "+endtime,"%Y-%m-%d  %H:%M:%S.%f")
        delta_time = dt.timedelta(seconds=float(dsec)-0.001)
        
        st_dt = end_dt-delta_time
        
        timestamp.append((st_dt,end_dt))

    # 날짜를 돌면서 1초동안에 포함되는 모든 작업 탐색
    process_time = dt.timedelta(seconds=0.999)
    # 최대 처리량 후보 구간들
    candi_time = []
    for st,end in timestamp:
        candi_time.append([st,st+process_time])
        candi_time.append([end,end+process_time])
    maxcnt = 0
    for process_st, process_end in candi_time:
        cnt = 0
        for st,end in timestamp:
            if (process_st<=st and st<=process_end) or (process_st<=end and end<=process_end) or(st<=process_st and process_end<=end):
                cnt+=1
            if cnt>maxcnt:
                maxcnt = cnt

    return maxcnt



# 처음 시도에는 날짜를 datetime을 사용하지 않고 구현하려 했지만 부동소수점문제 등의 발생과 time의 사칙연산이 힘들어 datetime module을 이용하기로 함.
# 오랜만에 다뤄보는 datetime에 대해 docu를 보면서 strptime, strftime, format 코드, timedelta에 대한 개념을 다시 학습
# 마지막 처리 작업수 분기에서 포함관계 조건에 대한 예외학습