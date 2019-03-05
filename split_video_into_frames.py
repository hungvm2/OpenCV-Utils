# This code is used to split video into jpeg images
# Argument including video input and number of frames to stride

import cv2
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', type=str, help='video input', required=True)
ap.add_argument('-o', '--output', type=str, help='output directory', required=True)
ap.add_argument('-f', type=int, help='amount of frame to skip', required=True)
args = vars(ap.parse_args())

filename = args.get('input').split('/')[-1][:-4]
output_dir = args.get('output')
vidcap = cv2.VideoCapture(args.get('input'))
success,image = vidcap.read()
count = 0

# number of frames to skip
numFrameToSave = args.get('f')

print ("Start splitting")
while success: # check success here might break your program
  success,image = vidcap.read() #success might be false and image might be None
  #check success here
  if not success:
    break
  
  # on every numFrameToSave
  if (count % numFrameToSave ==0):
    if os.path.isdir(output_dir):
      path = os.path.join(output_dir, '{}_{}.jpg'.format(filename,count))
      cv2.imwrite(path, image)
    else:
      os.mkdir(output_dir)
      path = os.path.join(output_dir, '{}_{}.jpg'.format(filename,count))
      cv2.imwrite(path, image)
          
  if cv2.waitKey(10) == 27:
      break
  count += 1

print('Done!')
