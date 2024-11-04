from . import *
import imaplib
import email
import re
from email.header import decode_header
import time
import csv
idcheck = []
l = {}
url = {}
vehicle = {}
@bot.on(events.callbackquery.CallbackQuery(data="profile"))
async def profile(event):
    idchecker = []
    prof = {}
    with open(r"bot/plugins/database/profile.csv", "r") as f2:
        wr = csv.DictReader(f2)
        for row in wr:
            idchecker.append(int(row['id'])) 
            prof[row["id"]]=row
            print(prof)
            
    print(idchecker)
    print(prof)
    if event.sender_id in idchecker:
        await event.edit(f'''
Profile Data-:
    Name -   {prof[str(event.sender_id)]['Name']}  
    Vehicle - {prof[str(event.sender_id)]['Vehicle']}  
    Current Latitude - {prof[str(event.sender_id)]['Latitude']}  
    Current Longitude - {prof[str(event.sender_id)]['Longitude']}             ''')
    
    else:
        await bot.send_message(event.sender_id, "What is Your Name?")


        @bot.on(events.NewMessage)
        async def handle_message(event):
        # This will be triggered for any new message
           Name = event.message.message
           l[event.sender_id]=Name
           print(l)
           print(Name)
        


        
        
    #     if Vehicle and Vehicle not in l:


           if Name and event.sender_id not in idcheck:
                text = '''TEXT CAN BE CUSTOMIZED
            1. Go To google maps
            2. click your profile icon.
            3. Tap On location sharing
            4. SWITCH THE TIMINGS TO UNTIL YOU TURN IT OFF
            5. SHARE THE LOCATION ACCESS TO Pandeytanmay978@gmail.com
            and after doing press the yes button below
            Note -: Never stop sharing your location else you wont get orders.'''
                await bot.send_message(event.sender_id, text, buttons=Button.inline("yes", data="yes"))
                id = event.sender_id
                idcheck.append(event.sender_id)
                print(id)
            
            



@bot.on(events.callbackquery.CallbackQuery(data="yes"))
async def yes(event):
    await event.edit("Wait Until I grab it.....")
# Set your email and app password
    

# Your email credentials
    username = "hackw565@gmail.com"
    password = "hjrt dwqv gitb dvzu"  # Use your app password if 2FA is enabled

    def connect_to_gmail():
        # Connect to Gmail IMAP server
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(username, password)
        return mail

    def fetch_emails(mail):
        # Select the inbox
        mail.select("inbox")

    # Search for all emails
        result, data = mail.search(None, "ALL")
        email_ids = data[0].split()

    # Fetch the latest email
        latest_email_id = email_ids[-1]

    # Fetch the email by ID
        result, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = msg_data[0][1]

    # Parse the email content
        msg = email.message_from_bytes(raw_email)
        return msg

    def print_email_content(msg):
        # Decode email subject
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else 'utf-8')
    
        print("Subject:", subject)

    # If the email message is multipart
        if msg.is_multipart():
            for part in msg.walk():
                # Extract content type of the email
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

            # Get the email body
                if content_type == "text/plain" and "attachment" not in content_disposition:
                    body = part.get_payload(decode=True).decode()
                    print("Body:", body)
                    url[event.sender_id]=body
                
        else:
            # If the email is not multipart
            body = msg.get_payload(decode=True).decode()
            print("Body:", body)
            url[event.sender_id]=body
    await event.edit("Grabbed successfully..")

    

    def main():
        mail = connect_to_gmail()
    
        
        msg = fetch_emails(mail)
        print_email_content(msg)
        # time.sleep(30)  # Wait for a minute before checking for new emails
    main()
    await event.edit("One Last Question for you....", buttons=Button.inline("answer",data="vehicle"))
    
    


@bot.on(events.callbackquery.CallbackQuery(data="vehicle"))
async def vehicles(event):
    await bot.send_message(event.sender_id, "Which Vehicle Do You Have?")
    @bot.on(events.NewMessage)
    async def handle(event):
    # This will be triggered for any new message
        veh = event.message.message
        vehicle[event.sender_id]=veh
        print(veh)
        def parseit(email_body):
            link_pattern = r'https://.*?(?=Learn)'
            print(email_body)
            match = re.search(link_pattern, email_body)
            print(match)

# Extracted link
            extracted_link = match.group(0) if match else "No link found"


            print("Extracted Link:", extracted_link)
            return extracted_link
        d = parseit(url[event.sender_id])
        
        s = getlatlong(d)
        print(s)

        lat = s[0]
        longi = s[1]
    
        with open(r"bot/plugins/database/profile.csv", "a") as f:
            wr = csv.writer(f)
            wr.writerow([event.sender_id, l[event.sender_id], d, vehicle[event.sender_id],lat, longi])




