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
def func():
    return 
```

```python
#cases=int(input())
file_name = "test1.txt"
file_handle = open(file_name)  
cases = int(next(file_handle))

for case in range(1,cases+1):
    nr1, nr2, letters = next(file_handle).split()
    nr1,nr2 = int(nr1), int(nr2)
    answer = func()
    print(f"Case #{case}: {answer}")
file_handle.close()
```

```python

```

```python

```
