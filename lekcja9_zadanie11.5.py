# algorytm comb sort

# nastepny gap
def find_next_gap(gap):
    gap = (gap * 10) // 13
    if gap < 1:
        return 1
    return gap


def comb_sort(arr):
    n = len(arr)
    gap = n
    swapped = True

    while gap != 1 or swapped == 1:
        gap = find_next_gap(gap)
        swapped = False
        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True


# test
array = [8, 4, 1, 3, -44, 23, -6, 28, 0]
comb_sort(array)
sorted_array = []
for x in range(len(array)):
    sorted_array.append(array[x])
print("Posortowane: " + str(sorted_array))

