some changes to get `make menuconfig` working.

NOTE: we run `make` with MSYS2 MinGW 64-bit instead of 32-bit.

*Huge* shoutout to Sonic-Amiga (PR#1239), btw.

---

in `tools/kconfig/symbol.c`:

near the top, replace `#include <sys/utsname.h>` with:
```
#ifndef _WIN32
#include <sys/utsname.h>
#endif
```

we modify `sym_init()`:
```
void sym_init(void)
{
#ifndef _WIN32
<a whole bunch of shit>
#endif
}
```

---

in `tools/kconfig/lxdialog/util.c`:

we modify `on_key_esc()`:
on the line right after `key = wgetch(win);`, put this in:
```	
#ifdef WIN32
    if (key == ERR)
      return KEY_ESC;
#endif
```

---

in `tools/kconfig/confdata.c`:

we modify `conf_write()`:
(near the end of the function body), right after `strcat(dirname, ".old");`, put this in:
```
#ifdef WIN32
    unlink(dirname);
#endif
```
