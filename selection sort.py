def selection_sort(arr):

    for i in range(len(arr)):
        index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        if index != i: # 说明需要调换位置
            arr[index], arr[i] = arr[i], arr[index]

    return arr



if __name__ == '__main__':
    
    arr = list(range(20))

    import random
    random.shuffle(arr)
    print(arr)

    print(selection_sort(arr))

# [15, 11, 9, 10, 6, 19, 0, 1, 12, 7, 5, 14, 18, 3, 13, 2, 17, 16, 4, 8]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
