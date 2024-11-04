from . import *

@bot.on(events.callbackquery.CallbackQuery(data="helpme"))
async def helper(event):
    text="I am a bot , i can do this, these are my commands, can be customized"
    await event.edit(text,
                     buttons=[
                         [Button.url("CUSTOMIZE", url="https://github.com/pandeytanmay"), Button.url("Dev", url="https://t.me/hustle_xy")],
                         [Button.url("CUSTOMIZE", url="https://GOOGLE.COM")],
                         [Button.inline("PROFILE", data="profile")]
                     ])