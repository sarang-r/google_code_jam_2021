def count_inv(numbers,size):
    inv = 0
    for i in range(0,size):
        minimum = i + 1
        argmin = numbers.index(minimum)
        numbers[i:argmin+1] = numbers[i:argmin+1][::-1]
        if i <= argmin+1:
            inv+=argmin +1  - i
    return inv - 1

def main_func(size,cost):
    return 0

cases=int(input())
for case in range(1,cases+1):
    size, cost = map(int, (input()).split())
    answer = main_func(size,cost)
    print(f"Case #{case}: {answer}")