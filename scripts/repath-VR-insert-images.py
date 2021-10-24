import re
from pathlib import Path

# Modify image paths in VR insert experiments directory so paths reflect movement of
# unsorted images into the assorted directory. This is part of an effort to 
# improve image organization. Images up to this point (10/20/21) were just
# placed into "images" dir without further organization. Now will be breaking
# things down by image category ex. gel, alignment etc.
# This script was run from the outermost lab-notes directory.

IMAGE_REGEX = r'\!\[.*\]\((images\/.+)\)'  # finds markdown links to files in the images folder
NEW_PATH = Path('images/assorted')
TARGET_DIR = Path('experiments/VR-inserts')


def point_image_new_dir(image_path_match):
    current_path = Path(image_path_match[1])  # path to image
    target_path = NEW_PATH.joinpath(current_path.name)
    return f'![]({target_path})'


for each_path in TARGET_DIR.iterdir():
    if each_path.suffix == '.md':  # is a markdown file
        print(each_path)
        with open(str(each_path)) as read_handle:
            path_contents = read_handle.read()
            sub = re.subn(IMAGE_REGEX, point_image_new_dir, path_contents)
        with open(str(each_path), 'w') as write_handle:
            write_handle.write(sub[0])




