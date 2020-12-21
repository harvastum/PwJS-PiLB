import os
import re

# this does not remove the listed strings 
# if case does not match or the string is a part of another word
pattern = re.compile(r"\b(self|and|never|why)\b",flags=(re.MULTILINE))

for item in os.scandir("samples"):
    with open(item.path, 'r+') as text:
        new_content = (re.sub(pattern, '', text.read()))
        text.seek(0)
        text.write(new_content)
        text.truncate()

