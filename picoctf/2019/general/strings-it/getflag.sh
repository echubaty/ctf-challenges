#!/bin/bash

strings strings | grep -oE "picoCTF{.*}" | tee flag.txt
