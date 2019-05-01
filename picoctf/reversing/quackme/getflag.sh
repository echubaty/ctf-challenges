#!/bin/bash

./crack.py | grep -oE "picoCTF{[a-z0-9_]*}"
