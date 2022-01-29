# vidTranslate

This is a program that translates the detected texts from videos to English

This program could be used for situation like:
  
  Japanese vlog contains a Japanese menu that doesn't have English description


This program uses OpenCV to extract frames from the Video then sends it to Google Cloud Vision API to detect texts within the frames. Then the texts are sent to Google Translate API to be translated. Then the retrieved results are saved as data frame in csv file

To use:

1. input the directory path which contains the video you would like to translate
2. input the name of the video including the extension
3. Enter the starting time frame you would like to start translating from in --:--:-- format
        ex: "00:00:00" would be the start of the video
4. Enter the ending time frame you would like to stop translating
5. Enter the time between each translated frame in seconds
        ex: 1, 2, 3, 4, ...


Warning:
  The program will create "temp" folder to saved the extracted frames (this will be deleted after translation process is done). Avoid having a folder named "temp" inside the working directory before starting the program.
