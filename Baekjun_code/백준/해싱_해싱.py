import string
length = int(input())
input_string = input()
alphabet = {}

for i,letter in enumerate(string.ascii_lowercase):
    alphabet[letter] = i+1
def solution(length,input_string):
    answer = 0
    for i in range(length):
        answer = answer + alphabet[input_string[i]] *(31**i)
    return answer%1234567891

print(solution(length,input_string))
