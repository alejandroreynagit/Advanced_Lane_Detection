# **Finding Lane Lines on the Road** 

## Writeup - Daniel Alejandro Reyna Torres

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./test_images_output/solidWhiteCurve_lanes.png "Pipeline"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps described as following:

- Since HLS seems to provide better contrast for detecting lanes (previous tests, they are in the Notebook), I first transform the RGB image to the HLS space.
- Yellow and white filters are set up.
- Both filters are combined and applied to my original (coloured) frame.
- The resultant image is converted to grayscale.
- A gaussian smoothing filter is applied in order to remove noise on the image, make the edges more soft.
- After the gaussian filter, I detect edges by applying the canny method.
- A ROI (region of interest) is defined in order to process only the section where I want to detect lanes. 
- Using the hough line method from opencv I extract all lines in the hough space.
- Now, I have lines that I used for predicting the whole lane in the frame.
- Finally, the resultant image (original frame + predicted lanes) are shown.

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by computing the slope, interception and length for each line detected. By doing so, I could separate left-lane-components (positive slope) and right-lane-components (negative slope). I then, averaged all lines so the resultant values are used to compute the "x" positions for the predicted lane. The "y" positions are fixed to the bottom and a fraction of the bottom of the image for the prediction.

The next image show the pipeline steps:

![alt text][image1]


### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be that sometimes there are some "jumps" in some frames. I think this is happeninig because something is missing in the color filtering section or because the way I am predicting the fane lane line is not that effective.

Another shortcoming would be the shadows! Although I think my code performs well, is not perfect. I tested about 21 different frames to ensure the code was working ok and to make adjustments. The output of theses images are in the notebook.


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to keep tunning filters, specially the white one. As you can see in the pipeline images, yellow and white are well extracted but also some blue (sky)! I think if I try an HSV filter can also be a good option.

Another potential improvement that would be very hulpful would be to include some lane tracking, i.e., we know lanes follow a line and if we suppose this line is not moving that much we then can adapt our resultant lanes to this, at least to avoid big jumps between frames, which happens in some of them. I am thinking on keeping kind of a buffer or just saving past frame values (lane position) and use them in the current one. 

### 4. Overall thoughts

This project has been challenging and very interesting, small pieces of code can bring a huge result, if they are well done. A mistake can take everything down though. Debugging in this case of scenarios is pretty different, in a good way, because we can visualise the results through images and not just numbers!


