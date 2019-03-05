# This code is used to split video into multiple parts
# Argument including video input and number of parts to divide

import numpy as np
import cv2
import time
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-v', '--video', type=str, help='video input', required=True)
args = vars(ap.parse_args())

vidcap = cv2.VideoCapture(args.get('video'))

print('Video resolution: %dx%d'%(vidcap.get(3), vidcap.get(4)))
print('Video frames per second: %d'%(vidcap.get(5)))
vidcap.release()
cv2.destroyAllWindows()
