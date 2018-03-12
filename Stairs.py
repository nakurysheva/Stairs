n = int(input())
last = tuple(range(1, n + 1))
leng = int(len(last))


def format(last):
    for i in last:
        print(last[i - 1], end="")


while n != 0:
    format(last[0:leng-(n-1)])
    print()
    n -= 1
