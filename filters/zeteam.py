import cv2
import imghdr
import os
import logger

def zeteam(img):
    """
        Applique du texte à l'image
        :param img: Une image
        :return: Une image et du texte
        """

    img_src = cv2.putText(img, 'Mr.Yang, Rat_balls, Eloi, Roro', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    logger.log("application du texte")
    return img_src




