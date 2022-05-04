def main():
    n = int(input())
    count_list = []
    for i in range(n):
        x = int(input())
        stack = [x]
        fcount, scount = 0, 0
        y = 31
        while y != x:
            if y < x: y += 4
            elif y > x: y -= 1
            fcount += 1
        y = 32
        while y != x:
            if y < x: y += 4
            elif y > x: y -= 1
            scount += 1
        if fcount < scount:
            count_list.append(31)
        else:
            count_list.append(32)
 
    for x in count_list:
        print(x)
 
 
main()
