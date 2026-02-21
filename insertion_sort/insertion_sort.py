def insertion_sort(array: list):
    for i in range(1,len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            array[j] = key
            j -= 1
        array[j+1] = key

if __name__ == '__main__':
    test_array = [4,3,1,2,9]
    insertion_sort(test_array)
    assert test_array == [1,2,3,4,9], f"{test_array}"
