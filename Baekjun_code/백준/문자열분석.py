import string

while True:
    try:
        s = input()
        res_dict = {'lower':0, 'upper':0, 'num':0,'space':0}
        for value in s:
            if value in string.ascii_lowercase:
                res_dict['lower'] +=1
            elif value in string.ascii_uppercase:
                res_dict['upper'] +=1
            elif value ==" ":
                res_dict['space'] +=1
            else:
                res_dict['num'] +=1


        for i in res_dict.values():
            print(i,end = " ")
    except EOFError:
        break