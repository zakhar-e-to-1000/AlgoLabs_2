def lps_const(string):
    lis = [0] * len(string)
    i, j = 1, 0
    while i != len(string):
        if string[j] == string[i]:
            j += 1
            lis[i] = j
            i += 1
        else:
            if j == 0:
                lis[i] = 0
                i += 1
            else:
                j = lis[j-1]
    return lis


def solve(key, word):
    lis = lps_const(key)
    i, j = 0, 0
    ans = []
    while i != len(word):
        if word[i] == key[j]:
            i += 1
            j += 1
            if j == len(key):
                ans.append(i-len(key))
                j = lis[len(key)-1]
        else:
            if j == 0:
                i += 1
            else:
                j = lis[j-1]
    return ans


def main():
    key = 'aaba'
    word = 'aabaacaadaabaaba'
    print(solve(key, word))


if __name__ == "__main__":
    main()
