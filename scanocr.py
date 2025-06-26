import easyocr
import cv2 as cv
import re
import random
import os

file_path = "WhatsApp Image 2025-05-06 at 11.41.24 AM.jpeg"

reader = easyocr.Reader(['en'])
img = cv.imread(file_path)
result = reader.readtext(img)
del reader

full_text = ' '.join([detection[1] for detection in result])
print("Full Text:", full_text)
pass

pattern = r'\b\d{2}-\d{5}-\d{6}\b'

match = re.search(pattern, full_text)
if match:
    number = match.group()
    print("Extracted Number:", number)
else:
    print("No matching number found.")