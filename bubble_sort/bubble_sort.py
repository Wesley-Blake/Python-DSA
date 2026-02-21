def bubble_sort(array: list) -> None:
    boundary = len(array) - 1
    for i in range(boundary):
        already_sorted = True
        for j in range(boundary - i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                already_sorted = False
        if already_sorted:
            break

if __name__ == '__main__':
    test_array = [4,2,3,1,9]
    bubble_sort(test_array)
    assert test_array == [1,2,3,4,9], f"{test_array}"