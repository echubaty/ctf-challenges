#!/bin/bash

ssh -q echubaty@2018shell4.picoctf.com "cd /problems/you-can-t-see-me_4_8bd1412e56df49a3c3757ebeb7ead77f; grep -R . | grep -oE 'picoCTF{.*}' "
