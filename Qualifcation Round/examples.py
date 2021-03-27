cases=int(input())
for case in range(1,cases+1):
    size=int(input())
    l=[]
    for i in range(size):
        l.append([int(i) for i in input().split()])
    t=sum(l[i][i] for i in range(size))
    r=sum(len(set(l[i]))!=size for i in range(size))
    c=sum(len(set(l[j][i] for j in range(size)))!=size for i in range(size))
    print('Case #'+str(case)+':',t,r,c)
#------------------------------------------------------------------
cases=int(input())
for case in range(1,cases+1):
    things=[int(i) for i in input()]+[0]
    s='('*things[0]
    for i in range(len(things)-1):
        s+=str(things[i])
        if things[i]>things[i+1]:
            s+=')'*(things[i]-things[i+1])
        else:
            s+='('*(things[i+1]-things[i])
    print('Case #'+str(case)+':',s)
#------------------------------------------------------------------
cases=int(input())
for case in range(1,cases+1):
    sch=int(input())
    slots=[[int(i) for i in input().split()]+[j] for j in range(sch)]
    slots.sort()
    cbusy=0
    jbusy=0
    s=['']*len(slots)
    for i in slots:
        if cbusy<=i[0]:
            cbusy=i[1]
            s[i[2]]='C'
        elif jbusy<=i[0]:
            jbusy=i[1]
            s[i[2]]='J'
        else:
            s=['IMPOSSIBLE']
            break
    print('Case #'+str(case)+':',''.join(s))
#------------------------------------------------------------------
import sys
DEBUG=False
def eprint(*args, **kwargs):
    if DEBUG:
        print(*args, file=sys.stderr, **kwargs)
    else:pass
cases,bits=input().split()
cases=int(cases)
bits=int(bits)
for i in range(cases):
    l=[-2]+[-1]*bits
    #-2 head
    #-1 not defined
    # 0 0 bit
    # 1 1 bit
    v=[-2]+[-1]*((bits+1)//2)
    #-2 head
    #-1 not defined
    # 0 equal
    # 1 inequal
    count=0
    count=0
    while count<148:
        if -1 not in l:break
        count+=2
        r=l.index(-1)
        print(r,flush=True)
        l[r]=int(input())
        print(bits+1-r,flush=True)
        l[-r]=int(input())
        v[r]=l[r]^l[-r]
        eprint('Current: ',*(l[1:]))
        if count%10==0:
            count+=2
            eprint('Notes: ',*(v[1:]))
            if 0 in v:
                r=v.index(0)
                print(r,flush=True)
                if l[r]!=int(input()):
                    l=[i^1 if i>-1 else i for i in l]
            else:
                print(1,flush=True)
                input()
            eprint('Neg-adjusted: ',*(l[1:]))
            if 1 in v:
                r=v.index(1)
                print(r,flush=True)
                if l[r]!=int(input()):
                    l=[l[-i] for i in range(bits+1)]
            else:
                print(1,flush=True)
                input()
            eprint('Ref-adjusted: ',*(l[1:]))
    print(*(l[1:]),sep='')
    eprint('Submitting: ',*(l[1:]),sep='')
    if input()=='N':
        break
#------------------------------------------------------------------
def main():
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    trace = sum([arr[i][i] for i in range(n)])
    rows = sum([1 if len(set([arr[i][j] for j in range(n)])) != n else 0 for i in range(n)])
    cols = sum([1 if len(set([arr[j][i] for j in range(n)])) != n else 0 for i in range(n)])
    return ' '.join([str(trace), str(rows), str(cols)])

t = int(input())

for i in range(t):
    print ("Case #{}: {}".format(i+1, main()))
#------------------------------------------------------------------
def main():
    s = input()
    res, last = '', 0
    for i in s:
        i = int(i)
        for j in range(i-last):
            res += '('
        for j in range(last-i):
            res += ')'
        res += str(i)
        last = i
    for i in range(last):
        res += ')'
    return res

t = int(input())

for i in range(t):
    print ("Case #{}: {}".format(i+1, main()))
#------------------------------------------------------------------
def main():
    n = int(input())
    things = [list(map(int, input().split())) for i in range(n)]
    things = [[things[i][0], things[i][1], i] for i in range(n)]
    things.sort(key=lambda x: x[0])
    a, b = -1, -1
    res = [None for i in range(n)]
    for i in range(n):
        if things[i][0] < a:
            if things[i][0] < b:
                return 'IMPOSSIBLE'
            else:
                b = max(b, things[i][1])
                res[things[i][2]] = 'J'
        else:
            a = max(a, things[i][1])
            res[things[i][2]] = 'C'
    return ''.join(res)

t = int(input())

for i in range(t):
    print ("Case #{}: {}".format(i+1, main()))
#------------------------------------------------------------------ 