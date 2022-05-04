def main():
  n, v = map(int, input().split())
  run, res = 0, 0
  if v >= n - 1:
      print(n - 1)
  else:
      for i in range(1, n + 1):
          want = n - i
          if run < want:
              res += (v - run) * i
              run += v - run
              run -= 1
          else:
              print(res)
              break

main()
