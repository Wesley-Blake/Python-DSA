def merge(left: list, right: list) -> list:
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    
    result = []
    left_index, right_index = 0, 0

    while len(result) < len(left) + len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
        
        if left_index == len(left):
            result += right[right_index:]
            break
        if right_index == len(right):
            result += left[left_index:]
            break
        
    return result

def merge_sort(array: list) -> list:
    if len(array) < 2:
        return array
    
    mid_point = len(array) // 2

    return merge(
        left=merge_sort(array[:mid_point]),
        right=merge_sort(array[mid_point:])
    )


if __name__ == '__main__':
    test_array = [4,2,3,1,9]
    new_array = merge_sort(test_array)
    assert new_array == [1,2,3,4,9], f"{new_array}"
