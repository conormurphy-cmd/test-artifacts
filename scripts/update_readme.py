#!/usr/bin/env python3
"""
Updates the Extensions table in README.md with the latest release info.

Usage:
    python3 scripts/update_readme.py <extension-name> <version> <download-url>

Example:
    python3 scripts/update_readme.py hello-world v1.2.0 https://github.com/.../hello-world-v1.2.0.zip
"""

import re
import sys

def display_name(slug: str) -> str:
    """Convert 'hello-world' -> 'Hello World'"""
    return ' '.join(word.capitalize() for word in slug.split('-'))

def update_readme(extension: str, version: str, url: str) -> None:
    name = display_name(extension)

    with open('README.md', 'r') as f:
        content = f.read()

    # Match the row for this extension (pipe-delimited markdown table row)
    row_re = re.compile(
        rf'^\| {re.escape(name)} \|.*$',
        re.MULTILINE
    )
    new_row = f'| {name} | `{version}` | [⬇️ Download]({url}) |'

    if row_re.search(content):
        content = row_re.sub(new_row, content)
    else:
        # Extension not in table yet — insert before the closing marker
        marker = '<!-- /EXTENSIONS_TABLE -->'
        if marker in content:
            content = content.replace(marker, new_row + '\n' + marker)
        else:
            print('Warning: could not find table marker in README.md', file=sys.stderr)
            sys.exit(1)

    with open('README.md', 'w') as f:
        f.write(content)

    print(f'README.md updated: {name} -> {version}')

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f'Usage: {sys.argv[0]} <extension-name> <version> <download-url>')
        sys.exit(1)
    update_readme(sys.argv[1], sys.argv[2], sys.argv[3])
