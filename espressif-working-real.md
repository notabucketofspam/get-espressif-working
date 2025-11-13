### download some stuff
install em with `pacman -U <the-whole-ass-file-name>`

you can also find them in the `some-packages` folder

- click
  - https://repo.msys2.org/mingw/mingw32/mingw-w64-i686-python-click-8.1.8-1-any.pkg.tar.zst

- pyserial
  - https://repo.msys2.org/mingw/mingw32/mingw-w64-i686-python-pyserial-3.5-3-any.pkg.tar.zst

- future
  - https://repo.msys2.org/mingw/mingw32/mingw-w64-i686-python-future-0.18.3-2-any.pkg.tar.zst

- the cryptography dependency tree is kind of a bitch
  - https://repo.msys2.org/mingw/mingw32/mingw-w64-i686-python-pycparser-2.22-2-any.pkg.tar.zst
  - https://repo.msys2.org/mingw/mingw32/mingw-w64-i686-python-cffi-1.17.1-2-any.pkg.tar.zst
  - https://repo.msys2.org/mingw/mingw32/mingw-w64-i686-python-cryptography-42.0.8-3-any.pkg.tar.zst

- pyparsing
  - https://repo.msys2.org/mingw/mingw32/mingw-w64-i686-python-pyparsing-3.2.5-1-any.pkg.tar.zst

- pyelftools
  - https://repo.msys2.org/mingw/mingw32/mingw-w64-i686-python-pyelftools-0.31-2-any.pkg.tar.zst



### fix python errors

slap this into the top of `ESP8266_RTOS_SDK/tools/check_python_dependencies.py`:

```
import sys
sys.exit(0)
```

put this in your ~/.bashrc:

```
export PYTHONPATH='C:/msys64/usr/lib/python3.12/site-packages'
```


### the rest of the owl

`cd` to your project folder

`make menuconfig` doesnt work, so you'll have to edit the sdkconfig file by-hand after running `make defconfig` (have fun with that)

```
make defconfig
make
```

- you can flash it using Espressif Flash Download Tool
  - https://docs.espressif.com/projects/esp-test-tools/en/latest/esp32/production_stage/tools/flash_download_tool.html
  - it's also in the `flashtool` folder

- or you can use the esptool binary
  - https://github.com/espressif/esptool/releases
