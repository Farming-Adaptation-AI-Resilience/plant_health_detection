import matplotlib.pyplot as plt
import numpy as np
from numpy import asarray
from PIL import Image
import os
from os import listdir
from os.path import isfile, join

def split_channels(file_, file_num):
    image = Image.open(file_)
    print(image.size)
    print(image)
    array = asarray(image)
    print(array.shape)


    patch_size = 384

    #channels = ['train_red', 'train_green', 'train_blue']
    channels = ['train_full_color']
    #color = ['red', 'green', 'blue']
    color = ['full_color']
    for channel in range(1):
        width_after = patch_size
        num = file_num
        #num = 1 
        print('New channels\n\n')
        for width in range(0, image.size[0], patch_size):
            print('width:')
            print(width)
            height_after = patch_size
            print('num:')
            print(num)
            print('height')
            for height in range(0, image.size[1], patch_size):
                print(height)
                patch = array[height:height_after,width:width_after, :]
                patch = Image.fromarray(patch)
                patch.save(channels[channel] + '/' + color[channel] + '_training_' + str(num) + '.TIF')
                #plt.savefig('../training/train_gt/ground_truth_' + str(num) + '.tif')
                num+=1
                height_after+=patch_size
                if(height_after > image.size[1]):
                    break

            width_after+=patch_size
            if(width_after > image.size[0]):
                break
    return num


full_color_images_folder = 'RGB/'
files = [f for f in listdir(full_color_images_folder) if isfile(join(full_color_images_folder, f))]
print(sorted(files))
files = sorted(files)
files = [x for x in files if 'IMG' in x]
print(files)

#folders = ['train_red', 'train_green', 'train_blue']
folders = ['train_full_color']
#files.sort()
#print(files)
file_num = 1
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

for file_ in files:
    file_num = split_channels(full_color_images_folder + file_, file_num) 
