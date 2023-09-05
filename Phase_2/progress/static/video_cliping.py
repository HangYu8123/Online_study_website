from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video import fx

# Load video
clip = VideoFileClip("Phase_2/progress/static/perfect_demo.avi")
clip = clip.subclip(20, 14 * 60 + 55).without_audio()

total_duration = clip.duration
segment_duration = total_duration / 15


clips = []

for i in range(15):
    start_time = i * segment_duration
    end_time = (i + 1) * segment_duration
    
    # Cut video into a clip
    cut_clip = clip.subclip(start_time, end_time)
    
    # Speed up the clip
    speed_up_factor = 6  # 2x speed
    fast_clip = cut_clip.fx(fx.all.speedx, speed_up_factor)
    fast_clip.write_videofile("Phase_2/progress/static/episode" + str(0)+"step"+str(i)+".mp4")





clip = VideoFileClip("Phase_2/progress/static/imperfect_demo.avi")
clip = clip.subclip(20, 13 * 60 + 20).without_audio()

total_duration = clip.duration
segment_duration = total_duration / 15


clips = []

for i in range(15):
    start_time = i * segment_duration
    end_time = (i + 1) * segment_duration
    
    # Cut video into a clip
    cut_clip = clip.subclip(start_time, end_time)
    
    # Speed up the clip
    speed_up_factor = 6  # 2x speed
    fast_clip = cut_clip.fx(fx.all.speedx, speed_up_factor)
    fast_clip.write_videofile("Phase_2/progress/static/episode" + str(1)+"step"+str(i)+".mp4")





clip = VideoFileClip("Phase_2/progress/static/non_recover_demo.avi")
clip = clip.subclip(0, 13 * 60 + 20).without_audio()

total_duration = clip.duration
segment_duration = total_duration / 15


clips = []

for i in range(15):
    start_time = i * segment_duration
    end_time = (i + 1) * segment_duration
    
    # Cut video into a clip
    cut_clip = clip.subclip(start_time, end_time)
    
    # Speed up the clip
    speed_up_factor = 6  # 2x speed
    fast_clip = cut_clip.fx(fx.all.speedx, speed_up_factor)
    fast_clip.write_videofile("Phase_2/progress/static/episode" + str(2)+"step"+str(i)+".mp4")


clip = VideoFileClip("Phase_2/progress/static/recover.mp4")
clip = clip.subclip(0, 13 * 60 + 20).without_audio()

total_duration = clip.duration
segment_duration = total_duration / 15

#Cut the video into three parts: before, during and after the segment to cut out
start_cut = 11*60 + 4   # time to start cut in seconds
end_cut = 11*60 + 24  # time to end cut in seconds

clip_before_cut = clip.subclip(0, start_cut)
clip_to_cut = clip.subclip(start_cut, end_cut)  # This part will be removed
clip_after_cut = clip.subclip(end_cut, clip.duration)
clip = concatenate_videoclips([clip_before_cut, clip_after_cut])
#Determine clip duration and the duration of each segment

total_duration = clip.duration
segment_duration = total_duration / 15

clips = []

for i in range(15):
    start_time = i * segment_duration
    end_time = (i + 1) * segment_duration
    
    # Cut video into a clip
    cut_clip = clip.subclip(start_time, end_time)
    
    # Speed up the clip
    speed_up_factor = 6  # 2x speed
    fast_clip = cut_clip.fx(fx.all.speedx, speed_up_factor)
    fast_clip.write_videofile("Phase_2/progress/static/episode" + str(3)+"step"+str(i)+".mp4")
    #fast_clip.write_videofile("Phase_2/progress/static/demo.mp4")



clip = VideoFileClip("Phase_2/progress/static/miss_cup_demo.avi")
clip = clip.subclip(20, 14 * 60 + 55).without_audio()

total_duration = clip.duration
segment_duration = total_duration / 15


clips = []

for i in range(15):
    start_time = i * segment_duration
    end_time = (i + 1) * segment_duration
    
    # Cut video into a clip
    cut_clip = clip.subclip(start_time, end_time)
    
    # Speed up the clip
    speed_up_factor = 6  # 2x speed
    fast_clip = cut_clip.fx(fx.all.speedx, speed_up_factor)
    fast_clip.write_videofile("Phase_2/progress/static/episode" + str(4)+"step"+str(i)+".mp4")


