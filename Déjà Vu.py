t = int(input())
 
for i in range(t):
    word = list(input())
    flag = False
    if word.count('a') == len(word):
        flag = True
        print("NO")
        continue
    for i in range(len(word)):
        if word[len(word) - 1 - i] != 'a':
            word.insert(i, 'a')
            flag = True
            print("YES")
            print("".join(word))
            break
    if not flag:
            print("NO")
