t = int(input()) 
for i in range(t):
    n = int(input())
    stud = list(map(int, input().split()))
    stud.reverse()
    c = 0
    pre = stud[0]
    for i in range(1,len(stud)):
        if pre > stud[i]:
            c += 1
        else:
            pre = stud[i]
    print(c)
