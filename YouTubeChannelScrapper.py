#This code works with Python 3.6 not 2.7
import socialreaper
from socialreaper import Youtube
import csv


#This function is used to return a tuple of data for ezach comement.
#of course I selected just the columns that I needed, but you can specify other columns
#For this, print (c) -line 54 in order to analyze the structure of the comment.

def getPartsVideo(c):
 
    a=c.get('snippet')
    b=a.get('topLevelComment')
    aa=c.get('original_video')
    bb=aa.get('snippet')
    
    if (b!=None):
        authorDisplayName=b['snippet']['authorDisplayName']
        authorProfileImageUrl=b['snippet']['authorProfileImageUrl']
        authorChannelUrl=b['snippet']['authorChannelUrl']
        authorChannelId=b['snippet']['authorChannelId']
        videoId=b['snippet']['videoId']
        textDisplay=b['snippet']['textDisplay']
        textOriginal=b['snippet']['textOriginal']        
        canRate=b['snippet']['canRate']
        viewerRating=b['snippet']['viewerRating']
        likeCount=b['snippet']['likeCount']
        publishedAt=b['snippet']['publishedAt']
        updatedAt=b['snippet']['updatedAt']
        #About the channel         
        OV_publishedAt=bb.get('publishedAt')
        OV_channelId=bb.get('channelId')
        OV_title=bb.get('title')
        OV_description=bb.get('description')
        OV_channelTitle=bb.get('channelTitle') 
        return (authorDisplayName,authorProfileImageUrl,authorChannelUrl,authorChannelId,videoId,textDisplay
            ,textOriginal,canRate,viewerRating,likeCount,publishedAt,updatedAt
            ,OV_publishedAt,OV_channelId,OV_title,OV_description,OV_channelTitle)  

with open('Channel_YouTube_Comments.csv', 'w') as file: #here you can specify the location of your CSV file and you can change its name.
        w = csv.writer(file)
        w.writerow(["authorDisplayName","authorProfileImageUrl","authorChannelUrl","authorChannelId","videoId",
                    "textDisplay","textOriginal","canRate","viewerRating","likeCount","publishedAt","updatedAt"
                    ,"OV_publishedAt","OV_channelId","OV_title","OV_description","OV_channelTitle"])  
        ytb = Youtube("put_youtube_API_KEY_here") #this is the access token that you get from youtube app 
        channel_id = "specify you channel_id" #here put the channel Id that you want to analyze (you get it from the url of the channel in youtube)

        comments = ytb.channel_video_comments(channel_id, video_count=5, 
                  comment_count=20,comment_format="plainText",part='snippet',mine='true')  #this funtion allows you to get the comments of the vidéos.
        # you can specify the number of the videos to analyse (video_count) and you can specify the number of comments to gather in comment_count.
        for c in comments:
        	print (c) #in order to have an idea about the format of the tupe of data that we get in JSON              
            if (getPartsVideo(c)!=None) : w.write(getPartsVideo(c))
               

print("Done!")
