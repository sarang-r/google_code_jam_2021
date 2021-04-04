def func(nr):
    print(nr)
    pass

#cases=int(input())
file_name = "test1.txt"
file_handle = open(file_name)  
cases = int(next(file_handle))

for case in range(1,cases+1):
    nr = int(next(file_handle))
    answer = func(nr)
    print(f"Case #{case}: {answer}")
file_handle.close()