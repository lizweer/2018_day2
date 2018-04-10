def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
        x -- 1D list numbers

    Output:
        idx -- list of indices of the local maxima in x
    """

    idx = []
    plateau = []

    for i in range(len(x)):

        if i != len(x) - 1 and x[i] == x[i+1]:
            plateau.append(i)
            plateau.append(i+1)
        if i == len(x) - 1:
            if x[i-1] < x[i]:
                idx.append(i)
        elif i == 0:
            if x[i+1] < x[i]:
                idx.append(i)
        # `i` is a local maximum if the signal decreases before and after it
        elif x[i-1] < x[i] and x[i+1] < x[i]:
            idx.append(i)

    print(plateau)
    if plateau != []:
        begin = plateau[0]
        end = plateau[-1]
        if end == len(x) - 1:
            if x[begin-1] < x[begin]:
                idx = idx + plateau
        elif begin == 0:
            if x[end+1] < x[end]:
                idx = idx + plateau
        # `i` is a local maximum if the signal decreases before and after it
        elif x[begin-1] < x[begin] and x[end+1] < x[end]:
            idx = idx + plateau
        idx.sort()
    return idx
