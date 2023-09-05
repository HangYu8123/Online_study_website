from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video import fx

# Load video
clip = VideoFileClip("Phase_2/progress/static/mistake_in_pouring.avi")
clip = clip.subclip(45, 955).without_audio()

total_duration = clip.duration
segment_duration = total_duration / 1


# Cut the video into three parts: before, during and after the segment to cut out
# start_cut = 917 - 45  # time to start cut in seconds
# end_cut = 922 - 45  # time to end cut in seconds

# clip_before_cut = clip.subclip(0, start_cut)
# clip_to_cut = clip.subclip(start_cut, end_cut)  # This part will be removed
# clip = clip.subclip(end_cut, clip.duration)


# Determine clip duration and the duration of each segment




clips = []

for i in range(1):
    start_time = i * segment_duration
    end_time = (i + 1) * segment_duration
    
    # Cut video into a clip
    cut_clip = clip.subclip(start_time, end_time)
    
    # Speed up the clip
    speed_up_factor = 30  # 2x speed
    fast_clip = cut_clip.fx(fx.all.speedx, speed_up_factor)
    #fast_clip.write_videofile("Phase_2/progress/static/episode" + str(1)+"step"+str(i)+".mp4")
    fast_clip.write_videofile("Phase_2/progress/static/demo.mp4")
# # Load video
# clip = VideoFileClip("webpage/static/marked_pouring.avi")
# clip = clip.subclip(40, 640)
# # Determine clip duration and the duration of each segment
# total_duration = clip.duration
# segment_duration = total_duration / 10

# clips = []

# for i in range(10):
#     start_time = i * segment_duration
#     end_time = (i + 1) * segment_duration
    
#     # Cut video into a clip
#     cut_clip = clip.subclip(start_time, end_time)
    
#     # Speed up the clip
#     speed_up_factor = 5  # 2x speed
#     fast_clip = cut_clip.fx(fx.all.speedx, speed_up_factor)
#     fast_clip.write_videofile("webpage/static/episode" + str(1)+"step"+str(i)+".mp4")

# # Load video
# clip = VideoFileClip("webpage/static/marked_spining.avi")
# clip = clip.subclip(30, 750)
# # Determine clip duration and the duration of each segment
# total_duration = clip.duration
# segment_duration = total_duration / 10

# clips = []

# for i in range(10):
#     start_time = i * segment_duration
#     end_time = (i + 1) * segment_duration
    
#     # Cut video into a clip
#     cut_clip = clip.subclip(start_time, end_time)
    
#     # Speed up the clip
#     speed_up_factor = 6  # 2x speed
#     fast_clip = cut_clip.fx(fx.all.speedx, speed_up_factor)
#     fast_clip.write_videofile("webpage/static/episode" + str(2)+"step"+str(i)+".mp4")



