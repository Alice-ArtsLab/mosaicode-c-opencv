#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Match Object class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class MatchObject(BlockModel):
	"""
	This class contains methods related the MatchObject class.
	"""

	def __init__(self):
		BlockModel.__init__(self)

		self.language = "c"
		self.framework = "opencv"
		self.label = "Match Object"
		self.color = "0:204:34:215"
		self.group = "Feature Detection"
		self.ports = [{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
						"name": "input_object",
						"label": "Input Match Object Image",
						"conn_type":"Input"},
						{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
						"name": "input_image",
						"label": "Input Image to Match",
						"conn_type":"Input"},
						{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
						"name": "output_image",
						"label": "Output Image",
						"conn_type":"Output"}
		]

# --------------------------- C/OpenCV Code --------------------------- #

		self.codes["declaration"] = \
"""
	Mat $port[input_object]$;
	Mat $port[input_image]$;
	Mat $port[output_image]$;
	Ptr<xfeatures2d::SURF> surf = xfeatures2d::SURF::create(400);
"""		

		self.codes["execution"] = \
"""
	if(!$port[input_object]$.empty() && !$port[input_image]$.empty()){
		cvtColor($port[input_object]$, $port[input_object]$, COLOR_BGR2GRAY);
		cvtColor($port[input_image]$, $port[input_image]$, COLOR_BGR2GRAY);
		vector<KeyPoint> keypoints_object, keypoints_image;
		vector<DMatch> good_matches;
		vector<Point2f> obj, image_dtc, obj_corners(4), image_corners(4);
		surf->detect($port[input_object]$, keypoints_object);
		surf->detect($port[input_image]$, keypoints_image);
		Mat descriptors_object, descriptors_image;
		surf->compute($port[input_object]$, keypoints_object, descriptors_object);
		surf->compute($port[input_image]$, keypoints_image, descriptors_image);
		double max_dist = 0; double min_dist = 100;
		FlannBasedMatcher matcher;
		vector<DMatch> matches;
		matcher.match(descriptors_object, descriptors_image, matches);
		for(int i = 0; i < descriptors_object.rows; i++){
			double distance = matches[i].distance;
    		if(distance < min_dist) 
    			min_dist = distance;
    		if(distance > max_dist) 
    			max_dist = distance;
		}    			
		for(int i = 0; i < descriptors_object.rows; i++){
			if(matches[i].distance < 3*min_dist){
				good_matches.push_back(matches[i]);
			}
		}
		drawMatches($port[input_object]$, keypoints_object, $port[input_image]$, keypoints_image, good_matches, 
		$port[output_image]$, Scalar(222,184,135), Scalar(222,184,135), vector<char>(), DrawMatchesFlags::NOT_DRAW_SINGLE_POINTS);
		for(int i = 0; i < good_matches.size(); i++){
			obj.push_back(keypoints_object[good_matches[i].queryIdx].pt);
    		image_dtc.push_back(keypoints_image[good_matches[i].trainIdx ].pt);
		}
		Mat homography = findHomography(obj, image_dtc, CV_RANSAC);
		obj_corners[0] = Point(0,0); 
		obj_corners[1] = Point($port[input_object]$.cols, 0);
  		obj_corners[2] = Point($port[input_object]$.cols, $port[input_object]$.rows);
  		obj_corners[3] = Point(0, $port[input_object]$.rows);
		perspectiveTransform(obj_corners, image_corners, homography);

		line($port[output_image]$, image_corners[0] + Point2f($port[input_object]$.cols, 0), image_corners[1] + Point2f($port[input_object]$.cols, 0), Scalar(0, 255, 0), 4);
		line($port[output_image]$, image_corners[1] + Point2f($port[input_object]$.cols, 0), image_corners[2] + Point2f($port[input_object]$.cols, 0), Scalar( 0, 255, 0), 4);
		line($port[output_image]$, image_corners[2] + Point2f($port[input_object]$.cols, 0), image_corners[3] + Point2f($port[input_object]$.cols, 0), Scalar( 0, 255, 0), 4);
		line($port[output_image]$, image_corners[3] + Point2f($port[input_object]$.cols, 0), image_corners[0] + Point2f($port[input_object]$.cols, 0), Scalar( 0, 255, 0), 4);
	}
"""		
		self.codes["deallocation"] = \
"""
	$port[input_object]$.release();
	$port[input_image]$.release();
	$port[output_image]$.release();
"""		

# --------------------------------------------------------------------- #