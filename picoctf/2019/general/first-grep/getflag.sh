#!/bin/bash

grep -oE "picoCTF{.*}" file | tee flag.txt
