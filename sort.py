import random


def test(fctn):
    for i in range(5):
        nums = [random.randint(-1000, 1000) for i in range(10)]
        tst = fctn(nums)
        ref = sorted(nums)
        print("### {} Test {}, sorted output {}, passed: {}".format(
            fctn.__name__, i, tst[-10:], tst == ref))


def insertSort(arr):
    out = []
    for num in arr:
        for idx in range(len(out)):
            if num < out[idx]:
                out.insert(idx, num)
                break
        else:
            out.append(num)
    return out


def qSort(arr):
    def swap(a, b):
        return b, a
    if len(arr) <= 1:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = swap(arr[0], arr[1])
        return arr
    med = int(len(arr) / 2)
    arr[med], arr[-1] = swap(arr[med], arr[-1])
    left = []
    right = []
    for i in range(len(arr) - 1):
        if arr[i] < arr[-1]:
            left.append(arr[i])
        else:
            right.append(arr[i])
    left = qSort(left)
    right = qSort(right)
    return left + [arr[-1]] + right


def qSortInPlace(arr):
    def swap(a, b):
        return b, a
    if len(arr) <= 1:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = swap(arr[0], arr[1])
        return arr
    pivot = int(len(arr)/2)
    arr[pivot], arr[-1] = swap(arr[pivot], arr[-1])
    curr = 0
    for i in range(len(arr) - 1):
        if arr[i] <= arr[-1]:
            arr[curr], arr[i] = swap(arr[curr], arr[i])
            curr += 1
    arr[curr], arr[-1] = swap(arr[curr], arr[-1])
    arr[:curr] = qSortInPlace(arr[:curr])
    arr[curr + 1:] = qSortInPlace(arr[curr + 1:])
    return arr


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = int(len(arr)/2)
    left = mergeSort(arr[: mid])
    right = mergeSort(arr[mid:])
    assert len(left) + len(right) == len(
        arr), "wrong split {} + {} != {}".format(len(left), len(right), len(arr))
    merged = []
    idx = idy = 0
    while idx < len(left) or idy < len(right):
        if idx == len(left):
            merged.append(right[idy])
            idy += 1
        elif idy == len(right):
            merged.append(left[idx])
            idx += 1
        elif left[idx] <= right[idy]:
            merged.append(left[idx])
            idx += 1
        else:
            merged.append(right[idy])
            idy += 1
    assert len(merged) == len(left) + len(right), "wrong merge"
    return merged


def heapSort(arr):
    def heapify(arr, idx, sz):
        # 0 -> 1, 2
        # 1 -> 3, 4
        # 2 -> 5, 6
        left = idx * 2 + 1
        right = idx * 2 + 2
        mx = idx
        if left < sz and arr[mx] < arr[left]:
            mx = left
            # swap LEFT to IDX as the current largest
        if right < sz and arr[mx] < arr[right]:
            mx = right
        if mx != idx:
            arr[mx], arr[idx] = arr[idx], arr[mx]
            return heapify(arr, mx, sz)
        return arr
    # build heap
    mid = int(len(arr)/2)
    for i in range(mid + 1):
        idx = mid - i
        arr = heapify(arr, idx, len(arr))
    # starting from the right, exchange the left most with this element
    # then rebuild heap for all to left
    for i in range(len(arr)):
        arr[-1 - i], arr[0] = arr[0], arr[-1 - i]
        arr = heapify(arr, 0, len(arr) - i - 1)
    return arr


if __name__ == "__main__":
    test(heapSort)
