while True:
    n = int(input())
    ll = list(map(int, input().split()))

    ans = [0]*n
    index = n/2

    ans[index] = ll[0]

    for i in range(1, int(n/2)+1, 2):
        ans[index-i] = ll[i]
        ans[index+i] = ll[i+1]

    print(ans)