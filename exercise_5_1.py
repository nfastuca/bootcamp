import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import glob
sns.set_style('dark')

#for image processing
import skimage.io
import skimage.exposure
import skimage.morphology
import skimage.filters
import skimage.segmentation

import image_processing_practice as ipp
# Loads files in numerical order
file_names = np.sort(glob.glob('data/bacterial_growth/*.tif'))

#Append image data to images
images = []
for name in file_names:
    images.append(skimage.io.imread(name))

#segment image using function from IPP
seg_ims = []
labeled_imgs = []
rgbs = []
for image in images:
    seg_im = ipp.segment(image)
    seg_ims.append(seg_im)
    im_labeled, _ = ipp.label_cells(image)
    labeled_imgs.append(im_labeled)
    #confused on rgb images
    im_rgb = np.dstack(3 * [ipp.med_filt(image) / ipp.phase_filt(image).max()])
    im_rgb[im_bw_filt, 0] = 0
    im_rgb[im_bw_filt, 1] =
    im_rgb[im_bw_filt, 2] = 0
