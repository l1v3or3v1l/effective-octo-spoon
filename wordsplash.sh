#/data/data/com.termux/files/usr/bin/bash

for i in $(seq 1 $2); do echo -n "$1 "; done | termux-clipboard-set


