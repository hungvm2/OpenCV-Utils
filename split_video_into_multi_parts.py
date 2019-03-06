# This code is used to split video into multiple parts
# Argument including video input and number of parts to divide

import numpy as np
import cv2
import time
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-v', '--video', type=str, help='video input', required=True)
ap.add_argument('-p', type=int, help='number of desired parts', required=True)
args = vars(ap.parse_args())

num_of_parts_to_slit = args.get('p')
num_of_parts_to_slit = args.get('p')
print ("Split the video into {} parts".format(str(num_of_parts_to_slit)))

filename = args.get('video')[:-4]
vidcap = cv2.VideoCapture(args.get('video'))
original_width = int(vidcap.get(3))
original_height = int(vidcap.get(4))
original_fps = int(vidcap.get(5))
original_frame_count = vidcap.get(7)
vidcap.set(3,original_width)
vidcap.set(4,original_height)
vidcap.set(5,original_fps)

# Caculate frames per part
frames_per_part = original_frame_count // num_of_parts_to_slit
fourcc = cv2.VideoWriter_fourcc(*'XVID')
def get_output(part):
  return cv2.VideoWriter(filename + '-' + str(part) + '.avi', fourcc ,original_fps, (original_width, original_height))

count = 0
while count < num_of_parts_to_slit:
  print(count)
  start_frame = 1 + frames_per_part * count
  end_frame = frames_per_part * (count + 1)

  # Set first frame of the video to start_frame
  vidcap.set(2,start_frame)

  output_video = get_output(count + 1)
  current_frame = start_frame
  while current_frame <= end_frame:
    ret,frame = vidcap.read()
    output_video.write(frame)
    current_frame += 1
  count += 1
vidcap.release()
cv2.destroyAllWindows()

print('The video was splitted successfully!')
