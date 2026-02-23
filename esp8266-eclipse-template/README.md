# esp8266-eclipse-template

Windows preconfigured project for the Eclipse IDE. Tested with Eclipse version 2025-12.

This template is based off of [the instructions provided by Espressif](https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/get-started/eclipse-setup-windows.html).

---

1. *Before anything else*, rename this template folder. The project name is based on the folder name (idk why).
1. Make sure that the whole rest of the IDF setup is done.
1. Run `update-project-name.bat`.

Now we can add the project to Eclipse:

1. File -> Open Projects from File System...
1. Hit "Directory...", navigate to the template folder, hit "Select Folder"
1. "Search for nested projects" must be **unchecked**.
1. "Detect and configure project natures" must be **unchecked**.
1. Finish

---

- The template assumes that MSYS2 is installed at `C:\msys64` (this is where MSYS2 64-bit is installed by default).
- An error for `Program "gcc" not found in PATH` should disappear once the build is completed.
- [The Espressif instructions describe how to flash the ESP8266 from within Eclipse.](https://docs.espressif.com/projects/esp8266-rtos-sdk/en/latest/get-started/eclipse-setup.html#flash-from-eclipse) 
- If something goes wrong, check the [quick reference](quick-reference.md).
