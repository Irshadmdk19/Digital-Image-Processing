import cv2
import numpy as np
import matplotlib.pyplot as plt

#Loading an image
img = cv2.imread('/CI2/Basic operations/road.jpg')

#Displaying the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Get the size of the image
height, width = img.shape[:2]
# Print the size
print("Image width:", width)
print("Image height:", height)

#Converting image to grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Applying filter
blur = cv2.GaussianBlur(gray, (5, 5), 0)
#This applies a Gaussian blur filter to the grayscale image. The (5, 5) parameter specifies the kernel size of the filter, and 0 specifies the standard deviation.

cv2.imshow('Image', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Threshold the image
ret, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY) 
#This applies a binary threshold to the blurred image, creating a black-and-white image where all pixels above a certain intensity value are white and all others are black.
# cv2.imshow('Image', ret)
cv2.imshow('Image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Get the image dimensions
rows, cols = img.shape[:2]

# Rotation
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
rotated = cv2.warpAffine(img, M, (cols, rows))

# Scaling
scaled = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Translation
M = np.float32([[1, 0, 50], [0, 1, 50]])
translated = cv2.warpAffine(img, M, (cols, rows))

# Display the original and transformed images
cv2.imshow('Original', img)
cv2.imshow('Rotated', rotated)
cv2.imshow('Scaled', scaled)
cv2.imshow('Translated', translated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Apply Canny edge detection
edges = cv2.Canny(gray, 100, 200)

# Display the edges
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()



# Resize the image to a specific width and height
resized_img = cv2.resize(img, (900, 400))

# Display the resized image
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Flip the image horizontally
flipped_img = cv2.flip(img, 1)

# Display the flipped image
cv2.imshow('Flipped Image', flipped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Flip the image vertically
flipped_img = cv2.flip(img,0)
# Display the flipped image
cv2.imshow('Flipped Image', flipped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

