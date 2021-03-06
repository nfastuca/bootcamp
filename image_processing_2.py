import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')

import skimage.io
import skimage.filters
import skimage.measure
import skimage.segmentation

#load an example phase images
phase_im = skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')

#show the image
plt.imshow(phase_im, cmap=plt.cm.viridis)
plt.show()
plt.close()

# Apply a gaussian blur to the image.
im_blur = skimage.filters.gaussian(phase_im, 50.0)

# Show blurred image
#plt.imshow(im_blur, cmap=plt.cm.viridis)

# Convert our phase image to a float
phase_float = skimage.img_as_float(phase_im)
phase_sub = phase_float - im_blur

#show both
plt.figure()
plt.imshow(phase_float, cmap=plt.cm.viridis)
plt.title('original')

plt.figure()
plt.imshow(phase_sub, cmap=plt.cm.viridis)
plt.title('subtracted')

plt.show()

plt.close()

#Apply otsu thresholding
thresh = skimage.filters.threshold_otsu(phase_sub)
seg = phase_sub < thresh

#Plot segmentation
plt.close('all')
plt.imshow(seg, cmap=plt.cm.Greys_r)

#Label them
seg_lab, num_cells = skimage.measure.label(seg, return_num=True, background=0)
plt.close()
plt.imshow(seg_lab, cmap=plt.cm.Spectral_r)

#compute the region properties and extract the area of each object.
ip_dist = 0.063 #um/pixel
props = skimage.measure.regionprops(seg_lab)

#Get the areas as an array
areas = np.array([prop.area for prop in props])
cutoff = 300

#Binary copy of original image
im_cells = np.copy(seg_lab) > 0

#removing segments smaller than 300
for i, _ in enumerate(areas):
    if areas[i] < cutoff:
        #this line confuses me
        im_cells[seg_lab==props[i].label] = 0

area_filt_lab = skimage.measure.label(im_cells)

plt.figure()
plt.imshow(area_filt_lab, cmap=plt.cm.Spectral_r)
