def insert_sort(i, j, arr, brr):
    # j - unsorted element
    boo = True
    while j > i and arr[j] < arr[j-1]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        boo = boo and (arr[j] == brr[j])
        j -= 1
    if not boo:
        return False
    for k in range(i, j+1):
        if arr[i] != brr[i]:
            return False
    return True

def sort(arr):
    for i in range(1, len(arr)):
        while i>0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1


def solve(arr: list):
    brr = arr.copy()
    sort(brr)
    ans = []
    start = -1
    end = -1
    for i in range(len(arr)):
        if arr[i] == brr[i]:
            continue
        start = i
        for j in range(i+1, len(arr)):
            if insert_sort(i, j, arr, brr):
                end = j
                ans.append((start, end))
                break
    return ans


def main():
    arr = [1, 2, 3, 6, 5, 7, 8, 9, 11, 10, 12, 13, 14]
    print(arr)
    print(list(sorted(arr)))
    print(solve(arr))


if __name__ == '__main__':
    main()
