from maxima import *
import numpy as np

def test_find_maxima():
    works = True
    x = [0, 1, 2, 1, 2, 1, 0]
    if find_maxima(x) != [2,4]:
        works = False

    x = [-i**2 for i in range(-3, 4)]
    if find_maxima(x) != [3]:
        works = False

    x = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    if find_maxima(x) != [16,78]:
        works = False

    return works
