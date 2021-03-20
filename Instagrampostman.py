#Import instabot
from instabot import Bot 

bot = Bot()
bot.login(username = "username",password = "password")
bot.upload_photo("path/*.jpg",caption="post info") 
