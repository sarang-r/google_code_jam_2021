def find_nearest_neighbour(direction, list_2d, x_coord, y_coord): # Update this
    person = 0
    x_index = x_coord
    y_index = y_coord
    if direction=="up":
        pass
    elif direction=="down":
        pass
    elif direction=="left":
        pass
    elif direction=="right":
        pass

def eliminate(list_2d):
    for x_coord,row in enumerate(list_2d):
        for y_coord, person in row:
            up = find_nearest_neighbour("up", list_2d, x_coord, y_coord)
            down = find_nearest_neighbour("down", list_2d, x_coord, y_coord)
            left = find_nearest_neighbour("left", list_2d, x_coord, y_coord)
            right = find_nearest_neighbour("right", list_2d, x_coord, y_coord)
            if (up+down+left+right)/4 > person:
                person = 0


def calculate_floor_value(list_2d):
    floor_swag = 0
    for row in list_2d:
        for person in row:
            floor_swag+=person

def check_if_finished(list_2d):
    for row in list_2d:
        if sum(i for i in row if i!=0)!=1 : return False
    for column_coord in range(len(list_2d)):
        if sum(i for i in row if i!=0)!=1 : return False
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
    file_name = "test1.txt"
    file_handle = open(file_name)  
    cases = int(next(file_handle))

    for case in range(1,cases+1):
        nr = int(next(file_handle))
        print(f"Case #{case}: {main(list_2d)}")
    file_handle.close()

if __name__=='__main__':
    competition()