This folder contains all of the scripts to run the recorder, including:

# recorder.py
This is the main recorder script which runs once a minute (by default). It's a wrapper for [arecord](https://alsa.opensrc.org/Arecord) and sends 192 kHz sampled, 24 bit float WAV files to /recordings (again by default).

# spectrogram.sh
This script creates a spectrogram PNG in /recordings/spectrograms using [SoX](https://sourceforge.net/projects/sox/) for a given WAV file, then executes the HTMLer.py script.

# HTMLer.py
This script creates a small HTML file for each WAV file in /recordings/html which uses [Spectrogram-Player](https://github.com/mike-brady/Spectrogram-Player?tab=MIT-1-ov-file) to play the sound file and scroll a cursor across it synchronously.

# TRHPLogger.py
This script records the temperature, relative humidity, and barometric pressure to 'TRHPLog.csv' from the attached BME280 sensor.

# TRHPLog.csv
This is a CSV file with timestamp, temperature, relative humidity, and barometric pressure logged in it once a minute.

# track.gpx
This is the track from the attached GPS receiver recorded directly from [gpxlogger](https://gpsd.gitlab.io/gpsd/gpxlogger.html).
