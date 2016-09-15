import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#for image processing
import skimage.io
import skimage.exposure
import skimage.morphology
import skimage.filters

#load image
phase_im = skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')

def illum_correct(phase_im):
    """
    Corrects for uneven illumination in an image by subtracting a gaussian
    blur of the input from the input.
    """
    # Apply a gaussian blur to the image.
    im_blur = skimage.filters.gaussian(phase_im, 50.0)

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
