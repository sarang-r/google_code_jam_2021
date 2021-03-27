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
def count_inv(numbers,size):
    inv = 0
    
    # findsmallest number
    for i in range(0,size):
        minimum = i + 1
        argmin = numbers.index(minimum)
        numbers[i:argmin+1] = numbers[i:argmin+1][::-1]
        if i <= argmin+1:
            inv+=argmin +1  - i
    return inv - 1
```

```python
#cases=int(input())
file_name = "test1.txt"
file_handle = open(file_name)  
cases = int(next(file_handle))

for case in range(1,cases+1):
    size = int(next(file_handle))
    numbers = [int(i) for i in next(file_handle).split()]
    inv = count_inv(numbers,size)
    print(f"Case #{case}: {inv}")
file_handle.close()
```

```python

```

```python

```
