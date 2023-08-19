import math
import random


def swap(arr, i, j):
    tmp = arr[j]
    arr[j] = arr[i]
    arr[i] = tmp
    return arr


def insertion_sort(arr):
    # sort subarrays from left to right
    # swap element in from the right to sort next subarray
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    # Stable

    for idx in range(1, len(arr)):
        for swap_idx in range(idx, 0, -1):
            if arr[swap_idx] < arr[swap_idx - 1]:
                arr = swap(arr, swap_idx, swap_idx - 1)


def merge_sort(arr):
    # divide and conquer
    # Time complexity: O(nlogn)
    # Space complexity: O(n) - we cannot merge in place
    # Stable

    if len(arr) == 1:
        return arr
    middle = math.ceil(len(arr) / 2)
    sorted_left = merge_sort(arr[:middle])
    sorted_right = merge_sort(arr[middle:])

    i, j = 0, 0
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] < sorted_right[j]:
            arr[i + j] = sorted_left[i]
            i = i + 1
        else:
            arr[i + j] = sorted_right[j]
            j = j + 1

    if j == len(sorted_right):
        arr[i + j :] = sorted_left[i:]
    elif i == len(sorted_left):
        arr[i + j :] = sorted_right[j:]

    return arr


def quick_sort(arr, s, e):
    # divide and conquer
    # Time complexity: O(nlogn) average, O(n^2) worst case
    # Space complexity: O(log n) - we CAN sort in place, but need new stack frame for every recursion level
    # Unstable

    if e - s + 1 == 1:
        return arr
    elif e - s + 1 == 0:
        return []

    boundary = s  # idx where smaller then pivot ends
    # get a random pivot
    pivot_id = random.randint(s, e - 1)
    pivot = arr[pivot_id]
    # swap pivot to end so we know where it is for later
    swap(arr, e - 1, pivot_id)

    # swap smaller than pivot to be before the boundary
    for idx in range(s, e):
        if arr[idx] < pivot:
            arr = swap(arr, idx, boundary)
            boundary += 1

    # swap pivot we store at the end back to middle
    swap(arr, boundary, e - 1)
    # quicksort the two merged halfs
    quick_sort(arr, 0, boundary)
    quick_sort(arr, boundary + 1, e)


def bucket_sort(arr, low, high):
    # Caveat: only works for known finite range of integers
    # Time complexity: O(n)
    # Space complexity: O(value range)
    # Unstable
    buckets = [0] * (high - low + 1)
    for el in arr:
        buckets[el - low] += 1

    bucket_id = 0
    bucket_count = 0
    for idx in range(len(arr)):
        while bucket_count >= buckets[bucket_id]:
            bucket_id += 1
            bucket_count = 0
        arr[idx] = bucket_id + low
        bucket_count += 1


if __name__ == "__main__":
    arr = [9, 2, 5, 8, 0, 5, 1, 3, 2]
    insertion_sort(arr)
    print(arr)

    arr = [9, 2, 5, 8, 0, 5, 1, 3, 2]
    new_arr = merge_sort(arr)
    print(new_arr)

    arr = [9, 2, 5, 8, 0, 5, 1, 3, 2]
    quick_sort(arr, 0, len(arr))
    print(arr)

    arr = [9, 2, 5, 8, 5, 5, 5, 1, 3, 2]
    bucket_sort(arr, 1, 9)
    print(arr)
