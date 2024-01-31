using System;
using System.Diagnostics;

class SortingComparison
{
    static void Main()
    {
        // Define array sizes to test
        int[] inputSizes = { 100, 1000, 5000, 10000, 50000 };

        // Measure execution time for Insertion Sort and Merge Sort
        Console.WriteLine("Array Size\tInsertion Sort Time (seconds)\tMerge Sort Time (seconds)");

        foreach (var size in inputSizes)
        {
            int[] randomArray = GenerateRandomArray(size);

            // Measure Insertion Sort execution time
            var insertionWatch = Stopwatch.StartNew();
            InsertionSort(randomArray);
            insertionWatch.Stop();
            double insertionTimeSeconds = insertionWatch.Elapsed.TotalSeconds;

            // Re-generate a random array for Merge Sort
            randomArray = GenerateRandomArray(size);

            // Measure Merge Sort execution time
            var mergeWatch = Stopwatch.StartNew();
            MergeSort(randomArray);
            mergeWatch.Stop();
            double mergeTimeSeconds = mergeWatch.Elapsed.TotalSeconds;

            Console.WriteLine($"{size}\t\t{insertionTimeSeconds:F8}\t\t\t\t\t{mergeTimeSeconds:F8}");
        }
    }

    static void InsertionSort(int[] arr)
    {
        int n = arr.Length;

        for (int i = 1; i < n; i++)
        {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > key)
            {
                arr[j + 1] = arr[j];
                j = j - 1;
            }

            arr[j + 1] = key;
        }
    }

    static void MergeSort(int[] arr)
    {
        if (arr.Length <= 1)
            return;

        int mid = arr.Length / 2;
        int[] left = new int[mid];
        int[] right = new int[arr.Length - mid];

        Array.Copy(arr, left, mid);
        Array.Copy(arr, mid, right, 0, arr.Length - mid);

        MergeSort(left);
        MergeSort(right);

        Merge(arr, left, right);
    }

    static void Merge(int[] arr, int[] left, int[] right)
    {
        int i = 0, j = 0, k = 0;

        while (i < left.Length && j < right.Length)
        {
            if (left[i] <= right[j])
            {
                arr[k] = left[i];
                i++;
            }
            else
            {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        while (i < left.Length)
        {
            arr[k] = left[i];
            i++;
            k++;
        }

        while (j < right.Length)
        {
            arr[k] = right[j];
            j++;
            k++;
        }
    }

    static int[] GenerateRandomArray(int size)
    {
        Random random = new Random();
        int[] array = new int[size];

        for (int i = 0; i < size; i++)
        {
            array[i] = random.Next();
        }

        return array;
    }
}
