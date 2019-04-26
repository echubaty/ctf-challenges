#!/bin/bash

ssh echubaty@2018shell4.picoctf.com "cat /etc/profile.d/flags.sh | grep -o -E 'picoCTF\{[0-9a-zA-Z_]*\}'"
