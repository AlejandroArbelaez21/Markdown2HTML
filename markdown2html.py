#!/usr/bin/python3
"""
    script that takes an argument 2 strings:
        - First argument is the name of the Markdown file
        - Second argument is the output file name
"""

import sys
import os
import re
import hashlib

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    if not os.path.exists(sys.argv[1]):
        sys.stderr.write("Missing " + sys.argv[1] + "\n")
        exit(1)

    with open(sys.argv[1]) as r:
        with open(sys.argv[2], 'w') as w:
            for line in r:
                length = len(line)
                headings = line.lstrip('#')
                heading_count = length - len(headings)

                if 1 <= heading_count <= 6:
                    line = '<h{}>'.format(
                        heading_count) + headings.strip() + '</h{}>\n'.format(
                        heading_count)

                if length > 1:
                    w.write(line)
    exit(0)
