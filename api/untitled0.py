# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 10:51:36 2025

@author: user
"""

from linebot import LineBotApi
from linebot.models import TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage, VideoSendMessage
line_bot_api = LineBotApi('TUGOvvyjEIPUn/5ynC7WkiY68G+uoT/wdhedKQvnvb2MynPpgetQsq4LkFfHpg/RrnQ8/7DY8OK26u53KA47Ub9uDxQ4hm3jZ5yxuW+Ke21PnHxAkTR66GsNoV/TLy0i3Zq0OU4e3uFdoSdJWbB66AdB04t89/1O/w1cDnyilFU=')
UserID = 'U2dddff042e60289dc63086227ea91186'

#text
text_message = TextSendMessage(text = 'hello world!')
line_bot_api.push_message(UserID, text_message)

#sticker
Sticker_message = StickerSendMessage(package_id = '789', sticker_id = '10855')
line_bot_api.push_message(UserID, Sticker_message)

#image
image_message = ImageSendMessage(
    original_content_url='https://i.imgur.com/xyPtn4m.jpeg',
    preview_image_url='https://i.imgur.com/xyPtn4m.jpeg')
line_bot_api.push_message(UserID,image_message)

#location
location_message = LocationSendMessage(
    title='CodingAPE猿創力程式設計學校',
    address='105台北市松山區延壽街374號',
    latitude=25.056434,
    longitude=121.558183)
line_bot_api.push_message(UserID,location_message)

#video
video_message = VideoSendMessage(
    original_content_url='https://i.imgur.com/oRcIXiM.mp4',
    preview_image_url='https://i.imgur.com/xyPtn4m.jpeg'
)
line_bot_api.push_message(UserID,video_message)


try:
  message = [video_message,text_message,Sticker_message,location_message,image_message]
  line_bot_api.push_message(UserID,message)
except:
  error_message = TextSendMessage(text = '發生錯誤！')
  line_bot_api.push_message(UserID, error_message)