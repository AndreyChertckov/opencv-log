import base64
import os

import cv2

import cvlog.html_logger as hl
from cvlog.config import Config, Mode
import time

html_logger = None


class Logger:

    def __init__(self, mode, level):
        self.html_logger = None
        self.mode = mode
        self.level = level
        if self.mode == Mode.LOG:
            self.html_logger = hl.HtmlLogger(Config().log_path() + f"/log_{int(time.time())}.html")

    def image(self, level, img=None, description=None):
        if img is None and description is None:
            return
        if img is not None:
            img = img[..., ::-1]
        try:
            if self.level.value < level.value:
                return
            if self.mode == Mode.DEBUG:
                self.show_image(level.name, img)
            elif self.mode == Mode.LOG:
                self.log_image(level.name, img, description)
        except Exception as e:
            print(e)

    def log_image(self, level, img, description):
        buffer = None
        if img is not None:
            retval, buffer = cv2.imencode('.png', img)
            if not retval:
                return None
            buffer = base64.b64encode(buffer).decode()
        self.html_logger.log_image(level, buffer, description)

    @staticmethod
    def show_image(title, img):
        cv2.namedWindow('window', cv2.WINDOW_NORMAL)
        cv2.setWindowTitle('window', title)
        cv2.imshow('window', img)
        value = cv2.waitKey(0)
        if value == 27:
            os._exit(1)
        return value


def getLogger(level, mode):
    return Logger(level, mode)
