def bact(n):
    res = 1 
    while n - res >= res:
        res *= 2
    return (n - res)
    
n = int(input())
nums = 0
while n > 0:
    nums +=1
    l = bact(n)
    if l > 0:
        n = l
    else:
        break
print(nums)
