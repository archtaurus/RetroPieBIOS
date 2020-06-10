# RetroPieBIOS

BIOS files collection for [RetroPie](https://retropie.org.uk) (current updated for RetroPie version 4.6).

Mentioned in [RetroPie's Docs](https://retropie.org.uk/docs/) - [BIOS section](https://retropie.org.uk/docs/BIOS/):

    Supported bios files for the libretro cores can be scanned using the official Bios.dat from Libretro-database

The file `Bios.dat` was renamed to [System.dat](https://raw.githubusercontent.com/libretro/libretro-database/master/dat/System.dat)
in the repository [RetroArch Database](https://github.com/libretro/libretro-database), and in this repository the file `bios.dat` is a copy of it.

`bios.dat` mentioned this:
    System, firmware, or BIOS files used by libretro.

I don't know, but maybe all the files listed in `bios.dat` is BIOS for RetroPie.

With google's help files were collected from the web and saved into the folder `bios/` and md5 hash values were verified.

May saving these bios files into your RetroPie's bios folder helps to run your games!

## Missing BIOS Files

Currentlly 189 files are listed in `bios.dat`. 187 were found already and 2 are missing. Maybe you could help to find them out.

| Platform       | filename    | size    | crc      | md5                              | sha1                                     |
| -------------- | ----------- | ------- | -------- | -------------------------------- | ---------------------------------------- |
| Wolfenstein 3D | ecwolf.pk3  | 178755  | 26dc3fba | c011b428819eea4a80b455c245a5a04d | 9259b87edfe9b9f6d0749788a75a6ccf158f50aa |
| ScummVM        | scummvm.zip | 9523360 | a93f1c4b | a17e0e0150155400d8cced329563d9c8 | 718c1a00d38e0810a1ad0ffde79f73447f846f01 |
