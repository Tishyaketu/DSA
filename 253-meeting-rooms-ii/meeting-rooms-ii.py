class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
      if not intervals: return 0
      start_times = sorted([i[0] for i in intervals])
      end_times = sorted(i[1] for i in intervals)
      L = len(intervals)
      ur, stp, etp = 0, 0, 0
      while stp<L:
        if start_times[stp]>=end_times[etp]:
          ur-=1
          etp+=1
        ur+=1
        stp+=1
      return ur