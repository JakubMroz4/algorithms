import input_generator
import  insertion_sort, quick_sort, heap_sort, merge_sort
import time


def measure_time():
    # pre measurement
    size_array = [10, 50, 100, 500, 1000, 5000, 10000, 20000, 30000, 40000, 50000]
    unsorted_lists = []

    for size in size_array:
        unsorted_lists.append(input_generator.generate_int_list(size))

    # measurement
    time_array = []

    for list in unsorted_lists:
        start = time.time()

        steps = insertion_sort.insertion_sort(list)
        #sorted, steps = merge_sort.merge_sort(list)
        #sorted, steps = heap_sort.heap_sort(list)
        #steps = quick_sort.quick_sort(list)

        end = time.time()
        time_array.append(end - start)

    print(f"Size : {size_array}")
    print(f"steps: {time_array}")



if __name__ == "__main__":
    measure_time()

#insertion:


#merge
#Size : [10, 50, 100, 500, 1000, 5000, 10000, 20000, 30000, 40000, 50000]
#steps: [0.0, 0.0, 0.0, 0.0009992122650146484, 0.0010020732879638672, 0.007998466491699219, 0.019001245498657227, 0.04000043869018555, 0.06241941452026367, 0.08900189399719238, 0.11499881744384766]

#heap
#Size : [10, 50, 100, 500, 1000, 5000, 10000, 20000, 30000, 40000, 50000]
#steps: [0.0, 0.0, 0.0, 0.0020020008087158203, 0.0019979476928710938, 0.01699972152709961, 0.03600001335144043, 0.08600187301635742, 0.14288759231567383, 0.17899847030639648, 0.2680025100708008]

#quick
#Size : [10, 50, 100, 500, 1000, 5000, 10000, 20000, 30000, 40000, 50000]
#steps: [0.0, 0.0, 0.0, 0.0010001659393310547, 0.0010001659393310547, 0.004999876022338867, 0.012001276016235352, 0.023000717163085938, 0.041999101638793945, 0.05299997329711914, 0.0690007209777832]