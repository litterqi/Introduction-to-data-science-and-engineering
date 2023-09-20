state = [0]*16
answers = []
route = []
def DFS(men, sheep, wolf, vegetable):
    if (men == 1 and sheep == 1 and wolf == 1 and vegetable == 1):
        answers.append(route[:])
        return
    if ((vegetable == sheep or wolf == sheep) and sheep != men):
        return
    state_idx = (men<<3) + (sheep<<2) + (wolf<<1) + vegetable
    if (state[state_idx] == 1):
        return
    else:
        state[state_idx] = 1
    if (men == sheep):
        if(men==0):
            route.append("农夫带羊过河")
        else:
            route.append("农夫带羊返回")    
        DFS(not men, not sheep, wolf, vegetable)
        route.pop()
    if (men == wolf):
        if(men==0):
            route.append("农夫带狼过河")
        else:
            route.append("农夫带狼返回")   
        DFS(not men, sheep, not wolf, vegetable)
        route.pop()
    if (men == vegetable):
        if(men==0):
            route.append("农夫带菜过河")
        else:
            route.append("农夫带菜返回") 
        DFS(not men, sheep, wolf, not vegetable)
        route.pop()
    if(men==0):
        route.append("农夫过河")
    else:
        route.append("农夫返回") 
    DFS(not men, sheep, wolf, vegetable)
    route.pop()
    state[state_idx] = 0
DFS(0, 0, 0, 0)
i=1
for answer in answers:
    print("方法",i)
    print(answer)
    i+=1