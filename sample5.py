a, b, c = map(int, input().split())
if a > b or a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)
