def solve1(str1,  str2, thresh):
    m = len(str1)
    n = len(str2)
    max_s = thresh
    max_i, max_j = -1, -1
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] != str2[j-1]:
                continue
            dp[i][j] = dp[i-1][j-1]+1
            if dp[i][j] > max_s:
                max_s = dp[i][j]
                max_i, max_j = i-dp[i][j], j-dp[i][j]

    return max_s, max_i, max_j


def main():
    with open('input_1.txt', 'r') as file:
        text_a = file.read()
        text_a.replace('\n', ' ')
    with open('input_2.txt', 'r') as file:
        text_b = file.read()
        text_b.replace('\n', ' ')
    max_s, max_i, max_j = solve1(text_a, text_b, -1)
    print(max_s, max_i, max_j)
    print(text_a[max_i:max_i+max_s])
    print(text_b[max_j:max_j+max_s])


if __name__ == '__main__':
    main()
