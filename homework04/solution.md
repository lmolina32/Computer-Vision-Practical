# Filtering 
I created a script called `generate_imgs.py` that creates imgs in an `img` directory. The images have all the different combinations of kernel size, sigma and lambda. I noticed that with higher sigma the peaks/dips of the sinusoidal are typically higher/lower. I noticed with lambda lower values give more periods in the sinusoidal function where higher lambda values had less periods in the sinusodial function. Similarly the kernel size, when the size was lower the sinusodial funciton had less periods and when the kernel size was higher it had more periods. 

* Filter -> used Kernel size 9, sigma 4, lambda 2. 
* morphological operation -> used kernel size 15, cv2.MORPH_CLOSE (Dilation followed by erosion)
* extra credit -> edge detection used sobel kernel 

# Filtering img 
![Filtering img](/homework04/imgs/filter_pattern.png)

# Binarization img 
![Binarization img](/homework04/imgs/binarization.png)

# Morphological img
![Morphological img](/homework04/imgs/final_image.png)

# Extra Credit
![Sobel kernel](/homework04/imgs/extra_credit.png)
