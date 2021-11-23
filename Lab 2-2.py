import os

os.system("ffmpeg -i BBB_video_cut.mp4 -vf split=2[a][b],[b]histogram,format=yuva444p,scale=100:240[hh],[a][hh]overlay BBB_video_cut_YUV.mp4")
os.system(f"ffplay BBB_video_cut_YUV.mp4")

