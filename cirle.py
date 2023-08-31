import cv2
import numpy as np

img = cv2.imread("C:\\Users\\nageswararao\\Pictures\\download (4).jpeg")
center = (200, 200)
radius = 50
color = (0, 255, 0) 
thickness = 2
cv2.circle(img, center, radius, color, thickness)
x = center[0] - radius
y = center[1] - radius
width = height = 2 * radius
roi = img[y:y+height, x:x+width]
cv2.imshow('Image with Circle', img)
cv2.imshow('Circle ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
