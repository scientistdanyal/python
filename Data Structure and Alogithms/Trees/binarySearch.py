arr = [1,2,3,4,6,7,8,9]


target = 4


def binary_search(arr, target):


    left, right = 0, len(arr)-1

    while left<= right:

        mid = (left + right) // 2

        if (arr[mid] == target):
            return mid       #this will return index
        elif (arr[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
        
    return -1

print(binary_search(arr, target))