@ECHO off
SETLOCAL
SET "PATH=C:\msys64\ucrt64\bin;C:\msys64\usr\bin;C:\msys64\opt\xtensa-lx106-elf\bin;%PATH%"
SET "IDF_PATH=C:/msys64/opt/ESP8266_RTOS_SDK"
SET MSYSTEM=UCRT64
SET CHERE_INVOKING=1
SET MSYS2_PATH_TYPE=inherit
C:\msys64\usr\bin\bash.exe --login -c "make -j menuconfig"
ENDLOCAL
CALL make-all.bat
ECHO DONE %~n0
