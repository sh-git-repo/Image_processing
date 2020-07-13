'''
NAME:
    numpill.py

DESCRIPTION
    Implementations for Pillow to Numpy adapters and vice versa.

CLASSES
    PillMatrix(path, mode='L')
    -------------------------------------------------
        Models an adapter for Pillow to Numpy.

        CONSTRUCTOR ARGUMENTS
        path -- Path to the image file.

        mode -- Mode to convert images into, defaults
        to 'L' for grayscale.

        METHODS
        np_matrix(self)
            Returns a 2D NumpyMatrix. 
    -------------------------------------------------
'''
from PIL import Image
import numpy as np

class PillMatrix():
    '''
    Models a Converter that can convert a pillow image into a numpy matrix.
    '''
    def __init__(self, path, mode='L'):
        self.path = path
        self.image = Image.open(self.path).convert(mode)

    def __str__(self):
        return str(self.image)

    def np_matrix(self):
        ''' Converts a pixel array into a 2D numpy matrix. '''
        shape = self.image.size
        img_array = tuple(self.image.getdata())
        return np.array(img_array).reshape(shape)
