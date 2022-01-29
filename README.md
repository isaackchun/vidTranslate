# vidTranslate

This is a program that translates the detected texts from videos to English
This program could be used for situation like:
  Japanese vlog contains a Japanese menu that doesn't have English description


This program uses OpenCV to extract frames from the Video then sends it to Google Cloud Vision API to detect texts within the frames. Then the texts are sent to Google Translate API to be translated. Then the retrieved results are saved as data frame in csv file

