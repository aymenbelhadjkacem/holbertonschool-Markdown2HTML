#!/usr/bin/env python3
"""
Script to convert Markdown to HTML.
Takes two arguments:
1. Name of the Markdown file (input)
2. Name of the HTML file (output)
"""

import re
import hashlib
import sys
import os


def convert_line_to_html(line, list_status):
    """Converts a single line of Markdown to HTML."""
    # Bold and italic replacements
    line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
    line = re.sub(r'__(.*?)__', r'<em>\1</em>', line)

    # Replace [[text]] with md5 hash of 'text'
    line = re.sub(r'\[\[(.+?)\]\]', lambda m: hashlib.md5(m.group(1).encode()).hexdigest(), line)

    # Remove 'C' or 'c' from ((text))
    line = re.sub(r'\(\((.+?)\)\)', lambda m: ''.join(c for c in m.group(1) if c.lower() != 'c'), line)

    # Handle headings
    heading_match = re.match(r