# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 22:32:03 2021

@author: PC - CASA
"""
import numpy as np
from PIL import Image  
from numpy import asarray
  
def main():
    
    # Open image
    image = Image.open('C:/Users/PC - CASA/Downloads/Nova pasta (4)/img/tbt_silvie.png')
    print(image.format)
    print(image.size)
    print(image.mode)
    print(image.bits)
    print(image.getextrema())
    
    # convert image to numpy array    
    npImage = np.array(image) 
    print(type(npImage ))
    
    # summarize shape
    print(npImage.shape)
    
    # value of pixel 0 0
    print(npImage[0][0])
    print(npImage[10][10])

    # values os a windows 5 X 5 
    print(npImage[0:5, 0:5])

    # divide by 2 pixels
    npImage =  (npImage / 2).astype(int);

    # values os a windows 5 X 5 
    print(npImage[0:5, 0:5])

#//-----------------------------------------------//
    
   # Change values of lines 10 - 25
   # npImage[10:25,:] = 255;

   # Change values of columns 10 - 25
   # npImage[:,10:25] = 0;

#//-----------------------------------------------//
            
# Teste para inversão de valores de pixels

    w, h = npImage.shape
    for x in range(w):
        for y in range(h):
            npImage[x, y] = abs(npImage[x, y] - 255)

#//-----------------------------------------------//

    #Convert ndarray image to Pillow image
    image2 = Image.fromarray(npImage)
    image2.show()

    image2.save('C:/Users/PC - CASA/Downloads/Nova pasta (4)/img_f/tbt_preto_e_branco.jpg')

    # create the histogram
    histogram, bin_edges = np.histogram(npImage, bins=256, range=(0, 255))
    print(histogram.shape)
         
if __name__ == "__main__":
    main()