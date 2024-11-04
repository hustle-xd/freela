from . import *

@bot.on(events.NewMessage(incoming=True, pattern="/start"))
async def _(event):
    xxx = await bot(GetFullUserRequest(event.sender_id))
    await bot.send_message(event.sender_id,"**hello this is start message, can be customized**",
                        buttons=[
                            [Button.inline("**Help**", data="helpme"), Button.url("can be customized ", url="https://github.com/pandeytanmoy")],
                            [Button.inline("**Profile**", data="profile")]
                        ])