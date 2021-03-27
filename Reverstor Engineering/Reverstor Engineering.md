---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.10.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]
```

```python
def factorial(size):
    factorial = 1
    for i in range (1,int(size)+1):
        factorial = factorial * i
    return factorial
```

```python
def count_inv(numbers,size):
    inv = 0
    for i in range(0,size):
        minimum = i + 1
        argmin = numbers.index(minimum)
        numbers[i:argmin+1] = numbers[i:argmin+1][::-1]
        if i <= argmin+1:
            inv+=argmin +1  - i
    return inv -1
```

```python
def main_func(size,cost):
    lst = [i for i in range(1,size+1)]
    generator = all_perms(lst)
    perm_nr = factorial(size)
    for i in range(perm_nr):
        lst = next(generator)
        temp_lst = lst.copy()
        inv_cost = count_inv(lst, size)
        if inv_cost == cost:
            return temp_lst
        
    return "IMPOSSIBLE"
```

```python
file_name = "test1.txt"
file_handle = open(file_name)  
cases = int(next(file_handle))

for case in range(1,cases+1):
    size, cost = map(int, (next(file_handle)).split())
#     print(size,cost)
    answer = main_func(size,cost)
    if answer=="IMPOSSIBLE":
        print(f"Case #{case}:",answer)
    else:
        print(f"Case #{case}:",*answer)
file_handle.close()
```
