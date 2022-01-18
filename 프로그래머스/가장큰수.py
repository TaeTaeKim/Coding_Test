# 내 풀이 1000자리 이하이므로 모든 숫자를 12자리로 맞춰서 크기를 비교한다.
def samesize(a):
    a = str(a)
    k = a*(12//len(a))
    return (a,k)
def solution(numbers):
    answer = ''
    tostr = []
    if sum(numbers) ==0:
        return '0'
    for i in numbers:
        tostr.append(samesize(i))
    tostr = sorted(tostr,key=lambda x:x[1],reverse=True)
    for num in tostr:
        answer+=num[0]
    return answer

# 다른사람의 짧은 코드풀이
# 비슷하게 자릿수를 3번 반복해서 문자열 비교연산을 이용하는 방법이지만
# 굳이 12자리까지 늘리지 않아도 *3만해도 문자열은 한자리씩 비교하기 때문에 가능했다.
def solution2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

a = [3, 30, 34, 5, 9]
print(solution(a))
b = [6, 10, 2]
print(solution(b))