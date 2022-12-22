import imghdr
import os
import sys

import cv2
from video import video_mk

from filters.blur import blur
from filters.grayscale import grayscale
from filters.dilate import dilate

from configparser import ConfigParser

import time

from rich.progress import Progress

filters_list = []

args = sys.argv

video = False
Conf = False
bool_visible = False

# Conditions pour les arguments qui sont rentrés dans l'invite de commande

for iteration, arg in enumerate(args):

    if arg == "--input_dir":
        input_path = args[iteration + 1]
    elif arg == "--conf-file":
        Conf = True
        conf_file = args[iteration + 1]

    if arg == "--output_dir":
        output_path = args[iteration + 1]
    elif arg == "--conf-file":
        Conf = True
        conf_file = args[iteration + 1]

    if arg == "--video":
        video = True
        video_name = args[iteration + 1]
    elif arg == "--conf-file":
        Conf = True
        conf_file = args[iteration + 1]

    if arg == "--filters":
        list = args[iteration + 1].split("|")
        list2 = []
        for v in list:
            a = v.split(":")

            filter = {
                "name": a[0]
            }
            if len(a) == 2:
                filter["intensity"] = a[1]
            filters_list.append(filter)
    elif arg == "--conf-file":
        Conf = True
        conf_file = args[iteration + 1]

    if arg == "--bling-bling":
        bool_visible = True

# Fichier ini

if Conf:
    config = ConfigParser()

    config.read('options.ini')

    input_path = config.get('general', 'input_dir')
    output_path = config.get('general', 'output_dir')
    log_file = config.get('general', 'log_file')
    filters = config.get('filters', 'filters')
    video = config.getboolean('video', 'video')
    video_name = config.get('video', 'video_name')

    list = filters.split("|")
    list2 = []
    for v in list:
        a = v.split(":")

        filter = {
            "name": a[0]
        }
        if len(a) == 2:
            filter["intensity"] = a[1]
        filters_list.append(filter)

img_list = os.listdir(input_path)

if video:
    img_list = video_mk(input_path, video_name)

# Permet de gérer les erreurs et d'appliquer les filtres

filter_loading = ""
filter_loading2 = ""

with Progress() as progress:
    task1 = progress.add_task("[red]Loading...", total=len(img_list), visible = bool_visible)


    for img in img_list:
        for iteration, arg in enumerate(args):
            if arg == "--bling-bling":
                progress.advance(task1)
                time.sleep(0.1)
        if video:
            input_path = "videoStorage/"
            img_src = cv2.imread(f'{input_path}{img}')

        else:
            img_src = cv2.imread(f'{input_path}{img}')

        if not os.path.isfile(f'{input_path}{img}'):
            print("(File not found")

        elif imghdr.what(f'{input_path}{img}') != 'jpeg' and imghdr.what(f'{input_path}{img}') != 'png':
            print("File isn't in the right format")

        else:

            for iterations in list:
                a = iterations.split(":")

                filter = {
                    "name": a[0]
                }
                if len(a) == 2:
                    filter["intensity"] = a[1]
                filters_list.append(filter)

                if filter["name"] == 'dilate':
                    img_src = dilate(img_src, int(filter["intensity"]))

                elif filter["name"] == 'blur':
                    img_src = blur(img_src, int(filter["intensity"]))

                elif iterations == 'grayscale':
                    img_src = grayscale(img_src)

            cv2.imwrite(f'{output_path}{img}', img_src)
        progress.console.print(img)



