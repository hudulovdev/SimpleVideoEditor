from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def cut_video(input_file, output_file, start_time, end_time):
    ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)

# Specify the input video file path
input_file = "input.mp4"

# Specify the output video file path
output_file = "output.mp4"

# Specify the start and end times in seconds
start_time = 60  # 1 minute
end_time = 180  # 3 minutes

# Call the function to cut the video
cut_video(input_file, output_file, start_time, end_time)
