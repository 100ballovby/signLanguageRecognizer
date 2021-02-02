import cv2
import numpy as np

background = None
accumulated_weight = 0.5

ROI_top = 100
ROI_bottom = 300
ROI_left = 350
ROI_right = 150


def cal_accum_avg(frame, accumulated_weight):
    global background

    if background is None:
        background = frame.copy().astype('float')
        return None

    cv2.accumulateWeighted(frame, background, accumulated_weight)


def segment_hand(frame, treshold=25):
    global background
    diff = cv2.absdiff(background.astype('uint8'), frame)


