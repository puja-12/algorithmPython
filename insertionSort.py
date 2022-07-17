def insertion_sort(arr):

    for i in range(1, len(arr)):

        val = arr[i]

        j = i - 1
        while j >= 0 and val < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val

    return arr


# given string
if __name__ == "__main__":
    sample_string = "stack"
    arr = [i for i in sample_string]
    sorted_arr = insertion_sort(arr)
    print(f"Original String: {sample_string}")
    print(f"Sorted String: {''.join(sorted_arr)}")