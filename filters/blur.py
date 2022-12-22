import cv2
import imghdr
import os

import logger


def blur(img, intensity):
    """
        Floute l'image avec une intensité
        :param img: Une image
        :param intensity : un entier qui représente l'intensité
        :return: Une image floue
    """

    if (intensity % 2) == 0:
        print("Parameters entered incorrect")
    elif intensity < 0:
        print("Parameters entered incorrect")
    else:
        img_resul = cv2.GaussianBlur(img, (intensity, intensity), 3)
        logger.log("application du blur")
        return img_resul
