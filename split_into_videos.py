from moviepy.editor import VideoFileClip
import os


video_path = '/data-home/ntu_data/our_dataset/out/raw.mkv'
output_path = '/data-home/ntu_data/our_dataset/out/output_test.txt'
output_dir = '/data-home/ntu_data/our_dataset/out/split'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

video = VideoFileClip(video_path)

with open(output_path, 'r') as file:
    lines = file.readlines()

for line in lines:
    start_frame, end_frame, video_name = line.strip().split()
    start_frame = int(start_frame)
    end_frame = int(end_frame)
    start_frame = start_frame+168
    end_frame = end_frame+168
    video_name += ".mp4" 

    fps = video.fps
    start_time = start_frame / fps
    end_time = end_frame / fps

    new_clip = video.subclip(start_time, end_time)
    
    new_clip.write_videofile(os.path.join(output_dir, video_name), codec='libx264', preset='ultrafast', audio_codec='aac')
    print(video_name)
    
video.close()