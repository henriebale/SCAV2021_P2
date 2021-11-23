import os

os.system("ffmpeg -i BBB_video_cut.mp4 -ac 1 -acodec mp3 BBB_video_cut_mono.mp4")
os.system(f"ffplay BBB_video_cut_mono.mp4")


