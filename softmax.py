import math
import numpy as np


def compute_softmax(array):
    denominator = 0
    for element in array:
        denominator += math.exp(element)

    print("denominator = ", denominator)

    result = []
    for element in array:
        result.append(math.exp(element) / denominator)

    return result


array = [1.0, 2.0, 3.0]
print("Softmax = ", compute_softmax(array))
print("Softmax = ", np.around(compute_softmax(array), 3))