ans = 0;
while True:
    num = int(input())
    if num == -1:
        break
    ans = ans*10 + num
    print(ans)