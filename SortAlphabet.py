def sortlist(lst,fst,snd):
    t = lst[fst]
    lst[fst] = lst[snd]
    lst[snd] = t

    

inp = input("Enter Input : ").split(" ")

temp = []
for i in range(len(inp)):

    for j in range(len(inp[i])):

        if inp[i][j].isalpha():

            temp += inp[i][j]
            # print(temp)

for j in range(len(inp)):

    for i in range(len(inp)):

        if i != len(inp)-1:

            if temp[i] > temp[i+1]:

                sortlist(temp,i,i+1)
                sortlist(inp,i,i+1)

# print(inp)
print(" ".join(inp))