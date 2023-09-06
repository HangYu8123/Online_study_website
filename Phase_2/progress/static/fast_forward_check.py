from moviepy.editor import VideoFileClip
from moviepy.video import fx
from moviepy.editor import concatenate_videoclips

# Input video name
path = "Phase_2/progress/static/"
#video_name = "recov_fixed_demo.avi"
video_name = "perfect_demo.avi"
# Read the video file
clip = VideoFileClip(path + video_name)

# #Cut the video into three parts: before, during and after the segment to cut out
# start_cut = 11*60 + 4   # time to start cut in seconds
# end_cut = 11*60 + 24  # time to end cut in seconds

# clip_before_cut = clip.subclip(0, start_cut)
# clip_to_cut = clip.subclip(start_cut, end_cut)  # This part will be removed
# clip_after_cut = clip.subclip(end_cut, clip.duration)
# clip = concatenate_videoclips([clip_before_cut, clip_after_cut])


# Apply color effect
clip = clip.fx(fx.all.speedx, 30)

# Debug: Print the output video name
print("Output Video name:", "fx" + video_name)

# Write the video file with explicit codec
clip.write_videofile( path + "demo.mp4")
