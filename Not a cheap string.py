def main():
    t = int(input())
    
    for i in range(t):
        letter = input()
        p = int(input())
        vals , total = [], 0
        for i , ch in enumerate(letter):
            vals.append((ord(ch) - 96, i))
            total += (ord(ch) - 96)
        vals.sort()
        ans, res = [], []
        idx = len(vals) -1
        while idx >= 0:
            if p < total:
                total -= vals[idx][0]
                idx -= 1 
            else:
                while idx >= 0:
                    ans.append(vals[idx])
                    idx -= 1
    ans.sort(key = lambda x: x[1])
    for i in range(len(ans)):
        res.append(letter[ans[i][1]])
    print("".join(res))

main()