import string

lowercase_dict = {s:101 for s in list(string.ascii_lowercase)}

value = input()

for i in range(len(value)):
    alphabet = value[i]
    if lowercase_dict[alphabet]>=i:
        lowercase_dict[alphabet] = i

for a in lowercase_dict.value():
    if a ==101:
        print(-1,end = " ")
    else:
        print(a, end = " ")