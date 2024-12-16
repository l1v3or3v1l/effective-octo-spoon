#/data/data/com.termux/files/usr/bin/bash

# To run
# bash wordsplash.sh <msg> <count>

for i in $(seq 1 $2); do echo -n "$1 "; done | termux-clipboard-set
