@echo off
C:\WINDOWS\system32\cmd.exe /c "set MSYSTEM=MINGW32&& set CHERE_INVOKING=1&& set MSYS2_PATH_TYPE=inherit&& C:\msys64\usr\bin\bash.exe --login -c ./update-project-name.sh"
echo done
pause
