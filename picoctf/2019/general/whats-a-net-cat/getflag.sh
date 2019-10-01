#!/bin/bash

nc 2019shell1.picoctf.com 12265 | grep -oE "picoCTF{.*}" | tee flag.txt
