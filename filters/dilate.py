import cv2
import numpy as np
import logger

def dilate(img, intensity):
    """
    Applique un filtre de dilatation à l'image
    :param img: Une image
    :param intensity: Un entier qui représente l'intensité
    :return: Une image dilatée
    """

    oui = np.ones((intensity, intensity), np.uint8)

    img_dilation = cv2.dilate(img, oui, 1)

    logger.log("application du dilate")
    return img_dilation
