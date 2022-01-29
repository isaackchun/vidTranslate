import io
import os
import pandas as pd
from google.cloud import vision_v1
import six
from google.cloud import translate_v2 as translate


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Enter your service account token here' # ex 'ServiceAccountToken.json'


vision_client = vision_v1.ImageAnnotatorClient()
translate_client = translate.Client()


# using cloud vision api to detect text from the image
def detectText(path):
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision_v1.types.Image(content = content)
    response = vision_client.text_detection(image = image)
    texts = response.text_annotations
    return texts

# using translate api to translate text to target text
def translate_text(target,text):
    result = translate_client.translate(text,target_language = target)
    return result

# detecting given text's language
def detect_language(text):
    result = translate_client.detect_language(text)
    return result
