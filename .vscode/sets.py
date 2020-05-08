from __future__ import division

def average(array):
    s = sum(set(arr))
    return s/len(set(arr))


if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    result = average(arr)
    print(result)
