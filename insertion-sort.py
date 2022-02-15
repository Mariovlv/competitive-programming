def insertionSort(arr):
    for item in range(1, len(arr)):
        j = item
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1

    return arr
