# Lib: OpenCV, Pillow, Tesseract

import cv2
import numpy as np
from PIL import Image
import pytesseract
from collections import Counter

# Function to load an image from a file
def load_image(image_path):
    """
    Loads an image from the specified file path and returns it as a NumPy array.
    """
    return cv2.imread(image_path)

# Function to convert an image to grayscale
def convert_to_grayscale(image):
    """
    Converts the given image to grayscale.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Function to detect edges in an image using Canny edge detection
def detect_edges(image, threshold1=100, threshold2=200):
    """
    Detects edges in an image using the Canny edge detection algorithm.
    """
    gray_image = convert_to_grayscale(image)
    edges = cv2.Canny(gray_image, threshold1, threshold2)
    return edges

# Function to extract text from an image using Tesseract OCR
def extract_text_from_image(image_path):
    """
    Extracts text from an image using Tesseract OCR.
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# Function to get the dominant color in an image
def get_dominant_color(image, k=1):
    """
    Returns the dominant color of the image using K-means clustering.
    `k` specifies the number of dominant colors to return.
    """
    pixels = np.float32(image.reshape(-1, 3))
    
    # Perform K-means clustering to find the dominant color
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, palette = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    dominant_color = palette[np.argmax(Counter(labels.flatten()))]
    return dominant_color

# Function to detect faces in an image using Haar cascades
def detect_faces(image, face_cascade_path='haarcascade_frontalface_default.xml'):
    """
    Detects faces in an image using Haar cascades and returns the coordinates of detected faces.
    """
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + face_cascade_path)
    gray_image = convert_to_grayscale(image)
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

# Function to draw rectangles around detected faces
def draw_faces(image, faces):
    """
    Draws rectangles around the detected faces on the image.
    """
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return image

# Function to calculate the histogram of an image
def calculate_histogram(image):
    """
    Calculates and returns the histogram of the image.
    """
    if len(image.shape) == 2:  # Grayscale image
        histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    else:
        histogram = []
        for i in range(3):  # BGR channels
            hist = cv2.calcHist([image], [i], None, [256], [0, 256])
            histogram.append(hist)
    return histogram

# Function to resize an image
def resize_image(image, width=None, height=None):
    """
    Resizes the image to the specified width or height while maintaining the aspect ratio.
    """
    if width is None and height is None:
        return image
    h, w = image.shape[:2]
    if width is None:
        ratio = height / float(h)
        new_size = (int(w * ratio), height)
    else:
        ratio = width / float(w)
        new_size = (width, int(h * ratio))
    return cv2.resize(image, new_size)

# Function to blur an image
def blur_image(image, kernel_size=(5, 5)):
    """
    Applies a Gaussian blur to the image with the specified kernel size.
    """
    return cv2.GaussianBlur(image, kernel_size, 0)

# Function to detect contours in an image
def detect_contours(image):
    """
    Detects contours in the image and returns them.
    """
    gray_image = convert_to_grayscale(image)
    edges = detect_edges(gray_image)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

# Function to draw contours on an image
def draw_contours(image, contours):
    """
    Draws detected contours on the image.
    """
    return cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Function to calculate the aspect ratio of an image
def calculate_aspect_ratio(image):
    """
    Calculates the aspect ratio of the image (width/height).
    """
    h, w = image.shape[:2]
    return w / h

