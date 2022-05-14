t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    bin_dig = bin(k)
    bin_dig = bin_dig.replace("0b", "")
    bin_dig = bin_dig[::-1]
 
    ans = 0
    for i in range(len(bin_dig)):
        if bin_dig[i] == "1":
            ans += (pow(n, i))
    
    print(ans%(pow(10,9)+7))
