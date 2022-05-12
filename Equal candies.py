t = int(input())
for i in range(t):
    i = input()
    lists = list(map(int, input().split()))
    lists.sort()
    eaten, prev = 0, lists[0]
    for i in lists:
        eaten += (i - prev)
    print(eaten)
