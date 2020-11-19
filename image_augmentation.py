#Importing class
import argparse
import os
import sys
from pathlib import Path
from numpy import expand_dims
import cv2
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import ImageDataGenerator

#Creating instance of the ImageDataGenerator class
datagen = ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        rescale=1./255,
        shear_range=0.5,
        zoom_range=0.1,
        horizontal_flip=True,
        brightness_range=[0.5,1.0], 
        fill_mode='nearest'
        )

        

def run_image(entry, augmented_image_path):
    try:
        # load the image
        img=cv2.imread(entry.path)
        
        
        # converting to numpy array
        data = img_to_array(img)
        
        # expanding the dimension to one sample
        samples = expand_dims(data, 0)

        # creating image data augmentation generator
        datagen = ImageDataGenerator(
            rotation_range=5, 
            #horizontal_flip=0, 
            brightness_range = [0.5,1.0], 
            width_shift_range=0.1, 
            height_shift_range=0.1,
            zoom_range=0.1
        )

        # preparing iterator
        it = datagen.flow(samples, batch_size=1)
        
        cv2.imwrite('{}/{}_aug_org.jpg'.format(augmented_image_path, entry.name,), img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        # generating samples and plotting
        for i in range(2):
            # generating batch of images
            batch = it.next()
            # converting to unsigned integers for viewing
            image = batch[0].astype('uint8')
            cv2.imwrite('{}/{}_aug_{}.jpg'.format(augmented_image_path, entry.name, i), image,[int(cv2.IMWRITE_JPEG_QUALITY), 100])
    
    except OSError as e:
        print(e)
    
    except:
        print('An exception occurred')


def main(args):
    with os.scandir(args.image_path) as entries:
        for entry in entries:
            if entry.is_file():
                # Read image
                print('Reading image file {}'.format(entry.name))
                try:
                
                    augmented_image_path = Path(os.path.join('{}_augmented'.format(entry.path)))
                    augmented_image_path.mkdir(exist_ok=True)
                    run_image(entry, augmented_image_path)
                    
                except OSError as e:
                   print(e)


def parse_arguments(argv):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--image_path", default='image', help="images for augmentation", type=str, )    
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
