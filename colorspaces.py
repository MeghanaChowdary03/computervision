import cv2
image_path = 'C:\\Users\\nageswararao\\Pictures\\download.jpeg'
original_image = cv2.imread(image_path)
rgb_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)
cv2.imshow('Original Image', original_image)
cv2.imshow('RGB Image', rgb_image)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
