import cv2
import numpy as np

def line_energy(image):
    # Implement line energy (i.e. image intensity)
    return image

def edge_energy(image):
    # Implement edge energy (i.e. gradient magnitude)
    gx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    edge = -np.sqrt(gx ** 2 + gy ** 2)
    return edge

def term_energy(image):
    # Implement term energy (i.e. curvature)
    gx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    gxx = cv2.Sobel(gx, cv2.CV_64F, 1, 0, ksize=3)
    gyy = cv2.Sobel(gy, cv2.CV_64F, 0, 1, ksize=3)
    gxy = cv2.Sobel(gx, cv2.CV_64F, 0, 1, ksize=3)

    # Add a small epsilon to avoid division by zero or near-zero values
    epsilon = 1e-5
    term = (gxx * gy ** 2 - 2 * gxy * gx * gy + gyy * gx ** 2) / (gx ** 2 + gy ** 2 + epsilon) ** 1.5

    return term

def external_energy(image, w_line, w_edge, w_term):
    # Implement external energy
    # Combine these three separate energy together times corresponding weights.
    e = w_line * line_energy(image) + w_edge * edge_energy(image) + w_term * term_energy(image)
    e_normalized = cv2.normalize(e, None, 0, 1, cv2.NORM_MINMAX, dtype=cv2.CV_64F)
    return e_normalized