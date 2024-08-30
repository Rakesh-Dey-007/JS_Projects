import cv2

# Read the image
image = cv2.imread("Image.jpg")

# Convert the image to grayscale
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Deepen the grayscale color by adjusting contrast and brightness
alpha = 1.5  # Contrast control (1.0-3.0)
beta = 0     # Brightness control (0-100)

deep_grey = cv2.convertScaleAbs(grey, alpha=alpha, beta=beta)

# Invert the deepened grayscale image
invert = cv2.bitwise_not(deep_grey)

# Apply Gaussian blur to the inverted image
blur = cv2.GaussianBlur(invert, (21, 21), 0)

# Invert the blurred image
invertblur = cv2.bitwise_not(blur)

# Create the sketch effect by dividing the deepened grayscale image by the inverted blur image
sketch = cv2.divide(deep_grey, invertblur, scale=256)

# Save the deepened sketch image
cv2.imwrite("deep_sketch.png", sketch)
