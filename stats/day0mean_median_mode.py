# finding mean, median,mode

import numpy as np
from scipy import stats

N = int(input('enter no. of element'))
X = list(map(int, input('enter list elements:').split()))
print(np.mean(X))
print(np.median(X))
print(int(stats.mode(X)[0]))
