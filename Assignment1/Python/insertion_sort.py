# insertion sort for integers

input_list = [12, 11, 7, 2, 20, 36, 13, 5, 6]


def insertion_sort(array):
    i = 1
    while i < len(array):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
        i += 1

    return array


print(insertion_sort(input_list))
