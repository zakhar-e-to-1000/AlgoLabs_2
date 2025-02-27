#variant no. 2

def find_left(arr):
    max_num = arr[0]
    last_i = 0
    for i, num in enumerate(arr):
        if num>=max_num: #normal behavior
            max_num = num
            last_i = i
        else: #detected error:
            break
    if last_i==len(arr)-1:
        return -1
    min_num = min(arr[last_i+1:])
    for i, num in enumerate(arr[:last_i+1]):
        if(num>min_num):
            return i

    return 0

def find_right(arr):
    n = len(arr)
    min_num = arr[-1]
    last_i = 0
    for i in range(n-1, -1, -1):
        num = arr[i]
        if num<=min_num: #normal behavior
            min_num = num
            last_i = i
        else: #detected error:
            break
    if last_i==0:
        return -1
    max_num = max(arr[:last_i])
    #find the most right less
    for i in range(n-1, last_i-1, -1):
        num = arr[i]
        if(num<max_num):
            return i

    return 0


arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print(arr)
arr.sort()
ans = (find_left(arr), find_right(arr))
print(ans)
print(len(arr))