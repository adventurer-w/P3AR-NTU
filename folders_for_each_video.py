import os
import shutil

def process_frames(input_dir, output_dir, definition_file):
    with open(definition_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        start_frame, end_frame, video_name = line.strip().split()
        start_frame = int(start_frame)
        end_frame = int(end_frame)

        start_frame = start_frame + 168
        end_frame = end_frame + 168

        video_folder = os.path.join(output_dir, video_name)
        os.makedirs(video_folder, exist_ok=True)

        for frame_number in range(start_frame, end_frame + 1):
            src_frame_name = f"frame_{frame_number:010d}.jpg"
            src_path = os.path.join(input_dir, src_frame_name)
            dest_path = os.path.join(video_folder, src_frame_name)
            
            if os.path.exists(src_path):
                shutil.copy(src_path, dest_path)

input_directory = '/data-home/ntu_data/our_dataset/out/frame'
output_directory = '/data-home/ntu_data/our_dataset/out/Video_Frame'
definition_path = '/data-home/ntu_data/our_dataset/out/output_v2.txt'


process_frames(input_directory, output_directory, definition_path)
