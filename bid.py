from telethon import TelegramClient, events, Button
import logging
import argparse
import json

# Set up logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
APP_ID = 2031518
API_HASH = "b2c81aace7412612bd7195438af94dbf"
BOT_TOKEN = "7085722606:AAEMVz-e_T_jv7JALYo6-7zX134miCdeyLI"
OWNER_ID = 1234

bot2 = TelegramClient('notificationbot', APP_ID, API_HASH).start(bot_token=BOT_TOKEN)
bidder = {}
async def sendtelegram(parsed_email_info, v):
    i = int(v)
    parsedit = json.loads(parsed_email_info)
    text = f'''
    Hello There,
    Just received an order:
    Order Id - {parsedit['order_id']}
    Pickup Address - {parsedit['PickupLocation']}
    Pickup Time - {parsedit['PickupTime']}
    Delivery Address - {parsedit['DeliveryAddress']} 
    Delivery Time - {parsedit['DeliveryTime']}
    Vehicle Required - {parsedit['VehicleRequired']} 
    Weight - {parsedit['Weight']}
    Dimensions - {parsedit['Dimensions']}
    Wanna Send Your Bid?
    
    '''
    print(text)
    
    await bot2.send_message(i, text, buttons=[Button.inline("Send Your Bid", data="sendbid")])

@bot2.on(events.CallbackQuery(func=sendtelegram))
async def handle_bid(event):
     if event.data=="sendbid":
         await bot2.send_message(event.sender_id, "Send ur bid")
         @bot2.on(events.NewMessage)
         async def handle(event):
     # This will be triggered for any new message
             bid = event.message.message
             bidder[event.sender_id]=bid
             print(bid)
                


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Send parsed data to a sender via Telegram.')
    parser.add_argument('parsed_email_info', type=str, help='The parsed data to send.')
    parser.add_argument('v', type=str, help='The sender ID to send data to.')
    
    args = parser.parse_args()
    a = sendtelegram(args.parsed_email_info, args.v)
    bot2.run_until_disconnected()
    # Call the main function with the parsed arguments
    
    

