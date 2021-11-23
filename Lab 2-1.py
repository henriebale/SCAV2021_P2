import os
print(f"Select starting point (format 00:00:00):")
start = input()
print(f"Select the duration of the cut (format 00:00:00):")
duration= input()
print(f"Cut from {start} with duration {duration}")
os.system(f"ffmpeg -i BBB_video.mp4 -ss {start} -t {duration} BBB_video_cut.mp4")
os.system(f"ffplay BBB_video_cut.mp4")


