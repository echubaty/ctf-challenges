#!/bin/bash

ssh -q echubaty@2018shell4.picoctf.com "echo 'yes' > permission.txt; /problems/absolutely-relative_3_c1a43555f1585c98aab8d5d2c7f0f9cc/absolutely-relative; rm permission.txt" | 
	grep "picoCTF{.*}"
