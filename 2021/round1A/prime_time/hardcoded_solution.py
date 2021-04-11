from itertools import permutations

def split_generator(card_list):
    pass
    # Get all possible combination for the first - and rest goes to the second
    # Iterate over length
    # Then Iterate over 
    for permutation in list(permutations(card_list)): # All the possible permutations
        for j in range(len(card_list)-1):
            yield (permutation[:j+1], permutation[j+1:])
            






def main(card_list):
    generator = split_generator()
    
    pass
        
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
    file_handle.close()

if __name__=='__main__':
    # competition()
    split_generator([1,2,3,4])