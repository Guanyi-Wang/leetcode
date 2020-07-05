class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def nextDay(cells):
            next =[0 for i in range(len(cells))]
            for i in range(1,len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    next[i] = 1
                else:
                    next[i] = 0
            return next
        seen = {}
        for n in range(1,N+1):
            cells = tuple(nextDay(cells))
            if cells in seen:
                cycle_len = n-1
                k = N%cycle_len
                if k == 0:
                    k = cycle_len
                for cell, t in seen.items():
                    if t == k:
                        return cell
            else:
                seen[cells] = n
        return list(cells)