from itertools import permutations

def split_generator(card_list):
    pass
    # Get all possible combination for the first - and rest goes to the second
    # Iterate over length
    # Then Iterate over 
    for permutation in list(permutations(card_list)): # All the possible permutations
        for j in range(len(card_list)-1):
            yield (permutation[:j+1], permutation[j+1:])
            

def multiply_arr(arr):
    result = 1 
    for nr in arr:
        result*= nr
    return result


def check(split,rest):
    if sum(split) == multiply_arr(rest):
        return sum(split)
    elif multiply_arr(split) == sum(rest):
        return sum(rest)
    else : return False


def main(card_list):
    for split, rest in split_generator(card_list):
        # print(split,rest)
        if check(split,rest): return check(split,rest)
    return 0
        
def competition():
    cases=int(input())
    for case in range(1,cases+1):
        card_list = []
        card_list_2d = []
        nr_of_different_primes = int(input())
        for i in range(nr_of_different_primes):
            prime, nr_of_primes  = map(int,input().split())
            for i in range(nr_of_primes) : card_list.append(prime)
        print(f"Case #{case}: {main(card_list)}")

competition()