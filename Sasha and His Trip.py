def main():
  n, v = map(int, input().split())
  run, res = 0, 0
  if c >= n - 1:
      print(n - 1)
  else:
      ne = (n-1) - c
      res += c
      idx = 2
      for i in range(ne):
          res += idx
          idx += 1
      
      print(res)

main()
