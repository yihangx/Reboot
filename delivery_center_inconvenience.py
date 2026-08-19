from collections import deque
from typing import List


class Solution:
    def minimumInconvenience(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        INF = rows + cols

        # Multi-source BFS using 8 directions.
        distance = [[INF] * cols for _ in range(rows)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    distance[r][c] = 0
                    queue.append((r, c))

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1),
        ]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and distance[nr][nc] == INF
                ):
                    distance[nr][nc] = distance[r][c] + 1
                    queue.append((nr, nc))

        def can_achieve(max_distance: int) -> bool:
            min_center_row = 0
            max_center_row = rows - 1
            min_center_col = 0
            max_center_col = cols - 1

            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 0 and distance[r][c] > max_distance:
                        min_center_row = max(
                            min_center_row, r - max_distance
                        )
                        max_center_row = min(
                            max_center_row, r + max_distance
                        )
                        min_center_col = max(
                            min_center_col, c - max_distance
                        )
                        max_center_col = min(
                            max_center_col, c + max_distance
                        )

                        if (
                            min_center_row > max_center_row
                            or min_center_col > max_center_col
                        ):
                            return False

            return True

        left, right = 0, max(rows, cols)

        while left < right:
            mid = (left + right) // 2

            if can_achieve(mid):
                right = mid
            else:
                left = mid + 1

        return left
