import random
import numpy as np
import math


def cal_dist(x, y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


def new_mean(nums):
    sum_x = sum(x[0] for x in nums)
    sum_y = sum(x[1] for x in nums)
    return sum_x/len(nums), sum_y/len(nums)


def kmeans(nums: list((float, float)), K=4, max_iter=200, tol=1E-2):
    if len(nums) <= K:
        return [[num] for num in nums], nums
    random.shuffle(nums)
    centroids = nums[:K]
    cur_iter = 0
    output = []
    while cur_iter < max_iter:
        output = [[] for _ in range(K)]
        for num in nums:
            assignment = 0
            dist = float("inf")
            for idx, centroid in enumerate(centroids):
                new_dist = cal_dist(num, centroid)
                if new_dist < dist:
                    dist = new_dist
                    assignment = idx
            output[assignment].append(num)
        new_centroids = [new_mean(assignments) for assignments in output]
        diffs = [cal_dist(new_centroid, old_centroid) for (
            new_centroid, old_centroid) in zip(new_centroids, centroids)]
        if min(diffs) < tol:
            print("At iteration {}, min diff is smaller than tol".format(cur_iter))
            break
        else:
            centroids = new_centroids
        cur_iter += 1
    return output, centroids


if __name__ == "__main__":
    nums = [(random.randint(-100, 100), random.randint(-50, 50))
            for _ in range(50)] + [(random.randint(-200, -100), random.randint(-50, 50))
                                   for _ in range(50)] + [(random.randint(-100, 100), random.randint(50, 150))
                                                          for _ in range(50)] + [(random.randint(100, 150), random.randint(250, 350))
                                                                                 for _ in range(50)]
    print(kmeans(nums))
