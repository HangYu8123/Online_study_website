from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video import fx

# Load video
clip = VideoFileClip(r'C:\Users\Hang Yu\Desktop\online_study\Online_study_website\webpage\static\spining.avi')
clip = clip.subclip(30, 500)
# Determine clip duration and the duration of each segment
total_duration = clip.duration
segment_duration = total_duration / 10

clips = []

for i in range(10):
    start_time = i * segment_duration
    end_time = (i + 1) * segment_duration
    
    # Cut video into a clip
    cut_clip = clip.subclip(start_time, end_time)
    
    # Speed up the clip
    speed_up_factor = 4  # 2x speed
    fast_clip = cut_clip.fx(fx.all.speedx, speed_up_factor)
    fast_clip.write_videofile(r"C:\Users\Hang Yu\Desktop\online_study\Online_study_website\webpage\static\episode" + str(2)+"step"+str(i)+".mp4")



# video_len = [19, 19, 13, 19, 13, 11]
# episodes = 6
# for j in range(0,episodes):
#     for i in range(video_len[j]):
#         clip = VideoFileClip(str(j) + ".mp4" ).subclip(i*4, i*4+4)
#         clipspeed = clip.speedx(1.36)
#         clipspeed.write_videofile("episode" + str(j)+"step"+str(i)+".mp4")