# https://github.com/CFC-Servers/gm_addon_optimization_tricks/blob/main/tools/sound-compression/wav-to-mp3.py
# Purpose: WAV -> MP3 since it's saves size and doesnt' have any comprehessions to it's quality

try:
  import pydub
except:
  print("[!] pydub is not installed, and it's required to use this script.")
  exit(0)

import os

PATH_TO_DIR = r"..."

old_size, new_size = 0, 0
replaced_count = 0
replaced_files = {}

# Convert .wav to .mp3
for path, dirs, files in os.walk(PATH_TO_DIR):
  for name in files:
    fpath = os.path.join(path, name)
    ftype = name.split(".")[-1]

    if ftype == ".wav":
      old_size += os.path.getsize(fpath)

      try:
        sound = pydub.AudioSegment.from_wav(fpath)
        sound.export(fpath, format="mp3")
      except:
        print(f"[!] {fpath} couldn't be exported to .mp3")

      new_size += os.path.getsize(fpath)
      replaced_count += 1

      fname = os.path.basename(fpath)
      replaced_files[fname] = fname.replace(".wav", ".mp3")

      print(f"[+] {fname} was converted to .mp3")

# Replacing all .wav occurences in .lua to .mp3
for path, dirs, files in os.walk(PATH_TO_DIR):
  for name in files:
    fpath = os.path.join(path, name)
    ftype = name.split(".")[-1]

    if ftype == ".lua":
      with open(fpath, "r", encoding="utf8") as file:
        contents = file.read()

      for old, new in replaced_files.items():
        contents = contents.replace(old, new)

      with open(fpath, "w", encoding="utf8") as file:
        file.write(contents)

# fi
print(f"[#] {replaced_count} files were replaced.")
print(f"[#] Reduced Size: {round((old_size - new_size) / 1048576)}MiB ({round((1 - new_size / old_size) * 100, 2)}%)")