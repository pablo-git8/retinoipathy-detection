# skimage imports
from skimage import data, color, filters, morphology, graph, measure, exposure
from skimage.filters import threshold_otsu, threshold_local, try_all_threshold, sobel, gaussian
from skimage.transform import rotate, rescale, resize
from skimage.feature import canny
from skimage.io import imsave
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


######### HELPER FUNCTION TO FOR SHOWING AND PLOTTING IMAGES

def show_image(image, title="Image", cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()
    print(type(image), image.shape)