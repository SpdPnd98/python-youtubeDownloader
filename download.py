import json
import youtube_dl

'''
adapted from https://dev.to/stokry/download-youtube-video-to-mp3-with-python-26p
'''
def run():
    with open('./links.json') as f:
        video_urls = json.load(f)
        for video_url in video_urls["links"]:
            video_info = youtube_dl.YoutubeDL().extract_info(
                url = video_url,download=False
            )
            filename = f"output\\{video_info['title']}.mp3"
            options={
                'format':'bestaudio/best',
                'keepvideo':False,
                'outtmpl':filename,
            }

            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([video_info['webpage_url']])

            print("Download complete... {}".format(filename))

if __name__=='__main__':
    run()
