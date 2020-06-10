import os
import re
import glob
import hashlib

# Extract all roms' information (filename, size, crc, md5, sha1) from `bios.dat`.
with open('bios.dat') as f:
    content = f.read()
    roms_info = re.findall(r'rom \( name "?(.+?)"? size (\d+) crc (\w+) md5 (\w+) sha1 (\w+) \)', content)

# print out missing or md5 hash value invalid bios files.
# try to find them!
print('Missing BIOS files:')
filenames = []
for filename, size, crc, md5, sha1 in roms_info:
    filenames.append(filename)
    local_file_path = f'bios/{filename}'
    if (not os.path.exists(local_file_path)
            or hashlib.md5(open(local_file_path, 'rb').read()).hexdigest() != md5):
        print(filename, size, crc, md5, sha1)

# print out bios files no longer in the current `bios.dat`.
print('\nUnnecessary files:')
for file_path in glob.glob('./bios/*'):
    filename = os.path.basename(file_path)
    if filename not in filenames:
        print(filename)
