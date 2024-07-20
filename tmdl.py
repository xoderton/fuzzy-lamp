# https://github.com/CFC-Servers/gm_addon_optimization_tricks/blob/main/tools/find-unused-files/unused_modelformat_remover.py
# Purpose: Annihilates useless model formats that are don't being used nowadays.

import os

PATH_TO_DIR = r"..."
FORMATS = [ ".dx80.vtx", ".xbox.vtx", ".sw.vtx" ]

total_size = 0

for path, dirs, files in os.walk(PATH_TO_DIR):
  for name in files:
    froot, fext = os.path.splitext(name)
    fpath = os.path.relpath(froot, PATH_TO_DIR)

    for format in FORMATS:
      if not name.endswith(format):
        continue

      total_size += os.path.getsize(os.path.join(froot, name))
      os.remove(os.path.join(froot, name))

      print(f"[+] {name} was removed")

print(f"[#] {round(total_size / 1048576)}MiB was saved.")