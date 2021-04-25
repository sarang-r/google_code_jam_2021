CONSTANT = 1/(1/12*10**10)


def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
                
def check_if_possible(lst):
    seconds, minutes, hours = lst

    seconds = seconds * CONSTANT /360 /60 
    minutes - minutes * CONSTANT /360 /60
    hours = hours * CONSTANT /360 / 12

    print(seconds, minutes, hours)













def main(nr1, nr2, nr3):
    for combinations in all_perms([nr1, nr2, nr3]):
        check_if_possible(combinations)

#cases=int(input())
def competition():
    file_name = "test1.txt"
    file_handle = open(file_name)
    cases = int(next(file_handle))

    for case in range(1,cases+1):
        nr1, nr2, nr3 = map(int,next(file_handle).split())
        answer = main(nr1, nr2, nr3)
        # print(nr1, nr2, nr3)
        print(f"Case #{case}: {answer}")
        break
    file_handle.close()



if __name__=="__main__":
    competition()
