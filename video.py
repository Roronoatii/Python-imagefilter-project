import os
from rich.progress import Progress
import time

import cv2


def video_mk(path, vid):
    """
        Elle découpe la vidéo en frames et les mets dans le dossier videoStorage
        :param path: Chemin de la vidéo
        :param vid: nom de la vidéo
        Renvoie toutes les frames (la liste des frames)
    """
    try:
        os.mkdir('videoStorage')
    except OSError:
        pass
    import cv2

    # read the video and extract info about it
    cap = cv2.VideoCapture(f'{path}{vid}')

    # get total number of frames and generate a list with each 30 th frame
    totalFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    x = [i for i in range(1, totalFrames) if divmod(i, int(10))[1] == 0]
    print("Starting conversion")
    print(f"Converting {vid}...")


    for myFrameNumber in x:
            # set which frame to read
            cap.set(cv2.CAP_PROP_POS_FRAMES, myFrameNumber)
            # read frame
            ret, frame = cap.read()
            # display frame
            cv2.imwrite(f"videoStorage/{vid}%#05d.jpg" % myFrameNumber, frame)

    img_list = os.listdir("videoStorage")
    return img_list
