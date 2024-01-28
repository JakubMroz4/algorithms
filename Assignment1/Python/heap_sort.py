import math

# heap sort for integers

input_list = [12, 11, 7, 2, 20, 36, 13, 5, 6]

# 0 based index !
# left(i) = 2i + 1
# right(i) = 2i + 2


def left_h(index):
    return 2*index + 1


def right_h(index):
    return 2*index + 2


def heap_sort(array):
    heap_size = len(array)

    build_max_heap(array)

    for i in range(heap_size - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        max_heapify(array, 0, i)

    return array


def build_max_heap(array):
    heap_size = len(array)

    for i in reversed(range(1, math.floor(len(array)/2))):
        max_heapify(array, i, heap_size)
        # print(i)


def max_heapify(array, root_index, heap_size):
    largest = root_index

    left = left_h(root_index)
    right = right_h(root_index)

    if left < heap_size and array[left] > array[largest]:
        largest = left

    if right < heap_size and array[right] > array[largest]:
        largest = right

    if largest != root_index:
        array[root_index], array[largest] = array[largest], array[root_index]
        max_heapify(array, largest, heap_size)


print(heap_sort(input_list))
