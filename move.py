import os, shutil

source = r'C:\Users\<Your windows username>\Downloads'
destination_images = r'C:\Users\<Your windows username>\Downloads\images'
destination_exe = r'C:\Users\<Your windows username>\Downloads\execute'
destination_videos = r'C:\Users\<Your windows username>\Downloads\videos'
destination_docs = r'C:\Users\<Your windows username>\Downloads\docs'

os.chdir(source)

print(os.getcwd())
for file in os.listdir():
    try:
        if "jpg" in file or "jpeg" in file or "png" in file or "raw" in file:
            shutil.move(file, destination_images)
            print(file)
        elif "doc" in file or "pdf" in file or "txt" in file:
            shutil.move(file,destination_docs)
        elif "exe" in file or ".zip" in file:
            shutil.move(file, destination_exe)
        else:
            if ".mp4" in file or ".mov" in file or ".wmv" in file or ".avi" in file:
                shutil.move(file, destination_videos)

    except shutil.Error:
        continue
