import numpy as np
import cv2
img = cv2.imread('D:\PYcode\images\image.jpg',0)  # 路径为绝对路径
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()