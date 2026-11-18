import os
import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

def cygpath_to_win(p: str) -> str:
    p = p.strip().strip('"').rstrip("\\")
    if p.startswith("/"):
        return subprocess.check_output(["cygpath", "-w", p]).decode().strip()
    return os.path.normpath(p)

def main():
    idf_path = os.environ.get("IDF_PATH", "C:/msys64/opt/ESP8266_RTOS_SDK")
    idf_win = cygpath_to_win(idf_path)
    xtensa_sys_inc = r"C:\msys64\opt\xtensa-lx106-elf\xtensa-lx106-elf\include"

    includes = set()
    # 1. Grab build/include (contains generated sdkconfig.h) & main/
    for local_dir in ["build/include", "main"]:
        if os.path.exists(local_dir):
            includes.add(os.path.abspath(local_dir))

    # 2. Scrape real compiler -I paths from existing .d files in build/ (instant, no make)
    for d_file in Path("build").rglob("*.d"):
        text = d_file.read_text(errors="ignore")
        for line in text.splitlines():
            # Dependency files list every header actually resolved during compilation
            for token in line.replace("\\", " ").split():
                if token.endswith(".h") and os.path.exists(token):
                    parent = os.path.dirname(os.path.abspath(token))
                    # Walk up to the 'include' root if inside a subfolder like freertos/FreeRTOS.h
                    if os.path.basename(os.path.dirname(parent)) == "include":
                        parent = os.path.dirname(parent)
                    includes.add(parent)

    # 3. Fallback: add all SDK component include/ directories if build/ wasn't populated yet
    comp_root = Path(idf_win) / "components"
    if comp_root.exists():
        for inc_dir in comp_root.rglob("include"):
            if inc_dir.is_dir():
                includes.add(str(inc_dir))

    if os.path.exists(xtensa_sys_inc):
        includes.add(xtensa_sys_inc)

    gcc_lib_root = Path(r"C:\msys64\opt\xtensa-lx106-elf\lib\gcc\xtensa-lx106-elf")
    if gcc_lib_root.exists():
        for gcc_inc in gcc_lib_root.glob("*/include"):
            includes.add(str(gcc_inc))
        for gcc_inc_fixed in gcc_lib_root.glob("*/include-fixed"):
            includes.add(str(gcc_inc_fixed))

    defines = [
        "__XTENSA__",
        "__ets__",
        "ICACHE_FLASH",
        "ESP_PLATFORM",
        "HAVE_CONFIG_H",
        "GCC_NOT_5_2_0=1",
        "WITH_POSIX",
        "__GNUC__=8",
        "__INT8_TYPE__=signed char",
        "__UINT8_TYPE__=unsigned char",
        "__INT16_TYPE__=short int",
        "__UINT16_TYPE__=short unsigned int",
        "__INT32_TYPE__=int",
        "__UINT32_TYPE__=unsigned int",
        "__INT64_TYPE__=long long int",
        "__UINT64_TYPE__=long long unsigned int",
        "__SIZE_TYPE__=unsigned int",
        "__PTRDIFF_TYPE__=int",
        "__INTPTR_TYPE__=int",
        "__UINTPTR_TYPE__=unsigned int",
        "__builtin_va_list=char*",
        "__builtin_expect(x,y)=(x)",
        "__attribute__(x)=",
        "__extension__=",
        "__inline__=inline",
        "__asm__(x)=",
        "asm(x)=",
    ]

    ns = "http://schemas.microsoft.com/developer/msbuild/2003"
    ET.register_namespace("", ns)
    project = ET.Element(f"{{{ns}}}Project")
    pg = ET.SubElement(project, f"{{{ns}}}PropertyGroup")

    inc_el = ET.SubElement(pg, f"{{{ns}}}NMakeIncludeSearchPath")
    inc_el.text = ";".join(sorted(includes)) + ";$(NMakeIncludeSearchPath)"

    def_el = ET.SubElement(pg, f"{{{ns}}}NMakePreprocessorDefinitions")
    def_el.text = ";".join(defines) + ";$(NMakePreprocessorDefinitions)"

    forced_includes = []
    sdkconfig_h = os.path.abspath("build/include/sdkconfig.h")
    if os.path.exists(sdkconfig_h):
        forced_includes.append(sdkconfig_h)

    newlib_stdint = os.path.join(xtensa_sys_inc, "stdint.h")
    if os.path.exists(newlib_stdint):
        forced_includes.append(newlib_stdint)

    if forced_includes:
        fi_el = ET.SubElement(pg, f"{{{ns}}}NMakeForcedIncludes")
        fi_el.text = ";".join(forced_includes) + ";$(NMakeForcedIncludes)"

    tree = ET.ElementTree(project)
    ET.indent(tree, space="  ")
    tree.write("esp8266_intellisense.props", encoding="utf-8", xml_declaration=True)
    print(f"Synced {len(includes)} include paths.")

if __name__ == "__main__":
    main()

