def header(*head, leng=[]):
    a = 0
    b = 0
    c = 0
    for i in head:
        if len(i) < leng[a]:
            print("+-"+"-"*leng[a]+"-", end="")
        else:
            print("+-"+"-"*len(i)+"-", end="")
        a+=1
    print("+")
    for i in head:
        i = str(i)
        if len(i) < leng[b]:
            print("| "+i+" "*(leng[b]-len(i))+" ", end="")
        else:
            print("| "+i+" ", end="")
        b+=1
    print("|")
    for i in head:
        if len(i) < leng[c]:
            print("+-"+"-"*leng[c]+"-", end="")
        else:
            print("+-"+"-"*len(i)+"-", end="")
        c+=1
    print("+")

def row(*row, leng=1):
    a = 0
    b = 0
    for i in row:
        i = str(i)
        if len(i) < leng[a]:
            print("| "+i+" "*(leng[a]-len(i))+" ", end="")
        else:
            print("| "+ i[:leng[a]] +" ", end="")
        a+=1
    print("|")
    for i in row:
        i = str(i)
        print("+-"+"-"*leng[b]+"-", end="")
        b+=1
    print("+")