def logToMessage(log,uid):
    message = []
    for act,userid in log:
        if act == 'Enter':
            message.append(f"{uid[userid]}님이 들어왔습니다.")
        else:
            message.append(f"{uid[userid]}님이 나갔습니다.")
    return message
        
        
def solution(recode):
    log = []
    uid = {}
    for command in recode:
        message = command.split(" ")
        action = message[0]
        if action=='Enter' or action=="Change":
            uid[message[1]] = message[2]
            if action=='Enter':
                log.append(['Enter',message[1]])
        else:
            log.append(['Leave',message[1]])
    answer = logToMessage(log,uid)
    return answer