#!/bin/env python3
import os
import re
import zlib
import hashlib

"PLATFORM,BIOS FILE,SIZE,MD5,SHA1,STATUS"

platform = 'unknown'
comment_line_pattern = re.compile(r'comment "(.+)"')
rom_line_pattern = re.compile(r'rom \( name "?(.+?)"? size (\d+) crc (\w+) md5 (\w+) sha1 (\w+) \)')


def crc32(filename):
    prev = 0
    for line in open(filename, 'rb'):
        prev = zlib.crc32(line, prev)
    return '%x' % (prev & 0xFFFFFFFF)


with open('System.dat') as data_file:
    for line in data_file:
        # or change platform with comment line
        if line.startswith('	comment'):
            platform = comment_line_pattern.search(line).group(1).strip()
        # parse data in rom line
        elif line.startswith('	rom'):
            filename, size, crc, md5, sha1 = rom_line_pattern.search(line).groups()
            local_path = f'bios/{filename}'
            local_exists = os.path.exists(local_path)
            local_data = open(local_path, 'rb').read() if local_exists else b''
            local_size = str(len(local_data))
            local_crc = crc32(local_path)
            local_md5 = hashlib.md5(local_data).hexdigest() if local_exists else ''
            local_sha1 = hashlib.sha1(local_data).hexdigest() if local_exists else ''
            size_verified = '🆗' if size == local_size else '💔'
            crc_verified = '🆗' if crc == local_crc else '💔'
            md5_verified = '🆗' if md5 == local_md5 else '💔'
            sha1_verified = '🆗' if sha1 == local_sha1 else '💔'
            print(
                f'| {platform:46s} | [{filename}](https://github.com/archtaurus/RetroPieBIOS/raw/master/bios/{filename})'
                f'| {size:7s} {size_verified} '
                f'| {crc} {crc_verified} '
                f'| {md5} {md5_verified} '
                f'| {sha1} {sha1_verified} |')
        else:
            platform = 'unknown'
