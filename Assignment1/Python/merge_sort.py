# merge sort for integers

input_list = [12, 11, 7, 2, 20, 36, 13, 5, 6]

def merge_sort(input):
    if len(input) <= 1:
        return input

    middle = int(len(input) / 2)
    left = input[:middle]
    right = input[middle:]

    return merge_sort(left) + merge_sort(right)

print(merge_sort(input_list))