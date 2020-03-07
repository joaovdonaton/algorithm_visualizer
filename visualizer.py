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
            yield l
        l[j+1] = k

#generate array, window height and width and the empty canvas for drawing with an
#empty copy to reset it every frame
arr = [randint(0, 500) for i in range(0, 50)]
HEIGHT = max(arr)+1
WIDTH = len(arr) * 10
img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
reset = img.copy()

for step in insertion_sort(arr):
    for i in range(len(arr)):
        img[HEIGHT:HEIGHT-arr[i]:-1, i*10:i*10+5] = 255, 255, 255
        cv2.imshow('', img)
    cv2.waitKey(1)
    img = reset.copy()

cv2.waitKey(0)
cv2.destroyAllWindows()