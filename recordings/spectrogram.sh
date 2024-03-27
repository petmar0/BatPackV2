#! /bin/sh
path="$1"
file=$(basename "$path")
sox "$1" -n spectrogram -m -l -r -o "/recordings/spectrograms/$file.png"
cd /recordings
python3 HTMLer.py $file
