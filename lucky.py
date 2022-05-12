t = int(input())
for i in range(t):
    s = input()
    sn = [int(i) for i in s]
    if sum(sn[:3]) == sum(sn[3:]):
        print("YES")
    else:
        print("NO")
