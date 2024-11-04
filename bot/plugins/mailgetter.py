import boto3
import os
import re
import json
import time
import asyncio
from telethon import TelegramClient, events, Button
import logging
import argparse
import asyncio
import json
import ast
from getlatitudes import get_lat_lon
from comparedist import comparedistance
bidd = []
parseit= {}
import subprocess
bidder = {}


# AWS Credentials
aws_access_key_id = 'AKIA2MNVLRQ75RKRYWPM'  # Replace with your AWS access key
aws_secret_access_key = 'N72n0jMFtxfVvwORCKzwcVU7Xyt1ZPisk7WkcsiE'  # Replace with your AWS secret key
aws_region = 'us-east-2'  # Replace with your AWS region
def list_files_in_directory(directory):
    # List all files in the specified directory
    files = os.listdir(directory)
    # Filter out directories, only keep files
    file_names = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    return file_names

# Example usage
directory_path = r'C:\Users\pande\OneDrive\Desktop\bot\emails'  # Change this to your folder path
downloaded_files = list_files_in_directory(directory_path)
print(downloaded_files)

# Configuration
bucket_name = 'lemmerecieveit'  # Replace with your bucket name
output_directory = 'emails/'  # Local directory to save emails
processed_prefix = 'processed-emails/'  # Prefix for processed emails

# Ensure output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Initialize S3 client with AWS credentials
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

async def main():
    while True:
        
        # List objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=processed_prefix)
        
        if 'Contents' in response:
            for obj in response['Contents']:
                email_key = obj['Key']
                file_name = email_key.split('/')[-1]  # Get the file name

                # Download new files
                if file_name not in downloaded_files:
                    s3_client.download_file(bucket_name, email_key, f'{output_directory}{file_name}')
                    print(f'Downloaded {file_name}')
                    downloaded_files.append(file_name)


                    # Read the content of the downloaded file
                    with open(f'{output_directory}{file_name}', 'r') as f:
                        body = f.read()
                        
        # Find the section between "bid on order" and "notes"
                        



# Define patterns for extraction
                        def parse_email(body): 
                            parsed_info = {}
                            lines = body.splitlines()
                            for i, line in enumerate(lines):
                                line = line.strip()  # Remove whit  
                                if line.startswith("*Bid on Order #"):
                                    parsed_info["order_id"] = line.split("#")[1].strip()
                                elif line.startswith("Pick-Up"):
                                    parsed_info["PickupLocation"] = lines[i + 2].strip()  # Next line
                                    parsed_info["PickupTime"] = lines[i + 4].strip()  # Next line (ASAP)
                                elif line.startswith("Delivery"):
                                    parsed_info["DeliveryAddress"] = lines[i + 2].strip()  # Next line
                                    parsed_info["DeliveryTime"] = lines[i + 4].strip()  # Next line (date and time)
                                elif "STOPS" in line:
                                    parsed_info["Stops"] = line
                                elif line.startswith("*Broker Name:"):
                                    parsed_info["Broker Name"] = line[12:].strip()
                                elif line.startswith("*Broker Phone:"):
                                    parsed_info["Broker Phone"] = line[13:].strip()
                                elif line.startswith("*Email:"):
                                    parsed_info["Broker Email"] = line[6:].strip()
                                elif line.startswith("*Posted:"):
                                    parsed_info["Posted"] = line[7:].strip()
                                elif line.startswith("*Expires:"):
                                    parsed_info["Expires"] = line[8:].strip()
                                elif line.startswith("*Dock Level:"):
                                    parsed_info["Dock Level"] = line[11:].strip()
                                elif line.startswith("*Hazmat:"):
                                    parsed_info["Hazmat"] = line[7:].strip()
                                elif line.startswith("*Posted Amount:"):
                                    parsed_info["Posted Amount"] = line[15:].strip()
                                elif line.startswith("*Load Type:"):
                                    parsed_info["VehicleRequired"] = line[10:].strip()
                                elif line.startswith("*Pieces:"):
                                    parsed_info["Pieces"] = line[7:].strip()
                                elif line.startswith("*Weight:"):
                                    parsed_info["Weight"] = line[7:].strip()
                                elif line.startswith("*Dimensions:"):
                                    parsed_info["Dimensions"] = line[11:].strip()
                                elif line.startswith("*Stackable:"):
                                    parsed_info["Stackable"] = line[10:].strip()
                                elif line.startswith("*CSA/Fast Load:"):
                                    parsed_info["CSA Fast Load"] = line[15:].strip()
                                elif line.startswith("*Notes:"):
                                    parsed_info["Notes"] = line[6:].strip()   
                            return parsed_info

# Pa                                                rse the email
                        parsed_email_info = parse_email(body)

# Pr                        int the extracted information
                        for key, value in parsed_email_info.items():
                            print(f"{key}: {value}")

                        a = parsed_email_info['PickupLocation']
                        m = parsed_email_info['order_id']
                        d = a.strip('*')
                        print(a)
                        print(d)
                        b = get_lat_lon(d)
                        c = comparedistance(b)
                        print(c)
                        tryjson = json.dumps(parsed_email_info)
                        parseit.update(parsed_email_info)
                        
                        for i in c: 
                            print(i)
                            bidd.append(i)
                            v = str(i)
                            print(v)
                            
                            # command = ['python', r'C:\Users\pande\OneDrive\Desktop\bot\bid2.py', tryjson, v]
                            # try:
                            #     result = subprocess.run(command, capture_output=True, text=True, check=True)
                            #     print("Script output:", result.stdout)
                            # except subprocess.CalledProcessError as e:
                            #     print(f"Error occurred while running script: {e}")
                            #     print("Return code:", e.returncode)
                            #     print("Error output:", e.stderr)
                            # except Exception as e:
                            #     print(f"An unexpected error occurred: {e}")
                            from datetime import datetime

                            # Get the current date and time
                            now = datetime.now()

                            # Format the timestamp
                            timestamp_str = now.strftime("%Y%m%d%H%M%S")
                            print("Current Timestamp:", timestamp_str)
                            for i in c:
                                with open(rf"C:\Users\pande\OneDrive\Desktop\bot\bot\plugins\more\{timestamp_str}.txt", 'w') as f:
                                
                                    f.writelines(str(i)+"\n")

                                    f.writelines(tryjson)


# Set up logging
                           
                            # Basics
                            await asyncio.sleep(1)                            

                            





                        
                        
                        
                        
                            

                        
                        
                 
    

                        


                                            

if __name__ == "__main__":
    try:
        asyncio.run(main())
        
        
    except Exception as e:
        print(f"An error occurred: {e}")