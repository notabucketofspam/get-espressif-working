Quick reference for Eclipse project settings, in case something goes wrong.

C/C++ Build

- Top level
  - \[Builder Settings\] "Use default build command" must be **unchecked**.
  - \[Builder Settings\] Build command: `python`
  - \[Behavior\] "Use custom build arguments" must be <u>checked</u>.
  - \[Behavior\] Build arguments: `eclipse_make.py -j`
- Environment
  - `BATCH_BUILD` : `1`
  - `IDF_PATH` : same as `%IDF_PATH%` but with back slashes converted to forward slashes
    - for example, `C:/msys64/home/Onion/esp/ESP8266_RTOS_SDK`
  - `PATH` : `C:\msys64\usr\bin;C:\msys64\mingw64\bin;C:\msys64\opt\xtensa-lx106-elf\bin`

C/C++ General

- Indexer
  - "Enable project specific settings" must be <u>checked</u>.
  - "Allow heuristic resolution of includes" must be **unchecked**.
- Preprocessor Include Paths, Macros etc.
  - \[Providers\] CDT GCC Build Output Parser: `xtensa-lx106-elf-(gcc|g\+\+|c\+\+|cc|cpp|clang)`
  - \[Providers\] CDT Cross GCC Built-in Compiler Settings Cygwin: `xtensa-lx106-elf-gcc ${FLAGS} -E -P -v -dD "${INPUTS}"`
