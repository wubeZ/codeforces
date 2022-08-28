def main():
    t = int(input())
 
    for i in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        even, odd = 0, 0
        for i in range(len(nums)):
            if nums[i] %2 == 0:
                even += 1
            else:
                odd += 1
    if even > odd:
        print(odd)        
    else:
        print(even)

main()