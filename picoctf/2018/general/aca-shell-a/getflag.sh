#!/bin/bash

nc 2018shell.picoctf.com 58422 < getflag.txt | grep -oE picoCTF{.*}
