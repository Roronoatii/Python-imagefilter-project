import imghdr
import os
import sys
import inspect
import cv2
from video import video_mk
from os import listdir
from os.path import isfile, join
from filters.blur import blur
from filters.grayscale import grayscale
from filters.dilate import dilate
from filters.zeteam import zeteam
from filters import message

from configparser import ConfigParser
from rich.progress import Progress
import time

filters_list = []

args = sys.argv

video = False
Conf = False
listing_filters = False
bool_visible = False

for iteration, arg in enumerate(args):
    if arg == "--list_filters":
        listing_filters = True
    if arg == "--conf_file":
        Conf = True
        conf_path = args[iteration + 1]
    if arg == "--input_dir":
        input_path = args[iteration + 1]
    if arg == "--output_dir":
        output_path = args[iteration + 1]
    if arg == "--video":
        video = True
        video_name = args[iteration + 1]
    if arg == "--filters":
        listing = args[iteration + 1].split("|")
        for v in listing:
            a = v.split(":")

            filter = {
                "name": a[0]
            }
            if len(a) == 3:
                filter["message"] = a[1]
                filter["color"] = a[2]
            elif len(a) == 2:
                filter["intensity"] = a[1]
            filters_list.append(filter)
    if arg == "--bling-bling":
        bool_visible = True

if Conf:
    config = ConfigParser()

    config.read(f'{conf_path}')

    input_path = config.get('general', 'input_dir')
    output_path = config.get('general', 'output_dir')
    log_file = config.get('general', 'log_file')
    bool_visible = config.getboolean('general', 'bling-bling')
    filters = config.get('filters', 'filters')
    video = config.getboolean('video', 'video')
    video_name = config.get('video', 'video_name')
    listing_filters = config.getboolean('filters', 'filter_list')

    listing = filters.split("|")
    for v in listing:
        a = v.split(":")

        filter = {
            "name": a[0]
        }
        if len(a) == 2:
            filter["intensity"] = a[1]
        filters_list.append(filter)

    for iteration, arg in enumerate(args):
        if arg == "--list_filters":
            listing_filters = True
        if arg == "--input_dir":
            input_path = args[iteration + 1]
        if arg == "--output_dir":
            output_path = args[iteration + 1]
        if arg == "--video":
            video = True
            video_name = args[iteration + 1]
        if arg == "--filters":
            listing = args[iteration + 1].split("|")
            list2 = []
            for v in listing:
                a = v.split(":")

                filter = {
                    "name": a[0]
                }
                if len(a) == 3:
                    filter["message"] = a[1]
                    filter["color"] = a[2]
                elif len(a) == 2:
                    filter["intensity"] = a[1]
                filters_list.append(filter)
        if arg == "--bling-bling":
            bool_visible = True

if listing_filters:
    onlyfiles = []
    for i in os.listdir("filters/"):
        clean = inspect.getmodulename(f"./filters/{i}")
        onlyfiles.append(clean)
        """remove spooky cache folder"""
        if clean is None:
            onlyfiles.pop(-1)
    onlyfiles.remove("__init__")
    print(onlyfiles)

try:
    img_list = os.listdir(input_path)
    if video:
        img_list = video_mk(input_path, video_name)
    with Progress() as progress:
        task1 = progress.add_task("[red]Loading...", total=len(img_list), visible=bool_visible)

        for img in img_list:
            if bool_visible:
                progress.advance(task1)
                if video:
                    time.sleep(0.1)
                    time.sleep(0.005)

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
                for iterations in listing:
                    a = iterations.split(":")

                    filter = {
                        "name": a[0]
                    }
                    if len(a) == 3:
                        filter["message"] = a[1]
                        filter["color"] = a[2]
                    elif len(a) == 2:
                        filter["intensity"] = a[1]
                    filters_list.append(filter)

                    if filter["name"] == 'dilate':
                        img_src = dilate(img_src, int(filter["intensity"]))
                    elif filter["name"] == 'blur':
                        img_src = blur(img_src, int(filter["intensity"]))
                    elif iterations == 'grayscale':
                        img_src = grayscale(img_src)
                    elif iterations == 'zeteam':
                        img_src = zeteam(img_src)
                    elif filter["name"] == 'message':
                        img_src = message.message(img_src, filter["message"], filter["color"])
                cv2.imwrite(f'{output_path}{img}', img_src)
            progress.console.print(img)
except NameError:
    pass
