n = int(input())
for i in range(n):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = []
    for i in range(n):
        ans.append((a[i],b[i]))
    ans.sort()
    for i in range(len(ans)):
        if ans[i][0] <= k:
            k += ans[i][1]
            
    print(k)