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

def main():
    _images = load_images()
    print(_images)
    print(IMAGE_PATH)
if __name__ == "__main__":
    main()

