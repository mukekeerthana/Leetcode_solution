from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        start = None
        litter = []

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter.append((r, c))

        k = len(litter)

        if k == 0:
            return 0

        lid = {pos: i for i, pos in enumerate(litter)}
        target = (1 << k) - 1

        
        best = [[[ -1] * (1 << k) for _ in range(n)]
                for _ in range(m)]

        q = deque()
        sr, sc = start

        q.append((sr, sc, energy, 0, 0))
        best[sr][sc][0] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, e, mask, moves = q.popleft()

            if mask == target:
                return moves

            if e == 0:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                ne = e - 1
                nmask = mask

                if (nr, nc) in lid:
                    nmask |= 1 << lid[(nr, nc)]

                if classroom[nr][nc] == 'R':
                    ne = energy

                
                if best[nr][nc][nmask] >= ne:
                    continue

                best[nr][nc][nmask] = ne
                q.append((nr, nc, ne, nmask, moves + 1))

        return -1



            
                


        


        