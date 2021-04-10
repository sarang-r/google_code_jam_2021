def special_case(prev_nr,next_nr):
    prev_len = len(str(prev_nr))
    next_len = len(str(next_nr))
    # Deal with 1099, 10 and 1089,10 or 1098,10
    rest = str(prev_nr)[next_len:]
    for index,nr in enumerate(rest):
        if nr!="9":
            next_nr*= 10**(prev_len - next_len)
            next_nr+= 10**(index) * (int(nr)+1) # Double check
            return next_nr, (prev_len - next_len)

    else : 
        next_nr*= 10**(prev_len - next_len+1)
        return next_nr, (prev_len - next_len+1)



def compare(prev_nr,next_nr):
    prev_len = len(str(prev_nr))
    next_len = len(str(next_nr))
    index = 0
    for a,b in zip(str(next_nr), str(prev_nr)):
        if(a>b):
            next_nr*= 10**(prev_len - next_len)
            return next_nr, prev_len - next_len
        elif(a==b):
            if index+1 == next_len:
                return special_case(prev_nr,next_nr)
            else: pass
        elif (a<b):
            next_nr*= 10**(prev_len - next_len + 1)
            return next_nr, prev_len - next_len + 1
        index+=1
    

def append(prev_nr,next_nr):
    if prev_nr<next_nr:
        return next_nr, 0
    elif prev_nr == next_nr:
        return next_nr*10, 1
    else :
        return compare(prev_nr,next_nr)


def main(array):
    appends = 0
    for index in range(len(array)-1):
        prev_nr = array[index]
        next_nr = array[index+1]
        if prev_nr>=next_nr:
            array[index+1] , nr_of_appends = append(prev_nr,next_nr)
            appends+=nr_of_appends

    return appends
        
def competition():
    cases=int(input()) 
    for case in range(1,cases+1):
        array_len =  int(input())
        array = list(map(int,input().split()))
        print(f"Case #{case}: {main(array)}")
competition()