import cv2
import imghdr
import os
import logger

def hex_to_bgr(hex):
    color = []
    for i in (1, 3, 5):
        decimal = int(hex[i:i + 2], 16)
        color.append(decimal)
    red = color[0]
    # R G B
    # B G R
    color[0] = color[2]
    color[2] = red

    return tuple(color)


def message(img, message, color):
    """
        Applique du texte à l'image
        :param img: Une image
        :return: Une image et du texte
        """

    img_src = cv2.putText(img, message,
                          (50, 50),
                          cv2.FONT_HERSHEY_SIMPLEX,
                          1,
                          hex_to_bgr(color), 2)
    logger.log("application du texte")
    return img_src
