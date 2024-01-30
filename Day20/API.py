from googleapiclient.discovery import build
#youtube API를 사용하기 위해 build 함수를 사용하여 youtube 서비스 클래스를 생성함
#youtube 와 v3버전입력,key입력
youtube = build ('youtube','v3' ,developerKey="AIzaSyA8VRK8GqobS2yWJHn4Aj7-VDnqei_H82g")

response = youtube.commentThreads().list(
    part= 'snippet',
    videoId = '5K-7Qm1sZuk',
    textFormat = 'plainText'
).execute()

youtubeList = []

for i in response['items']:
    review = i['snippet']['topLevelComment']['snippet']
    comment = review['textDisplay']
    like = review['likeCount']
    author = review['authorDisplayName']
    youtubeList.append({'댓글':comment,'좋아요':like,'글쓴이':comment})
print(youtubeList)

