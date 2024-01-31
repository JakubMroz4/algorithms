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
    steps = 0
    heap_size = len(array)
    steps_build_heap = build_max_heap(array)
    steps += 2 + steps_build_heap

    for i in range(heap_size - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        steps_heapify = max_heapify(array, 0, i)
        steps += 2 + steps_heapify

    return array, steps


def build_max_heap(array):
    heap_size = len(array)
    steps = 1

    for i in reversed(range(-1, len(array)//2)):
        steps_heapify = max_heapify(array, i, heap_size)
        steps += 1 + steps_heapify

    return steps


def max_heapify(array, root_index, heap_size):
    largest = root_index

    left = left_h(root_index)
    right = right_h(root_index)
    steps = 3

    if left < heap_size and array[left] > array[largest]:
        largest = left
        steps += 1

    if right < heap_size and array[right] > array[largest]:
        largest = right
        steps += 1

    if largest != root_index:
        array[root_index], array[largest] = array[largest], array[root_index]
        steps_heapify = max_heapify(array, largest, heap_size)
        steps += 2 + steps_heapify

    return steps


if __name__ == "__main__":
    input_list = [12, 11, 7, 2, 20, 36, 13, 5, 6]
    sorted, steps = heap_sort(input_list)
    print(sorted)
    print(steps)