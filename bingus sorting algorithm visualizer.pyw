import cv2
import numpy as np
import random
from ffpyplayer.player import MediaPlayer
video_path="bingus.mp4"

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()

x = 10
w = frame.shape[0] // x
h = frame.shape[1] // x
tiles = [frame[x:x+w, y:y+h] for x in range(0, frame.shape[0], w) for y in range(0, frame.shape[1], h)]



def PlayVideo(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()


li = [i for i in range(x*x)]


random.Random(1).shuffle(tiles)
random.Random(1).shuffle(li)
def assemble(x):
    i = 0
    j = 0
    while i < x:
        while j < x:
            if j == 0:
                row = tiles[i*x]
            else:
                row = np.concatenate((row, tiles[j+i*x], ), axis=1)
            j+=1
        if i == 0:
            img = row
        else:
            img = np.concatenate((img, row), axis=0)
        i+=1
        j = 0
    return img

img = assemble(x)

for j in range(x*x):
    for i in range(x*x-j-1):
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i]
            tiles[i], tiles[i+1] = tiles[i+1], tiles[i]
            img = assemble(x)
            cv2.imshow('Video', img)
            k=cv2.waitKey(1) & 0XFF
            if k == 27:
                break

PlayVideo(video_path)