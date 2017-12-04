#This code works with Python 3 not 2
import json
import csv

def getPartsVideo(c):
 
    a=c.get('snippet')
    b=a.get('topLevelComment')
    aa=c.get('original_video')
    bb=aa.get('snippet')
    #print(b)
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
