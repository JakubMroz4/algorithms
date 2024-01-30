# merge sort for integers

input_list = [12, 11, 7, 2, 20, 36, 13, 5, 6]

def merge_sort(array):
    result = []
    steps = 1

    if len(array) <= 1:
        return array, steps

    middle = int(len(array) / 2)

    sorted_left, steps_left = merge_sort(array[:middle])
    sorted_right, steps_right = merge_sort(array[middle:])

    i = 0 # left index
    j = 0 # right index

    steps += 5
    steps += steps_left
    steps += steps_left

    # combine both sorted lists
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] < sorted_right[j]:
            result.append(sorted_left[i])
            i += 1
            steps += 2
            continue

        result.append(sorted_right[j])
        j += 1
        steps += 2

    # check if anything is left in sorted halves
    while i < len(sorted_left):
        result.append(sorted_left[i])
        i += 1
        steps += 2

    while j < len(sorted_right):
        result.append(sorted_right[j])
        j += 1
        steps += 2

    return result, steps


if __name__ == "__main__":
    input_list = [12, 11, 7, 2, 20, 36, 13, 5, 6]
    sorted, steps = merge_sort(input_list)
    print(sorted)
    print(f"steps: {steps}")