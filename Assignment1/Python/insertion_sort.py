# insertion sort for integers

input_list = [12, 11, 7, 2, 20, 36, 13, 5, 6]


def insertion_sort(array):
    i = 1
    steps = 1
    while i < len(array):
        j = i
        steps += 1
        while j > 0 and array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
            steps += 2
        i += 1
        steps += 1

    return steps


if __name__ == "__main__":
    input_list = [12, 11, 7, 2, 20, 36, 13, 5, 6]
    steps = insertion_sort(input_list)
    print(input_list)
    print(f"steps: {steps}")
