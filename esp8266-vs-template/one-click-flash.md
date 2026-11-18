**HOWTO**: bind an External Tool entry for both ESP8266 Flash and ESP8266 Menuconfig:

- Title: ```ESP8266 Flash```
- Command: ```cmd.exe```
- Arguments: ```/c set "PATH=C:\msys64\ucrt64\bin;C:\msys64\usr\bin;C:\msys64\opt\xtensa-lx106-elf\bin;%PATH%" && set "IDF_PATH=C:/msys64/opt/ESP8266_RTOS_SDK" && python eclipse_make.py -j flash```
- Initial directory: ```$(ProjectDir)```
- Check: ```Use Output window```
