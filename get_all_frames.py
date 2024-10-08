import cv2
import os

def extract_frames_reverse(video_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    frame_count = 0
    total_frames = 8156030
    for i in range(total_frames - 1, -1, -1):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if not ret:
            continue  
        

        frame_filename = f"{output_dir}/frame_{i:010d}.jpg"

        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    cap.release()
    
extract_frames_reverse('/data-home/ntu_data/our_dataset/out/raw.mkv', '/data-home/ntu_data/our_dataset/out/frame')
