#!/usr/bin/python

# Taken from an assignment from COMP4140 I did previously

import string
import itertools

uppercase = string.ascii_uppercase

def decrypt_shift_cipher(ciphertext, key):
    # Use a string translation table to "shift" the characters with the found key
    return ciphertext.translate(string.maketrans(uppercase[key:] + uppercase[:key], uppercase))


def decrypt_vigenere_cipher(ciphertext, key):
    # Convert key string into array of ints
    key_arr = [ord(x) - ord('A') for x in key]
    cipher_parts, plaintext_parts = list(), list()

    # Generate the "streams" of the ciphertext
    for x in [ciphertext[i::len(key)] for i in range(len(key))]:
        cipher_parts.append(x)

    # Decrypt each cipher stream into a plaintext stream
    for i in range(0, len(key_arr)):
        plaintext_parts.append(decrypt_shift_cipher(cipher_parts[i], key_arr[i]))

    # "Zip" the plaintext parts back together for final plaintext
    zipped_plaintext = list(itertools.izip_longest(*plaintext_parts))

    # Flatten the zipped plaintext and omit any None's
    flattened_plaintext = [x for x in list(itertools.chain.from_iterable(zipped_plaintext)) if x is not None]

    # Convert list of characters into string for final plaintext
    return ''.join(flattened_plaintext)

print("picoCTF{%s}" % decrypt_vigenere_cipher("llkjmlmpadkkc".upper(), "thisisalilkey".upper()))
