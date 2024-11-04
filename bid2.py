from telethon import TelegramClient, events, Button
import logging
import argparse
import asyncio
import json
import ast

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
async def sendtelegram(file):
    id = [6689020204, 7205241877]
    jsonstring = ""
    with open(rf"C:\Users\pande\OneDrive\Desktop\bot\bot\plugins\more\{file}", "r") as f:
        for line in f:
            stripped_line = line.strip()  # Remove leading/trailing whitespace

            # Check if the line starts with a digit, indicating a phone number
            # if stripped_line and stripped_line[0].isdigit():
            #     id.append(int(stripped_line)) # Add phone number to the list
            if stripped_line and stripped_line[0]=="{":  # If the line is not empty
                parsedit = json.loads(stripped_line)
    print(jsonstring) 
    print(id) # Accumulate lines for JSON
    


    
    
    # Replace single quotes with double quotes
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
    
    for i in id:
        
        print(i)
        await bot2.send_message(i, text, buttons=[Button.inline("Send Your Bid", data="sendbid")])
       

@bot2.on(events.callbackquery.CallbackQuery(data="sendbid"))
async def handle_bid(event):
    try:
        
        await bot2.send_message(event.sender_id, "Send ur bid")
        @bot2.on(events.NewMessage)
        async def handle(event):
         # This will be triggered for any new message
            bid = event.message.message
            bidder[event.sender_id]=bid
            print(bid)
            print(bidder)
            
            
    except Exception as e:
        print(e)
        
                



    
parser = argparse.ArgumentParser(description='Send parsed data to a sender via Telegram.')
parser.add_argument('file', type=str, help='The parsed data to send.')
args = parser.parse_args()
print("abcd")

try:
    loop = asyncio.get_event_loop()
    # Check if the loop is running
    if loop.is_running():
        # If it's running, create a new task
        task = loop.create_task(sendtelegram(args.file))
        

        
        print("start")
          # Yield control to the event loop
    else:
        print("end")
        # If not running, run the main function normally
        loop.run_until_complete(sendtelegram(args.file))
        bot2.run_until_disconnected()
    
        

except RuntimeError:  # No event loop running
    asyncio.run(sendtelegram(args.file))
    print("man")
    
    
    
    

    
   
 
    

