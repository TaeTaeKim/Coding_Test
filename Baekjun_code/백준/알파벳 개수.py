import string

lowercase_dict = {s:0 for s in list(string.ascii_lowercase)}

value = input()

for s in value:
    lowercase_dict[s] +=1

for i in list(lowercase_dict.values()):
    print(i,end=" ")