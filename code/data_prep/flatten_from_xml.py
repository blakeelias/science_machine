import re


def flatten_xml(file_name):
    text = re.sub('<[^<]+>', " ", open(file_name).read())
    return text

def write_to_file(text, file_name):
    with open(file_name, "w") as f:
        f.write(text)

        
def main(orig_file, dest_file):
    flattened = flatten_xml(orig_file)
    write_to_file(flattened, dest_file)


if __name__ == '__main__':
    ORIG_FILE = "data/1_parsed/xml/andyClark.pdf.tei.xml"
    DEST_FILE = "data/2_flattened/flattened_from_xml/andyClark.pdf.tei.txt"
    main(ORIG_FILE, DEST_FILE)
