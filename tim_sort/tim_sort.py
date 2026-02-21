from random import randint
from insertion_sort import insertion_sort
from merge_sort import merge

def tim_sort(array):
    min_run = 32
    n = len(array)

    for i in range(0,n,min_run):
        insertion_sort(array, i, min((i+min_run-1),n-1))
        
    size = min_run
    while size < n:
        for start in range(0, n, size*2):
            key = start + size - 1
            end = min((start+size-1),n-1)

            merged_array = merge(
                left=array[start:key+1],
                right=array[key+1:end+1]
            )
            array[start:start + len(merged_array)] = merged_array
        size *= 2


if __name__ == '__main__':
    test_array = []
    for i in range(100):
        test_array.append(randint(0,1_000_000))
    copy = test_array
    tim_sort(copy)

    test_array.sort()
    assert copy == test_array
