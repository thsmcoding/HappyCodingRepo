def checking(str):
    if len(str) > 1:
        return str[0] is str[1]
    return False


def reducingliste(l):
    nb_length= len(l)
    if nb_length == 0:
        return True
    for i in range(nb_length-1):
        if l[i] == l[i + 1]:
            return True
    return False


def cutting(mylist, str):
    if len(str) == 0:
        return
    if len(str) == 1:
        mylist.append(str)
        return
    checkingstring = checking(str)
    if checkingstring == False:
        mylist.append(str[0])
        reduce = str[1:]
    else:
        reduce = str[1:]
        reduce = reduce[1:]
    cutting(mylist, reduce)


def superreducingstring(str):
    l = []
    cutting(l, str)
    lastcondition = reducingliste(l)
    if lastcondition == False:
        print(''.join(l), end='')
    else:
        print("Empty String", end='')



str_1 = "aa"
expected = "abd"
superreducingstring(str_1)