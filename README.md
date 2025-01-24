# P3AR-NTU

## Overview
This repository provides the processing steps for the P3AR-NTU dataset, which is based on the NTU RGB+D 120 dataset. Follow the steps below to download and prepare the dataset for further use.

## Steps to Follow

### Step 1: Download P3AR-NTU Dataset
First, download the original P3AR-NTU dataset we created from the following link:  
[P3AR-NTU Download Link](https://pan.baidu.com/s/1BcO7uwanPu-1msp7o1gl3Q?pwd=l3tb)  
**Access Code:** l3tb

### Step 2: Obtain NTU RGB+D 120 Data
Download the original NTU RGB+D 120 dataset separately.  
Run the `get_output_txt.py` script to extract the sample name, start frame, and end frame for each video. The output of this step will be saved as `output_v2.txt`.  
This step has already been pre-processed and can be skipped if the `output_v2.txt` file is available.

### Step 3: Extract Frames from Videos
Run the `get_all_frames.py` script to split each frame from the `raw.mkv` videos. This will generate individual frames from the videos.

### Step 4: Organize Video Samples
Run the `folders_for_each_video.py` script to organize the P3AR-NTU dataset. This script uses the information in `output_v2.txt` to sort the video frames into corresponding folders, each representing a video sample.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
