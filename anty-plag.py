def solve1(str1: str,  str2: str, thresh: int):
    m = len(str1)
    n = len(str2)
    ans = []
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(0, m+1):
        for j in range(0, n+1):
            if (i >= m or j >= n):
                if dp[i][j] > thresh:
                    ans.append((dp[i][j], i-dp[i][j], j-dp[i][j]))
                continue
            if str1[i].capitalize() == str2[j].capitalize():  # next character validation
                dp[i+1][j+1] = 1+dp[i][j]
            elif dp[i][j] > thresh:
                ans.append((dp[i][j], i-dp[i][j], j-dp[i][j]))
    return ans


def sort_sols(sols):
    boo = True
    while boo:
        boo = False
        for i in range(len(sols)-1):
            if sols[i][0] < sols[i+1][0]:
                boo = True
                sols[i], sols[i+1] = sols[i+1], sols[i]
    return sols


def main():
    with open('input_1.txt', 'r') as file:
        text_a = file.read()
        text_a.replace('\n', ' ')
    with open('input_2.txt', 'r') as file:
        text_b = file.read()
        text_b.replace('\n', ' ')
    for sol in sort_sols(solve1(text_a, text_b, 10)):
        max_s, max_i, max_j = sol
        print(max_s, max_i, max_j)
        print(text_a[max_i:max_i+max_s])
        print(text_b[max_j:max_j+max_s])


if __name__ == '__main__':
    main()
