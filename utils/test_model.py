import cv2
import os
import numpy as np

import sys
sys.path.append('../')
sys.path.append('../utils/')
sys.path.append('../brisque')
import imquality.brisque as brisque
from brisque import BRISQUE
from show_image import draw_image
from add_distortions import get_horizont_motion_blur

def mean_absolute_percentage_error(y_true, y_pred): 
    return np.mean(np.abs((np.array(y_true) - np.array(y_pred)) / np.array(y_true))) * 100

def mse(y_true, y_pred):
    return np.mean((np.array(y_true) - np.array(y_pred)) ** 2)

def r2(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    return 1 - (np.sum((y_true - y_pred) ** 2))/(np.sum((y_true - np.mean(y_true)) ** 2))



def test_reg(estimator, path_test_images = '../data/test_images' , show_images = True, num_imgs = 15, target_area = None):
    '''
    Make predictions on test images (from dataset of another production place) and their distorted version, 
    calculate metrics and shows results 
    
    If target_area != None, crops the target area from image
    In this case target area represents tuple ([y1, y2], [x1, x2]), where x1, x2, y1, y2 - the bounds of target area
    num_imgs - number of showed images.
    
    
    '''
    y_pred = []
    y_true = []
    brisq = BRISQUE()
    count = 0
    for img_name in os.listdir(path_test_images):
        if img_name == '.DS_Store':
            continue
        img = cv2.imread(os.path.join(path_test_images, img_name))
        if target_area != None:
            y1, y2 = target_area[1]
            x1, x2 = target_area[0]
            img = img[y1: y2, x1 : x2]
        def make_pred(img, true_label):
            pred_label = estimator.predict(brisq.get_feature(img).reshape(1, -1))
            y_true.append(true_label)
            y_pred.append(pred_label[0])
            nonlocal count
            if show_images and count < num_imgs:
                draw_image(img, f' pred label: {int(pred_label[0])} true label {true_label}')
                count += 1
        
        make_pred(img, true_label = 10)
        for distort_param in [15, 25]:
            true_label = 40 if distort_param == 15 else 60
            blur_img = cv2.blur(img, (distort_param, distort_param))
            horizont_blur_img = get_horizont_motion_blur(img, kernel_size = distort_param)
            make_pred(blur_img, true_label)
            make_pred(horizont_blur_img, true_label)

            
    return y_true, y_pred, mean_absolute_percentage_error(y_true, y_pred), mse(y_true, y_pred)
