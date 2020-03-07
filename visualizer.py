import cv2
import numpy as np
from random import randint, shuffle

def isSorted(l):
    previous = l[0]
    for i in range(1, len(l)):
        if l[i] < previous:
            return False
        previous = l[i]
    return True

def insertion_sort(l):
    for index in range(1, len(l)):
        k = l[index]
        j = index-1
        while j >= 0 and k < l[j]:
            l[j+1] = l[j]
            j-=1
            yield l
        l[j+1] = k

def selection_sort(l):
    for i in range(len(l)):  
        min_ind = i 
        for j in range(i+1, len(l)):
            if l[j] < l[min_ind]:
                min_ind = j
        l[i], l[min_ind] = l[min_ind], l[i]
        yield l

def bogo_sort(l):
    while not isSorted(l):
        shuffle(l)
        yield l 
    yield l 

#generate array, window height and width and the empty canvas for drawing with an
#empty copy to reset it every frame
arr = [randint(0, 500) for i in range(0, 30)]
HEIGHT = max(arr)+1
WIDTH = len(arr) * 10
img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
reset = img.copy()

steps = insertion_sort(arr)

for step in steps:
    for i in range(len(arr)):
        img[HEIGHT:HEIGHT-arr[i]:-1, i*10:i*10+5] = 255, 255, 255
        cv2.imshow('', img)
    cv2.waitKey(10)
    img = reset.copy()

cv2.waitKey(0)
cv2.destroyAllWindows()