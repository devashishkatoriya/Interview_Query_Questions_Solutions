
"""
This question was asked by: Intuit
Given a dictionary with weights, write a function that returns a key at random with a probability proportional to the weights.

weights = {'A': 1, 'B': 2}
random_key(weights) -> return A 33.3%, B 66.6%

weights = {'A': 1, 'B': 1}
random_key(weights) -> return A 50%, B 50%

"""

import random

def random_key(weights):
    """
    Function that returns a key at random with a probability proportional to the weights
    """
    list1 = []

    for key in weights:
        for _ in range (0, weights[key]):
            list1.append(str(key))
    n = len(list1)
    #print(list1)

    return list1[random.randint(0, n-1)]


weights = {'A': 1, 'B': 1, 'C': 5}

print('Given weights:', weights)

count = dict()
for key in weights:
    count[key] = 0

n_iter = 100000
for i in range(0, n_iter):
    key = random_key(weights)
    count[key] = count[key] + 1

print('Resulted output:', count)
print('Total:', n_iter)
print('Ratios:-')

for key in weights:
    print(key, count[key]/n_iter)