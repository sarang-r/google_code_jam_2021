def find_nearest_neighbour(direction, list_2d, x_coord, y_coord): # Update this
    row_len = len(list_2d[0])
    column_len = len(list_2d)
    person = 0
    if direction=="up":
        while person==0 and x_coord!=0:
            x_coord-=1
            person = list_2d[x_coord][y_coord]
    elif direction=="down":
        while person==0 and x_coord!=column_len-1:
            x_coord+=1
            person = list_2d[x_coord][y_coord]
    elif direction=="left":
        while person==0 and y_coord!=0:
            y_coord-=1
            person = list_2d[x_coord][y_coord]
    elif direction=="right":
        while person==0 and y_coord!=row_len-1:
            y_coord+=1
            person = list_2d[x_coord][y_coord]
    return (x_coord,y_coord)

def eliminate(list_2d):
    for x_coord,row in enumerate(list_2d):
        for y_coord, person in row:
            up = find_nearest_neighbour("up", list_2d, x_coord, y_coord)
            down = find_nearest_neighbour("down", list_2d, x_coord, y_coord)
            left = find_nearest_neighbour("left", list_2d, x_coord, y_coord)
            right = find_nearest_neighbour("right", list_2d, x_coord, y_coord)
            if (up+down+left+right)/4 > person:
                person = 0

# Works
def calculate_floor_value(list_2d):
    floor_swag = 0
    for row in list_2d:
        for person in row:
            floor_swag+=person
    return floor_swag


# Works
def check_if_finished(list_2d): # Work
    for row in list_2d:
        if sum([1 for i in row if i!=0])>1 : return False
    for y in range (len(list_2d[0])):
        column_sum = 0
        for x in range(len(list_2d)):
            if list_2d[x][y]!=0: column_sum+=1
        if column_sum > 1 : return False
    return True


def main(list_2d):
    fsum = 0
    while True:
        fsum+= calculate_floor_value(list_2d)
        if check_if_finished(list_2d):
            return fsum
        list_2d = eliminate(list_2d)
        
def competition():
    #cases=int(input())
    file_name = "finish_tests.txt"
    # file_name = "test1.txt"
    file_handle = open(file_name)  
    cases = int(next(file_handle))

    for case in range(1,cases+1):
        list_2d = []
        nr_rows, nr_columns= map(int,(next(file_handle).split()))
        for i in range(nr_rows):
            list_2d.append(list(map(int,next(file_handle).split())))

        print(list_2d)
        print(eliminate(list_2d))
        # print(f"Case #{case}: {main(list_2d)}")
    file_handle.close()

if __name__=='__main__':
    # competition()
    # list_2d = [[3, 4, 2], [6, 7, 3], [11, 1, 0], [9, 8, 7]]
    x,y = 2,0
    direction = "right"
    list_2d = [[0, 1, 2], [0, 0, 0], [0, 4, 0], [3, 0, 7]]
    print("list2d:")
    for row in list_2d:
        print(row)
    print(f"our coords : {x} {y}")
    print(f"our direction: {direction}")
    print()
    print(f"nearest neighbour:{find_nearest_neighbour(direction,list_2d,x,y)}")