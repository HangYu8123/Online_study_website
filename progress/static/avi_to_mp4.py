from moviepy.editor import VideoFileClip

def convert_avi_to_mp4(avi_file_path, output_name):
    clip = VideoFileClip(avi_file_path)
    clip.write_videofile(f"{output_name}.mp4")

# usage
convert_avi_to_mp4(r"C:\Users\Hang Yu\Desktop\online_study\Online_study_website\webpage\static\moving.avi", "moving")
