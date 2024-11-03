"""bad keyboard"""
def bkb (word) :
    """fixed"""
    for i in word :
        if i == "I" :
            i = i.replace("I","O")
        elif i == "O" :
            i = i.replace("O","I")
        elif i == "i" :
            i = i.replace("i","o")
        else :
            i = i.replace("o","i")
        print(i, end = "")
bkb(input())
