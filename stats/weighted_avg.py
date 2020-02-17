import numpy as np
n = int(input())
x = np.array(map(int, input().split()))
y = np.array(map(int, input().split()))
print(np.average(x, y))