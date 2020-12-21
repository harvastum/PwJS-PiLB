import os
import re

# I picked some made up words; they are sufficient to demonstrate that the script works.
# A
words = {"and": "andn't",
        "also": "alson't",
        "never": "nevern't",
        "why": "whyn't",
        "andn't": "and",
        "alson't": "also",
        "nevern't": "never",
        "whyn't": "why"}

pattern = re.compile('|'.join(f'\\b{i}\\b' for i in words.keys()))
for item in os.scandir("samples"):
    with open(item.path, 'r+') as text:
        new_content = (pattern.sub(lambda match: words[match.group()], text.read()))
        text.seek(0)
        text.write(new_content)
        text.truncate()
