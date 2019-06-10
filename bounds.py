def upper_bound(arr, el):
    left = 0
    right = len(arr) - 1
    while True:
        if right - left == 1:
            if el <= arr[left]:
                return left
            if el <= arr[right]:
                return right
            return right + 1
        if left == right:
            if el <= arr[right]:
                return right
            return right + 1
        mid = (left + right) // 2
        if arr[mid] == el:
            return mid
        if arr[mid] < el:
            left = mid + 1
        else:
            right = mid - 1
            
def lower_bound(arr, el):
    left = 0
    right = len(arr) - 1
    while True:
        if right - left == 1:
            if arr[right] <= el:
                return right
            if arr[left] <= el:
                return left
            return left - 1
        if left == right:
            if arr[left] <= el:
                return left
            return left - 1
        mid = (left + right) // 2
        if arr[mid] == el:
            return mid
        if arr[mid] < el:
            left = mid + 1
        else:
            right = mid - 1
