from collections import Counter
from typing import List


class Solution:
    def getMinAmount(self, quality: List[int]) -> int:
        frequency = Counter(quality)

        last_position = {}
        for i, value in enumerate(quality):
            last_position[value] = i

        total_cost = 0
        segment_start = 0
        segment_end = 0
        largest_frequency = 0

        for i, value in enumerate(quality):
            segment_end = max(
                segment_end,
                last_position[value]
            )

            largest_frequency = max(
                largest_frequency,
                frequency[value]
            )

            # No value in this segment appears after this index.
            if i == segment_end:
                segment_length = i - segment_start + 1

                total_cost += (
                    segment_length - largest_frequency
                )

                segment_start = i + 1
                largest_frequency = 0

        return total_cost
