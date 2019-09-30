#!/bin/bash

python fiximage.py
mkdir mount
sudo mount ext-super-magic-fixed.img mount/
sleep 3
cp mount/flag.jpg .
sudo umount mount/
sleep 3
sudo rm -rf mount

# The flag is stored in flag.jpg, have wrote this to the file flag.txt manually
