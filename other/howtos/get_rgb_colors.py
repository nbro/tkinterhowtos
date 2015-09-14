"""
Obtain available colors on Linux and Mac OS X systems.
"""

import sys, os


rgb_path = ["/usr/share/X11/rgb.txt",     # linux
            "/usr/X11/share/X11/rgb.txt", # OS X
            ]

COLORS = []

for filename in rgb_path:
    if os.path.exists(filename):
        with open(filename, 'r') as filedesc:
            for line in filedesc:
                if not (line.isspace() or line.startswith("#")):
                    # take the part after the last \t rsplit("\t",[-1])
                    # and remove the carriage return character [:-1]
                    COLORS.append(line.rsplit("\t",1)[-1][:-1])
        break

print(COLORS)
