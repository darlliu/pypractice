from typing import List
import heapq
# Write any import statements here

# total damage = (H1/B) * (D1 + D2) + D2(H2/B)


def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
    backline_queue = []
    frontline_queue = []
    mean_damage = sum(D) / len(D)
    mean_health = sum(H) / len(H)
    for idx in range(N):
        damage1 = mean_health / B * \
            (mean_damage + D[idx]) + H[idx] / B * D[idx]
        damage2 = H[idx] / B * (D[idx] + mean_damage) + \
            mean_health / B * mean_damage
        heapq.heappush(frontline_queue, (-damage1, idx))
        heapq.heappush(backline_queue, (-damage2, idx))
    _, front = heapq.heappop(frontline_queue)
    _, back = heapq.heappop(backline_queue)
    if front != back:
        return H[back] / B * (D[back] + D[front]) + H[front] / B * D[front]
    else:
        _, front2 = heapq.heappop(frontline_queue)
        _, back2 = heapq.heappop(backline_queue)
        return max(H[back] / B * (D[back] + D[front2]) + H[front2] / B * D[front2],
                   H[back2] / B * (D[back2] + D[front]) + H[front] / B * D[front])


print(getMaxDamageDealt(3, [2, 1, 4], [3, 1, 2], 4))
