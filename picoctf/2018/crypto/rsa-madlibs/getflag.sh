#!/bin/bash

python getflag.py | grep -oE picoCTF{.*}
