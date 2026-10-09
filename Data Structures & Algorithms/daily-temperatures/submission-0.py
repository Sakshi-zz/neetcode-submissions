from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []                       # indices, temperatures decreasing

        for i, temp in enumerate(temperatures):
            # Pop all indices whose next warmer day is today
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                result[prev] = i - prev
            stack.append(i)

        return result