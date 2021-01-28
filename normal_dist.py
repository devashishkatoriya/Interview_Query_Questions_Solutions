"""
Given a percentile threshold and N samples, write a function to simulate a truncated normal distribution.

Example:

Input

threshold = 0.75
n = 6
truncated_dist(n, percentile_threshold)
Output

# with mean of 2 and std deviation of 1
output = [2, 1.1, 2.2, 3, 1.5, 1.3]
"""

import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

res = []

for i in range(1000):
    n = np.random.normal()
    if n < st.norm.cdf(0.75):
        res.append(n)

plt.hist(res)
plt.show()