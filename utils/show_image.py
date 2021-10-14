import cv2
from matplotlib import pyplot as plt


# Supporting functions for printing images

def image_for_plot(im):
    return cv2.cvtColor(im, cv2.COLOR_BGR2RGB)


def draw_image(img, img_name = None):
    plt.figure(figsize = (38, 21))
    plt.imshow(image_for_plot(img))
    plt.title(img_name, size = 30)

def compare_images(im1, imgs):
    plt.figure(figsize = (38, 21))
    plt.imshow(image_for_plot(im1))
    for im in imgs:
        plt.figure(figsize = (38, 21))
        plt.imshow(image_for_plot(im))
