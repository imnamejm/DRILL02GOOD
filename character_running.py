Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from pico2d import*
Pico2d is prepared.
>>> open_canvas()
>>> grass = load_image('grass.png')
cannot load grass.png
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    grass = load_image('grass.png')
  File "C:\Users\윤정민\Lib\site-packages\pico2d\pico2d.py", line 349, in load_image
    raise IOError
OSError
>>> import math
>>> import os
>>> os.chdir('C:\\2DGP\\DRILL02GOOD')
>>> os.listdir
<built-in function listdir>
>>> os.listdir()
['.git', '.gitattributes', '.gitignore', 'character.png', 'character_grass.py', 'character_run.py', 'grass.png', 'README.md']
>>> grass = loat_image('grass.png')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    grass = loat_image('grass.png')
NameError: name 'loat_image' is not defined
>>> grass = load_image('grass.png')
