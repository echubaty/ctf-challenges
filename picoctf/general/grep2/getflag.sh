#!/bin/bash

ssh echubaty@2018shell4.picoctf.com "cd /problems/grep-2_2_413a577106278d0711d28a98f4f6ac28/files; grep -r -o -E 'picoCTF\{[0-9a-zA-Z_]*\}'"
