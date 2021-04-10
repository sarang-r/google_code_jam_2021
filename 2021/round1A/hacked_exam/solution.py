def main():
    pass
        
def competition():
    #cases=int(input())
    file_name = "test1.txt"
    file_handle = open(file_name)  
    cases = int(next(file_handle))
    for case in range(1,cases+1):
        list_2d = []
        nr_rows, nr_columns= map(int,(next(file_handle).split()))
        for i in range(nr_rows):
            list_2d.append(list(map(int,next(file_handle).split())))
        # print(f"Case #{case}: {main(list_2d)}")
    file_handle.close()

if __name__=='__main__':
    competition()