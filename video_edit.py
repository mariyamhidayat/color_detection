import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer

cap=cv2.VideoCapture("C:\\Users\\Swan Computers\\.vscode\\extensions\\nida.MP4")
player=MediaPlayer("C:\\Users\\Swan Computers\\.vscode\\extensions\\nida.MP4")
#Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video file")
while(cap.isOpened()):
      
# Capture frame-by-frame
    ret, frame = cap.read()
    audio_frame,val=player.get_frame()
    bro=cv2.copyMakeBorder(frame,10,10,10,10,cv2.BORDER_CONSTANT)
    #rot=cv2.rotate(bro,cv2.ROTATE_90_CLOCKWISE)
    #blur=cv2.GaussianBlur(rot,(7,7),0)
    if ret == True:
    # Display the resulting frame
        cv2.imshow('Frame', bro)
          
    # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

  
# Break the loop
    else:
        break
    # When everything done, release
# the video capture object
cap.release()
  
# Closes all the frames
cv2.destroyAllWindows()