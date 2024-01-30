# quick sort with pivot around last element

def quick_sort_inner(array, low, high):
  if low < high:
    pivot = partition(array, low, high)

    # left half (<pivot)
    quick_sort_inner(array, low, pivot - 1)
    # right half (>pivot)
    quick_sort_inner(array, pivot + 1, high)


def partition(array, low, high):
    pivot = array[high]

    # index for element greater than pivot
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if j is smaller than pivot then swap j with i
            i = i + 1

            # Swapping element at i with element at j
            array[i], array[j] = array[j], array[i]

    # swap pivot with i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return pivot position
    return i + 1

def quick_sort(array):
    quick_sort_inner(array, 0, len(array)-1)


if __name__ == "__main__":
    input_list = [12, 11, 7, 2, 20, 36, 13, 5, 6]
    sorted = quick_sort(input_list)
    print(input_list)