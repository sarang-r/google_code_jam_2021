class point():
    def __init__(self,x,y):
        self.x = x
        self.y = y



    

def hardcoded(final_coords):
    if final_coords.x%2 == final_coords.y%2: return "Not possible"

    to_be_used_list = [1,2,4,8,16,32] # Possibly change

    # Assign each randomly & calculate - if it agrees return
    for i in range(len(to_be_used_list)):
        sub_list = to_be_used_list[:i+1]





def write_in_binary(x):
    return



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

'''
Understand & reproduce the solution 
https://stackoverflow.com/questions/61310121/how-to-the-algorithms-for-expogo-work-google-code-jam-2020-round-1b
'''


