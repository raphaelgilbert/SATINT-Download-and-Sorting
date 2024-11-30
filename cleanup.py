import geojson
import os
import json
import re
import cv2
from datetime import datetime
import json
from PIL import Image 
import keyboard
import time
from image_downloading import download_image

from main import run

dir = str(os.path.dirname(__file__)+'\\images')

os.remove(str(dir+'\\temp.png'))
with open('raw.geojson', 'r') as file:
    data = geojson.load(file)

with open(os.path.join(os.path.dirname(__file__), 'preferences.json'), 'r', encoding='utf-8') as f:
    pref = json.loads(f.read())

result = {"type": "FeatureCollection"}

for i in data['features'] : 
    coordinate_rawX, coordinate_rawY= i['geometry']['coordinates'][1], i['geometry']['coordinates'][0]
    lat1 = float(coordinate_rawX + 0.0035)
    lat2 = float(coordinate_rawX - 0.0035)
    lon1 = float(coordinate_rawY - 0.0035)
    lon2 = float(coordinate_rawY + 0.0035)
    img = download_image(lat1, lon1, lat2, lon2, 20, pref['url'],
        pref['headers'], 256, 3)
    
    cv2.imwrite(os.path.join(pref['dir'], 'temp.png'), img)
    print(i['geometry'])
    time.sleep(3)
    img_a_check = Image.open(str(os.path.dirname(__file__)+'\\images\\temp.png'))
    img_a_check.show()
    while keyboard.is_pressed('sapce') == False :
        if keyboard.is_pressed('right') :






#input