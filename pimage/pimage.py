# functions for the pimage library

import cv2
import numpy as np

# loads an image using cv2 & converts the colour space. By default will read the image in grayscale
# Returns 1 on fail to read, returns 2 on invalid colour space
def load_image(filename, colour_space="gray"):

    try:
        # read the image
        if colour_space == "rgb":
            im = cv2.imread(filename, cv2.IMREAD_COLOR)
            # convert the colour space
            im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        elif colour_space == "gray":
            im = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        else:
            return 2

    except Exception as e:
        print(e)
        return 1
    
    return im


# given an image (numpy format) applies the given lambda function to each pixel in the original image & outputs a new image
def single_pixel_operation(im, function):

    g = np.zeros(im.shape)

    # use numpy nditerate function
    for i, l in np.ndenumerate(im):
        # i is a tuple containing the x & y values, l is the gray value

        # apply the function to the gray at that location
        g[i[0]][i[1]] = function(l)

    return g