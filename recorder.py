#!/usr/bin/python3

import time
import datetime
import subprocess
import pathlib
import argparse

def find_device_number():
    completed = subprocess.run(["arecord", "-l"], capture_output=True)
    lines = [l.decode('utf-8').split(":") for l in completed.stdout.splitlines() if "Lavalier" in str(l)]
    assert len(lines) > 0, "Mic not found."
    device = lines[0][0].replace("card", "").strip()
    return int(device)

def block_for_new_minute():
    started = datetime.datetime.now()
    while datetime.datetime.now().minute == started.minute:
        time.sleep(0.01)
    return datetime.datetime.now()


def consume_child_procs(children):
    for proc in children:
        code = proc.poll()
        if code is not None:
            children.remove(proc)

def main():
    device_number = find_device_number()

    device = "plughw:%d,0" % device_number

    print(f"found device {device}...")

#    block_for_new_minute()

    now = datetime.datetime.now()
    fn = now.strftime('%Y%m%d_%H%M00')
    full_path = "/recordings/" + fn + ".wav"
    png_path = "/recordings/spectrograms/" + fn + ".png"
    subprocess.run(["arecord", "-D", device, "-d", "60", "-f", "S32_LE", "-r", "192000", "-c", "1", full_path])
    time.sleep(1)
    subprocess.run(["sox", full_path, "-n", "spectrogram", "-o", png_path])

if __name__ == '__main__':
    main()
