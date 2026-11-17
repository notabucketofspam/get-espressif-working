#!/usr/bin/sh

# check this
if test $MSYSTEM != UCRT64;then
	echo "Use MSYS2 UCRT64, not MSYS2 MSYS et al."
	exit 1
fi

# store the repo diff for later
REPO_DIFF="$(cat repo.diff)"

# where to put it
cd /opt

# you get somefiles
pacman -Syu --noconfirm
pacman -S --needed --noconfirm unzip gcc make git pkg-config python3 wget perl
pacman -S --needed --noconfirm mingw-w64-ucrt-x86_64-python-click mingw-w64-ucrt-x86_64-python-pyserial mingw-w64-ucrt-x86_64-python-future mingw-w64-ucrt-x86_64-python-cryptography mingw-w64-ucrt-x86_64-python-pyparsing mingw-w64-ucrt-x86_64-python-pyelftools

wget --no-clobber "https://dl.espressif.com/dl/xtensa-lx106-elf-gcc8_4_0-esp-2020r3-win32.zip"
unzip -n "xtensa-lx106-elf-gcc8_4_0-esp-2020r3-win32.zip"
git -C ESP8266_RTOS_SDK pull || git clone --recurse-submodules https://github.com/espressif/ESP8266_RTOS_SDK.git

# apply the git diff
git -C ESP8266_RTOS_SDK apply --reverse --check - <<< "$REPO_DIFF" 2>/dev/null || git -C ESP8266_RTOS_SDK apply - <<< "$REPO_DIFF"


# some config
if grep -v -q "/opt/xtensa-lx106-elf/bin" <<< "$PATH"; then  
  export PATH="$PATH:/opt/xtensa-lx106-elf/bin"
  echo 'export PATH="$PATH:/opt/xtensa-lx106-elf/bin"'>> ~/.bashrc
fi
if test "$IDF_PATH" != '/opt/ESP8266_RTOS_SDK'; then
	export IDF_PATH='/opt/ESP8266_RTOS_SDK'
	echo "export IDF_PATH='/opt/ESP8266_RTOS_SDK'">> ~/.bashrc
fi
PYTHONPATH_DESIRED="$(python -c 'import site; print(site.getsitepackages()[0])')"
if test "$PYTHONPATH" != "$PYTHONPATH_DESIRED"; then
	export PYTHONPATH="'$PYTHONPATH_DESIRED'"
	echo "export PYTHONPATH='$PYTHONPATH_DESIRED'">> ~/.bashrc
fi

CMD_RESULT="$(cmd //c 'echo %IDF_PATH%')"

if grep -v -q '/opt/ESP8266_RTOS_SDK' <<< "$CMD_RESULT"; then
	cat <<EOF
========================================

Don't forget that you still need to set %IDF_PATH% in Windows.
Open an Administrator Command Prompt and do:

SETX IDF_PATH C:\msys64\opt\ESP8266_RTOS_SDK /m

========================================
EOF
fi

# basically done
echo '========================================'
echo "Ok cool. The MSYS2 setup is complete."
read -rsn1 -p "Press any key to continue . . ."
