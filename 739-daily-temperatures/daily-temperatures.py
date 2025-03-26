class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        hottest = 0
        answer = [0]*n
        for i in range(n-1,-1,-1):
          ct = temperatures[i]
          if ct>=hottest:
            hottest = ct
            continue
          waiting_days = 1
          while temperatures[i+waiting_days]<=ct:
            waiting_days += answer[i+waiting_days]
          answer[i] = waiting_days
        return answer