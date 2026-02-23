# ESP8266_RTOS_SDK

yeah it works on windows

### some links

- ESP8266 toolchain for Windows
  - https://dl.espressif.com/dl/xtensa-lx106-elf-gcc8_4_0-esp-2020r3-win32.zip
  - this'll eventually go in `C:\msys64\opt`

- espressif/ESP8266_RTOS_SDK GitHub
  - https://github.com/espressif/ESP8266_RTOS_SDK.git
  - note: to clone this, you need `git clone --recurse-submodules https://github.com/espressif/ESP8266_RTOS_SDK.git`
  - you cau use `rundll32 sysdm.cpl,EditEnvironmentVariables` to set `%IDF_PATH%` easier

- ESP8266 RTOS SDK Programming Guide
  - https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/get-started/
  - follow those instructions until you get stuck, then come back here

- MSYS2
  - https://www.msys2.org/
  
### msys2 mingw64

install the python packages:

```
pacman -S mingw-w64-x86_64-python-click mingw-w64-x86_64-python-pyserial mingw-w64-x86_64-python-future mingw-w64-x86_64-python-cryptography mingw-w64-x86_64-python-pyparsing mingw-w64-x86_64-python-pyelftools
```

get rid of a warning when we run `make` later:

```
sed -i s,MINGW32,MINGW64,g $IDF_PATH/make/project.mk
```

if you *gotta* use mingw32, check [for-mingw32-enjoyers.md](for-mingw32-enjoyers.md)

### fix python errors

slap this into the top of `ESP8266_RTOS_SDK/tools/check_python_dependencies.py`:

```
import sys
sys.exit(0)
```

put this in your `~/.bashrc`:

```
export PYTHONPATH='C:/msys64/usr/lib/python3.12/site-packages'
```

### the rest of the owl

`cd` to your project folder

if you wanna use `make menuconfig`, there's instructions in [howto-make-menuconfig.md](howto-make-menuconfig.md)

otherwise, you'll have to edit the sdkconfig file by-hand after running `make defconfig` (have fun with that)

- you can flash it using Espressif Flash Download Tool
  - https://docs.espressif.com/projects/esp-test-tools/en/latest/esp32/production_stage/tools/flash_download_tool.html
  - it's also in the `flashtool` folder

- or you can use the esptool binary
  - https://github.com/espressif/esptool/releases

### the Eclipse template

it works pretty well, imo.
