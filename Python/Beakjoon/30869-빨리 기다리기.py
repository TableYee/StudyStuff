def getShortestNode():
    minNode = 0
    minTime = 10001
    for i in range(1,n+1):
        if not visited[i] and minTime > times[i]:
            minNode = i
    return minNode

def getArrivalTime(start):
    times[start] = 0
    curTime = 0
    for i in lanes[start]:
        times[i[0]] = i[1]
    
    for i in range(n-1):
        minStation = getShortestNode()
        visited[minStation] = True
        for j in lanes[minStation]:
            totalTime = times[minStation] + i[1]
            if times[i[0]] > totalTime:
                times[i[0]] = totalTime

n,m,k = map(int,input().split())
lanes = [[] for i in range(m+1)]
times = [10001] * (n+1)
visited = [False] * (n+1)
delay = [0] * (n+1)
for i in range(m):
    s,e,t,g = map(int,input().split())
    lanes[s].append([e,t,g])

getArrivalTime(1)