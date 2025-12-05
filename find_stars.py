import numpy as np
import scipy as sp
from scipy.ndimage import gaussian_filter


def find_stars(image):
   
    # print(f"Before: min: {np.min(image)} max: {np.max(image)} median: {np.median(image)} length: {len(image)}")
    im = np.array(image)
    
    im = gaussian_filter(im, sigma=1)
    
    noise = np.median(im)
    
    rms = 1.48 * np.median(np.abs(im - noise))
    # print(rms)
    
    threshold = noise + (rms * 5)



    # print(f"After: min: {np.min(im)} max: {np.max(im)} median: {np.median(im)} length: {len(im)}")

    
    
    i,j = np.where(im > threshold)

    
    
    width = 5
    output_i = []
    output_j = []
    tuple_list= []
    
    

    
    for index in range(len(i)):
        
        x , y = i[index] , j[index]
        
        x_min = max(x - width , 0)
        x_max = min(x + width , image.shape[0])
        y_min = max(y - width, 0)
        y_max = min(y + width + 1 , image.shape[1])
        
        one_star = im[ x_min:x_max , y_min:y_max]
        
        if (im[x,y] == np.max(one_star)) and ((x,y) not in tuple_list):
            tuple_list.append((x,y))
            output_i.append(x)
            output_j.append(y)
        # print(x,y)
        
    # print(len(tuple_list))
    i = np.array(output_i)
    j = np.array(output_j)
    return i, j
