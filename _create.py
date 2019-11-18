import os 
import random
from src.image_augmentation import preprocess_dict, path_create
from src.image_augmentation import load_images
import Automold.Helpers as hp 
import Automold.Automold as am
import matplotlib.pyplot as plt 

IMAGE_PATH = './image'
_files = os.listdir(IMAGE_PATH)
print("Number of files {}".format(len(_files)))


def main():
    _ix = random.randint(1, len(_files) )
    #_files[_ix]
    IMAGE_PATH = os.path.join('./image', _files[_ix])
    _images = load_images()
    _dict = preprocess_dict()
    print(_dict)
    darken_im =  _dict['darken'](_images)
    hp.visualize(darken_im)    


if __name__ == "__main__":
    main()
