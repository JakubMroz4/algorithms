# merge sort for integers

input_list = [12, 11, 7, 2, 20, 36, 13, 5, 6]

def merge_sort(input):
    result = []

    if len(input) <= 1:
        return input

    middle = int(len(input) / 2)
    left = input[:middle]
    right = input[middle:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    i = 0 # left index
    j = 0 # right index

    # combine both sorted lists
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] < sorted_right[j]:
            result.append(sorted_left[i])
            i += 1
            continue

        result.append(sorted_right[j])
        j += 1

    # check if anything is left in sorted halves
    while i < len(sorted_left):
        result.append(sorted_left[i])
        i += 1

    while j < len(sorted_right):
        result.append(sorted_right[j])
        j += 1

    return result

print(merge_sort(input_list))