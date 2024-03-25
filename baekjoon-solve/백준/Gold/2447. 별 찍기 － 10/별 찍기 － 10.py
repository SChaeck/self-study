def make_star(N) :
  global star
  if N == 3 : 
    star[0][:3] = star[2][:3] = ['*']*3
    star[1][:3] = ['*', ' ', '*']
    return

  d = N//3 
  make_star(d) 
  for r in range(3) :
    for c in range(3) :
      if r == 1 and c == 1 : # 가운데 비우기
        continue
      for k in range(d) :
        star[d*r+k][d*c:d*(c+1)] = star[k][:d]

N = int(input())

star = [[' ' for _ in range(N)] for _ in range(N)]

make_star(N)

for i in range(N) :
  for j in range(N) :
    print(star[i][j], end = "")
  print()