from moviepy.editor import VideoFileClip, concatenate_videoclips

# Load the two video clips
clip1 = VideoFileClip("Phase_2/progress/static/recover_demo.avi")
clip2 = VideoFileClip("Phase_2/progress/static/patch_demo.avi")

clip1 = clip1.subclip( 0, 12 * 60 + 50).without_audio()
clip2 = clip2.subclip(80, 120).without_audio()


# Concatenate the clips
final_clip = concatenate_videoclips([clip1, clip2])

# Write the result to a file
final_clip.write_videofile("Phase_2/progress/static/recover.avi")
