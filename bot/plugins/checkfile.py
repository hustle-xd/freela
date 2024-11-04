import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

def on_created(event):
    if not event.is_directory:  # Ignore directory events
        print(f'New file created: {event.src_path}')
        # Execute the Python script
        full_path = event.src_path
        # Extract the file name from the full path
        filename = os.path.basename(full_path)
        print(filename)
        
        file = str(filename)
        print(file)
        try:
            result = subprocess.run(['python', r'C:\Users\pande\OneDrive\Desktop\bot\bid2.py', file], capture_output=True, text=True, check= True)
            print("Script output:", result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running script: {e}")
            print("Return code:", e.returncode)
            print("Error output:", e.stderr)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")  
                  # Change to your script


def monitor_folder(folder_path):
    event_handler = FileSystemEventHandler()
    event_handler.on_created = on_created  # Set the event handler function

    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folder_to_monitor = r'C:\Users\pande\OneDrive\Desktop\bot\bot\plugins\more'  # Change this to your target folder
    monitor_folder(folder_to_monitor)
