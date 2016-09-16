import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#for image processing
import skimage.io
import skimage.exposure
import skimage.morphology
import skimage.filters
import skimage.segmentation

#load image
phase_im = skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')

def med_filt(phase_im):
    """
    Median filter to remove artificially high pixels. Returns edited image file.
    """
    selem = skimage.morphology.square(3)
    im_cfp_filt = skimage.filters.median(phase_im, selem)
    return im_cfp_filt


def illum_correct(phase_im):
    """
    Corrects for uneven illumination in an image by subtracting a gaussian
    blur of the input from the input.
    """

    filt_im = med_filt(phase_im)

    # Apply a gaussian blur to the image.
    im_blur = skimage.filters.gaussian(filt_im, 50.0)

    #Convert image file to array of normalized floats
    phase_float = skimage.img_as_float(phase_im)

    #subtract gaussian blur from normalized image to correct uneven ilumination
    phase_sub = phase_float - im_blur

    return phase_sub

def segment(phase_im):
    """
    Converts illum corrected image to an array of bools evaluated  for
    otsu threshold intensity
    """
    phase_sub = illum_correct(phase_im)
    #Apply otsu thresholding to illum corrected image
    thresh = skimage.filters.threshold_otsu(phase_sub)
    seg = phase_sub < thresh
    return seg

def border_remove(phase_im):
    """Remove any objects near the border"""
    return skimage.segmentation.clear_border(segment(phase_im), buffer_size=5)

def label_cells(phase_im):
    """
    Labels objects with indicies from filtered, illum corrected, border
    corrected data.  Returns labeled image and number of objects.
    """
    im_labeled, n_labels = skimage.measure.label(border_remove(phase_im),
                                                 background=0, return_num=True)
    return im_labeled, n_labels

def area_cells(phase_im, low=300, high=700):
    """
    computes properties of all objects and converts those outside of (low, high)
    to background by assigning label of 0
    """
    #create array of labeled objects
    im_labeled, _ = label_cells(phase_im)
    # Compute properties of labeled objects
    im_props = skimage.measure.regionprops(im_labeled)
    #Create a copyw w/ background object removed
    im_bw_filt = im_labeled > 0
    #
    n = 0
    for prop in im_props:
        # Remove properties w/ area <low or > high
        if prop.area < low or prop.area > high:
            #Change index of prop outside of region in the copy 'im_bw_filt'
            #to 0 (==background)
            im_bw_filt[im_labeled==prop.label] = 0
        #If within area range, count it!
        else:
            n += 1

    return im_bw_filt, n
