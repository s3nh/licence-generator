"""
Allows you to generate licence plate 
"""
import os
import yaml
import numpy as np  
from setuptools import setup, find_packages
from PIL import Image 
from PIL import ImageFont, ImageDraw
import random
import string
CONFIG_PATH = None
IMAGE_PATH = 'image'
letters = string.ascii_uppercase
digits = string.digits

def gen_plate():

    TWN = [''.join(random.choice(string.ascii_uppercase)) for _ in range(2)]
    DIGITS = [''.join(random.choice(string.ascii_uppercase + string.digits)) for i in range(5)]
    plate = ''.join([el for el in TWN]) + "  " + ''.join([el for el in DIGITS])
    return plate


def example_demo(folder = IMAGE_PATH):
    text = gen_plate()
    """
    Example from docs
        Reference :
         https://pillow.readthedocs.io/en/3.0.x/reference/ImageFont.html
   """
    image = Image.fromarray(np.array(np.zeros((300, 300 ))+240))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("font/arklatrs-webfont.ttf", 115)
    draw.text((0, 0), text, font = font)
    image = image.convert('RGB')
    image.save(os.path.join(folder, '{}.png'.format(text)))    
    
    print("Image {} saved in {}".format(text, os.path.join(folder)))

def read_yaml_config(conf_path = CONFIG_PATH):
    with open(conf_path, 'r') as confile:
        _config = yaml.safe_load(confile)
    return _config 

def test_gen():
    """
    Example testing image
    """

def main():
   _font =  example_demo()
   print(_font)
    
if __name__ == "__main__":
    main()