#!/bin/bash

binwalk --dd=".*" animals.dd
cd _animals.dd.extracted

# Look at the "2DCA00" file as an image, exiftool says its a jpeg. The flag is in the image.