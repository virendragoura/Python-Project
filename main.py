from instabot import Bot
import time

bot = Bot()

# Login to Instagram
bot.login(username="veergoura", password="123456")


# Follow a user
bot.follow("virendragoura")
time.sleep(5)  # Give Instagram time to process

# Unfollow a user
bot.unfollow("yoozax")
time.sleep(5)

# Send a message (ensure target is in a list)
bot.send_message("Hello! This is an automated message.", ["virendragoura"])
time.sleep(5)

# Upload a post (image with caption)
bot.upload_photo("Linkedin_Virendra.jpg", caption="This is an automated post! 🚀")
time.sleep(5)

# Get list of followers
followers = bot.get_user_followers("virendragoura")
for follower in followers:
    print(bot.get_user_info(follower))
    
# Logout
bot.logout()
