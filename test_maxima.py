from maxima import *
import numpy as np

def test_find_maxima_1():
    x = [0, 1, 2, 1, 2, 1, 0]
    assert find_maxima(x) == [2,4]

def test_find_maxima_2():
    x = [-i**2 for i in range(-3, 4)]
    assert find_maxima(x) == [3]

def test_find_maxima_3():
    x = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    assert find_maxima(x) == [16,78]

def test_find_maxima_4():
    x = [4, 2, 1, 3, 1, 2]
    assert find_maxima(x) == [0,3,5]

def test_find_maxima_5():
    x = [4, 2, 1, 3, 1, 5]
    assert find_maxima(x) == [0,3,5]

def test_find_maxima_6():
    x = [4, 2, 1, 3, 1]
    assert find_maxima(x) == [0,3]
