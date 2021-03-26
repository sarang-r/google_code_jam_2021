#cases=int(input())
file_name = "test1.txt"
file_handle = open(file_name)  
cases = int(next(file_handle))

for case in range(1,cases+1):
    size = int(next(file_handle))
    numbers = [int(i) for i in next(file_handle).split()]
        




















file_handle.close()