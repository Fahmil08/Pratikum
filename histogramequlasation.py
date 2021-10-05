import cv2
import numpy as np

citra = cv2.imread('gambar a .jpg', 0)

ekual = cv2.equalizeHist(citra)
hasil = np.hstack((citra, ekual))

cv2.imshow('contoh hasil equlasation',hasil)
cv2.waitKey(0)