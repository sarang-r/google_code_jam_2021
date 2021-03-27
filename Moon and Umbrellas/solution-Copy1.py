def trim(string):
    # Cut all the '?' from beginning
    ind = 0
    while string[ind] =="?" and ind<len(string)-1:
        ind+=1
    string = string[ind:]
    # Handle very specific corner cases of entire string being ???
    if string =="?":
        return None
    
    # Cut all the '?' from the end
    ind = 1
    while string[-ind] =="?":
        ind+=1
    if ind==1:
        return string
    else :
        return string[:-ind+1]
    
    return string

def func(CJ_cost,JC_cost,string):
#     print(string)
#     print(trim(string))
    string = trim(string)
    if string ==None:
        return 0
    
    ind, cost = 0,0
    while ind < len(string)-1:
        left = string[ind]
        right = string[ind+1]
        if left!=right:
            if left == "C":
                cost+=CJ_cost
            elif left =="J":
                cost+=JC_cost
                
        ind+=1
    return cost


cases=int(input())
for case in range(1,cases+1):
    nr1, nr2, string = input().split()
    CJ_cost, JC_cost = int(nr1), int(nr2)
    answer = func(CJ_cost,JC_cost,string)
    print(f"Case #{case}: {answer}")