from typing import List, Tuple


class Solution:
    def assignShelves(
        self,
        numShelves: int,
        limit: List[int]
    ) -> List[int]:

        size = 1
        while size < numShelves:
            size *= 2

        INF = 10**18
        tree = [(INF, INF)] * (2 * size)

        for shelf in range(numShelves):
            tree[size + shelf] = (0, shelf)

        for node in range(size - 1, 0, -1):
            tree[node] = min(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query_prefix(right: int) -> Tuple[int, int]:
            left = size
            right += size
            best = (INF, INF)

            while left < right:
                if left % 2 == 1:
                    best = min(best, tree[left])
                    left += 1

                if right % 2 == 1:
                    right -= 1
                    best = min(best, tree[right])

                left //= 2
                right //= 2

            return best

        def add_book(shelf: int) -> None:
            node = size + shelf
            count = tree[node][0]

            tree[node] = (count + 1, shelf)
            node //= 2

            while node > 0:
                tree[node] = min(
                    tree[node * 2],
                    tree[node * 2 + 1]
                )
                node //= 2

        result = []

        for current_limit in limit:
            _, shelf = query_prefix(current_limit)
            result.append(shelf)
            add_book(shelf)

        return result
