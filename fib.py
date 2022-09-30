def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


n = int(input())
sum = 0

print("--------------")

for i in range(1, n+1):
    a = fib(i)
    print(a)

    sum += a

print(sum)
