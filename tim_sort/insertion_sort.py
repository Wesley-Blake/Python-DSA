def insertion_sort(array: list, left=0, right=None):
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
        key = array[i]
        j = i - 1
        while j >= left and array[j] > key:
            array[j+1] = array[j]
            array[j] = key
            j -= 1
        array[j+1] = key

if __name__ == '__main__':
    test_array = [4,3,1,2,9]
    insertion_sort(test_array)
    assert test_array == [1,2,3,4,9], f"{test_array}"
