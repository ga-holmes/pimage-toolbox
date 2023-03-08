# pimage-toolbox
A basic image processing toolbox written in Python.
*Garrett Holmes, 2023*

The program is run as a command line tool which can also be used as a library.
OpenCV is used to read image files, all other image transformation operations are done using basic python and numpy.
MatPlotLib is used for image & chart display.

***
## **Features**

### Part 1
- [] Crop an image
- [] Horizontal/Vertical Flip
- [] Change image scale
- [] Rotate image
- Stretch:
    - [] Colour image processing
    - [] Bicubic/Bilinear interpolation (interpolation method)
    - [] Circular/reflected indexing (padding method)
    - [] Horizontal/Vertical shear or other geometric spatial transformations.

### Part 2
- [] Linear gray level mapping
- [] Power law gray level mapping
- [] Image Histrograms
- [] Histogram equalization

### Part 3
- [] Kernel Convolutions on images
    - Specify padding method

***
## **Usage**

### requirements
pip: 

    pip install -r requirements.txt

conda:

    conda create -n [envname] python=[3.10+] pip
    pip install -r requirements.txt

### running the CLI

    python pimage_cli.py

### using the package

    from pimage/pimage import *

***
## **Documentation**

### Defaults
- Interpolation: Nearest Neighbor
- Padding: Zero Padding
