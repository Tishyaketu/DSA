class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        hottest = 0
        waiting_days_array = [0] * n
        for cd in range(n - 1, -1, -1):
            ct = temperatures[cd]
            if ct >= hottest:
                hottest = ct
                continue
            waiting_days = 1
            while temperatures[cd + waiting_days] <= ct:
                waiting_days += waiting_days_array[cd + waiting_days]
            waiting_days_array[cd] = waiting_days
        return waiting_days_array