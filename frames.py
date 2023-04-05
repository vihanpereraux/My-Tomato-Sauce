import cv2
import os

vidcap = cv2.VideoCapture('video03-void-c60-n60.avi')
success,image = vidcap.read()
count = 0
path = 'D:/Projects/Python/Datamosh-Visualizer/frames'  #D:\Projects\Python\Datamosh-Visualizer\frames
while success:
  cv2.imwrite(os.path.join(path, "frame%d.jpg" % count), image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1