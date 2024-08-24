import os  
import shutil  
import schedule  
import time  
from pathlib import Path  

# Function to perform the backup  
def backup_files():  
    # Define source folders  
    user_home = Path.home()  
    source_folders = [  
        user_home / 'Desktop',  
        user_home / 'Downloads',  
        user_home / 'Documents'  
    ]  

    # Define backup location on D drive  
    backup_location = Path('D:/Backups')  

    # Create backup directory if not exists  
    if not backup_location.exists():  
        backup_location.mkdir(parents=True)  

    # Define file extensions to back up  
    file_extensions = ('.doc', '.docx', '.jpg', '.png', '.pdf')  

    # Back up files  
    for folder in source_folders:  
        if folder.exists():  
            for root, dirs, files in os.walk(folder):  
                for file in files:  
                    if file.lower().endswith(file_extensions):  # Case-insensitive check  
                        # Define the source file and the target backup path  
                        source_file = Path(root) / file  
                        target_file = backup_location / source_file.relative_to(folder)  # Keep folder structure  
                        
                        # Create target directories if they don't exist  
                        target_file.parent.mkdir(parents=True, exist_ok=True)  

                        # Copy the file  
                        shutil.copy2(source_file, target_file)  # Use copy2 to preserve metadata  
                        print(f'Backed up: {source_file} to {target_file}')  

# Schedule the backup every 3 hours  
schedule.every(3).minutes.do(backup_files)  

print("Har 3 daghighe az file haye mohem mojood dar desktop,downloads,ducuments toye drive D:/backups copy gerefte mishavad \n lotfan in panjere minimize shavad...")  

# Keep the script running  
while True:  
    schedule.run_pending()  
    time.sleep(1)
