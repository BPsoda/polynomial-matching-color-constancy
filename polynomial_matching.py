import numpy as np
from sklearn.linear_model import LinearRegression

class polyCoeff:
    def __init__(self) -> None:
        self.M = np.zeros([11, 3])

    def __init__(self, src, tgt) -> None:
        '''The class of polynomial matching coefficient.'''
        source = src.astype(np.float64)
        target = tgt.astype(np.float64)
        self.M = self.match(source, target)

    def to_npy(self, file_path):
        '''Save the matrix to .npy file'''
        with open(file_path, 'wb') as f:
            np.save(f, self.M)

    def read_npy(self, file_path):
        '''Read .npy file'''
        with open(file_path, 'rb') as f:
            self.M = np.load(f)

    def match(self, src, tgt):
        '''Given source colors and destination colors, calculate and return the coefficient matrix'''
        #  [r g b rg rb gb r2 g2 b2 rgb 1].
        h = np.array([src[:,0], src[:,1], src[:,2], src[:,0]*src[:,1], src[:,0]*src[:,2], src[:,1]*src[:,2],
        src[:,0]*src[:,0], src[:,1]*src[:,1], src[:,2]*src[:,2], src[:,0]*src[:,1]*src[:,2], np.ones(np.shape(src[:,0]))]).T
        regr = LinearRegression(fit_intercept=False).fit(h, tgt)
        return regr.coef_


    def transform(self, image):
        '''Given source image and polynomial matching coefficient, return the transformed image.'''
        img = image.astype(np.float64)
        h_img = np.array([img[:,:,0], img[:,:,1], img[:,:,2], img[:,:,0]*img[:,:,1], img[:,:,0]*img[:,:,2], img[:,:,1]*img[:,:,2],
        img[:,:,0]*img[:,:,0], img[:,:,1]*img[:,:,1], img[:,:,2]*img[:,:,2], img[:,:,0]*img[:,:,1]*img[:,:,2], np.ones(np.shape(img[:,:,0]))]).T
        rtn = np.matmul(h_img, self.M.T)
        rtn[rtn>255] = 255
        rtn[rtn<0] = 0
        return rtn.astype(np.uint8).swapaxes(0,1)
       
# 18 19 20 21 22 23
# 12 13 14 15 16 17
# 6  7  8  9  10 11
# 0  1  2  3  4  5
ColorChecker2005_Adobe = np.array([[245,245,242],
[200,201,201],
[160,161,162],
[120,120,121],
[84,85,86],
[52,53,54],
[49,65,143],
[99,148,80],
[155,52,59],
[227,197,52],
[169,85,147],
[61,135,167],
[201,123,56],
[77,92,166],
[174,83,97],
[86,61,104],
[167,188,75],
[213,160,55],
[107,82,70],
[184,146,129],
[101,122,153],
[95,107,69],
[128,127,173],
[129,188,171]], dtype=np.float64)

ColorChecker2005_sRGB = np.array([
    [245,245,243],
    [200,202,202],
    [161,163,163],
    [121,121,122],
    [82,84,86],
    [49,49,51],
    [35,63,147],
    [67,149,74],
    [180,49,57],
    [238,198,20],
    [193,84,151],
    [0,136,170],
    [224,124,47],
    [68,91,170],
    [198,82,97],
    [94,58,106],
    [159,189,63],
    [230,162,39],
    [116,81,67],
    [199,147,129],
    [91,122,156],
    [90,108,64],
    [130,128,176],
    [92,190,172]
])