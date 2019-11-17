import Automold.Automold as am 
import Automold.Helpers as hp

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

