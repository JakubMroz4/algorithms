# insertion sort for integers

input_list = [12, 11, 7, 2, 20, 36, 13, 5, 6]

def insertion_sort(input):
    i = 1
    while i < len(input):
        j = i
        while j > 0 and input[j-1] > input[j]:
            input[j], input[j-1] = input[j-1], input[j]
            j -= 1
        i += 1

    return input



print(insertion_sort(input_list))