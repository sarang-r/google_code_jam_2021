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
def trim(string):
    # Cut all the '?' from beginning
    ind = 0
    while string[ind] =="?" and ind<len(string)-1:
        ind+=1
    string = string[ind:]
    # Handle very specific corner cases of entire string being '??????'
    if string =="?":
        return None
    
    # Cut all the '?' from the end
    ind = 1
    while string[-ind] =="?":
        ind+=1
    if ind==1:
        return string
    else :
        return string[:-ind+1]
    return string
```

```python
def func(CJ_cost,JC_cost,string):
#     print(string)
#     print(trim(string))
    string = trim(string)
    if string ==None:
        return 0
    
    ind, cost = 0,0
    while ind < len(string)-1:
        left = string[ind]
        right = string[ind+1]
        if right !="?":
            if left!=right:
                if left == "C":
                    cost+=CJ_cost
                elif left =="J":
                    cost+=JC_cost
        else:
            while right=="?":
                ind+=1
                right = string[ind+1]
            if left !=right:
                if left == "C":
                    cost+=CJ_cost
                elif left =="J":
                    cost+=JC_cost
        ind+=1
    return cost
```

```python
#cases=int(input())
file_name = "test1.txt"
file_handle = open(file_name)  
cases = int(next(file_handle))

for case in range(1,cases+1):
    nr1, nr2, string = next(file_handle).split()
    CJ_cost, JC_cost = int(nr1), int(nr2)
    answer = func(CJ_cost,JC_cost,string)
    print(f"Case #{case}: {answer}")
file_handle.close()
```
