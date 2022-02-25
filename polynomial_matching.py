import numpy as np

class polyCoeff:
    def __init__(self, src, tgt) -> None:
        '''The class of polynomial matching coefficient.'''
        self.src = src
        self.target = tgt
        self.M = self.match()

    def to_npy(self):
        '''Save the matrix to .npy file'''

    def read_npy(self):
        '''Read .npy file'''

    def match(self):
        '''Given source colors and destination colors, calculate and return the coefficient matrix'''
        h = np.array()

    def transform(self, img):
        '''Given source image and polynomial matching coefficient, return the transformed image.'''
        pass

ColorChecker2005 = np.array([[107,82,70],
[184,146,129],
[101,122,153],
[95,107,69],
[128,127,173],
[129,188,171],
[201,123,56],
[77,92,166],
[174,83,97],
[86,61,104],
[167,188,75],
[213,160,55],
[49,65,143],
[99,148,80],
[155,52,59],
[227,197,52],
[169,85,147],
[61,135,167],
[245,245,242],
[200,201,201],
[160,161,162],
[120,120,121],
[84,85,86],
[52,53,54]])