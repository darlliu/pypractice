from typing import List
# Write any import statements here


def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    # Write your code here
    P = sorted(P)
    # [. .2 3 . . . 7 8 . .]
    # [. . . 3 4 . . 7 8 . .]

    def hopnext(P, total_steps):
        print(P, total_steps)
        if not P:
            return total_steps
        pivot = P[0]
        P = P[1:]
        next_stop = None
        for idx, num in enumerate(P):
            pivot += 1
            if num != pivot:
                next_stop = num
                break
        pivot = pivot + 1
        if pivot == N:
            return hopnext(P, total_steps + 1)
        if next_stop is None:
            return hopnext(P + [pivot], total_steps + 1)
        else:
            P = P[: idx] + [pivot - 1] + P[idx:]
            return hopnext(P, total_steps + 1)
    return hopnext(P, 0)


print(getSecondsRequired(3, 1, [1]))
print(getSecondsRequired(
    108, 12, [78, 79, 23, 24, 88, 77,  18, 16, 5, 2, 4, 1]))
