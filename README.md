# Advanced Lane Finding
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

## Writeup - Daniel Alejandro Reyna Torres

In this project, goal is to write a software pipeline to identify the lane boundaries in a video. 

---

## The Project

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

---

## Camera Calibration

The very fist step in this project is camera calibration. We have to be sure that we have under certain control our image acquisition process. In order to deal with distortion caused by the camera we use OpenCV functions to perform the camera calibration. During the calibration process we calculate the distortion matrix and distortion coefficients. These values are used in our images for ***distortion correction***. The following image is one of the images used to perform camera calibration, it can be seen both the original image and one ot the same image but undistorted (edges look straight):

![calibration]

Once we have performed the camera calibration, let's deep dive in the pipeline for lane detection.

---

## **Pipeline**

## Distortion Correction

We apply the distortion correction to one of the the test_images:
![undistorted]

This undistorted image is used as reference for lane detection within the pipeline.

## Threshold Image - Filtering

We apply color and gradient thresholding, i.e., filtering, in order to better detect lanes that will be used for fitting the lane. This is a key step in the pipeline. There are several colorspaces and for this project we explore RGB, HSV, HLS, LAB and the Sobel operator to detect edges (or gradients).

Results of these colorspaces are shown here:

![colorspaces]

On the RGB components, we see that the red channel captures both yellow and white lines. For HSV and HLS, the S channel (saturation) gives the best result on detecting the lane lines. Finally, the LAB colorspace through the B channel seems to detect well only the yellow lines.

The Sobel operator is useful to identify changes in color intensity that allow us to filter line components going in either the vertical or horizontal direction. For this propject we used the HLS colorspace for lane line detection. Results of sobel operator using the S and L channels:
![sobel]

The goal in this section is to find right thresholds for detecting both yellow and white lines of the lane, we should consider that images were taken under different lighting conditions, shades, etc. We have to deal with this in order to perform a stable lane lines detection.

Finally, the thresholded image that we came up with at the end of this process is the following:

![thresholded]

## Perspective Transformation - "Birds-eye-view"

Now that we have our thresholded image we have to select a region of interest (ROI) that will go through a perspective transformation that will turn the image view into a birds-eye-view! This helps when fitting lines for the lane lines.

Since the camera position throughout all the images is constant, we manually defined the 4 ROI points that makes possible the perspective transformation. Lines should appear parallel in the warped image, which corresponds to a top view of the image. The perspective transformation produces the following results:
![roi_warped]

## Lane Fit

Now, let's try to fit the lane. 

We compute a ***histogram*** of the warped image in the y direction. We identify the positions where  pixel intensities are highest. The peaks on the histogram represents an approximation of the lane lines position!

![histogram]

Next is to run a ***sliding window*** search over the warped image, using the peaks of the histogram as starting points, in order to estimate both left and right lane lines. The sliding window runs from bottom to top searching for pixels that belongs to a line. If find a certain numer of pixels, the window is re-centered, this will ensure that lane lines are well estimated. At the end, we fit a 2nd order polynomial to each group so we end up with an estimation of both lane lines.
![windowing]

Given the polynomial fit for the left and right lane lines obtained from the sliding window process, was calculated the radius of curvature for each line according to the formula: 



The results are given in pixels, so be sure to converted the values from pixels to meters for more realistic interpretation. Results are display in the final results shown below.

## Final Result

At the end of the process we end up with this:

![result]










---

## Improvements to your pipeline

A possible improvement would be to keep tunning filters, specially the white one. As you can see in the pipeline images, yellow and white are well extracted but also some blue (sky)! I think if I try an HSV filter can also be a good option.

Another potential improvement that would be very hulpful would be to include some lane tracking, i.e., we know lanes follow a line and if we suppose this line is not moving that much we then can adapt our resultant lanes to this, at least to avoid big jumps between frames, which happens in some of them. I am thinking on keeping kind of a buffer or just saving past frame values (lane position) and use them in the current one. 

```
python main.py -c <camera selection> -n <face collection name>
```
---

## Discussion

This project has been challenging and very interesting, small pieces of code can bring a huge result, if they are well done. A mistake can take everything down though. Debugging in this case of scenarios is pretty different, in a good way, because we can visualise the results through images and not just numbers!


[calibration]: output_images/Calibration.png 
[undistorted]: output_images/Real_Undistorted.png 
[colorspaces]: output_images/Thresh_colorspaces.png
[sobel]: output_images/Thresh_Sobel.png
[thresholded]: output_images/Thresholded.png
[roi_warped]: output_images/ROI_Warped.png
[histogram]: output_images/Histogram.png
[windowing]: output_images/Windowing.png
[result]: output_images/ResultPipeline.png