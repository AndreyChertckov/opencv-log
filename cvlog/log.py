import base64
import os

import cv2

import cvlog.html_logger as hl
from cvlog.config import Config, Mode
import time

html_logger = None


def image(level, img=None, description=None):
    if img is None and description is None:
        return
    if img is not None:
        img = img[..., ::-1]
    try:
        __init()
        if Config().curent_level().value < level.value:
            return
        if Config().curent_mode() == Mode.DEBUG:
            show_image(level.name, img)
        elif Config().curent_mode() == Mode.LOG:
            log_image(level.name, img, description)
    except Exception as e:
        print(e)


def log_image(level, img, description):
    buffer = None
    if img is not None:
        retval, buffer = cv2.imencode('.png', img)
        if not retval:
            return None
        buffer = base64.b64encode(buffer).decode()
    html_logger.log_image(level, buffer, description)


def show_image(title, img):
    cv2.namedWindow('window', cv2.WINDOW_NORMAL)
    cv2.setWindowTitle('window', title)
    cv2.imshow('window', img)
    value = cv2.waitKey(0)
    if value == 27:
        os._exit(1)
    return value


def __init():
    global html_logger
    if Config().curent_mode() == Mode.LOG and html_logger is None:
        html_logger = hl.HtmlLogger(Config().log_path() + f"/log_{int(time.time())}.html")
