def BBSORT(lst):
    n =len(lst)-1 
    # print(n)
    for k in range(n):
        for i in range(n):
            if i != n :
                S = True
                j = i+1
                if lst[i] < 0:
                    S = False
                elif lst[j] < 0:
                    while(lst[j] < 0):
                        if j != n:
                            j+=1

                        else:
                            j = i
                            
                if lst[i] >= lst[j] and S == True:
                    temp = lst[j]
                    lst[j] = lst[i]
                    lst[i]=temp


    return lst

inp = list(map(int,input("Enter Input : ").split(" ")))
Ninp = map(str,BBSORT(inp))
# BBSORT(inp)
print(" ".join(Ninp))