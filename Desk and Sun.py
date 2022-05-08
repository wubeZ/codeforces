n , m = map(int,(input().split()))
grid = {} 
for i in range(n):
    a,b = (map(int, input().split()))
    if (a,b) in grid:
        grid[(a,b)] += 1
    else:
        grid[(a,b)] = 1
        
for i in range(m):
    a,b,c,d = map(int, input().split())
    count = 0
    for i in range(a,c + 1):
        for j in range(b, d + 1):
            if (i, j) in grid:
                count += grid[(i, j)]
                
    print(count)
