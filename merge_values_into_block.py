from typing import List, Optional

class Solution:
    def minOperations(self, arr: List[int]) -> int:
        last_position = {}
        for i, value in enumerate(arr):
            last_position[value] = i

        segment_count = 0
        segment_end = 0

        for i, value in enumerate(arr):
            segment_end = max(segment_end, last_position[value])

            if i == segment_end:
                segment_count += 1

        distinct_values = len(last_position)
        return distinct_values - segment_count
