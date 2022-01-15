import random
from copy import deepcopy
from time import time

random_list = [random.randint(0, 100000) for _ in range(100000)]


def bubble_sort(items):
    """
    >>> bubble_sort([2, 1, 4, 6, 3])
    [1, 2, 3, 4, 6]
    """
    items = deepcopy(items)

    for iter_num in range(len(items) - 1, 0, -1):
        for idx in range(iter_num):
            if items[idx] > items[idx + 1]:
                temp = items[idx]
                items[idx] = items[idx + 1]
                items[idx + 1] = temp
    return items


def insertion_sort(items):
    """
    >>> insertion_sort([2, 1, 4, 6, 3])
    [1, 2, 3, 4, 6]
    """
    sorted_items = []
    for i in items:
        if not sorted_items:
            sorted_items.append(i)
        else:
            for ind, item in enumerate(sorted_items):
                if i < item:
                    sorted_items.insert(ind, i)
                    break
            else:
                sorted_items.append(i)

    return sorted_items


def binary_search(items, item, start=0, end=None):
    if not end:
        end = len(items) - 1
    if end >= start:
        mid = start + (end - 1) // 2
        if items[mid] == item:
            return mid
        if items[mid] > item:
            return binary_search(items, item, start=start, end=mid - 1)
        else:
            return binary_search(items, item, start=mid + 1, end=end)
    else:
        return -1

    # items = [i for i in enumerate(items)]
    # while True:
    #     items_len = len(items)
    #     center_item = items[items_len // 2]
    #     if item == center_item[1]:
    #         return center_item[0]
    #     if item < center_item[1]:
    #         items = items[:items_len // 2]
    #     if item > center_item[1]:
    #         items = items[items_len // 2 + 1:]


sorted_list = [0, 3, 4, 5, 6, 36, 89, 314, 678, 900]
item_to_search = 4
i = binary_search(sorted_list, item_to_search)
print(i)


if __name__ == "__main__":
    # start = time()
    # bubble_sorted = bubble_sort(random_list)
    # print(time() - start)
    start = time()
    insertion_sorted = insertion_sort(random_list)
    print(time() - start)
    start = time()
    sorted_list = sorted(random_list)
    print(time() - start)

    # assert bubble_sorted == insertion_sorted == sorted_list

