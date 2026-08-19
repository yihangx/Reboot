from typing import List


class Solution:
    def minimumRedistributionCost(
        self,
        products: List[int]
    ) -> int:
        n = len(products)
        target = sum(products) // n

        def clockwise_cost(values) -> int:
            prefix = 0
            minimum_prefix = 0
            prefix_sum = 0

            for amount in values:
                prefix += amount - target
                minimum_prefix = min(minimum_prefix, prefix)
                prefix_sum += prefix

            return prefix_sum - n * minimum_prefix

        clockwise = clockwise_cost(products)
        counterclockwise = clockwise_cost(reversed(products))

        return min(clockwise, counterclockwise)
