'''
NAME
    matrix_utilities.py

DESCRIPTION
    Implementations for utility functions.

FUNCTIONS
    pad_matrix(matrix, num=0, window_size=3)
    ----------------------------------------------------
        Returns a padded matrix, the padded matrix
        has same number of rows and columns, the padding
        is done in such a manner as to make each element
        of the original matrix accessible as the mid
        element of a window.

        matrix -- The 2D matrix to be padded.

        window_size -- The matrix is padded based
        on the window_size.
    ----------------------------------------------------

    matrix_median(matrix)
    --------------------------------------------------
        Selects the median based on the position
        of sorted values and not on values themselves.

        matrix - It is a 2D NumPy matrix.
    --------------------------------------------------

    probability_array(probability=0.5)
    ---------------------------------------------------------------
        Returns a probability array based on the given probability,
        this array is used to make binary decision.

        probability -- probability of occurence of the first type
        of element in the array.
    ---------------------------------------------------------------

    choose_between(group_one, group_two, gt_probability):
    ---------------------------------------------------------------------------
        Chooses an element between two groups.
        The choice between elements inside their respective groups is equiprobable.

        group_one -- An iterable.

        group_two -- An iterable.

        gt_probability -- It is the probability of selecting group two elements
        over group one.
    ---------------------------------------------------------------------------
'''
import numpy as np

def pad_matrix(matrix, num=0, window_size=3):
    '''
    Returns a padded matrix, the padded matrix
    has same number of rows and columns, the padding
    is done in such a manner as to make each element
    of the original matrix accessible as the mid
    element of a window.

    matrix -- The 2D matrix to be padded.

    window_size -- The matrix is padded based
    on the window_size.
    '''
    rows = (window_size - 1) + matrix.shape[0]
    columns = (window_size - 1) + matrix.shape[1]
    new_matrix = np.full((rows, columns), num)
    row_mid, col_mid = int(window_size/2), int(window_size/2)
    reset_col = col_mid
    for row_pos in range(matrix.shape[0]):
        for col_pos in range(matrix.shape[1]):
            new_matrix[row_mid, col_mid] = matrix[
                row_pos, col_pos
            ]
            col_mid += 1
        row_mid += 1
        col_mid = reset_col
    return new_matrix

def matrix_median(matrix):
    '''
    matrix_median(matrix)

    Selects the median based on position
    of sorted values and not on values themselves.

    matrix - It is a 2D NumPy matrix.
    '''
    mid_ele = int(matrix.shape[0]/2)
    return np.sort(matrix, axis=None)[mid_ele]

def probability_array(probability=0.5):
    '''
    Returns a probability array based on the given probability,
    this array is used to make binary decision.

    probability -- probability of occurence of the first type
    of element in the array.
    '''
    if 0 <= probability <= 1:
        cmp_value = probability * 100
        probabilities = []
        for _ in range(0, 100):
            if cmp_value <= 0:
                probabilities.append(1)
            else:
                probabilities.append(0)
                cmp_value -= 1
        return probabilities
    else:
        raise ValueError(' Only float values between 0 and 1 allowed. ')

def choose_between(group_one, group_two, gt_probability):
    '''
    Chooses an element between two groups.
    The choice between elements inside their respective groups is equiprobable.

    group_one -- An iterable.

    group_two -- An iterable.

    gt_probability -- It is the probability of selecting group two elements
    over group one.
    '''
    probabilities = probability_array(gt_probability)
    index = np.random.randint(0, 99)
    if probabilities[index] == 1:
        return group_one[index%len(group_one)]
    return group_two[index%len(group_two)]
