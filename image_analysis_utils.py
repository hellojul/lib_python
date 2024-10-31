# Lib: OpenCV, Pillow, Tesseract

import cv2
import numpy as np
from PIL import Image
import pytesseract
from collections import Counter

# Fonction pour charger une image à partir d'un fichier
def load_image(image_path):
    """
    Charge une image à partir du chemin de fichier spécifié et la retourne sous forme de tableau NumPy.
    """
    return cv2.imread(image_path)

# Fonction pour convertir une image en niveaux de gris
def convert_to_grayscale(image):
    """
    Convertit l'image donnée en niveaux de gris.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Fonction pour détecter les contours dans une image en utilisant la détection de contours Canny
def detect_edges(image, threshold1=100, threshold2=200):
    """
    Détecte les contours dans une image en utilisant l'algorithme de détection de contours Canny.
    """
    gray_image = convert_to_grayscale(image)
    edges = cv2.Canny(gray_image, threshold1, threshold2)
    return edges

# Fonction pour extraire du texte d'une image à l'aide de Tesseract OCR
def extract_text_from_image(image_path):
    """
    Extrait du texte d'une image à l'aide de Tesseract OCR.
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# Fonction pour obtenir la couleur dominante dans une image
def get_dominant_color(image, k=1):
    """
    Retourne la couleur dominante de l'image en utilisant le clustering K-means.
    `k` spécifie le nombre de couleurs dominantes à retourner.
    """
    pixels = np.float32(image.reshape(-1, 3))
    
    # Effectuer le clustering K-means pour trouver la couleur dominante
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, palette = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    dominant_color = palette[np.argmax(Counter(labels.flatten()))]
    return dominant_color

# Fonction pour détecter les visages dans une image en utilisant des cascades de Haar
def detect_faces(image, face_cascade_path='haarcascade_frontalface_default.xml'):
    """
    Détecte les visages dans une image en utilisant des cascades de Haar et retourne les coordonnées des visages détectés.
    """
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + face_cascade_path)
    gray_image = convert_to_grayscale(image)
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

# Fonction pour dessiner des rectangles autour des visages détectés
def draw_faces(image, faces):
    """
    Dessine des rectangles autour des visages détectés sur l'image.
    """
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return image

# Fonction pour calculer l'histogramme d'une image
def calculate_histogram(image):
    """
    Calcule et retourne l'histogramme de l'image.
    """
    if len(image.shape) == 2:  # Image en niveaux de gris
        histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    else:
        histogram = []
        for i in range(3):  # Canaux BGR
            hist = cv2.calcHist([image], [i], None, [256], [0, 256])
            histogram.append(hist)
    return histogram

# Fonction pour redimensionner une image
def resize_image(image, width=None, height=None):
    """
    Redimensionne l'image à la largeur ou hauteur spécifiée en conservant le rapport d'aspect.
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

# Fonction pour flouter une image
def blur_image(image, kernel_size=(5, 5)):
    """
    Applique un flou gaussien à l'image avec la taille de noyau spécifiée.
    """
    return cv2.GaussianBlur(image, kernel_size, 0)

# Fonction pour détecter les contours dans une image
def detect_contours(image):
    """
    Détecte les contours dans l'image et les retourne.
    """
    gray_image = convert_to_grayscale(image)
    edges = detect_edges(gray_image)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

# Fonction pour dessiner les contours sur une image
def draw_contours(image, contours):
    """
    Dessine les contours détectés sur l'image.
    """
    return cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Fonction pour calculer le rapport d'aspect d'une image
def calculate_aspect_ratio(image):
    """
    Calcule le rapport d'aspect de l'image (largeur/hauteur).
    """
    h, w = image.shape[:2]
    return w / h

