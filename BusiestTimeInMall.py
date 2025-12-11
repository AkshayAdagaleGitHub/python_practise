from typing import List

def find_busiest_time(times: List[List[int]]) -> int:
    n = len(times)
    if n == 0:
        return 0

    runningCount = 0
    maxCount = 0
    busiestTime = 0
    i = 0

    while i < n:
        currentTime = times[i][0]
        if times[i][2] == 1:
            runningCount += times[i][1]
        else:
            runningCount -= times[i][1]

        i+=1
        if i < n and currentTime == times[i][0]:
            continue

        if runningCount > maxCount:
            maxCount = runningCount
            busiestTime = currentTime

    return busiestTime


print(find_busiest_time([[1487799425, 14, 1],
                         [1487799425, 4, 1],
                         [1487799425, 2, 1],
                         [1487800378, 10, 1],
                         [1487801478, 18, 1],
                         [1487901013, 1, 1],
                         [1487901211, 7, 1],
                         [1487901211, 7, 1]]))

# expected output : 1487901211