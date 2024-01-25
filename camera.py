import cv2
import numpy as np
cp=cv2.VideoCapture(0)
if(cp.isOpened==False):
    print(" video error ")

frame_width=int(cp.get(3))
farem_heigt=int(cp.get(4))
size=(frame_width,farem_heigt)
''' Syntax: cv.VideoWriter(filename, fourcc, fps, frameSize)
    filename: Input video file
fourcc: 4-character code of codec used to compress the frames
fps: framerate of videostream
framesize: Height and width of frame

    '''

result=cv2.VideoWriter('filename.mp4v',  cv2.VideoWriter_fourcc(*"MJPG"),10, size)


while True:
    ret,frame=cp.read()
    if ret == True:
         result.write(frame)
         cv2.imshow('Frame', frame)
    
         if cv2.waitKey(1)==ord('q'):
            break
    else:
        break

cp.release()
result.release()
cv2.destroyAllWindows()