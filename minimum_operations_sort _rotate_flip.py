from collections import deque
from typing import List


class Solution:
    def minSteps(self, arr: List[int]) -> int:
        start = tuple(arr)
        target = tuple(sorted(arr))

        if start == target:
            return 0

        queue = deque([(start, 0)])
        visited = {start}

        while queue:
            current, steps = queue.popleft()

            rotated = current[1:] + current[:1]
            flipped = current[::-1]

            for next_state in (rotated, flipped):
                if next_state == target:
                    return steps + 1

                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, steps + 1))

        return -1
