import sys


def java2Pyth():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        minimum = sys.maxsize

        ar = []
        ar_values = input().split()
        for j in range(n):
            ar.append(int(ar_values[j]))
            if ar[j] >= k:
                rem = ar[j] % k
                minimum = min(minimum, rem)
        if minimum == sys.maxsize:
            print("-1")
        else:
            print(minimum)


java2Pyth()
