def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]
            
def factorial(size):
    factorial = 1
    for i in range (1,int(size)+1):
        factorial = factorial * i
    return factorial

def count_inv(numbers,size):
    inv = 0
    for i in range(0,size):
        minimum = i + 1
        argmin = numbers.index(minimum)
        numbers[i:argmin+1] = numbers[i:argmin+1][::-1]
        if i <= argmin+1:
            inv+=argmin +1  - i
    return inv -1

def main_func(size,cost):
    lst = [i for i in range(1,size+1)]
    generator = all_perms(lst)
    perm_nr = factorial(size)
    for i in range(perm_nr):
        lst = next(generator)
        temp_lst = lst.copy()
        inv_cost = count_inv(lst, size)
        if inv_cost == cost:
            return temp_lst
    return "IMPOSSIBLE"

cases=int(input())
for case in range(1,cases+1):
    size, cost = map(int, (input()).split())
    answer = main_func(size,cost)
    if answer=="IMPOSSIBLE":
        print(f"Case #{case}:",answer)
    else:
        print(f"Case #{case}:",*answer)