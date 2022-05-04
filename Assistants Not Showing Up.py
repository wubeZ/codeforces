def main():
    n, m = map(int, input().split())
    time = []
    merged = []
    for i in range(m):
        x, y = map(int, input().split())
        time.append([x, y])
    time.sort()
    start = time[0][0]
    end = time[0][1]
    for i in range(1, len(time)):
        if time[i][0] <= end + 1:
            end = max(end, time[i][1])
        elif end + 1 < time[i][0]:
            merged.append([start, end])
            start = time[i][0]
            end = time[i][1]
 
    merged.append([start,end])
 
    if len(merged) == 1 and merged[-1][0] == 0 and merged[-1][1] == n-1:
        print('NO')
    else:
        print('YES')
