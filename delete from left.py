
sl = input()
tl = input()
s = [i for i in sl]
t = [i for i in tl]
count = 0
i = len(s) - 1
j = len(t) - 1
while i > -1 and j > -1:
    if s[i] == t[j]:
        count += 1
    else:
        break
    i-=1
    j-=1
 
print(len(s) + len(t) - 2*count)
