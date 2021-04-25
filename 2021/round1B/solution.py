def main():
    pass

#cases=int(input())
def competition():
    file_name = "test1.txt"
    file_handle = open(file_name)
    cases = int(next(file_handle))

    for case in range(1,cases+1):
        nr1, nr2 = map(int,next(file_handle).split())
        answer = main()
        print(f"Case #{case}: {answer}")
    file_handle.close()



if __name__=="__main__":
    competition()
