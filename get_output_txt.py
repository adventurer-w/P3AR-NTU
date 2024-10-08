import os
import cv2

def process_videos(directory, output_file):
    begin = 0
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(directory):
            dirs.sort()
            files.sort()

            for file in files:
                if file.endswith('.avi'):
                    full_path = os.path.join(root, file)
                    cap = cv2.VideoCapture(full_path)
                    if cap.isOpened():
                        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                        end = begin + frame_count -1
                        f.write(f"{begin} {end} {file}\n")
                        begin = end + 1
                    cap.release()

directory_path = '/data-home/ntu_data/ntu_dataset'
output_file_path = '/data-home/ntu_data/our_dataset/out/output_v2.txt'

process_videos(directory_path, output_file_path)
