t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    wlist = []
    for _ in range(n):
        wlist.append(input())
    ans = float("inf")
    sub = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(m):
                sub += abs(ord(wlist[i][k]) - ord(wlist[j][k]))
            ans = min(ans, sub)
            sub = 0
            
    print(ans)
