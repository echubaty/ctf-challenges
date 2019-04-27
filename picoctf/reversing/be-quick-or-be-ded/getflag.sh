#!/bin/bash

gdb -x ./gdb.in ./be-quick-or-be-dead-1 | grep -oE "picoCTF{.*}"

