def main():
    n = int(input())
    food = list(map(int, input().split()))
    max_count, count = 0, 0
    slow, fast = 0, 0
    while fast < len(food):
        while fast < len(food) and food[slow] == food[fast]:
            fast += 1
        ftemp = fast
        stemp = slow
        while fast < len(food) and food[ftemp] == food[fast] and food[stemp] == food[slow]:
            count += 1
            slow += 1
            fast += 1
        max_count = max(max_count, count)
        count = 0
        slow = fast = ftemp
 
    print(2*max_count)
 
 
main()
