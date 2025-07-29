from typing import List

class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        result = []
        if not schedule:
            return result

        # Flatten and sort intervals by start time
        flats = sorted([iv for employee in schedule for iv in employee], key=lambda x: x.start)

        temp = flats[0]

        for i in range(1, len(flats)):
            cur = flats[i]
            if cur.start <= temp.end:
                temp.end = max(temp.end, cur.end)
            else:
                result.append(Interval(temp.end, cur.start))
                temp = cur

        return result
