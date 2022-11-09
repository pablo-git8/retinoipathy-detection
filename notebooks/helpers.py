# skimage imports
from skimage import data, color, filters, morphology, graph, measure, exposure
from skimage.filters import threshold_otsu, threshold_local, try_all_threshold, sobel, gaussian
from skimage.transform import rotate, rescale, resize
from skimage.feature import canny
from skimage.io import imsave
from skimage.util import img_as_ubyte
# scipy for image
from scipy import ndimage as ndi
# import for file interaction
import os
import io
# imports for reading from zip files
import zipfile
from PIL import Image
# array and data frame imports
import numpy as np
import pandas as pd
#pip install xlrd
# visualization tools
import matplotlib.pyplot as plt


######## HELPER FUNCTION TO PARSE EACH IMAGE FILE

def parse_images(file_names, dir_path, op='original', height=800, width=800):
    # variables for reshaping
    #height = 744 # 744 372
    #width = 1120 # 1120 560

    for file in file_names:
        # reading the zip files
        if '.zip' in file:
            # reading internal files
            zip_file = zipfile.ZipFile('{}\data\{}'.format(dir_path, file))
            for int_file in zip_file.namelist():
                # reading tif files
                if '.tif' in int_file:
                    ifile = zip_file.open(int_file)
                    img_nparray = np.asarray(Image.open(ifile)) # converting them to np.arrays
                    int_file = remove_base_x(int_file, ch='/')
                    if op == 'original':
                        imsave('{}\data_processed\data_original\{}'.format(dir_path, int_file), img_nparray) # Saving images to path
                    if op == 'resize':
                        image_resized = resize(img_nparray, (height, width)) # Resize image using height and width
                        image_resized = img_as_ubyte(image_resized)
            print('{} file read!'.format(file))


######## HELPER FUNCTION FOR READING ZIP FILES 

def read_zip(zip_fn, extract_fn=None):
    '''
    Helper function for reading excel label files from zip files
    '''
    zf = zipfile.ZipFile(zip_fn)
    if extract_fn:
        return zf.read(extract_fn)
    else:
        return {name:zf.read(name) for name in zf.namelist()}


######## HELPER FUNCTION TO SWAP COLUMNS IN A DATA FRAME

def swap_columns(df, col1, col2):
    col_list = list(df.columns)
    x, y = col_list.index(col1), col_list.index(col2)
    col_list[y], col_list[x] = col_list[x], col_list[y]
    df = df[col_list]
    return df


######## HELPER FUNCTION TO REMOVE 'BaseX' STRING FROM IMAGE NAME

def remove_base_x(str_value, ch='/'):
    list_words = str_value.split(ch, 1)
    try:
        return list_words[1]
    except:
        return str_value


######### HELPER FUNCTION TO FOR SHOWING AND PLOTTING IMAGES

def show_image(image, title="Image", cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()
    print(type(image), image.shape)