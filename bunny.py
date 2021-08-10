from typing import List
# Write any import statements here


def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
    cycles = [0 for _ in L]
    for idx in range(len(L)):
        visited = {idx: 0}
        pivot = idx
        steps = 0
        while (L[pivot] - 1) not in visited:
            pivot = L[pivot] - 1
            steps += 1
            visited[pivot] = steps
        if visited[L[pivot] - 1] == 0:
            cycles[idx] = len(visited)
    max_steps = 0
    print(cycles)
    for idx in range(len(L)):
        pivot = idx
        steps = 0
        while cycles[pivot] == 0:
            pivot = L[pivot] - 1
            steps += 1
        print(steps, cycles[pivot])
        max_steps = max(steps + cycles[pivot], max_steps)
    return max_steps


print(getMaxVisitableWebpages(5, [2, 4, 2, 2, 3]))
