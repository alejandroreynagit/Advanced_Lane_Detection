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

The very fist step in this project is camera calibration. We have to be sure that we have under certain control our image acquisition process. In order to deal with distortion caused by the camera we use OpenCV functions to perform the camera calibration. During the calibration process we calculate the distortion matrix and distortion coefficients. These values are used in our images for **distortion correction**. The following image is one of the images used to perform camera calibration, it can be seen both the original image and one ot the same image but undistorted:

![calibration]

Once we have performed the camera calibration, let's deep dive in the pipeline for lane detection.

---

## **Pipeline**

## Distortion Correction

We apply the distortion correction to one of the the test_images:

![undistorted]

This undistorted image is used as reference for lane detection within the pipeline.

## Threshold Image - Filtering

We apply color and gradient thresholding, i.e., filtering, in order to better detect lanes that will be used for fitting the lane. This is a key step in the pipeline. There are several colorspaces and for this project we explore RGB, HSV, HLS, LAB and the Sobel pperator to detect edges (or gradients).

Results of these colorspaces are shown here:

![rgb]
![hsv]
![hls]
![lab]

Imagen Undistr y filtrada
## Perspective Transformation - "Birds-eye-view"
Filtrada y birds eye 

## Lane Fit


## Final Result












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
[rgb]: output_images/Thresh_RGB.png
[hsv]: output_images/Thresh_HSV.png
[hls]: output_images/Thresh_HLS.png
[lab]: output_images/Thresh_LAB.png