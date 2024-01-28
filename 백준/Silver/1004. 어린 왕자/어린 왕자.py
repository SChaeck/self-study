def judge (arr, x, y) :
  if (x-arr[0])**2 + (y-arr[1])**2 < arr[2]**2 :
    return 1
  else :
    return 0

test_case = int(input())

for _ in range(test_case) :
  x1, y1, x2, y2 = map(int, input().split()) 
  planetary = [None] * int(input())
  cnt = 0
  for i in range(len(planetary)) :
    planetary[i] = list(map(int, input().split()))
    if judge(planetary[i], x1, y1) != judge(planetary[i], x2, y2) :
      cnt += 1
  print(cnt)