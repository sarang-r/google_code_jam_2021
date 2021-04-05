def find_biggest_2_multiply(nr):
    i = 1
    while 2**i <=nr:  # Edge case might not work
        i+=1
    return i-1

def find_actual_row(nr):
    row_nr = find_biggest_2_multiply(nr)
    if find_biggest_2_multiply(nr) == find_biggest_2_multiply(nr-row_nr): return row_nr
    else : return row_nr-1

def how_many_1s_to_fill(nr):
    row_nr = find_actual_row(nr)
    return nr - row_nr - output_sum_of_row(row_nr)







def print_road(nr):
    if nr ==1:
        print("1 1")
        return


    waste_moves = how_many_1s_to_fill(nr)
    row_nr = find_actual_row(nr)

    # Waste around
    print("Wasting around:")
    for _ in range(int(waste_moves/2)):
        print("1 1")
        print("1 2")
    print()

    # Travel to approp row
    print("Travel to approp row:")
    for i in range(row_nr):
        print(f"1 {i+1}")
    print()

    # Travel through that row
    print("Traverse through approp row:")
    for i in range(row_nr):
        print(f"{i+1} {row_nr}")
    print()


    # Waste one final move if needed
    print("Waste one final move if needed:")
    if waste_moves%2 == 1:
        print(f"{row_nr} {row_nr+1}") # Fill this in 
    


def competition():
    #cases=int(input())
    file_name = "test1.txt"
    file_handle = open(file_name)  
    cases = int(next(file_handle))

    for case in range(1,cases+1):
        nr = int(next(file_handle))
        print(f"Case #{case}:")
        print_road(nr)
    file_handle.close()


def output_sum_of_row(n):
    return 2**(n-1)


if __name__=='__main__':
    competition()