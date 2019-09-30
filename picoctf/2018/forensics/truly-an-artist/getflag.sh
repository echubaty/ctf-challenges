#!/bin/bash

exiftool 2018.png | grep -o -E "picoCTF\{[a-zA-Z0-9_]*\}"
