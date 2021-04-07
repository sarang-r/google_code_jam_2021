def main(final_coords):
    if final_coords.x%2 == final_coords.y%2: return "Not possible"
    pass




#cases=int(input())
def competition():
    file_name = "test1.txt"
    file_handle = open(file_name)  
    cases = int(next(file_handle))

    for case in range(1,cases+1):
        x,y = map(int,next(file_handle).split())
        final_coords = point(x,y)
        # answer = main(final_coords)
        answer = hardcoded(final_coords)
        print(f"Case #{case}: {answer}")
    file_handle.close()




if __name__=="__main__":
    competition()