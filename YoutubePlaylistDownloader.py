from pytube import YouTube
import sys,requests,re

location="F:\\Computer\\TheNewBoston Python Webcrawling"
mainsite="https://www.youtube.com/"
#Give the url of the playlist page
playlisturl="https://www.youtube.com/playlist?list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0q"

r=requests.get(playlisturl)

try:
    r.raise_for_status()
except:
    print("Error in opening playlist page. Check internet Connection")
    sys.exit(1)

print("Got access to playlist")

playlist_id = playlisturl[playlisturl.index('=')+1:]
vid_url_pat = re.compile(r'watch\?v=\S+?list=' + playlist_id)
dlinks = list(set(re.findall(vid_url_pat, r.text)))

#now we have all the watch ids of the  videos .
#print(dlinks)

for vid in dlinks:
    url=mainsite+vid[0:vid.index(';')]
    yt = YouTube(url)
    print("Downloading : "+yt.filename)
    try:
        video = yt.get('mp4', '1080p')
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
                    continue;

    try:
        video.download(location)
    except:
        continue

    print("Downloaded : " + yt.filename)

print("Downloaded all videos")