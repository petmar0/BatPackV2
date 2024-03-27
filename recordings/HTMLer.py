import sys

file = sys.argv[1]
out = "/recordings/html/" + file + ".html"
f = open(out, 'w')
message1 = """<!DOCTYPE html>
<html>
<head>

  <meta charset="UTF-8">
  <title>"""

message2 = """</title>
  <link rel="stylesheet" type="text/css" href="src/style.css" />
  <style>
    body { font-family: sans-serif; }
  </style>
</head>
<body>
<head>"""

message3 = """</head>
  <script type="text/javascript" src="../src/spectrogram-player.js"></script>
  <div class="spectrogram-player" data-width="1000" data-height="400" data-freq-min="0" data-freq-max="96">
    <img src="../spectrograms/"""

message4 = """.png" />
    <audio controls controlsList="nodownload">
      <source src="../"""

message5 = """" type="audio/wav">
    </audio>
  </div>
  Position: $lat °, $long °, $alt m<br>
  Temperature: $T °C, Humidity: $RH %RH, Pressure: $P kPa<br>
  <a href="../"""

message6 = """">Download """

message7 = """</a>
</body>
</html>"""

f.write(message1)
f.write(file)
f.write(message2)
f.write(file)
f.write(message3)
f.write(file)
f.write(message4)
f.write(file)
f.write(message5)
f.write(file)
f.write(message6)
f.write(file)
f.write(message7)
f.close()
