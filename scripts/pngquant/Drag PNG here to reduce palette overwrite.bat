@echo off

set path=%~d0%~p0

:start

"%path%pngquant.exe" --force --ext=.png --speed=1 --verbose --quality=45-85 %1

shift
if NOT x%1==x goto start




