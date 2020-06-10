import os
import re
import hashlib

# Extract all roms' information (filename, size, crc, md5, sha1) from `bios.dat`.
with open('bios.dat') as f:
    content = f.read()
    roms_info = re.findall(r'rom \( name "?(.+?)"? size (\d+) crc (\w+) md5 (\w+) sha1 (\w+) \)', content)

for filename, size, crc, md5, sha1 in roms_info:
    local_file_path = f'bios/{filename}'
    download = os.path.exists(local_file_path)
    verified = download and hashlib.md5(open(local_file_path, 'rb').read()).hexdigest() == md5
    print(
        f'| | [{filename}](https://github.com/archtaurus/RetroPieBIOS/raw/master/bios/{filename}) | '
        f'{"🆗" if download else "💔"} | {"🆗" if verified else "💔"} | {size} | {md5} |'
    )
