#!/usr/bin/sh

# check this
if test $MSYSTEM != MINGW64;then
	echo "Use MSYS2 MINGW64, not MSYS2 MSYS et al."
	exit 1
fi

# where to put it
cd /opt

# you get somefiles
pacman -Syu --noconfirm
pacman -S --needed --noconfirm unzip gcc make git pkg-config python3 wget perl
pacman -S --needed --noconfirm mingw-w64-x86_64-python-click mingw-w64-x86_64-python-pyserial mingw-w64-x86_64-python-future mingw-w64-x86_64-python-cryptography mingw-w64-x86_64-python-pyparsing mingw-w64-x86_64-python-pyelftools

wget --no-clobber "https://dl.espressif.com/dl/xtensa-lx106-elf-gcc8_4_0-esp-2020r3-win32.zip"
unzip "xtensa-lx106-elf-gcc8_4_0-esp-2020r3-win32.zip"
git -C ESP8266_RTOS_SDK pull || git clone --recurse-submodules https://github.com/espressif/ESP8266_RTOS_SDK.git

# some config
if test $IDF_PATH != '/opt/ESP8266_RTOS_SDK'; then
	export IDF_PATH=/opt/ESP8266_RTOS_SDK
	echo "export IDF_PATH=/opt/ESP8266_RTOS_SDK">> ~/.bashrc
fi
if test $PYTHONPATH != 'C:/msys64/usr/lib/python3.12/site-packages'; then
	export PYTHONPATH='C:/msys64/usr/lib/python3.12/site-packages'
	echo "export PYTHONPATH='C:/msys64/usr/lib/python3.12/site-packages'">> ~/.bashrc
fi




echo "Don't forget that you still need to set %IDF_PATH% in Windows."
echo "Open an Administrator Command Prompt and do:"
echo 'SETX IDF_PATH C:\msys64\opt\ESP8266_RTOS_SDK /m'
echo
read -rsn1 -p "Press any key to continue . . ."
