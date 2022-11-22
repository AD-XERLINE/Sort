
def BBSORT(lst,i,j,n):
    if i == n:
        return lst
    else:
        if j == n:
            i+=1
            j=0
        if lst[j] > lst[j+1]:
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1]=temp
        return BBSORT(lst,i,j+1,n)
    
inp = list(map(int,input("Enter Input : ").split(" ")))
n = len(inp)-1
print(BBSORT(inp,0,0,n))