from pytube import YouTube
import sys

location="C:\\Users\\HP -)(- HP\\Desktop"

url="https://www.youtube.com/watch?v=ETsfylK7kzM"

yt=YouTube(url)
print(yt.get_videos())
try:
    video=yt.get('mp4','1080p')
    print("Video Quality -  1080p")
except:
    try:
        video = yt.get('mp4', '720p')
        print("Video Quality - 720p")
    except:
        try:
            video = yt.get('mp4', '480p')
            print("Video Quality - 480p")
        except:
            try:
                video = yt.get('mp4', '360p')
                print("Video Quality - 360p")
            except:
                print("video has a very low quality. You wont enjoy it!! Aborting Download")
                sys.exit(1)


video.download(location)

print("Downloaded : "+yt.filename)