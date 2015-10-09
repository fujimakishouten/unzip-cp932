#!/usr/bin/env python3

# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:



import argparse
import os
import zipfile


parser = argparse.ArgumentParser(description = "Extract zip file includes cp932 encoding file name")
parser.add_argument("file")
args = parser.parse_args()

with zipfile.ZipFile(args.file, 'r') as archive:
    for item in archive.namelist():
        filename = item.encode("cp437").decode("cp932")
        directory = os.path.dirname(filename)

        if not os.path.exists(directory):
            os.makedirs(directory)

        if os.path.basename(filename):
            with open(filename, "wb") as data:
                data.write(archive.read(item))



# Local variables:
# tab-width: 4
# c-basic-offset: 4
# c-hanging-comment-ender-p: nil
# End:
