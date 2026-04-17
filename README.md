# RetroPie BIOS Collection

[![ALL BIOS FILES MD5SUM CHECK](https://github.com/archtaurus/RetroPieBIOS/actions/workflows/all-bios-files-md5sum-check.yml/badge.svg)](https://github.com/archtaurus/RetroPieBIOS/actions/workflows/all-bios-files-md5sum-check.yml)

This repository is the BIOS collection for [RetroPie](https://retropie.org.uk).

All BIOS files have been verified in agreement with [System.dat](https://github.com/libretro/libretro-database/blob/master/dat/System.dat) (v1.19.0) from [Libretro-database](https://github.com/libretro/libretro-database).

Just copy all files from `BIOS` folder into your RetroPie's `BIOS` folder and enjoy your games! 😉

---

## Legal Disclaimer

The BIOS files in this repository are provided for **educational and archival purposes only**.

You are responsible for:
- Ensuring you own the original hardware from which these BIOS were extracted
- Complying with all applicable copyright laws in your jurisdiction
- Removing these files if requested by the copyright holder

No copyright infringement is intended. If you are a rights holder and object to the inclusion of certain files, please open an issue for removal.

---

## Md5sum Check Result

> ⚠️ 13 files are skipped (Amiga BIOS ROMs and Dinothawr.zip are not included in this collection)

```shell
PASS ./md5sum.test.js
  all files md5sum check
    ✓ md5sum("3do_arcade_saot.bin") should be "8970fc987ab89a7f64da9f8a8c4333ff" (4 ms)
    ✓ md5sum("goldstar.bin") should be "8639fd5e549bd6238cfee79e3e749114" (2 ms)
    ✓ md5sum("panafz1-kanji.bin") should be "b8dc97f778a6245c58e064b0312e8281" (3 ms)
    ✓ md5sum("panafz1.bin") should be "f47264dd47fe30f73ab3c010015c155b" (3 ms)
    ✓ md5sum("panafz10-norsa.bin") should be "1477bda80dc33731a65468c1f5bcbee9" (3 ms)
    ✓ md5sum("panafz10.bin") should be "51f2f43ae2f3508a14d9f56597e2d3ce" (3 ms)
    ✓ md5sum("panafz10e-anvil-norsa.bin") should be "cf11bbb5a16d7af9875cca9de9a15e09" (3 ms)
    ✓ md5sum("panafz10e-anvil.bin") should be "a48e6746bd7edec0f40cff078f0bb19f" (2 ms)
    ✓ md5sum("panafz10ja-anvil-kanji.bin") should be "428577250f43edc902ea239c50d2240d" (2 ms)
    ✓ md5sum("panafz1j-kanji.bin") should be "c23fb5d5e6bb1c240d02cf968972be37" (3 ms)
    ✓ md5sum("panafz1j-norsa.bin") should be "f6c71de7470d16abe4f71b1444883dc8" (3 ms)
    ✓ md5sum("panafz1j.bin") should be "a496cfdded3da562759be3561317b605" (2 ms)
    ✓ md5sum("sanyotry.bin") should be "35fa1a1ebaaeea286dc5cd15487c13ea" (2 ms)
    ✓ md5sum("cpc464.rom") should be "a993f85b88ac4350cf4d41554e87fe4f"
    ✓ md5sum("cpc664.rom") should be "5a384a2310f472c7857888371c00ed66"
    ✓ md5sum("cpc6128.rom") should be "b96280dc6c95a48857b4b8eb931533ae"
    ✓ md5sum("cpc_amsdos.rom") should be "25629dfe870d097469c217b95fdc1c95" (1 ms)
    ✓ md5sum("bubsys.zip") should be "f81298afd68a1a24a49a1a2d9f087964"
    ✓ md5sum("cchip.zip") should be "df6f8a3d83c028a5cb9f2f2be60773f3"
    ✓ md5sum("decocass.zip") should be "b7e1189b341bf6a8e270017c096d21b0" (1 ms)
    ✓ md5sum("isgsm.zip") should be "4a56d56e2219c5e2b006b66a4263c01c"
    ✓ md5sum("midssio.zip") should be "5904b0de768d1d506e766aa7e18994c1"
    ✓ md5sum("neogeo.zip") should be "00dad01abdbf8ea9e79ad2fe11bdb182" (5 ms)
    ✓ md5sum("nmk004.zip") should be "bfacf1a68792d5348f93cf724d2f1dda" (1 ms)
    ✓ md5sum("pgm.zip") should be "87cc944eef4c671aa2629a8ba48a08e0" (5 ms)
    ✓ md5sum("skns.zip") should be "3f956c4e7008804cb47cbde49bd5b908" (3 ms)
    ✓ md5sum("ym2608.zip") should be "79ae0d2bb1901b7e606b6dc339b79a97"
    ✓ md5sum("ATARIBAS.ROM") should be "0bac0c6a50104045d902df4503a4c30b"
    ✓ md5sum("ATARIOSA.ROM") should be "eb1f32f5d9f382db1bbfb8d7f9cb343a"
    ✓ md5sum("ATARIOSB.ROM") should be "a3e8d617c95d08031fe1b20d541434b2"
    ✓ md5sum("ATARIXL.ROM") should be "06daac977823773a3eea3422fd26a703" (1 ms)
    ✓ md5sum("BB01R4_OS.ROM") should be "b7a2a04677d34f069eeb643d5238bf86"
    ✓ md5sum("XEGAME.ROM") should be "d7eb37aec6960cba36bc500e0e5d00bc" (1 ms)
    ✓ md5sum("5200.rom") should be "281f20ea4320404ec820fb7ec0693b38"
    ✓ md5sum("7800 BIOS (E).rom") should be "397bb566584be7b9764e7a68974c4263" (1 ms)
    ✓ md5sum("7800 BIOS (U).rom") should be "0763f1ffb006ddbe32e52d497ee848ae"
    ✓ md5sum("lynxboot.img") should be "fcd403db69f54290b51035d82f835e7b" (1 ms)
    ✓ md5sum("tos.img") should be "c1c57ce48e8ee4135885cee9e63a68a2" (1 ms)
    ✓ md5sum("colecovision.rom") should be "2c66f5911e5b42b8ebe113403548eee7" (1 ms)
    ✓ md5sum("JiffyDOS_C128.bin") should be "cbbd1bbcb5e4fd8046b6030ab71fc021" (1 ms)
    ✓ md5sum("JiffyDOS_C64.bin") should be "be09394f0576cf81fa8bacf634daf9a2" (1 ms)
    ✓ md5sum("JiffyDOS_1541-II.bin") should be "1b1e985ea5325a1f46eb7fd9681707bf"
    ✓ md5sum("JiffyDOS_1571_repl310654.bin") should be "41c6cc528e9515ffd0ed9b180f8467c0"
    ✓ md5sum("JiffyDOS_1581.bin") should be "20b6885c6dc2d42c38754a365b043d71" (1 ms)
    ✓ md5sum("MT32_CONTROL.ROM") should be "5626206284b22c2734f3e9efefcd2675" (1 ms)
    ✓ md5sum("MT32_PCM.ROM") should be "89e42e386e82e0cacb4a2704a03706ca" (1 ms)
    ✓ md5sum("CM32L_CONTROL.ROM") should be "bfff32b6144c1d706109accb6e6b1113"
    ✓ md5sum("CM32L_PCM.ROM") should be "08cdcfa0ed93e9cb16afa76e6ac5f0a4" (3 ms)
    ✓ md5sum("bk/B11M_BOS.ROM") should be "fe4627d1e3a1535874085050733263e7" (1 ms)
    ✓ md5sum("bk/B11M_EXT.ROM") should be "dc52f365d56fa1951f5d35b1101b9e3f"
    ✓ md5sum("bk/BAS11M_0.ROM") should be "946f6f23ded03c0e26187f0b3ca75993" (1 ms)
    ✓ md5sum("bk/BAS11M_1.ROM") should be "1e6637f32aa7d1de03510030cac40bcf"
    ✓ md5sum("bk/DISK_327.ROM") should be "5015228eeeb238e65da8edcd1b6dfac7" (1 ms)
    ✓ md5sum("bk/BASIC10.ROM") should be "3fa774326d75410a065659aea80252f0"
    ✓ md5sum("bk/FOCAL10.ROM") should be "5737f972e8638831ab71e9139abae052" (1 ms)
    ✓ md5sum("bk/MONIT10.ROM") should be "95f8c41c6abf7640e35a6a03cecebd01"
    ✓ md5sum("hun.rom") should be "22167938f142c222f40992839aa21a06" (1 ms)
    ✓ md5sum("brd.rom") should be "6af0402906944fd134004b85097c8524"
    ✓ md5sum("exos20.rom") should be "5ad3baaad3b5156d6b60b34229a676fb"
    ✓ md5sum("exos21.rom") should be "f36f24cbb87745fbd2714e4df881db09"
    ✓ md5sum("zt19uk.rom") should be "228540b6be83ae2acd7569c8ff0f91d0" (1 ms)
    ✓ md5sum("basic20.rom") should be "8e18edce4a7acb2c33cc0ab18f988482"
    ✓ md5sum("basic21.rom") should be "e972fe42b398c9ff1d93ff014786aec6" (1 ms)
    ✓ md5sum("exdos13.rom") should be "ddff70c014d1958dc75378b6c9aab6f8"
    ✓ md5sum("epd19hft.rom") should be "12cfc9c7e48c8a16c2e09edbd926d467" (1 ms)
    ✓ md5sum("zt18hfnt.rom") should be "3082dc488d32f30a612761b99074199b"
    ✓ md5sum("epfileio.rom") should be "a68ebcbc73a4d2178d755b7755bf18fe" (1 ms)
    ✓ md5sum("exos24uk.rom") should be "55af78f877a21ca45eb2df68a74fcc60"
    ✓ md5sum("upd7801g.s01") should be "635a978fd40db9a18ee44eff449fc126" (1 ms)
    ✓ md5sum("sl31253.bin") should be "ac9804d4c0e9d07e33472e3726ed15c3"
    ✓ md5sum("sl31254.bin") should be "da98f4bb3242ab80d76629021bb27585" (1 ms)
    ✓ md5sum("sl90025.bin") should be "95d339631d867c8f1d15a5f2ec26069d"
    ✓ md5sum("prboom.wad") should be "72ae1b47820fcc93cc0df9c428d0face" (1 ms)
    ✓ md5sum("freej2me-lr.jar") should be "ccd92e7156ce2f0ce14c88ffb68a16eb" (2 ms)
    ✓ md5sum("freej2me-sdl.jar") should be "4da74084fc1b1bd3d776ed8d3ee648de" (2 ms)
    ✓ md5sum("freej2me.jar") should be "29a92d0867da2917275b7c6c805d256f" (1 ms)
    ✓ md5sum("MacII.ROM") should be "66223be1497460f1e60885eeb35e03cc"
    ✓ md5sum("o2rom.bin") should be "562d5ebf9e030a40d6fabfc2f33139fd"
    ✓ md5sum("c52.bin") should be "f1071cdb0b6b10dde94d3bc8a6146387"
    ✓ md5sum("g7400.bin") should be "c500ff71236068e0dc0d0603d265ae76" (1 ms)
    ✓ md5sum("jopac.bin") should be "279008e4a0db2dc5f1c048853b033828"
    ✓ md5sum("exec.bin") should be "62e761035cb657903761800f4437b8af" (1 ms)
    ✓ md5sum("grom.bin") should be "0cd5946c6473e42e8e4c2137785e427f"
    ✓ md5sum("CARTS.SHA") should be "74b0f217fa0e2b8bb5a2f8e2ecc69da3" (1 ms)
    ✓ md5sum("CYRILLIC.FNT") should be "85b38e4128bbc300e675f55b278683a8"
    ✓ md5sum("DISK.ROM") should be "80dcd1ad1a4cf65d64b7ba10504e8190" (1 ms)
    ✓ md5sum("FMPAC.ROM") should be "6f69cc8b5ed761b03afd78000dfb0e19"
    ✓ md5sum("FMPAC16.ROM") should be "af8537262df8df267072f359399a7635" (1 ms)
    ✓ md5sum("ITALIC.FNT") should be "c83e50e9f33b8dd893c414691822740d"
    ✓ md5sum("KANJI.ROM") should be "febe8782b466d7c3b16de6d104826b34" (1 ms)
    ✓ md5sum("MSX.ROM") should be "aa95aea2563cd5ec0a0919b44cc17d47"
    ✓ md5sum("MSX2.ROM") should be "ec3a01c91f24fbddcbcab0ad301bc9ef" (1 ms)
    ✓ md5sum("MSX2EXT.ROM") should be "2183c2aff17cf4297bdb496de78c2e8a"
    ✓ md5sum("MSX2P.ROM") should be "6d8c0ca64e726c82a4b726e9b01cdf1e" (1 ms)
    ✓ md5sum("MSX2PEXT.ROM") should be "7c8243c71d8f143b2531f01afa6a05dc"
    ✓ md5sum("MSXDOS2.ROM") should be "6418d091cd6907bbcf940324339e43bb"
    ✓ md5sum("PAINTER.ROM") should be "403cdea1cbd2bb24fae506941f8f655e" (3 ms)
    ✓ md5sum("RS232.ROM") should be "279efd1eae0d358eecd4edc7d9adedf3"
    ✓ md5sum("gecard.pce") should be "6d2cb14fc3e1f65ceb135633d1694122"
    ✓ md5sum("gexpress.pce") should be "6d2cb14fc3e1f65ceb135633d1694122" (1 ms)
    ✓ md5sum("syscard1.pce") should be "2b7ccb3d86baa18f6402c176f3065082"
    ✓ md5sum("syscard2.pce") should be "3cdd6614a918616bfc41c862e889dd79" (1 ms)
    ✓ md5sum("syscard2u.pce") should be "94279f315e8b52904f65ab3108542afe" (1 ms)
    ✓ md5sum("syscard3.pce") should be "38179df8f4ac870017db21ebcbf53114"
    ✓ md5sum("syscard3u.pce") should be "0754f903b52e3b3342202bdafb13efa5"
    ✓ md5sum("2608_bd.wav") should be "d94546e70f17fd899be8df3544ab6cbb"
    ✓ md5sum("2608_hh.wav") should be "08c54a0c1f774a5538a848a6665a34b4" (1 ms)
    ✓ md5sum("2608_rim.wav") should be "465ea0768b27da404aec45dfc501404b"
    ✓ md5sum("2608_sd.wav") should be "d71004351c8bbfdad53b18222c061d49"
    ✓ md5sum("2608_tom.wav") should be "96a4ead13f364734f79b0c58af2f0e1f" (1 ms)
    ✓ md5sum("2608_top.wav") should be "593cff6597ab9380d822b8f824fd2c28"
    ✓ md5sum("bios.rom") should be "cd237e16e7e77c06bb58540e9e9fca68"
    ✓ md5sum("font.bmp") should be "7da1e5b7c482d4108d22a5b09631d967" (1 ms)
    ✓ md5sum("font.rom") should be "38d32748ae49d1815b0614970849fd40" (1 ms)
    ✓ md5sum("itf.rom") should be "72ea51443070f0e9212bfc9b793ee28e"
    ✓ md5sum("sound.rom") should be "524473c1a5a03b17e21d86a0408ff827"
    ✓ md5sum("fx-scsi.rom") should be "430e9745f9235c515bc8e652d6ca3004" (2 ms)
    ✓ md5sum("pcfx.rom") should be "08e36edbea28a017f79f8d4f7ff9b6d7" (2 ms)
    ✓ md5sum("pcfxbios.bin") should be "08e36edbea28a017f79f8d4f7ff9b6d7" (2 ms)
    ✓ md5sum("pcfxga.rom") should be "5885bc9a64bf80d4530b9b9b978ff587" (3 ms)
    ✓ md5sum("pcfxv101.bin") should be "e2fb7c7220e3a7838c2dd7e401a7f3d8" (2 ms)
    ✓ md5sum("disksys.rom") should be "ca30b50f880eb660a320674ed365ef7a"
    ✓ md5sum("gamegenie.nes") should be "7f98d77d7a094ad7d069b74bd553ec98" (1 ms)
    ✓ md5sum("dmg_boot.bin") should be "32fbbd84168d3482956eb3c5051637f5"
    ✓ md5sum("gb_bios.bin") should be "32fbbd84168d3482956eb3c5051637f5"
    ✓ md5sum("gba_bios.bin") should be "a860e8c0b6d573d191e4ec7db1b1e4f6"
    ✓ md5sum("cgb_boot.bin") should be "dbfce9db9deaa2567f6a84fde55f9680" (1 ms)
    ✓ md5sum("gbc_bios.bin") should be "dbfce9db9deaa2567f6a84fde55f9680"
    ✓ md5sum("gc-dvd-20010608.bin") should be "561532ad496f644897952d2cef5bb431" (1 ms)
    ✓ md5sum("gc-dvd-20010831.bin") should be "b953eb1a8fc9922b3f7051c1cdc451f1"
    ✓ md5sum("gc-dvd-20020402.bin") should be "413154dd0e2c824c9b18b807fd03ec4e"
    ✓ md5sum("gc-dvd-20020823.bin") should be "c03f6bbaf644eb9b3ee261dbe199eb42"
    ✓ md5sum("gc-ntsc-10.bin") should be "fc924a7c879b661abc37cec4f018fdf3" (4 ms)
    ✓ md5sum("gc-ntsc-11.bin") should be "019e39822a9ca3029124f74dd4d55ac4" (5 ms)
    ✓ md5sum("gc-ntsc-12.bin") should be "b17148254a5799684c7d783206504926" (4 ms)
    ✓ md5sum("gc-pal-10.bin") should be "0cdda509e2da83c85bfe423dd87346cc" (5 ms)
    ✓ md5sum("gc-pal-11.bin") should be "339848a0b7c2124cf155276c1e79cbd0" (4 ms)
    ✓ md5sum("gc-pal-12.bin") should be "db92574caab77a7ec99d4605fd6f2450" (5 ms)
    ✓ md5sum("64DD_IPL.bin") should be "8d3d9f294b6e174bc7b1d2fd1c727530" (10 ms)
    ✓ md5sum("bios7.bin") should be "df692a80a5b1bc90728bc3dfc76cd948"
    ✓ md5sum("bios9.bin") should be "a392174eb3e572fed6447e956bde4b25"
    ✓ md5sum("firmware.bin") should be "e45033d9b0fa6b0de071292bba7c9d13" (1 ms)
    ✓ md5sum("NstDatabase.xml") should be "7bfe8c0540ed4bd6a0f1e2a0f0118ced" (3 ms)
    ✓ md5sum("bios.min") should be "1e4fb124a3a886865acb574f388c803d"
    ✓ md5sum("BS-X.bin") should be "fed4d8242cfbed61343d53d48432aced" (3 ms)
    ✓ md5sum("BS-X (En).bin") should be "33b62505da6ca4525e3839db4e1a7bca" (3 ms)
    ✓ md5sum("BS-X (En) (DRM-Free).bin") should be "4ed9648505ab33a4daec93707b16caba" (3 ms)
    ✓ md5sum("STBIOS.bin") should be "d3a44ba7d42a74d3ac58cb9c14c6a5ca" (1 ms)
    ✓ md5sum("SGB1.sfc") should be "b15ddb15721c657d82c5bab6db982ee9" (1 ms)
    ✓ md5sum("SGB2.sfc") should be "8ecd73eb4edf7ed7e81aef1be80031d5" (1 ms)
    ✓ md5sum("sgb1.boot.rom") should be "d574d4f9c12f305074798f54c091a8b4"
    ✓ md5sum("sgb1.program.rom") should be "b15ddb15721c657d82c5bab6db982ee9" (1 ms)
    ✓ md5sum("sgb2.boot.rom") should be "e0430bca9925fb9882148fd2dc2418c1" (1 ms)
    ✓ md5sum("sgb2.program.rom") should be "8ecd73eb4edf7ed7e81aef1be80031d5" (1 ms)
    ✓ md5sum("sgb2_bios.bin") should be "e0430bca9925fb9882148fd2dc2418c1"
    ✓ md5sum("sgb_bios.bin") should be "d574d4f9c12f305074798f54c091a8b4" (1 ms)
    ✓ md5sum("cx4.data.rom") should be "037ac4296b6b6a5c47c440188d3c72e3"
    ✓ md5sum("dsp1.data.rom") should be "3d81b45fa0c2aa8b852dfb1ece7c0971"
    ✓ md5sum("dsp1.program.rom") should be "ae209fbe789fbf11a48aea5ab1197321" (1 ms)
    ✓ md5sum("dsp1b.data.rom") should be "1e3f568634a7d8284020dddc0ae905bc"
    ✓ md5sum("dsp1b.program.rom") should be "d10f446888e097cbf500f3f663cf4f6d" (1 ms)
    ✓ md5sum("dsp2.data.rom") should be "e9417e29223b139c3c4b635a2a3b8744"
    ✓ md5sum("dsp2.program.rom") should be "aa6e5922a3ed5ded54f24247c11143c5"
    ✓ md5sum("dsp3.data.rom") should be "0a81210c0a940b997dd9843281008ee6" (1 ms)
    ✓ md5sum("dsp3.program.rom") should be "d99ca4562818d49cee1f242705bba6f8"
    ✓ md5sum("dsp4.data.rom") should be "ee4990879eb68e3cbca239c5bc20303d"
    ✓ md5sum("dsp4.program.rom") should be "a151023b948b90ffc23a5b594bb6fef2"
    ✓ md5sum("st010.data.rom") should be "254d70762b6f59f99c27c395aba7d07d" (1 ms)
    ✓ md5sum("st010.program.rom") should be "1d70019179a59a566a0bb5d3f2845544"
    ✓ md5sum("st011.data.rom") should be "10bd3f4aa949737ab9836512c35bcc29" (1 ms)
    ✓ md5sum("st011.program.rom") should be "95222ebf1c0c2990bcf25db43743f032"
    ✓ md5sum("st018.data.rom") should be "49c898b60d0f15e90d0ba780dd12f366"
    ✓ md5sum("st018.program.rom") should be "dda40ccd57390c96e49d30a041f9a9e7" (1 ms)
    ✓ md5sum("c52.bin") should be "f1071cdb0b6b10dde94d3bc8a6146387"
    ✓ md5sum("g7400.bin") should be "c500ff71236068e0dc0d0603d265ae76" (1 ms)
    ✓ md5sum("jopac.bin") should be "279008e4a0db2dc5f1c048853b033828"
    ✓ md5sum("dc/dc_boot.bin") should be "e10c53c2f8b90bab96ead2d368858623" (5 ms)
    ✓ md5sum("dc/boot.bin") should be "e10c53c2f8b90bab96ead2d368858623" (6 ms)
    ✓ md5sum("dc/flash.bin") should be "0a93f7940c455905bea6e392dfde92a4"
    ✓ md5sum("dc/airlbios.zip") should be "7a11bfe0cc72886d032e386db68f890c" (2 ms)
    ✓ md5sum("dc/awbios.zip") should be "85254fbe320ca82a768ec2c26bb08def"
    ✓ md5sum("dc/f355bios.zip") should be "547f3d12aed389058ca06148f1cca0ed" (4 ms)
    ✓ md5sum("dc/f355dlx.zip") should be "1028615bcac4c31634a3364ce5c04044" (5 ms)
    ✓ md5sum("dc/hod2bios.zip") should be "f4011d3116500354edf7302a90402711" (4 ms)
    ✓ md5sum("dc/naomi.zip") should be "526eda1e2a7920c92c88178789d71d84" (22 ms)
    ✓ md5sum("dc/naomi2.zip") should be "c50072cbab75673e1b1a6b94355e6fa8" (16 ms)
    ✓ md5sum("bios.gg") should be "672e104c3be3a238301aceffc3b23fd6" (1 ms)
    ✓ md5sum("bios.sms") should be "840481177270d5642a14ca71ee72844c"
    ✓ md5sum("bios_E.sms") should be "840481177270d5642a14ca71ee72844c" (1 ms)
    ✓ md5sum("bios_J.sms") should be "24a519c53f67b00640d0048ef7089105"
    ✓ md5sum("bios_U.sms") should be "840481177270d5642a14ca71ee72844c"
    ✓ md5sum("bios_CD_E.bin") should be "e66fa1dc5820d254611fdcdba0662372" (1 ms)
    ✓ md5sum("bios_CD_J.bin") should be "278a9397d192149e84e820ac621a8edd" (1 ms)
    ✓ md5sum("bios_CD_U.bin") should be "2efd74e3232ff260e371b99f84024f7f" (1 ms)
    ✓ md5sum("areplay.bin") should be "a0028b3043f9d59ceeb03da5b073b30d"
    ✓ md5sum("bios_MD.bin") should be "d3293ebaaa7f4eb2a6766b68a0fb4609"
    ✓ md5sum("ggenie.bin") should be "e8af7fe115a75c849f6aab3701e7799b" (1 ms)
    ✓ md5sum("rom.db") should be "ff4a3572475236e859e3e9ac5c87d1f1" (1 ms)
    ✓ md5sum("sk.bin") should be "4ea493ea4e9f6c9ebfccbdb15110367e" (3 ms)
    ✓ md5sum("sk2chip.bin") should be "b4e76e416b887f4e7413ba76fa735f16" (1 ms)
    ✓ md5sum("hisaturn.bin") should be "3ea3202e2634cb47cb90f3a05c015010" (1 ms)
    ✓ md5sum("mpr-17933.bin") should be "3240872c70984b6cbfda1586cab68dbe" (1 ms)
    ✓ md5sum("mpr-18100.bin") should be "cb2cebc1b6e573b7c44523d037edcd45" (1 ms)
    ✓ md5sum("mpr-18811-mx.ic1") should be "255113ba943c92a54facd25a10fd780c" (3 ms)
    ✓ md5sum("mpr-19367-mx.ic1") should be "1cd19988d1d72a3e7caa0b73234c96b4" (3 ms)
    ✓ md5sum("saturn_bios.bin") should be "af5828fdff51384f99b3c4926be27762" (1 ms)
    ✓ md5sum("sega1003.bin") should be "74570fed4d44b2682b560c8cd44b8b6a" (1 ms)
    ✓ md5sum("sega_100.bin") should be "af5828fdff51384f99b3c4926be27762" (1 ms)
    ✓ md5sum("sega_100a.bin") should be "f273555d7d91e8a5a6bfd9bcf066331c" (1 ms)
    ✓ md5sum("sega_101.bin") should be "85ec9ca47d8f6807718151cbcca8b964" (1 ms)
    ✓ md5sum("vsaturn.bin") should be "ac4e4b6522e200c0d23d371a8cecbfd3" (1 ms)
    ✓ md5sum("iplrom.x1") should be "eeeea1cd29c6e0e8b094790ae969bfa7"
    ✓ md5sum("iplrom.x1t") should be "851e4a5936f17d13f8c39a980cf00d77"
    ✓ md5sum("cgrom.dat") should be "cb0a5cfcf7247a7eab74bb2716260269" (1 ms)
    ✓ md5sum("iplrom.dat") should be "7fd4caabac1d9169e289f0f7bbf71d8e" (1 ms)
    ✓ md5sum("iplrom30.dat") should be "f373003710ab4322642f527f567e020a"
    ✓ md5sum("iplromco.dat") should be "cc78d4f4900f622bd6de1aed7f52592f"
    ✓ md5sum("iplromxv.dat") should be "0617321daa182c3f3d6f41fd02fb3275"
    ✓ md5sum("128-0.rom") should be "b4d2692115a9f2924df92a3cbfb358fb"
    ✓ md5sum("128-1.rom") should be "6e09e5d3c4aef166601669feaaadc01c"
    ✓ md5sum("128-spanish-0.rom") should be "c1231a70b8129311216acb7479b031d5" (1 ms)
    ✓ md5sum("128-spanish-1.rom") should be "4f341936594cbcab75cfa62ce96e3682"
    ✓ md5sum("128p-0.rom") should be "a249565f03b98d004ee7f019570069cd"
    ✓ md5sum("128p-1.rom") should be "6e09e5d3c4aef166601669feaaadc01c"
    ✓ md5sum("256s-0.rom") should be "b9fda5b6a747ff037365b0e2d8c4379a" (1 ms)
    ✓ md5sum("256s-1.rom") should be "643861ad34831b255bf2eb64e8b6ecb8"
    ✓ md5sum("256s-2.rom") should be "d8ad507b1c915a9acfe0d73957082926"
    ✓ md5sum("256s-3.rom") should be "ce0723f9bc02f4948c15d3b3230ae831" (1 ms)
    ✓ md5sum("48.rom") should be "4c42a2f075212361c3117015b107ff68"
    ✓ md5sum("disciple.rom") should be "78e61a2a02121873c1756b21fd1398b1"
    ✓ md5sum("disk_plus3.szx") should be "e6db6b9f6ad15012851115a7bc4b31d8"
    ✓ md5sum("gluck.rom") should be "d5869034604dbfd2c1d54170e874fd0a" (1 ms)
    ✓ md5sum("if1-1.rom") should be "5c11c61a2dd2ca4bf39328d9ff42d289"
    ✓ md5sum("if1-2.rom") should be "31b704ae925305e74f50699271fddd9a"
    ✓ md5sum("plus2-0.rom") should be "4ed7af4636308b8a48d7a35e6c5b546b"
    ✓ md5sum("plus2-1.rom") should be "b3db95931cc844efaeb82db9c171b9f3" (1 ms)
    ✓ md5sum("plus3-0.rom") should be "9833b8b73384dd5fa3678377ff00a2bb"
    ✓ md5sum("plus3-1.rom") should be "0f711ceb5ab801b4701989982e0f334c"
    ✓ md5sum("plus3-2.rom") should be "3b6dd659d5e4ec97f0e2f7878152c987" (1 ms)
    ✓ md5sum("plus3-3.rom") should be "a148bcc575e51389e84fdf5d555c3196"
    ✓ md5sum("plus3e-0.rom") should be "bc123f625e245c225f92ef05933ed134"
    ✓ md5sum("plus3e-1.rom") should be "617364264c587d20c9fc4746c29679f2"
    ✓ md5sum("plus3e-2.rom") should be "c363e95dcd0a90e6e7f847e6e47e0179"
    ✓ md5sum("plus3e-3.rom") should be "a148bcc575e51389e84fdf5d555c3196"
    ✓ md5sum("plusd.rom") should be "42e5de16fb5e50082bb954ec7ce45851" (1 ms)
    ✓ md5sum("se-0.rom") should be "fb3f86eb1e5a695d9c50c124e7cfb875"
    ✓ md5sum("se-1.rom") should be "88de4a3129086f34bb9ca559acc51e6c"
    ✓ md5sum("speccyboot-1.4.rom") should be "c54aa8f374b0971f51546c29d5d1eba1"
    ✓ md5sum("tape_128.szx") should be "8942b43b73ed4eb7f32bd1741709a4dc" (1 ms)
    ✓ md5sum("tape_16.szx") should be "fec97eb9ea1b017cae84de78508feb4a"
    ✓ md5sum("tape_2048.szx") should be "116f732bbae4e49d625aaf2f311474d0"
    ✓ md5sum("tape_2068.szx") should be "0b0f267b95d556318bb652af2e8dc25c"
    ✓ md5sum("tape_48.szx") should be "ee2ae810711594db3a134a7432baabff"
    ✓ md5sum("tape_pentagon.szx") should be "bd7698603bd9079d337cdedfb04942d9"
    ✓ md5sum("tape_plus2.szx") should be "166d4aa1a5aa4fbd99cc963b4e7c19cc"
    ✓ md5sum("tape_plus2a.szx") should be "445d4817d5557bb363a216fbd6eeaa84"
    ✓ md5sum("tape_plus3.szx") should be "0dc8828ac1db2e0efa915ac55191e96f"
    ✓ md5sum("tape_plus3e.szx") should be "bf07537f028bbcb3309464bd30da779c"
    ✓ md5sum("tape_scorpion.szx") should be "c10e677d3deb5a445689d3a599880745"
    ✓ md5sum("tape_se.szx") should be "2518f9334bef8c44804a4185085579b5"
    ✓ md5sum("tape_ts2068.szx") should be "1d360c09d370bb52a9a44b30cc7c59e6"
    ✓ md5sum("tc2048.rom") should be "9dd7ecf784a6c04265c073c236f5fadb"
    ✓ md5sum("tc2068-0.rom") should be "55d462fccc6c536037404ef4ced08bec"
    ✓ md5sum("tc2068-1.rom") should be "575d203c6e15e679fba0b73f854ec7a2" (1 ms)
    ✓ md5sum("trdos.rom") should be "0da70a5d2a0e733398e005b96b7e4ba6"
    ✓ md5sum("zx48.rom") should be "4c42a2f075212361c3117015b107ff68"
    ✓ md5sum("zx128.rom") should be "85fede415f4294cc777517d7eada482e"
    ✓ md5sum("000-lo.lo") should be "fc7599f3f871578fe9a0453662d1c966" (1 ms)
    ✓ md5sum("front-sp1.bin") should be "5c2366f25ff92d71788468ca492ebeca" (1 ms)
    ✓ md5sum("neocd.bin") should be "f39572af7584cb5b3f70ae8cc848aba2" (1 ms)
    ✓ md5sum("neocd_f.rom") should be "8834880c33164ccbe6476b559f3e37de" (1 ms)
    ✓ md5sum("neocd_sf.rom") should be "043d76d5f0ef836500700c34faef774d" (1 ms)
    ✓ md5sum("neocd_st.rom") should be "f6325a33c6d63ea4b9162a3fa8c32727" (1 ms)
    ✓ md5sum("neocd_sz.rom") should be "971ee8a36fb72da57aed01758f0a37f5" (1 ms)
    ✓ md5sum("neocd_t.rom") should be "de3cf45d227ad44645b22aa83b49f450" (1 ms)
    ✓ md5sum("neocd_z.rom") should be "11526d58d4c524daef7d5d677dc6b004" (1 ms)
    ✓ md5sum("top-sp1.bin") should be "122aee210324c72e8a11116e6ef9c0d0" (1 ms)
    ✓ md5sum("uni-bioscd.rom") should be "08ca8b2dba6662e8024f9e789711c6fc" (2 ms)
    ✓ md5sum("scph1000.bin") should be "239665b1a3dade1b5a52c06338011044" (1 ms)
    ✓ md5sum("scph1001.bin") should be "924e392ed05558ffdb115408c263dccf" (1 ms)
    ✓ md5sum("scph1002.bin") should be "54847e693405ffeb0359c6287434cbef" (1 ms)
    ✓ md5sum("scph100.bin") should be "8abc1b549a4a80954addc48ef02c4521" (1 ms)
    ✓ md5sum("scph101.bin") should be "6e3735ff4c7dc899ee98981385f6f3d0" (1 ms)
    ✓ md5sum("scph102A.bin") should be "b10f5e0e3d9eb60e5159690680b1e774" (1 ms)
    ✓ md5sum("scph102B.bin") should be "de93caec13d1a141a40a79f5c86168d6" (1 ms)
    ✓ md5sum("scph102C.bin") should be "de93caec13d1a141a40a79f5c86168d6" (2 ms)
    ✓ md5sum("scph3000.bin") should be "849515939161e62f6b866f6853006780" (1 ms)
    ✓ md5sum("scph3500.bin") should be "cba733ceeff5aef5c32254f1d617fa62" (1 ms)
    ✓ md5sum("scph5000.bin") should be "eb201d2d98251a598af467d4347bb62f" (2 ms)
    ✓ md5sum("scph5500.bin") should be "8dd7d5296a650fac7319bce665a6a53c" (1 ms)
    ✓ md5sum("scph5501.bin") should be "490f666e1afb15b7362b406ed1cea246" (1 ms)
    ✓ md5sum("scph5502.bin") should be "32736f17079d0b2b7024407c39bd3050" (1 ms)
    ✓ md5sum("scph5552.bin") should be "32736f17079d0b2b7024407c39bd3050" (1 ms)
    ✓ md5sum("scph7001.bin") should be "1e68c231d0896b7eadcad1d7d8e76129" (2 ms)
    ✓ md5sum("scph7002.bin") should be "b9d9a0286c33dc6b7237bb13cd46fdee" (1 ms)
    ✓ md5sum("scph7003.bin") should be "490f666e1afb15b7362b406ed1cea246" (1 ms)
    ✓ md5sum("scph7502.bin") should be "b9d9a0286c33dc6b7237bb13cd46fdee" (1 ms)
    ✓ md5sum("scph9002(7502).bin") should be "b9d9a0286c33dc6b7237bb13cd46fdee" (1 ms)
    ✓ md5sum("psxonpsp660.bin") should be "c53ca5908936d412331790f4426c6c33" (2 ms)
    ✓ md5sum("ps1_rom.bin") should be "81bbe60ba7a3d1cea1d48c14cbcc647b" (1 ms)
    ✓ md5sum("pcsx2/bios/ps2-0100jd-20000117.bin") should be "32f2e4d5ff5ee11072a6bc45530f5765" (8 ms)
    ✓ md5sum("pcsx2/bios/ps2-0100j-20000117.bin") should be "acf4730ceb38ac9d8c7d8e21f2614600" (7 ms)
    ✓ md5sum("pcsx2/bios/ps2-0101jd-20000217.bin") should be "acf9968c8f596d2b15f42272082513d1" (8 ms)
    ✓ md5sum("pcsx2/bios/ps2-0101j-20000217.bin") should be "b1459d7446c69e3e97e6ace3ae23dd1c" (9 ms)
    ✓ md5sum("pcsx2/bios/ps2-0101xd-20000224.bin") should be "d3f1853a16c2ec18f3cd1ae655213308" (9 ms)
    ✓ md5sum("pcsx2/bios/ps2-0110ad-20000727.bin") should be "63e6fd9b3c72e0d7b920e80cf76645cd" (7 ms)
    ✓ md5sum("pcsx2/bios/ps2-0110a-20000727.bin") should be "a20c97c02210f16678ca3010127caf36" (8 ms)
    ✓ md5sum("pcsx2/bios/ps2-0120a-20000902.bin") should be "8db2fbbac7413bf3e7154c1e0715e565" (10 ms)
    ✓ md5sum("pcsx2/bios/ps2-0120ed-20000902.bin") should be "91c87cb2f2eb6ce529a2360f80ce2457" (10 ms)
    ✓ md5sum("pcsx2/bios/ps2-0120ed-20000902-20030110.bin") should be "3016b3dd42148a67e2c048595ca4d7ce" (11 ms)
    ✓ md5sum("pcsx2/bios/ps2-0120e-20000902.bin") should be "b7fa11e87d51752a98b38e3e691cbf17" (13 ms)
    ✓ md5sum("pcsx2/bios/ps2-0120j-20001027-185015.bin") should be "f63bc530bd7ad7c026fcd6f7bd0d9525" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0120j-20001027-191435.bin") should be "cee06bd68c333fc5768244eae77e4495" (7 ms)
    ✓ md5sum("pcsx2/bios/ps2-0150ad-20001228-20030520.bin") should be "0bf988e9c7aaa4c051805b0fa6eb3387" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0150a-20001228.bin") should be "8accc3c49ac45f5ae2c5db0adc854633" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0150ed-20001228-20030520.bin") should be "6f9a6feb749f0533aaae2cc45090b0ed" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0150e-20001228.bin") should be "838544f12de9b0abc90811279ee223c8" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0150jd-20010118.bin") should be "bb6bbc850458fff08af30e969ffd0175" (7 ms)
    ✓ md5sum("pcsx2/bios/ps2-0150j-20010118.bin") should be "815ac991d8bc3b364696bead3457de7d" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0160a-20010427.bin") should be "b107b5710042abe887c0f6175f6e94bb" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0160j-20010427.bin") should be "ab55cceea548303c22c72570cfd4dd71" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0160a-20010704.bin") should be "18bcaadb9ff74ed3add26cdf709fff2e" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0160e-20010704.bin") should be "491209dd815ceee9de02dbbc408c06d6" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0160a-20011004.bin") should be "7200a03d51cacc4c14fcdfdbc4898431" (7 ms)
    ✓ md5sum("pcsx2/bios/ps2-0160e-20011004.bin") should be "8359638e857c8bc18c3c18ac17d9cc3c" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0160h-20010730.bin") should be "352d2ff9b3f68be7e6fa7e6dd8389346" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0160a-20020207.bin") should be "d5ce2c7d119f563ce04bc04dbc3a323e" (10 ms)
    ✓ md5sum("pcsx2/bios/ps2-0160e-20020319.bin") should be "0d2228e6fd4fb639c9c39d077a9ec10c" (10 ms)
    ✓ md5sum("pcsx2/bios/ps2-0160j-20020426.bin") should be "72da56fccb8fcd77bba16d1b6f479914" (13 ms)
    ✓ md5sum("pcsx2/bios/ps2-0160e-20020426.bin") should be "5b1f47fbeb277c6be2fccdd6344ff2fd" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0160h-20020426.bin") should be "315a4003535dfda689752cb25f24785c" (7 ms)
    ✓ md5sum("pcsx2/bios/ps2-0170j-20030206.bin") should be "312ad4816c232a9606e56f946bc0678a" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0170ed-20030227.bin") should be "666018ffec65c5c7e04796081295c6c7" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0170e-20030227.bin") should be "6e69920fa6eef8522a1d688a11e41bc6" (7 ms)
    ✓ md5sum("pcsx2/bios/ps2-0170ad-20030325.bin") should be "eb960de68f0c0f7f9fa083e9f79d0360" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0170a-20030325.bin") should be "8aa12ce243210128c5074552d3b86251" (7 ms)
    ✓ md5sum("pcsx2/bios/ps2-0180cd-20030224.bin") should be "240d4c5ddd4b54069bdc4a3cd2faf99d" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0180j-20031028.bin") should be "1c6cd089e6c83da618fbf2a081eb4888" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0190j-20030623.bin") should be "463d87789c555a4a7604e97d7db545d1" (7 ms)
    ✓ md5sum("pcsx2/bios/ps2-0190a-20030623.bin") should be "35461cecaa51712b300b2d6798825048" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0190e-20030623.bin") should be "bd6415094e1ce9e05daabe85de807666" (7 ms)
    ✓ md5sum("pcsx2/bios/ps2-0190h-20030623.bin") should be "2e70ad008d4ec8549aada8002fdf42fb" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0190r-20030623.bin") should be "b53d51edc7fc086685e31b811dc32aad" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0190c-20030623.bin") should be "1b6e631b536247756287b916f9396872" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0190j-20030822.bin") should be "00da1b177096cfd2532c8fa22b43e667" (7 ms)
    ✓ md5sum("pcsx2/bios/ps2-0190e-20030822.bin") should be "afde410bd026c16be605a1ae4bd651fd" (7 ms)
    ✓ md5sum("pcsx2/bios/ps2-0190a-20040329.bin") should be "81f4336c1de607dd0865011c0447052e" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0200j-20040614.bin") should be "0eee5d1c779aa50e94edd168b4ebf42e" (9 ms)
    ✓ md5sum("pcsx2/bios/ps2-0200a-20040614.bin") should be "d333558cc14561c1fdc334c75d5f37b7" (7 ms)
    ✓ md5sum("pcsx2/bios/ps2-0200e-20040614.bin") should be "dc752f160044f2ed5fc1f4964db2a095" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0200ed-20040614.bin") should be "63ead1d74893bf7f36880af81f68a82d" (7 ms)
    ✓ md5sum("pcsx2/bios/ps2-0200h-20040614.bin") should be "3e3e030c0f600442fa05b94f87a1e238" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0210j-20040917.bin") should be "1ad977bb539fc9448a08ab276a836bbc" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0220j-20050620.bin") should be "eb4f40fcf4911ede39c1bbfe91e7a89a" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0220ad-20050620.bin") should be "9959ad7a8685cad66206e7752ca23f8b" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0220a-20050620.bin") should be "929a14baca1776b00869f983aa6e14d2" (7 ms)
    ✓ md5sum("pcsx2/bios/ps2-0220e-20050620.bin") should be "573f7d4a430c32b3cc0fd0c41e104bbd" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0220h-20050620.bin") should be "df63a604e8bff5b0599bd1a6c2721bd0" (7 ms)
    ✓ md5sum("pcsx2/bios/ps2-0220j-20060210.bin") should be "5b1ba4bb914406fae75ab8e38901684d" (7 ms)
    ✓ md5sum("pcsx2/bios/ps2-0220a-20060210.bin") should be "cb801b7920a7d536ba07b6534d2433ca" (9 ms)
    ✓ md5sum("pcsx2/bios/ps2-0220e-20060210.bin") should be "af60e6d1a939019d55e5b330d24b1c25" (8 ms)
    ✓ md5sum("pcsx2/bios/ps2-0220h-20060210.bin") should be "549a66d0c698635ca9fa3ab012da7129" (8 ms)
    ✓ md5sum("pcsx2/bios/ps2-0220j-20060905.bin") should be "5de9d0d730ff1e7ad122806335332524" (8 ms)
    ✓ md5sum("pcsx2/bios/ps2-0220ad-20060905.bin") should be "21fe4cad111f7dc0f9af29477057f88d" (8 ms)
    ✓ md5sum("pcsx2/bios/ps2-0220a-20060905.bin") should be "40c11c063b3b9409aa5e4058e984e30c" (8 ms)
    ✓ md5sum("pcsx2/bios/ps2-0220e-20060905.bin") should be "80bbb237a6af9c611df43b16b930b683" (8 ms)
    ✓ md5sum("pcsx2/bios/ps2-0220h-20060905.bin") should be "c37bce95d32b2be480f87dd32704e664" (8 ms)
    ✓ md5sum("pcsx2/bios/ps2-0230j-20080220.bin") should be "80ac46fa7e77b8ab4366e86948e54f83" (8 ms)
    ✓ md5sum("pcsx2/bios/ps2-0230a-20080220.bin") should be "21038400dc633070a78ad53090c53017" (8 ms)
    ✓ md5sum("pcsx2/bios/ps2-0230e-20080220.bin") should be "dc69f0643a3030aaa4797501b483d6c4" (10 ms)
    ✓ md5sum("pcsx2/bios/ps2-0230h-20080220.bin") should be "30d56e79d89fbddf10938fa67fe3f34e" (7 ms)
    ✓ md5sum("pcsx2/bios/ps2-0250e-20100415.bin") should be "93ea3bcee4252627919175ff1b16a1d9" (6 ms)
    ✓ md5sum("pcsx2/bios/ps2-0250j-20100415.bin") should be "d3e81e95db25f5a86a7b7474550a2155" (6 ms)
    ✓ md5sum("ppge_atlas.zim") should be "866855cc330b9b95cc69135fb7b41d38" (2 ms)
    ✓ md5sum("ti83se.rom") should be "c6ff8204c5c81b7be34614dbbd690c8b" (3 ms)
    ✓ md5sum("ti83plus.rom") should be "8011181f810b5ec4e9d6a03f0e14257a" (1 ms)
    ✓ md5sum("ti83.rom") should be "d4448d09bbfde687c04f9e3310e023ab" (1 ms)
    ✓ md5sum("tvcfileio.rom") should be "a2cf86ba8e7fc58b242137fe59036832"
    ✓ md5sum("tvc22_ext.rom") should be "5ce95a26ceed5bec73995d83568da9cf"
    ✓ md5sum("tvc22_sys.rom") should be "8c54285f541930cde766069942bad0f2"
    ✓ md5sum("tvc_dos12d.rom") should be "88dc7876d584f90e4106f91444ab23b7"
    ✓ md5sum("ecwolf.pk3") should be "c011b428819eea4a80b455c245a5a04d" (1 ms)
    ✓ md5sum("scummvm.zip") should be "a17e0e0150155400d8cced329563d9c8" (13 ms)
    ✓ md5sum("fbneo/ngp.zip") should be "505a71c75aa742abd0caf9c7da606f8d"
    ✓ md5sum("fbneo/channelf.zip") should be "2f2f8de3827ae1faf2495e497ca95232"
    ✓ md5sum("TI-994A.ctg") should be "412ecbf991edcb68edd0e76c2caa4a59"
    ✓ md5sum("d32.rom") should be "3420b96031078a4ef408cad7bf21a33f" (1 ms)
    ✓ md5sum("vMac.ROM") should be "8a41e0754ffd1bb00d8183875c55164c"
    ✓ md5sum("bas13.rom") should be "c2fc43556eb6b7b25bdf5955bd9df825"
    ✓ md5sum("extbas11.rom") should be "21070aa0496142b886c562bf76d7c113" (1 ms)
    ✓ md5sum("coco3.rom") should be "42d0962b862f861ff4f74582c2454934"
    ✓ md5sum("coco3p.rom") should be "4ae57e5a8e7494e5485446fefedb580b" (1 ms)
    ○ skipped md5sum("kick33180.A500") should be "85ad74194e87c08904327de1a9443b7a" (skipped: file not found)
    ○ skipped md5sum("kick34005.CDTV") should be "89da1838a24460e4b93f4f0c5d92d48d" (skipped: file not found)
    ○ skipped md5sum("kick40060.CD32") should be "5f8924d013dd57a89cf349f4cdedc6b1" (skipped: file not found)
    ○ skipped md5sum("kick34005.A500") should be "82a21c1890cae844b3df741f2762d48d" (skipped: file not found)
    ○ skipped md5sum("kick40063.A600") should be "e40a5dfb3d017ba8779faba30cbd1c8e" (skipped: file not found)
    ○ skipped md5sum("kick40068.A1200") should be "646773759326fbac3b2311fd8c8793ee" (skipped: file not found)
    ○ skipped md5sum("kick37175.A500") should be "dc10d7bdd1b6f450773dfb558477c230" (skipped: file not found)
    ○ skipped md5sum("kick37350.A600") should be "465646c9b6729f77eea5314d1f057951" (skipped: file not found)
    ○ skipped md5sum("kick39106.A1200") should be "b7cc148386aa631136f510cd29e42fc3" (skipped: file not found)
    ○ skipped md5sum("kick39106.A4000") should be "9b8bdd5a3fd32c2a5a6f5b1aefc799a5" (skipped: file not found)
    ○ skipped md5sum("kick40068.A4000") should be "9bdedde6a4f33555b4a270c8ca53297d" (skipped: file not found)
    ○ skipped md5sum("kick40060.CD32.ext") should be "bb72565701b1b6faece07d68ea5da639" (skipped: file not found)
    ○ skipped md5sum("Dinothawr.zip") should be "a2e891e330d146c4046c2b622fc31462" (skipped: file not found)

Test Suites: 1 passed, 1 total
Tests:       13 skipped, 392 passed, 405 total
Snapshots:   0 total
Time:        1.149 s, estimated 2 s
Ran all test suites.
```

---

## Missing Files

This collection excludes copyrighted Amiga Kickstart ROMs. Please source them legally if needed.

Dinothawr.zip is missing (MD5 mismatch with available versions).

---

## 💖 Sponsor & Support

Maintaining this BIOS collection takes time and effort. If it helps you, consider buying me a coffee!

<div align="center">

| WeChat Pay | Alipay |
|:-:|:-:|
| <img src="wechat.png" alt="WeChat" width="180"/> | <img src="alipay.jpg" alt="Alipay" width="180"/> |
| **archtaurus** (WeChat) | **7176466@qq.com** (Alipay) |

</div>

<p align="center">
  <sub>
  💬 赞助后欢迎备注 GitHub 用户名，我会在 README 中致谢！<br>
  ⚡ Your support keeps this project alive!<br>
  Thanks to all backers! 🙌
  </sub>
</p>

---

### 🌟 Other Ways to Support

- ⭐ Star this repo
- 🐛 Report issues or send PRs
- 📢 Share with friends who need BIOS files

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=archtaurus/RetroPieBIOS&type=Date)](https://star-history.com/#archtaurus/RetroPieBIOS&Date)
