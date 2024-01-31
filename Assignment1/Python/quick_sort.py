# quick sort with pivot around last element

def quick_sort_inner(array, low, high):
    steps = 0

    if low < high:
        pivot, steps_partition = partition(array, low, high)

        # left half (<pivot)
        steps_left = quick_sort_inner(array, low, pivot - 1)
        # right half (>pivot)
        steps_right = quick_sort_inner(array, pivot + 1, high)
        steps += 3 + steps_partition + steps_right + steps_left

    return steps


def partition(array, low, high):
    steps = 0

    pivot = array[high]

    # index for element greater than pivot
    i = low - 1
    steps += 2

    # go through all elements and compare each element to pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if j is smaller than pivot then swap j with i
            i = i + 1
            array[i], array[j] = array[j], array[i]
            steps += 2

    # swap pivot with i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    steps += 1

    # return pivot position
    return i + 1, steps

def quick_sort(array):
    steps = quick_sort_inner(array, 0, len(array)-1)
    return steps


if __name__ == "__main__":
    input_list = [12, 11, 7, 2, 20, 36, 13, 5, 6]
    steps = quick_sort(input_list)
    print(input_list)
    print(steps)