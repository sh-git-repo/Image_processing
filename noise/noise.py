'''
NAME:
    noise.py

DESCRIPTION:
    Implementation for various noise models.

CLASSES:
    Noise(img_path, noise_probability=0.1)
    -----------------------------------------------------------
        Basic class for noise models.

        CONSTRUCTOR ARGUMENTS
        img_path -- The path to the image file.

        noise_probability -- The chance that a given pixel will
        contain noise, value ranges from 0 to 1 inclusive.

        METHODS
        add_noise(self) -- 
            abstract method.
    -----------------------------------------------------------

    SnPNoise(img_path, noise_probability)
    ----------------------------------------------------------------------------
        Models salt and pepper noise.

        CONSTRCUTOR ARGUMENTS
        see help(Noise)

        METHODS
            Returns an image with added noise, the noise is randomly added based
            on the noise probability, distinction between salt and pepper is
            equiprobable.
    ----------------------------------------------------------------------------
'''
from utilities.numpill import PillMatrix
from utilities.matrix_utilities import choose_between

class Noise():
    '''
    Base class for all noise models.
    '''
    def __init__(self, img_path, noise_probability=0.1):
        self.img_path = img_path
        self.img = PillMatrix(self.img_path).np_matrix()
        self.noise_probability = noise_probability

    def add_noise(self):
        ''' abstract method. '''
        raise NotImplementedError(" Override method. ")

class SnPNoise(Noise):
    '''
    Models salt and pepper noise.

    CONSTRCUTOR ARGUMENTS
    see help(Noise)
    '''
    def add_noise(self):
        '''
        Returns an image with added noise, the noise is randomly added based
        on the noise probability, distinction between salt and pepper is
        equiprobable.
        '''
        for row_pos in range(self.img.shape[0]):
            for col_pos in range(self.img.shape[1]):
                pixel = self.img[row_pos, col_pos]
                self.img[row_pos, col_pos] = choose_between(
                    (pixel,),
                    (255, 0),
                    self.noise_probability
                )
        return self.img
