from math import gcd

def bsearch_right(left, right, width, height, need):
    right+=1
    while left!=right:
        mid = (left+right)//2
        if num_fits(mid, width, height) < need:
            left = mid+1
        else:
            right = mid
    return left


def num_fits(side, width, height):
    rows = side//height
    columns = side//width
    return rows*columns

def interval(number, width, height):
    #scale down size to speed up
    #improve by adding bi_search
    g = gcd(width, height)
    width //= g
    height //= g
    prev = max(width, height)
    nev = prev*2
    while True:
        if num_fits(nev, width, height)>=number:
            return (prev, nev)
        prev = nev
        nev *= 2

def solve(num, wid, hei):
    left, right = interval(num, wid, hei)
    return bsearch_right(left, right, wid, hei, num)

def main():
    num, wid, hei = 2, 1000000000, 999999999
    solve(num, wid, hei)

if __name__=='__main__':
    main()