from typing import List, Any


def meeting_planner(slotsA: List[List[int]], slotsB: List[List[int]], dur: int) -> list[int] | list[Any]:
    ia, ib = 0, 0

    while ia < len(slotsA) and ib < len(slotsB):
        start = max(slotsA[ia][0], slotsB[ib][0])
        end = min(slotsA[ia][1], slotsB[ib][1])

        if (start + dur) <= end:
            return [start, start + dur]

        if slotsA[ia][1] < slotsB[ib][1]:
            ia+=1
        else:
            ib+=1

    return []


# input:
slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 8
print(meeting_planner(slotsA, slotsB, dur))
#output: [60, 68]

#input:
slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 12
print(meeting_planner(slotsA, slotsB, dur))
#output: [] # since there is no common slot whose duration is 12
