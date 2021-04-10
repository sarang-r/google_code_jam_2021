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

    # print(f"final array looks like this: {array}")
    return appends
        
def competition():
    #cases=int(input())
    file_name = "test1.txt"
    file_handle = open(file_name)  
    cases = int(next(file_handle))
    for case in range(1,cases+1):
        array_len =  int(next(file_handle))
        array = list(map(int,next(file_handle).split()))
        print(f"Case #{case}: {main(array)}")
    file_handle.close()

if __name__=='__main__':
    competition()
    # print(f"{append(109,10)} should be (1000,2)")
    # print(f"{append(153,153)} should be (1530,1)")
    # print(f"{append(15,16)} should be (16,0)")
    # print(f"{append(101,10)} should be (102,1)")


    # print(f"{compare(101,10)} should be (102,1)")
    # print(f"{compare(7,5)} should be (50,1)")
    # print(f"{compare(109,10)} should be (1000,2)")
    # print(f"{compare(193,19)} should be (194,1)")