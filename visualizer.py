import cv2
import numpy as np
from random import randint

def insertion_sort(l):
    for index in range(1, len(l)):
        k = l[index]
        j = index-1
        while j >= 0 and k < l[j]:
            l[j+1] = l[j]
            j-=1
        l[j+1] = k

    return l

arr = [randint(0, 300) for i in range(0, 25)]
img = np.zeros((500, 500, 3), np.uint8)

for i in range(len(arr)):
    img[499:499-arr[i]:-1, i*10:i*10+5] = 255, 255, 255

cv2.imshow('', img)

cv2.waitKey(0)
cv2.destroyAllWindows()