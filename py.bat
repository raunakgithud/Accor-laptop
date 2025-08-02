@echo on

if exist C:\Users\Lenovo\OneDrive\Desktop\*.py  echo %date%%time%"found it" *.py>>D:\py\pylog.txt   



copy  C:\Users\Lenovo\OneDrive\Desktop\*.py   D:\py\*.py
del   C:\Users\Lenovo\OneDrive\Desktop\*.py