@ECHO off
TITLE %~n0
SETLOCAL
SET "PATH=C:\msys64\ucrt64\bin;C:\msys64\usr\bin;C:\msys64\opt\xtensa-lx106-elf\bin;%PATH%"
SET "IDF_PATH=C:/msys64/opt/ESP8266_RTOS_SDK"
python eclipse_make.py -j flash
ENDLOCAL
ECHO DONE %~n0
