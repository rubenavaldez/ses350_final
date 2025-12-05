import numpy as np
import scipy as sp
from scipy.ndimage import *


def measure_stars(image, x, y):
    output = []
    # print(f"Before: min: {np.min(image)} max: {np.max(image)} median: {np.median(image)} length: {len(image)}")

    im = np.array(image)
    
    im = gaussian_filter(im, sigma=1)
    
    im -= np.median(im)
    
    # print(f"After: min: {np.min(im)} max: {np.max(im)} median: {np.median(im)} length: {len(im)}")
    
    width = 3
    
    for index in range(len(x)):
        
        i = x[index]
        j = y[index]
        
        i_min = max(i - width , 0)
        i_max = min(i + width , image.shape[0])
        j_min = max(j - width, 0)
        j_max = min(j + width + 1 , image.shape[1])
    
        one_star = im[ i_min:i_max , j_min:j_max]
        
        onestar_median = np.median(one_star)
        
        flux_one_star = 0
        for pixel in one_star:
            # if pixel > onestar_median:
                # flux_one_star += pixel
            for f in pixel:
                if f > onestar_median:
                    flux_one_star += f
            
        # print(flux_one_star)
        output.append(flux_one_star)
        

        
        
        
        
        
        
    # define your function here to calculate the flux at each
    #  of the positions represented by the vectors x and y 
    #  in the image
    
    # filter the image
    # remove noise
    # loop through the list of indexes
    # create a thumbnail 
    #find the max and minimum
    #add up all the pixels that are not minimum or bright than the median
    
    flux = np.array(output)
    
    # print(flux)
    return flux
    
