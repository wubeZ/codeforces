def main():
  t = int(input())
  ans = []
  for i in range(t):
      n = int(input())

      arr = list(map(int, input().split()))
      counter = {}
      flag = True
      for i in arr:
          if i in counter:
              counter[i] += 1
          else:
              counter[i] = 1
          if counter[i] >= 3:
              flag = False
              print(i)
              break
      if flag == True:
          print(-1)
          
main()
