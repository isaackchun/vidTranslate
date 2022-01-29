from fileinput import filename
from cv2 import findChessboardCornersSBWithMeta
import Google_Vision_Translate
import cv2
import os
import pandas as pd
import shutil
import datetime
import time

def work_directory(path):
    read_path = None
    while read_path is None:
        try:
            os.chdir(path)
            read_path = True
        except FileNotFoundError:
            print("Directory: {0} does not exist".format(path))
            path = input("PATH: ")
            pass
        except NotADirectoryError:
            print("{0} is not a directory".format(path))
            path = input("PATH: ")
            pass
        except PermissionError:
            print("You do not have permissions to change to {0}".format(path))
            path = input("PATH: ")
            pass
        except:
            print("Bad input")
            path = input("PATH: ")
            pass

    return path

def open_file(file_name):
    read_file = None
    while read_file is None:
        
        try:
            file = open(file_name)
            file.close()
            read_file = True
        except FileNotFoundError:
            print("File: {0} does not exist".format(file_name))
            file_name = input("FILE NAME: ")
            pass
        except:
            print("Bad input")
            file_name = input("FILE NAME: ")
            pass
    
    return file_name

def extractImages(pathIn, pathOut, start, end, increment):
    vidcap = cv2.VideoCapture(pathIn)
    success, image = vidcap.read()
    while success and start <= end:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(start*1000))
        success, image = vidcap.read()
        cv2.imwrite(pathOut + "\\%d.jpg" % start, image)
        start += increment
    vidcap.release()
    cv2.destroyAllWindows()

def get_duration(filename):
    video = cv2.VideoCapture(filename)
    if video.isOpened() == False:
        return - 1
    duration = video.get(cv2.CAP_PROP_POS_MSEC)
    #frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

    return duration # frame_count


path = input("PATH: ")
path = work_directory(path)

file_name = input("FILE NAME: ")
file_name = open_file(file_name)

# temp folder to save images extracted from video
temp = os.path.join(path, "temp")
os.mkdir(temp)


# getting time info 
time_start = input("Enter the start time in 00:00:00 format: ")
x = time.strptime(time_start.split(',')[0],'%H:%M:%S')
time_start = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()

time_end = input("Enter the end time in 00:00:00 format: ")
x = time.strptime(time_end.split(',')[0],'%H:%M:%S')
time_end = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()

time_increment = int(input("Seconds between each extracted image: "))

# extracting
extractImages(os.path.join(path,file_name), temp, time_start, time_end, time_increment)

df = pd.DataFrame(columns = ['locale', 'description', 'translation', 'frame'])

for filename in os.listdir(temp):
    f = os.path.join(temp, filename)
    
    texts = Google_Vision_Translate.detectText(f)
    for text in texts:
        #if detected language matches target language append
        result = Google_Vision_Translate.translate_text("en", text.description)
        print(text.description)
        df = df.append(
            dict(
                locale = text.locale,
                description = text.description,
                translation = result["translatedText"],
                frame = str(datetime.timedelta(seconds = int(filename[:-4])))
            ),
            ignore_index = True
        )

df.to_csv(str(os.path.splitext(file_name)[0]) + '_translated.csv')


# delete temp directory
shutil.rmtree(temp)



