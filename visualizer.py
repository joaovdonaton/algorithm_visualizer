import cv2
import numpy as np
from random import randint

arr = [randint(0, 500) for i in range(0, 100)]
HEIGHT = max(arr)+1
WIDTH = len(arr) * 10
img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
reset = img.copy()

for index in range(1, len(arr)):
    k = arr[index]
    j = index-1
    while j >= 0 and k < arr[j]:
        arr[j+1] = arr[j]
        j-=1
        for i in range(len(arr)):
            img[HEIGHT:HEIGHT-arr[i]:-1, i*10:i*10+5] = 255, 255, 255
            cv2.imshow('', img)
        cv2.waitKey(1)
        img = reset.copy()
    arr[j+1] = k

cv2.waitKey(0)
cv2.destroyAllWindows()