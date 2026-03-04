from random import choice

def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array

    small, same, large = [],[],[]
    key = choice(array)

    for i in array:
        if i < key:
            small.append(i)
        elif i == key:
            same.append(i)
        else:
            large.append(i)

    return quick_sort(small) + same + quick_sort(large)

if __name__ == '__main__':
    test_array = [4,2,3,1,9]
    result_array = quick_sort(test_array)
    assert result_array == [1,2,3,4,9], f"{result_array}"
