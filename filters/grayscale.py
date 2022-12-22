import cv2
import imghdr
import os
import logger

def grayscale(img):
    """
        Applique un filtre de black&white à l'image
        :param img: Une image
        :return: Une image en noir&blanc
        """

    img_src = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    logger.log("application du grayscale")
    return img_src
