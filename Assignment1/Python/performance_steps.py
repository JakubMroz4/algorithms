import input_generator
import  insertion_sort, quick_sort, heap_sort, merge_sort

def measure_steps():
    # pre measurement
    size_array = [10, 50, 100, 500, 1000, 5000, 10000, 20000, 30000, 40000, 50000]
    unsorted_lists = []

    for size in size_array:
        unsorted_lists.append(input_generator.generate_int_list(size))

    # measurement
    steps_array = []

    for list in unsorted_lists:
        #steps = insertion_sort.insertion_sort(list)
        #sorted, steps = merge_sort.merge_sort(list)
        #sorted, steps = heap_sort.heap_sort(list)
        steps = quick_sort.quick_sort(list)
        steps_array.append(steps)

    print(f"Size : {size_array}")
    print(f"steps: {steps_array}")


if __name__ == "__main__":
    measure_steps()

#insertion:
#Size : [10, 50, 100, 500, 1000, 5000, 10000, 20000, 30000, 40000, 50000]
#steps: [61, 1315, 5111, 121629, 503179, 12489673, 49795355, 199083153, 449078971, 802750211, 1248806643]

#merge
#Size : [10, 50, 100, 500, 1000, 5000, 10000, 20000, 30000, 40000, 50000]
#steps: [106, 706, 1618, 9394, 20794, 143930, 307866, 655738, 936986, 1391482, 1719834]

#heap
#Size : [10, 50, 100, 500, 1000, 5000, 10000, 20000, 30000, 40000, 50000]
#steps: [191, 1645, 3790, 26274, 59215, 371451, 806573, 1745008, 2729833, 3752350, 4797634]

#quick
#Size : [10, 50, 100, 500, 1000, 5000, 10000, 20000, 30000, 40000, 50000]
#steps: [58, 428, 1098, 7204, 14772, 100842, 196814, 417560, 692746, 928860, 1129202]

