import os 
import Automold.Automold as am 
import Automold.Helpers as hp

os.makedirs('rain', exist_ok=True)
os.makedirs('darken', exist_ok=True)
os.makedirs('lighten', exist_ok=True)
IMAGE_PATH = 'image/*.png'

def load_images():
    im = hp.load_images(IMAGE_PATH)
    return im


# Brighten / darken / random_brightness / add_Shadow 
# 


def preprocess_dict():

    funs = {"darken" : am.darken, 
            "brighten": am.brighten, 
            "random_brightness" : am.random_brightness, 
            "add_shadow" : am.add_shadow, 
            "add_autumn" : am.add_autumn, 
            "add_blur" : am.add_blur, 
            "add_snow" : am.add_snow, 
            "add_speed" : am.add_speed, 
            "add_sunflare": am.add_sun_flare
    }

    return funs

def get_images():
    # Create file by file 
    # So list is of files is needed 
    listed_images = os.listdir(IMAGE_PATH)
    print("Number of files to processing {}".format(len(_images)))
    return listed_images _

def main():
    _images = load_images()
    print(_images)
    print(IMAGE_PATH)
    bright_images = am.brighten(_images[0:3])
    hp.visualize(bright_images, column=3)
if __name__ == "__main__":
    main()