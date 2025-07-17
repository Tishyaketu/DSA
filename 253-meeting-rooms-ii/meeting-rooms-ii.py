class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        wR = 0
        st = sorted([i[0] for i in intervals])
        et = sorted(i[1] for i in intervals)
        stp,etp = 0, 0
        L = len(intervals)
        while stp<L:
          if st[stp]>=et[etp]:
            wR-=1
            etp+=1
          wR+=1
          stp+=1
        return wR
