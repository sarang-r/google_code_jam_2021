from itertools import combinations

# def split_generator(card_list):
#     pass
#     # Get all possible combination for the first - and rest goes to the second
#     # Iterate over length
#     # Then Iterate over 
#     for permutation in list(permutations(card_list)): # All the possible permutations
#         for j in range(len(card_list)-1):
#             yield (permutation[:j+1], permutation[j+1:])


def print_split_generatorv2(card_list):
    pass

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
    for split, rest in print_split_generatorv2(card_list):
        # print(split,rest)
        if check(split,rest): return check(split,rest)
    return 0
        
def competition():
    #cases=int(input())
    file_name = "test1.txt"
    file_handle = open(file_name)  
    cases = int(next(file_handle))
    for case in range(1,cases+1):
        card_list = []
        card_list_2d = []
        nr_of_different_primes= int(next(file_handle))
        for i in range(nr_of_different_primes):
            prime, nr_of_primes  = map(int,next(file_handle).split())
            for i in range(nr_of_primes) : card_list.append(prime)
            card_list_2d.append([prime, nr_of_primes])
        print(f"Case #{case}: {main(card_list)}")
        print_split_generator(card_list)
        print()
    file_handle.close()

if __name__=='__main__':
    competition()