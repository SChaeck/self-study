input()
# se = set(map(int, input().split()))
se = list(map(int, input().split()))
k = int(input())
li = list(map(int, input().split()))

se.sort()
print(se)
for j in li :
    if j in se :
        print(1)
    else : 
        print(0)
        
# [in 연산자를 쓸 때는 set으로 바꿔서 쓰면 빠르다.]

# set은 해시 함수와 해시 테이블을 이용해서 만든 자료구조이기 때문에
# List처럼 선형적으로 탐색하지 않습니다.

# 그래서 맨 첫번째 값을 검사하나, 맨 마지막 값을 검사하나 시간에는 
# 큰 차이가 없는 것을 확인할 수 있습니다.

# 따라서 set의 경우에는 해시 함수 연산 시간만큼 걸리므로, 데이터가 
# 커지더라도 일정한 속도가 보장됩니다.

# 그래서 무언가 값이 있는지 확인하려면 set() 으로 변경한다음 
# in 연산을 사용하는 것이 좋습니다.