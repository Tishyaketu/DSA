class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        st = []
        for i in range(n):
          st.append(intervals[i][0])
        st = sorted(st)
        et = []
        for i in range(n):
          et.append(intervals[i][1])
        et = sorted(et)
        wR = 0
        stp, etp = 0, 0
        while stp<n:
          if st[stp]>=et[etp]:
            wR-=1
            etp+=1
          wR+=1
          stp+=1
        return wR