def sortlist(lst,fst,snd):
    t = lst[fst]
    lst[fst] = lst[snd]
    lst[snd] = t

def TotalPoints(lst):
    # win 3,loss 0,draw 1
    # lst[1] lst[2] lat[3]
    totalScore = (3*int(lst[1])) + (0*int(lst[2])) + (1*int(lst[3]))
    return totalScore

def GoalDifference(lst):
    totaldif = int(lst[4]) - int(lst[5])
    return totaldif

# team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88, "conceded": 20 }

inp = input("Enter Input : ").split("/")
for i in range(len(inp)):
    inp[i] = inp[i].split(",")

temp = []
# print(inp)
print("== results ==")
for j in range(len(inp)):
    for i in range(len(inp)):

        if i != len(inp)-1:

            if TotalPoints(inp[i]) < TotalPoints(inp[i+1]):
                sortlist(inp,i,i+1)
                
            elif TotalPoints(inp[i]) == TotalPoints(inp[i+1]):
                
                if GoalDifference(inp[i]) < GoalDifference(inp[i+1]):
                    sortlist(inp,i,i+1)

# print(inp)
for i in range(len(inp)):
    print("['"+inp[i][0]+"', "+ "{'points': " + str(TotalPoints(inp[i])) + "}, " +"{'gd': "+ str(GoalDifference(inp[i])) + "}]")