import shutil
import os
import sys
import replicate
from dotenv import load_dotenv
import requests

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} sticker-description")

dir_name = "temp"

if os.path.isdir(dir_name):
    shutil.rmtree(dir_name)

os.mkdir(dir_name)

load_dotenv()

emojis = [
    "grinning face",
    "beaming face",
    "face with tears of joy",
    "slightly smiling face",
    "upside down face",
    "melting face",
    "winking face",
    "money mouth face",
    "shushing face",
    "thinking face",
    "neutral face",
    "smirking face",
    "unamused face",
    "grimacing face",
    "sleepy face",
    "hot face",
    "cold face",
    "exploding head face",
    "confused face",
    "sad face",
    "angry red face",
]

for i, emoji in enumerate(emojis):
    print(f"{i+1}/{len(emojis)}")
    input_prompt = f"{emoji} {sys.argv[1]}" 
    input = {
        "output_quality": 100,
        "prompt": input_prompt,
        "output_format": "webp",
        "number_of_images": 1,
    }

    path = "fofr/sticker-maker:4acb778eb059772225ec213948f0660867b2e03f277448f18cf1800b96a65a1a"

    output = replicate.run(path, input=input)
    url = output[0]
    r = requests.get(url, allow_redirects=True)
    open(os.path.join(dir_name, input_prompt) + ".webp", "wb").write(r.content)

