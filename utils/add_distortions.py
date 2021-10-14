import numpy as np
import cv2

'''
    This function add horizont motion blur to an image 
'''

def get_horizont_motion_blur(img, kernel_size = 50):
      
    # Create the vertical kernel. 
    kernel_h = np.zeros((kernel_size, kernel_size)) 

    #Fill the middle row with ones. 
    kernel_h[int((kernel_size - 1)/2), :] = np.ones(kernel_size) 

    # Normalize. 
    kernel_h /= kernel_size 

    # Apply the horizontal kernel to the input image
    horizonal_mb = cv2.filter2D(img, -1, kernel_h) 
    return horizonal_mb


# Similarly for vertical motion

def get_vertical_motion_blur(img, kernel_size = 50):
    kernel_v = np.zeros((kernel_size, kernel_size)) 
    kernel_v[:, int((kernel_size - 1)/2)] = np.ones(kernel_size)   
    kernel_v /= kernel_size 
    vertical_mb = cv2.filter2D(img, -1, kernel_v) 
    return vertical_mb
