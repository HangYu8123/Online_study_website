from moviepy.editor import *
import time
video_len = [19, 19, 13, 19, 13, 11]
episodes = 6
for j in range(0,episodes):
    for i in range(video_len[j]):
        clip = VideoFileClip(str(j) + ".mp4" ).subclip(i*4, i*4+4)
        clipspeed = clip.speedx(1.36)
        clipspeed.write_videofile("episode" + str(j)+"step"+str(i)+".mp4")