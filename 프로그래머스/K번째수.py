def solution(array,command):
    answer = []
    for i in command:
        answer.append(sorted(array[i[0]-1:i[1]])[i[2]-1])
    return answer

a = [1, 5, 2, 6, 3, 7, 4]
command = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(a,command))