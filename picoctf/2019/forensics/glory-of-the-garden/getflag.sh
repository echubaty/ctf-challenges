#!/bin/bash
strings garden.jpg | grep -oE "picoCTF{.*}" | tee flag.txt