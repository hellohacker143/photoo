import pytesseract
import cv2
import numpy as np
from PIL import Image
import re

def extract_numbers(uploaded_file):
    image = Image.open(uploaded_file)
    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    numbers = re.findall(r'\d+', text)
    numbers = [int(n) for n in numbers]

    total = sum(numbers)

    return numbers, total, text