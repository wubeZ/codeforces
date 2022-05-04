def main():
    n = int(input())
    prices = list(map(int, input().split()))
    q = int(input())
    ans = []
    prices.sort()
    for i in range(q):
        m = int(input())
        best = -1
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left)//2
            if prices[mid] <= m:
                best = mid
                left = mid + 1
            else:
                right = mid - 1
 
        ans.append(best + 1)
 
    for i in ans:
        print(i)
 
 
main()
