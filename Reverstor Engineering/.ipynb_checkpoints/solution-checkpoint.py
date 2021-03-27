def count_inv(numbers,size):
    inv = 0
    for i in range(0,size):
        minimum = i + 1
        argmin = numbers.index(minimum)
        numbers[i:argmin+1] = numbers[i:argmin+1][::-1]
        if i <= argmin+1:
            inv+=argmin +1  - i
    return inv - 1

cases=int(input())
for case in range(1,cases+1):
    size = int(input())
    numbers = [int(i) for i in input().split()]
    inv = count_inv(numbers,size)
    print(f"Case #{case}: {inv}")
