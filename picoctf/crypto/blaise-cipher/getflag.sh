#!/bin/bash

# Plaintext generated from https://www.dcode.fr/vigenere-cipher. Blaise is the challenge name, Vigenere is his last name. Key was "FLAG"

grep -oE "picoCTF{.*}" plain.txt > flag.txt
cat flag.txt
