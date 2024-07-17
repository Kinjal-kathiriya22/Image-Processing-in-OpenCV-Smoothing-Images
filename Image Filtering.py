import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os

# Define the path to the image file
image_path = '/Users/kdmac/Downloads/world.jpg'

# Check if the file exists
if not os.path.exists(image_path):
    raise FileNotFoundError(f"File not found: {image_path}")

# Load the image
img = cv.imread(image_path)
assert img is not None, "file could not be read, check with os.path.exists()"

# Create an averaging kernel
kernel = np.ones((5,5),np.float32)/25

# Apply the averaging filter
dst = cv.filter2D(img, -1, kernel)

# Display images using Matplotlib
plt.subplot(121), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv.cvtColor(dst, cv.COLOR_BGR2RGB)), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
