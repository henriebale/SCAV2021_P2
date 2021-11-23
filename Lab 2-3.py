import os
res=1
while res!= "0":
    print("Select size 720,480,240 or 120: (insert 0 to end)")
    res=input()
    print(f" {res}p selected")
    if res=="720":
        os.system("ffmpeg -i BBB_video_cut.mp4 -vf scale=1280:720 BBB_video_cut_720.mp4")
        print(f"Playing the {res}p version (closa window to continue)")
        os.system(f"ffplay BBB_video_cut_720.mp4")
    elif ex=="480":
        os.system("ffmpeg -i BBB_video_cut.mp4 -vf scale=640:480 BBB_video_cut_480.mp4")
        print(f"Playing the {res}p version (closa window to continue)")
        os.system(f"ffplay BBB_video_cut_480.mp4")
    elif ex=="240":
        os.system("ffmpeg -i BBB_video_cut.mp4 -vf scale=360:240 BBB_video_cut_240.mp4")
        print(f"Playing the {res}p version (closa window to continue)")
        os.system(f"ffplay BBB_video_cut_248.mp4")
    elif ex=="120":
        os.system("ffmpeg -i BBB_video_cut.mp4 -vf scale=160:120 BBB_video_cut_120.mp4")
        print(f"Playing the {res}p version (closa window to continue)")
        os.system(f"ffplay BBB_video_cut_120.mp4")
    else:
        print(f"Size {res}p not supported")

