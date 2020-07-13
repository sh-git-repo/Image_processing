'''
NAME:
    filters.py

DESCRIPTION:
    Implementations of various image filters.

CLASSES:
    Filter(img_path, window_size=3)
    --------------------------------------------------------
        Base class for all image filters.

        CONSTRUCTOR ARGUMENTS
        img_path -- It is the path to the image file.

        window_size -- It the size of the sliding window in
        which the mid element is the pixel getting filtered.

        METHODS
        filter(self) --
            It is an abstract method.
    --------------------------------------------------------

    MedianFilter(img_path, window_size=3)
    -----------------------------------------------------------------
        Models a median filter.

        CONSTRUCTOR AGUMENTS
        see help(Filter)

        METHODS
        filter(self) -- 
            Returns a filtered matrix, where each value in the matrix
            is replaced by the value found the at the middle of the
            sorted matrix of the given window size.
    -----------------------------------------------------------------
'''
import numpy as np
from utilities.numpill import PillMatrix
from utilities.matrix_utilities import pad_matrix, matrix_median

class Filter():
    '''
    Base class for all image filters.

    CONSTRUCTOR ARGUMENTS
    img_path -- It is the path to the image file.

    window_size -- It the size of the sliding window in
    which the mid element is the pixel getting filtered.
    '''
    def __init__(self, img_path, window_size):
        self.window_size = window_size
        self.img_path = img_path
        self.img = PillMatrix(self.img_path).np_matrix()

    def filter(self):
        ''' It is an abstract method. '''
        raise NotImplementedError(" Must be overridden ")

class MedianFilter(Filter):
    '''
    Models a median filter.

    CONSTRUCTOR AGUMENTS
    see help(Filter)
    '''
    def filter(self):
        '''
        Returns a filtered matrix, where each value in the matrix
        is replaced by the value found the at the middle of the sorted
        matrix of the given window size. 
        '''
        padded_img = pad_matrix(self.img, 0, self.window_size)
        row_start, col_start = 0, 0
        filtered_img = np.zeros(self.img.shape)
        for row_stop in range(self.window_size, padded_img.shape[0]+1):
            for col_stop in range(self.window_size, padded_img.shape[1]+1):
                img_slice = padded_img[row_start:row_stop, col_start:col_stop]
                filtered_img[row_start, col_start] = matrix_median(img_slice)
                col_start += 1
            col_start = 0
            row_start += 1
        return filtered_img
