import heapq, sys

for _ in range(int(sys.stdin.readline())) :
    minHeap = []
    maxHeap = []
    visited = []
    k = 0
    for _ in range(int(sys.stdin.readline())) :
        cmd, num = sys.stdin.readline().rstrip().split()
        if cmd == 'I' :
            heapq.heappush(minHeap, (int(num), k))
            heapq.heappush(maxHeap, (-int(num), k))
            visited.append(False)
            k += 1
        else :
            if num[0] == '-' :
                while minHeap and visited[minHeap[0][1]] : heapq.heappop(minHeap)
                if minHeap :
                    visited[minHeap[0][1]] = True
                    heapq.heappop(minHeap)
            else :
                while maxHeap and visited[maxHeap[0][1]] : heapq.heappop(maxHeap)                   
                if maxHeap :
                    visited[maxHeap[0][1]] = True
                    heapq.heappop(maxHeap)
                
    while minHeap and visited[minHeap[0][1]] : heapq.heappop(minHeap)
    while maxHeap and visited[maxHeap[0][1]] : heapq.heappop(maxHeap)                   
    if minHeap and maxHeap :
        print(-heapq.heappop(maxHeap)[0], heapq.heappop(minHeap)[0])
    else :
        print("EMPTY")