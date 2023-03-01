import numpy as np
import cv2
import moviepy.editor as mp
import subprocess

# path to input video that needs to be edited
inputVideoPath = "input_video.mp4"

# path where you want your edited video to be saved
outputVideoPath = "output\\"

video = mp.VideoFileClip(inputVideoPath)

# type text here, line 1 and line 2 will appear above the video
# while line 3 aur line 4 appears below.
text = input("Enter you name:- ")
name = "Hi "+ text

# enter your desired font size below, can be in decimal too 0.1 or 1.3 or 2
fontsize = 3
maroon_background = 65
bottomBanner = None

cap = cv2.VideoCapture(inputVideoPath)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None
print(cap.isOpened())
while (cap.isOpened()):
    ret, frame = cap.read()
    if frame is None:
        break
    height, width, ch = frame.shape

    if out is None:
        out = cv2.VideoWriter(outputVideoPath+'output.mp4', fourcc,video.fps, (width, height + fontsize*100), True)
        bottomBanner = np.ones([fontsize*100, width, 3], dtype=np.uint8)* maroon_background
        

        ## put text in banner ##
        cv2.putText(bottomBanner, name, (10, 50 + fontsize*20), cv2.FONT_HERSHEY_SIMPLEX,
                    fontsize, (249, 246, 238), 5)
        


    output = np.vstack((frame, bottomBanner))

    out.write(output)

    if cv2.waitKey(1) & 255 == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

command = "echo y | ffmpeg -i " + outputVideoPath + "output.mp4 -i " + \
    inputVideoPath + " -codec copy -shortest " + \
    outputVideoPath + "converted_video.mp4"
subprocess.call(command, shell=True)

command = "del " + outputVideoPath + "output.mp4"
subprocess.call(command, shell=True)

print("\n conversion successfully completed. Find your output video at " + outputVideoPath+"converted_video.mp4")