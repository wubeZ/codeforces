def main():
    t = int(input())
 
    for i in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen and nums[i] + 1 not in seen:
                nums[i] += 1
            seen.add(nums[i])
                    
    print(len(set(nums)))

main()