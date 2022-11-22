def STD(inp):
    t = 0
    Temp = 0
    # Metadrome
    for i in range(len(inp)):
        if i != len(inp)-1:
            if inp[i] < inp[i+1]:
                t += 1
            else:
                break
        else:
            Temp = t
    if Temp != 0:
        return print("Metadrome")


    t = 0
    Temp = 0
    # Repdrome
    for i in range(len(inp)):
        if i != len(inp)-1:
            if inp[i] == inp[i+1]:
                t += 1
            else:
                break
        else:
            Temp = t
    if Temp != 0:
        return print("Repdrome")
        

    t = 0
    Temp = 0
    # Plaindrome
    for i in range(len(inp)):
        if i != len(inp)-1:
            if inp[i] <= inp[i+1]:
                t += 1
            else:
                break
        else:
            Temp = t
    if Temp != 0:
        return print("Plaindrome")
        

    t = 0
    Temp = 0
    # Katadrome
    for i in range(len(inp)):
        if i != len(inp)-1:
            if inp[i] > inp[i+1]:
                t += 1
            else:
                break
        else:
            Temp = t
    if Temp != 0:
        return print("Katadrome")
        


    t = 0
    Temp = 0
    # Nialpdrome
    for i in range(len(inp)):
        if i != len(inp)-1:
            if inp[i] >= inp[i+1]:
                t += 1
            else:
                break
        else:
            Temp = t
    if Temp != 0:
        return print("Nialpdrome")
    else:
        return print("Nondrome")
        

inp = input("Enter Input : ")
STD(inp)