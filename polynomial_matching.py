import numpy as np
from sklearn.linear_model import LinearRegression

class polyCoeff:
    def __init__(self) -> None:
        self.M = np.zeros([11, 3])

    def __init__(self, src, tgt) -> None:
        '''The class of polynomial matching coefficient.'''
        self.src = src.astype(np.float64)
        self.target = tgt.astype(np.float64)
        self.M = self.match()

    def to_npy(self, file_path):
        '''Save the matrix to .npy file'''
        with open(file_path, 'wb') as f:
            np.save(f, self.M)

    def read_npy(self, file_path):
        '''Read .npy file'''
        with open(file_path, 'rb') as f:
            self.M = np.load(f)

    def match(self):
        '''Given source colors and destination colors, calculate and return the coefficient matrix'''
        #  [r g b rg rb gb r2 g2 b2 rgb 1].
        h = np.array([self.src[:,0], self.src[:,1], self.src[:,2], self.src[:,0]*self.src[:,1], self.src[:,0]*self.src[:,2], self.src[:,1]*self.src[:,2],
        self.src[:,0]*self.src[:,0], self.src[:,1]*self.src[:,1], self.src[:,2]*self.src[:,2], self.src[:,0]*self.src[:,1]*self.src[:,3], np.ones(np.shape(self.src[:,0]))])
        regr = LinearRegression(fit_intercept=False).fit(h, self.target)
        return regr.coef_


    def transform(self, img):
        '''Given source image and polynomial matching coefficient, return the transformed image.'''
        h_img = np.array([img[:,0], img[:,1], img[:,2], img[:,0]*img[:,1], img[:,0]*img[:,2], img[:,1]*img[:,2],
        img[:,0]*img[:,0], img[:,1]*img[:,1], img[:,2]*img[:,2], img[:,0]*img[:,1]*img[:,3], np.ones(np.shape(img[:,0]))])
        return np.matmul(h_img, self.M)
       

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
[52,53,54]], dtype=np.float64)