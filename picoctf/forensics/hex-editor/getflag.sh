#!/bin/bash

strings hex_editor.jpg | grep -o -E 'picoCTF\{[0-9a-zA-Z_]*\}'
