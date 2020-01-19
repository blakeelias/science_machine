import re
import os
from pdb import set_trace as b

def flatten_xml(file_name):
    text = re.sub('<[^<]+>', " ", open(file_name).read())
    return text

def trim(text):
    return text.replace('\n', ' ').replace('\t', ' ')

def write_to_file(text, file_name):
    with open(file_name, "w") as f:
        f.write(text)

        
def main(orig_file, dest_file):
    flattened = flatten_xml(orig_file)
    trimmed = trim(flattened)
    write_to_file(trimmed, dest_file)


if __name__ == '__main__':
    ORIG_FILES_DIR = "data/1_parsed/xml/"
    for orig_file_name in os.listdir(ORIG_FILES_DIR):
        dest_file = "data/2_flattened/flattened_from_xml/" + orig_file_name.replace('.xml', '.txt')
        orig_file = ORIG_FILES_DIR + orig_file_name
        main(orig_file, dest_file)
